"""Provider-neutral ablation runner for the document benchmark."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from docs_benchmark.benchmark.analysis import (
    analyze_submission,
    group_results_by_feature_flags,
    group_results_by_field,
    group_results_by_membership,
    summarize_expected_entry_groups,
    summarize_results,
)
from docs_benchmark.benchmark.manifests import record_manifest_row, write_jsonl
from docs_benchmark.benchmark.parser import SubmissionParseError, parse_submission
from docs_benchmark.benchmark.prompt import (
    PROMPT_VARIANT_BASELINE,
    PROMPT_VARIANT_GUIDED_PRIVATE_SOLVE,
    PROMPT_VARIANT_SELF_CHECK,
    PROMPT_VARIANTS,
    VISIBILITY_VARIANT_NO_ALLOWED_ACCOUNTS,
    VISIBILITY_VARIANT_NO_DISTRACTORS_ORACLE,
    VISIBILITY_VARIANT_NORMAL,
    VISIBILITY_VARIANT_OCR_ONLY,
    VISIBILITY_VARIANT_SUPPORT_DOCS_REMOVED,
    VISIBILITY_VARIANTS,
    build_prompt,
)
from docs_benchmark.benchmark.tools import (
    TOOL_VARIANT_CALCULATOR,
    TOOL_VARIANT_DOCUMENT_SEARCH,
    TOOL_VARIANT_FULL_TOOL_AGENT,
    TOOL_VARIANT_LEDGER_CHECK,
    TOOL_VARIANT_NO_TOOLS,
    TOOL_VARIANTS,
    TOOLS_BY_VARIANT,
    ChatClient,
    ToolAgentResult,
    run_no_tool_completion,
    run_tool_agent_completion,
)
from docs_benchmark.schemas import DocumentRecord, ParsedSubmission, ensure_parent


@dataclass(frozen=True)
class AblationSpec:
    name: str
    prompt_variant: str = PROMPT_VARIANT_BASELINE
    visibility_variant: str = VISIBILITY_VARIANT_NORMAL
    tool_variant: str = TOOL_VARIANT_NO_TOOLS

    def __post_init__(self) -> None:
        if self.prompt_variant not in PROMPT_VARIANTS:
            raise ValueError(f"Unknown prompt variant '{self.prompt_variant}'")
        if self.visibility_variant not in VISIBILITY_VARIANTS:
            raise ValueError(f"Unknown visibility variant '{self.visibility_variant}'")
        if self.tool_variant not in TOOL_VARIANTS:
            raise ValueError(f"Unknown tool variant '{self.tool_variant}'")


COVERAGE_ABLATION_SPECS = (
    AblationSpec("prompt_baseline"),
    AblationSpec("prompt_guided_private_solve", prompt_variant=PROMPT_VARIANT_GUIDED_PRIVATE_SOLVE),
    AblationSpec("prompt_self_check", prompt_variant=PROMPT_VARIANT_SELF_CHECK),
    AblationSpec("visibility_ocr_only", visibility_variant=VISIBILITY_VARIANT_OCR_ONLY),
    AblationSpec("visibility_no_distractors_oracle", visibility_variant=VISIBILITY_VARIANT_NO_DISTRACTORS_ORACLE),
    AblationSpec("visibility_support_docs_removed", visibility_variant=VISIBILITY_VARIANT_SUPPORT_DOCS_REMOVED),
    AblationSpec("visibility_no_allowed_accounts", visibility_variant=VISIBILITY_VARIANT_NO_ALLOWED_ACCOUNTS),
    AblationSpec("tool_no_tools"),
    AblationSpec("tool_calculator", tool_variant=TOOL_VARIANT_CALCULATOR),
    AblationSpec("tool_document_search", tool_variant=TOOL_VARIANT_DOCUMENT_SEARCH),
    AblationSpec("tool_ledger_check", tool_variant=TOOL_VARIANT_LEDGER_CHECK),
    AblationSpec("tool_full_tool_agent", tool_variant=TOOL_VARIANT_FULL_TOOL_AGENT),
)


SLICE_FIELDS = (
    "difficulty_level",
    "industry",
    "period_type",
    "tax_regime",
    "expected_inconsistency_code",
    "document_count",
    "expected_entry_count",
    "doc_dependency_depth",
    "subledger_count",
    "jurisdictional_depth",
    "temporal_lookback_depth",
    "has_asc606",
    "has_asset_disposal",
    "has_deferred_tax",
    "has_lease",
    "has_tax_exemption",
)
MEMBERSHIP_SLICE_FIELDS = (
    "scenario_sequence",
    "ledger_families_present",
    "posting_labels_present",
    "doc_types_present",
)
CONCEPT_FLAGS = (
    "has_asc606",
    "has_asset_disposal",
    "has_deferred_tax",
    "has_lease",
    "has_tax_exemption",
)


def select_ablation_specs(
    *,
    matrix: str = "coverage",
    names: list[str] | None = None,
) -> list[AblationSpec]:
    if matrix != "coverage":
        raise ValueError(f"Unknown ablation matrix '{matrix}'")
    specs = list(COVERAGE_ABLATION_SPECS)
    if not names:
        return specs
    by_name = {spec.name: spec for spec in specs}
    missing = [name for name in names if name not in by_name]
    if missing:
        raise ValueError(f"Unknown ablation names: {', '.join(missing)}")
    return [by_name[name] for name in names]


def apply_visibility_variant(
    record: DocumentRecord,
    visibility_variant: str,
) -> tuple[DocumentRecord, dict[str, Any]]:
    if visibility_variant not in VISIBILITY_VARIANTS:
        raise ValueError(f"Unknown visibility variant '{visibility_variant}'")

    documents = list(record.documents)
    allowed_accounts = list(record.allowed_accounts)
    if visibility_variant == VISIBILITY_VARIANT_NO_DISTRACTORS_ORACLE:
        documents = [document for document in documents if document.role != "distractor_doc"]
    elif visibility_variant == VISIBILITY_VARIANT_SUPPORT_DOCS_REMOVED:
        documents = [document for document in documents if document.role != "support_doc"]
    elif visibility_variant == VISIBILITY_VARIANT_NO_ALLOWED_ACCOUNTS:
        allowed_accounts = []

    transformed = replace(
        record,
        documents=documents,
        allowed_accounts=allowed_accounts,
        metadata=dict(record.metadata),
    )
    visible_doc_ids = {document.doc_id for document in documents}
    return transformed, {
        "original_document_count": len(record.documents),
        "visible_document_count": len(documents),
        "removed_document_ids": [
            document.doc_id for document in record.documents if document.doc_id not in visible_doc_ids
        ],
        "original_allowed_account_count": len(record.allowed_accounts),
        "visible_allowed_account_count": len(allowed_accounts),
    }


def run_ablation_evaluation(
    records: list[DocumentRecord],
    *,
    client: ChatClient,
    dataset_path: str,
    spec: AblationSpec,
    backend_name: str = "openrouter",
    temperature: float = 0.0,
    max_tokens: int = 8192,
    timeout: int = 180,
    agent_max_steps: int = 8,
) -> dict[str, Any]:
    started_at = datetime.now(timezone.utc).isoformat()
    results: list[dict[str, Any]] = []

    for record in records:
        visible_record, visibility_metadata = apply_visibility_variant(record, spec.visibility_variant)
        prompt = build_prompt(
            visible_record,
            prompt_variant=spec.prompt_variant,
            visibility_variant=spec.visibility_variant,
        )
        completion = ToolAgentResult()
        error_message = ""
        parse_success = False
        parsed = _empty_submission()

        try:
            if spec.tool_variant == TOOL_VARIANT_NO_TOOLS:
                completion = run_no_tool_completion(
                    client,
                    prompt,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    timeout=timeout,
                )
            else:
                completion = run_tool_agent_completion(
                    visible_record,
                    client,
                    prompt,
                    allowed_tools=TOOLS_BY_VARIANT[spec.tool_variant],
                    agent_max_steps=agent_max_steps,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    timeout=timeout,
                )
            parsed = parse_submission(completion.response_text)
            parse_success = True
        except SubmissionParseError as exc:
            error_message = str(exc)
        except Exception as exc:  # pragma: no cover - exercised by integration runs
            error_message = str(exc)

        analysis = analyze_submission(record, parsed, parse_success=parse_success)
        usage = dict(completion.response_payload.get("usage", {})) if isinstance(completion.response_payload, dict) else {}
        record_features = record_manifest_row(record)
        result = {
            "record_id": record.record_id,
            "industry": record.industry,
            "difficulty_level": record.difficulty_level,
            "period_type": record.metadata.get("period_type"),
            "period_label": record.metadata.get("period_label"),
            "ablation_name": spec.name,
            "prompt_variant": spec.prompt_variant,
            "visibility_variant": spec.visibility_variant,
            "tool_variant": spec.tool_variant,
            "agent_max_steps": int(agent_max_steps),
            "tool_calls": completion.tool_calls,
            "tool_call_failures": completion.tool_call_failures,
            "latency_seconds": completion.latency_seconds,
            "document_index": {
                document.doc_id: {"doc_type": document.doc_type, "role": document.role}
                for document in record.documents
            },
            "visible_document_index": {
                document.doc_id: {"doc_type": document.doc_type, "role": document.role}
                for document in visible_record.documents
            },
            "visibility_metadata": visibility_metadata,
            "record_features": record_features,
            "metrics": analysis["metrics"],
            "parsed_submission": analysis["parsed_submission"],
            "reconstructed_balance_sheet": analysis["reconstructed_balance_sheet"],
            "entry_diagnostics": analysis["entry_diagnostics"],
            "usage": usage,
            "cost": float(usage.get("cost", 0.0)) if usage else 0.0,
            "prompt_tokens": int(usage.get("prompt_tokens", 0)) if usage else 0,
            "completion_tokens": int(usage.get("completion_tokens", 0)) if usage else 0,
            "total_tokens": int(usage.get("total_tokens", 0)) if usage else 0,
            "error": error_message,
            "raw_response": completion.response_text,
            "raw_provider_payload": completion.response_payload,
        }
        results.append(result)

    return {
        "dataset_path": dataset_path,
        "model": client.model,
        "backend": backend_name,
        "ablation_name": spec.name,
        "prompt_variant": spec.prompt_variant,
        "visibility_variant": spec.visibility_variant,
        "tool_variant": spec.tool_variant,
        "agent_max_steps": int(agent_max_steps),
        "run_started_at": started_at,
        "run_completed_at": datetime.now(timezone.utc).isoformat(),
        "temperature": temperature,
        "max_tokens": max_tokens,
        "timeout": timeout,
        "summary": summarize_ablation_results(results),
        "results": results,
    }


def summarize_ablation_results(results: list[dict[str, Any]]) -> dict[str, Any]:
    summary = summarize_results(results)
    for field in SLICE_FIELDS:
        summary[f"by_{field}"] = group_results_by_field(results, field)
    summary["by_inconsistency_code"] = group_results_by_field(results, "expected_inconsistency_code")
    for field in MEMBERSHIP_SLICE_FIELDS:
        summary[f"by_{field}"] = group_results_by_membership(results, field)
    summary["by_scenario_family"] = group_results_by_membership(results, "scenario_sequence")
    summary["by_ledger_family"] = group_results_by_membership(results, "ledger_families_present")
    summary["by_posting_label"] = group_results_by_membership(results, "posting_labels_present")
    summary["by_doc_type"] = group_results_by_membership(results, "doc_types_present")
    summary["by_feature_flags"] = group_results_by_feature_flags(results)
    summary["entry_groups"] = {
        "posting_label": summarize_expected_entry_groups(results, "posting_label"),
        "ledger_family": summarize_expected_entry_groups(results, "ledger_family"),
        "doc_type": summarize_expected_entry_groups(results, "doc_type"),
    }
    summary["error_taxonomy"] = summarize_error_taxonomy(results)
    summary["concept_failures"] = summarize_concept_failures(results)
    summary["tool_call_count_total"] = sum(len(result.get("tool_calls", [])) for result in results)
    summary["tool_call_failures_total"] = sum(int(result.get("tool_call_failures", 0)) for result in results)
    summary["latency_seconds_total"] = round(sum(float(result.get("latency_seconds", 0.0)) for result in results), 4)
    summary["latency_seconds_average"] = round(summary["latency_seconds_total"] / len(results), 4) if results else 0.0
    return summary


def summarize_error_taxonomy(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    standard_results = [result for result in results if not result["metrics"]["expected_inconsistency"]]
    inconsistency_results = [result for result in results if result["metrics"]["expected_inconsistency"]]

    taxonomy = [
        _entry_error_row("arithmetic_failure", "wrong_amount_count", standard_results),
        _entry_error_row("account_selection_failure", "wrong_account_count", standard_results),
        _entry_error_row("document_linking_failure", "doc_refs_mismatch_count", standard_results),
        _entry_error_row("omission_failure", "missing_entry_count", standard_results),
        _entry_error_row("hallucinated_extra_entry", "extra_entry_count", standard_results),
        _record_error_row(
            "balance_reconstruction_failure",
            standard_results,
            lambda metrics: not metrics.get("predicted_entries_reconstruct_correct_final_balance_sheet", False),
        ),
        _record_error_row(
            "inconsistency_detection_failure",
            results,
            lambda metrics: bool(
                metrics.get("false_inconsistency_alarm")
                or metrics.get("missed_inconsistency")
                or (metrics.get("expected_inconsistency") and not metrics.get("inconsistency_code_matches"))
            ),
        ),
    ]
    taxonomy.append(
        {
            "error_type": "inconsistency_code_failure",
            "affected_record_count": sum(
                1 for result in inconsistency_results if not result["metrics"].get("inconsistency_code_matches")
            ),
            "total_records": len(inconsistency_results),
            "affected_record_rate": _rate(
                sum(1 for result in inconsistency_results if not result["metrics"].get("inconsistency_code_matches")),
                len(inconsistency_results),
            ),
            "entry_count": 0,
        }
    )
    return taxonomy


def summarize_concept_failures(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for flag in CONCEPT_FLAGS:
        subset = [result for result in results if result.get("record_features", {}).get(flag)]
        failures = [
            result
            for result in subset
            if not result["metrics"].get("final_balance_sheet_and_journal_entries_match")
            and not result["metrics"].get("inconsistency_code_matches")
        ]
        rows.append(
            {
                "concept": flag.removeprefix("has_"),
                "feature_flag": flag,
                "records": len(subset),
                "failure_count": len(failures),
                "failure_rate": _rate(len(failures), len(subset)),
            }
        )
    return rows


def write_ablation_outputs(evaluation: dict[str, Any], output_root: str | Path) -> Path:
    ablation_dir = Path(output_root) / str(evaluation["ablation_name"])
    ensure_parent(ablation_dir / "evaluation.json").write_text(
        json.dumps(evaluation, indent=2),
        encoding="utf-8",
    )
    ensure_parent(ablation_dir / "summary.json").write_text(
        json.dumps(evaluation["summary"], indent=2),
        encoding="utf-8",
    )
    write_jsonl(ablation_dir / "per_record_results.jsonl", evaluation["results"])
    _write_slice_tables(evaluation["summary"], ablation_dir / "slice_tables")
    return ablation_dir


def _write_slice_tables(summary: dict[str, Any], tables_dir: Path) -> None:
    for key, value in summary.items():
        if key.startswith("by_") and isinstance(value, dict):
            _write_grouped_csv(tables_dir / f"{key}.csv", value)
    entry_groups = summary.get("entry_groups", {})
    if isinstance(entry_groups, dict):
        for key, value in entry_groups.items():
            if isinstance(value, dict):
                _write_grouped_csv(tables_dir / f"entry_group_by_{key}.csv", value)
    if isinstance(summary.get("error_taxonomy"), list):
        _write_rows_csv(tables_dir / "error_taxonomy.csv", summary["error_taxonomy"])
    if isinstance(summary.get("concept_failures"), list):
        _write_rows_csv(tables_dir / "concept_failures.csv", summary["concept_failures"])


def _write_grouped_csv(path: Path, grouped: dict[str, dict[str, Any]]) -> None:
    rows = []
    for group, values in grouped.items():
        row = {"slice": group}
        row.update(_scalar_items(values))
        rows.append(row)
    _write_rows_csv(path, rows)


def _write_rows_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    output = ensure_parent(path)
    fieldnames = sorted({key for row in rows for key in row})
    if "slice" in fieldnames:
        fieldnames = ["slice"] + [field for field in fieldnames if field != "slice"]
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _scalar_items(values: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in values.items()
        if isinstance(value, (str, int, float, bool)) or value is None
    }


def _entry_error_row(error_type: str, count_field: str, results: list[dict[str, Any]]) -> dict[str, Any]:
    entry_count = sum(int(result["metrics"].get(count_field, 0)) for result in results)
    affected = sum(1 for result in results if int(result["metrics"].get(count_field, 0)) > 0)
    return {
        "error_type": error_type,
        "affected_record_count": affected,
        "total_records": len(results),
        "affected_record_rate": _rate(affected, len(results)),
        "entry_count": entry_count,
    }


def _record_error_row(
    error_type: str,
    results: list[dict[str, Any]],
    predicate: Any,
) -> dict[str, Any]:
    affected = sum(1 for result in results if predicate(result["metrics"]))
    return {
        "error_type": error_type,
        "affected_record_count": affected,
        "total_records": len(results),
        "affected_record_rate": _rate(affected, len(results)),
        "entry_count": 0,
    }


def _rate(numerator: int, denominator: int) -> float:
    if denominator <= 0:
        return 0.0
    return round(numerator / denominator, 4)


def _empty_submission() -> ParsedSubmission:
    return ParsedSubmission(
        entries=[],
        balance_sheet={"assets": {}, "liabilities": {}, "equity": {}},
        has_inconsistency=False,
        inconsistency_codes=[],
        inconsistency_notes=[],
        raw={},
    )
