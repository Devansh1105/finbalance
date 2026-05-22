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
from docs_benchmark.benchmark.model import OpenRouterRequestError
from docs_benchmark.benchmark.parser import SubmissionParseError, parse_submission
from docs_benchmark.benchmark.prompt import (
    PROMPT_VARIANT_BASELINE,
    PROMPT_VARIANT_BALANCE_RECONSTRUCTION,
    PROMPT_VARIANT_DOC_REFS_STRICT,
    PROMPT_VARIANT_GUIDED_PRIVATE_SOLVE,
    PROMPT_VARIANT_SELF_CHECK,
    PROMPT_VARIANTS,
    VISIBILITY_VARIANT_EVIDENCE_ONLY,
    VISIBILITY_VARIANT_EVIDENCE_PLUS_15_DISTRACTORS,
    VISIBILITY_VARIANT_EVIDENCE_PLUS_30_DISTRACTORS,
    VISIBILITY_VARIANT_EVIDENCE_PLUS_5_DISTRACTORS,
    VISIBILITY_VARIANT_EVIDENCE_RELEVANT_LAST,
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
    TOOL_VARIANT_FORCED_LEDGER_VERIFIER,
    TOOL_VARIANT_FORCED_LEDGER_VERIFIER_2PASS,
    TOOL_VARIANT_FULL_TOOL_AGENT,
    TOOL_VARIANT_LEDGER_CHECK,
    TOOL_VARIANT_NO_TOOLS,
    TOOL_VARIANT_SELF_CONSISTENCY_K3,
    TOOL_VARIANTS,
    TOOLS_BY_VARIANT,
    ChatClient,
    ToolAgentResult,
    run_forced_ledger_verifier_completion,
    run_no_tool_completion,
    run_self_consistency_completion,
    run_tool_agent_completion,
)
from docs_benchmark.schemas import DocumentRecord, ParsedSubmission, ensure_parent


FATAL_PROVIDER_STATUS_CODES = {401, 402, 403, 404}


class FatalAblationRunError(RuntimeError):
    """Provider failure that should stop the run instead of producing parse-zero rows."""


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

TARGETED_ABLATION_SPECS = (
    AblationSpec("prompt_baseline"),
    AblationSpec("forced_ledger_verifier", tool_variant=TOOL_VARIANT_FORCED_LEDGER_VERIFIER),
    AblationSpec("forced_ledger_verifier_2pass", tool_variant=TOOL_VARIANT_FORCED_LEDGER_VERIFIER_2PASS),
    AblationSpec("self_consistency_k3", tool_variant=TOOL_VARIANT_SELF_CONSISTENCY_K3),
    AblationSpec("prompt_balance_reconstruction", prompt_variant=PROMPT_VARIANT_BALANCE_RECONSTRUCTION),
    AblationSpec("prompt_doc_refs_strict", prompt_variant=PROMPT_VARIANT_DOC_REFS_STRICT),
    AblationSpec("evidence_only", visibility_variant=VISIBILITY_VARIANT_EVIDENCE_ONLY),
    AblationSpec("evidence_plus_5_distractors", visibility_variant=VISIBILITY_VARIANT_EVIDENCE_PLUS_5_DISTRACTORS),
    AblationSpec("evidence_plus_15_distractors", visibility_variant=VISIBILITY_VARIANT_EVIDENCE_PLUS_15_DISTRACTORS),
    AblationSpec("evidence_plus_30_distractors", visibility_variant=VISIBILITY_VARIANT_EVIDENCE_PLUS_30_DISTRACTORS),
    AblationSpec("evidence_relevant_last", visibility_variant=VISIBILITY_VARIANT_EVIDENCE_RELEVANT_LAST),
)

CONTEXT_STRESS_ABLATION_SPECS = (
    AblationSpec("prompt_baseline"),
    AblationSpec("evidence_only", visibility_variant=VISIBILITY_VARIANT_EVIDENCE_ONLY),
    AblationSpec("evidence_plus_5_distractors", visibility_variant=VISIBILITY_VARIANT_EVIDENCE_PLUS_5_DISTRACTORS),
    AblationSpec("evidence_plus_15_distractors", visibility_variant=VISIBILITY_VARIANT_EVIDENCE_PLUS_15_DISTRACTORS),
    AblationSpec("evidence_plus_30_distractors", visibility_variant=VISIBILITY_VARIANT_EVIDENCE_PLUS_30_DISTRACTORS),
    AblationSpec("evidence_relevant_last", visibility_variant=VISIBILITY_VARIANT_EVIDENCE_RELEVANT_LAST),
)

ABLATION_MATRICES = {
    "coverage": COVERAGE_ABLATION_SPECS,
    "targeted": TARGETED_ABLATION_SPECS,
    "context_stress": CONTEXT_STRESS_ABLATION_SPECS,
}

ALL_ABLATION_SPECS = tuple(
    {spec.name: spec for specs in ABLATION_MATRICES.values() for spec in specs}.values()
)

CONTEXT_PADDING_BY_VARIANT = {
    VISIBILITY_VARIANT_EVIDENCE_ONLY: 0,
    VISIBILITY_VARIANT_EVIDENCE_PLUS_5_DISTRACTORS: 5,
    VISIBILITY_VARIANT_EVIDENCE_PLUS_15_DISTRACTORS: 15,
    VISIBILITY_VARIANT_EVIDENCE_PLUS_30_DISTRACTORS: 30,
    VISIBILITY_VARIANT_EVIDENCE_RELEVANT_LAST: 15,
}


SLICE_FIELDS = (
    "difficulty_level",
    "industry",
    "period_type",
    "tax_regime",
    "expected_inconsistency_code",
    "document_count",
    "visible_document_count",
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
    if matrix not in ABLATION_MATRICES:
        raise ValueError(f"Unknown ablation matrix '{matrix}'")
    specs = list(ABLATION_MATRICES[matrix])
    if not names:
        return specs
    by_name = {spec.name: spec for spec in ALL_ABLATION_SPECS}
    missing = [name for name in names if name not in by_name]
    if missing:
        raise ValueError(f"Unknown ablation names: {', '.join(missing)}")
    return [by_name[name] for name in names]


def apply_visibility_variant(
    record: DocumentRecord,
    visibility_variant: str,
    *,
    corpus_records: list[DocumentRecord] | None = None,
) -> tuple[DocumentRecord, dict[str, Any]]:
    if visibility_variant not in VISIBILITY_VARIANTS:
        raise ValueError(f"Unknown visibility variant '{visibility_variant}'")

    documents = list(record.documents)
    allowed_accounts = list(record.allowed_accounts)
    injected_documents: list[dict[str, Any]] = []
    kept_evidence_doc_ids: list[str] = []
    padding_doc_ids: list[str] = []
    if visibility_variant == VISIBILITY_VARIANT_NO_DISTRACTORS_ORACLE:
        documents = [document for document in documents if document.role != "distractor_doc"]
    elif visibility_variant == VISIBILITY_VARIANT_SUPPORT_DOCS_REMOVED:
        documents = [document for document in documents if document.role != "support_doc"]
    elif visibility_variant == VISIBILITY_VARIANT_NO_ALLOWED_ACCOUNTS:
        allowed_accounts = []
    elif visibility_variant in CONTEXT_PADDING_BY_VARIANT:
        documents, context_metadata = _context_documents_for_variant(
            record,
            visibility_variant,
            corpus_records=corpus_records or [record],
        )
        kept_evidence_doc_ids = context_metadata["kept_evidence_doc_ids"]
        padding_doc_ids = context_metadata["padding_doc_ids"]
        injected_documents = context_metadata["injected_documents"]

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
        "kept_evidence_doc_ids": kept_evidence_doc_ids,
        "padding_doc_ids": padding_doc_ids,
        "injected_documents": injected_documents,
        "original_allowed_account_count": len(record.allowed_accounts),
        "visible_allowed_account_count": len(allowed_accounts),
    }


def _context_documents_for_variant(
    record: DocumentRecord,
    visibility_variant: str,
    *,
    corpus_records: list[DocumentRecord],
) -> tuple[list[Any], dict[str, Any]]:
    target_padding = CONTEXT_PADDING_BY_VARIANT[visibility_variant]
    relevant_last = visibility_variant == VISIBILITY_VARIANT_EVIDENCE_RELEVANT_LAST
    evidence_doc_ids = _evidence_document_ids(record)
    original_by_id = {document.doc_id: document for document in record.documents}
    evidence_documents = [document for document in record.documents if document.doc_id in evidence_doc_ids]

    padding_documents: list[Any] = []
    for document in record.documents:
        if len(padding_documents) >= target_padding:
            break
        if document.doc_id in evidence_doc_ids or document.role != "distractor_doc":
            continue
        padding_documents.append(document)

    injected_documents: list[dict[str, Any]] = []
    injected_index = 1
    if len(padding_documents) < target_padding:
        for source_record in corpus_records:
            if len(padding_documents) >= target_padding:
                break
            if source_record.record_id == record.record_id:
                continue
            for source_document in source_record.documents:
                if len(padding_documents) >= target_padding:
                    break
                if source_document.role != "distractor_doc":
                    continue
                new_doc_id = f"PX{injected_index:03d}"
                while new_doc_id in original_by_id:
                    injected_index += 1
                    new_doc_id = f"PX{injected_index:03d}"
                injected_index += 1
                padding_documents.append(
                    replace(
                        source_document,
                        doc_id=new_doc_id,
                        metadata={
                            **source_document.metadata,
                            "injected_from_record_id": source_record.record_id,
                            "injected_from_doc_id": source_document.doc_id,
                        },
                    )
                )
                injected_documents.append(
                    {
                        "new_doc_id": new_doc_id,
                        "source_record_id": source_record.record_id,
                        "source_doc_id": source_document.doc_id,
                    }
                )

    if relevant_last:
        documents = padding_documents + evidence_documents
    else:
        documents = evidence_documents + padding_documents
    return documents, {
        "kept_evidence_doc_ids": [document.doc_id for document in evidence_documents],
        "padding_doc_ids": [document.doc_id for document in padding_documents],
        "injected_documents": injected_documents,
    }


def _evidence_document_ids(record: DocumentRecord) -> set[str]:
    evidence_doc_ids = {
        document.doc_id
        for document in record.documents
        if document.doc_type == "opening_trial_balance"
        or document.title.strip().lower() == "opening trial balance"
    }
    for entry in record.expected_entries:
        evidence_doc_ids.update(str(doc_ref) for doc_ref in entry.doc_refs)

    if record.expected_inconsistency and not record.expected_entries:
        evidence_doc_ids.update(
            document.doc_id for document in record.documents if document.role != "distractor_doc"
        )

    return evidence_doc_ids


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
    existing_results: list[dict[str, Any]] | None = None,
    checkpoint_output_root: str | Path | None = None,
    checkpoint_every: int = 0,
    abort_on_max_token_parse_failure: bool = False,
) -> dict[str, Any]:
    started_at = datetime.now(timezone.utc).isoformat()
    results: list[dict[str, Any]] = []
    existing_by_record_id = {
        str(result.get("record_id")): result
        for result in (existing_results or [])
        if result.get("record_id")
    }
    checkpoint_every = max(int(checkpoint_every), 0)

    for record in records:
        if record.record_id in existing_by_record_id:
            results.append(existing_by_record_id[record.record_id])
            continue

        visible_record, visibility_metadata = apply_visibility_variant(
            record,
            spec.visibility_variant,
            corpus_records=records,
        )
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
            elif spec.tool_variant in {
                TOOL_VARIANT_FORCED_LEDGER_VERIFIER,
                TOOL_VARIANT_FORCED_LEDGER_VERIFIER_2PASS,
            }:
                completion = run_forced_ledger_verifier_completion(
                    visible_record,
                    client,
                    prompt,
                    verifier_passes=2
                    if spec.tool_variant == TOOL_VARIANT_FORCED_LEDGER_VERIFIER_2PASS
                    else 1,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    timeout=timeout,
                )
            elif spec.tool_variant == TOOL_VARIANT_SELF_CONSISTENCY_K3:
                completion = run_self_consistency_completion(
                    visible_record,
                    client,
                    prompt,
                    samples=3,
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
            if _is_fatal_provider_error(exc):
                if checkpoint_output_root is not None and results:
                    _write_ablation_checkpoint(
                        records=results,
                        client=client,
                        dataset_path=dataset_path,
                        spec=spec,
                        backend_name=backend_name,
                        started_at=started_at,
                        temperature=temperature,
                        max_tokens=max_tokens,
                        timeout=timeout,
                        agent_max_steps=agent_max_steps,
                        output_root=checkpoint_output_root,
                    )
                raise FatalAblationRunError(
                    f"Stopping {spec.name} on record {record.record_id}: {exc}"
                ) from exc
            error_message = str(exc)

        usage = dict(completion.response_payload.get("usage", {})) if isinstance(completion.response_payload, dict) else {}
        if (
            abort_on_max_token_parse_failure
            and not parse_success
            and int(usage.get("completion_tokens", 0)) >= int(max_tokens)
        ):
            if checkpoint_output_root is not None and results:
                _write_ablation_checkpoint(
                    records=results,
                    client=client,
                    dataset_path=dataset_path,
                    spec=spec,
                    backend_name=backend_name,
                    started_at=started_at,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    timeout=timeout,
                    agent_max_steps=agent_max_steps,
                    output_root=checkpoint_output_root,
                )
            raise FatalAblationRunError(
                f"Stopping {spec.name} on record {record.record_id}: response hit max_tokens={max_tokens} "
                "and did not parse as benchmark JSON"
            )

        analysis = analyze_submission(record, parsed, parse_success=parse_success)
        record_features = record_manifest_row(record)
        result = {
            "record_id": record.record_id,
            "industry": record.industry,
            "difficulty_level": record.difficulty_level,
            "period_type": record.metadata.get("period_type"),
            "period_label": record.metadata.get("period_label"),
            "visible_document_count": visibility_metadata["visible_document_count"],
            "ablation_name": spec.name,
            "prompt_variant": spec.prompt_variant,
            "visibility_variant": spec.visibility_variant,
            "tool_variant": spec.tool_variant,
            "agent_max_steps": int(agent_max_steps),
            "tool_calls": completion.tool_calls,
            "tool_call_failures": completion.tool_call_failures,
            "verifier_passes": completion.verifier_passes,
            "verifier_feedback": completion.verifier_feedback,
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
        if checkpoint_output_root is not None and checkpoint_every and len(results) % checkpoint_every == 0:
            _write_ablation_checkpoint(
                records=results,
                client=client,
                dataset_path=dataset_path,
                spec=spec,
                backend_name=backend_name,
                started_at=started_at,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=timeout,
                agent_max_steps=agent_max_steps,
                output_root=checkpoint_output_root,
            )

    evaluation = {
        "dataset_path": dataset_path,
        "model": client.model,
        "backend": backend_name,
        "ablation_name": spec.name,
        "prompt_variant": spec.prompt_variant,
        "visibility_variant": spec.visibility_variant,
        "tool_variant": spec.tool_variant,
        "reasoning_effort": getattr(client, "reasoning_effort", None),
        "agent_max_steps": int(agent_max_steps),
        "run_started_at": started_at,
        "run_completed_at": datetime.now(timezone.utc).isoformat(),
        "temperature": temperature,
        "max_tokens": max_tokens,
        "timeout": timeout,
        "summary": summarize_ablation_results(results),
        "results": results,
    }
    if checkpoint_output_root is not None:
        write_ablation_outputs(evaluation, checkpoint_output_root)
    return evaluation


def load_existing_ablation_results(
    output_root: str | Path,
    ablation_name: str,
    *,
    parse_success_only: bool = False,
) -> list[dict[str, Any]]:
    path = Path(output_root) / ablation_name / "per_record_results.jsonl"
    if not path.exists():
        return []
    results = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped:
                result = json.loads(stripped)
                if parse_success_only and not result.get("metrics", {}).get("parse_success", False):
                    continue
                results.append(result)
    return results


def _write_ablation_checkpoint(
    *,
    records: list[dict[str, Any]],
    client: ChatClient,
    dataset_path: str,
    spec: AblationSpec,
    backend_name: str,
    started_at: str,
    temperature: float,
    max_tokens: int,
    timeout: int,
    agent_max_steps: int,
    output_root: str | Path,
) -> None:
    evaluation = {
        "dataset_path": dataset_path,
        "model": client.model,
        "backend": backend_name,
        "ablation_name": spec.name,
        "prompt_variant": spec.prompt_variant,
        "visibility_variant": spec.visibility_variant,
        "tool_variant": spec.tool_variant,
        "reasoning_effort": getattr(client, "reasoning_effort", None),
        "agent_max_steps": int(agent_max_steps),
        "run_started_at": started_at,
        "run_completed_at": datetime.now(timezone.utc).isoformat(),
        "temperature": temperature,
        "max_tokens": max_tokens,
        "timeout": timeout,
        "summary": summarize_ablation_results(records),
        "results": records,
    }
    write_ablation_outputs(evaluation, output_root)


def _is_fatal_provider_error(exc: Exception) -> bool:
    status_code = getattr(exc, "status_code", None)
    if isinstance(exc, OpenRouterRequestError):
        status_code = exc.status_code
    return int(status_code) in FATAL_PROVIDER_STATUS_CODES if status_code is not None else False


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
    summary["verifier_passes_total"] = sum(int(result.get("verifier_passes", 0)) for result in results)
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
