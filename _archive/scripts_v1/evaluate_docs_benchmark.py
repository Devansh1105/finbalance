#!/usr/bin/env python3
"""Run and analyze docs_benchmark evaluations."""

from __future__ import annotations

import csv
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from docs_benchmark.benchmark import (
    OpenRouterClient,
    filter_records,
    group_results_by_feature_flags,
    group_results_by_field,
    group_results_by_membership,
    load_records,
    run_openrouter_evaluation,
    summarize_result_subset,
)
from docs_benchmark.benchmark.analysis import summarize_expected_entry_groups


# Edit this section before running the script.
DATASET_NAME = "coverage"  # "coverage" or "main"
DATASET_RECORDS_PATH = PROJECT_ROOT / "docs_benchmark" / "data" / DATASET_NAME / "records.jsonl"
RUN_LABEL = "manual_eval"
MODELS: list[str] = []
INDUSTRIES: list[str] | None = None
PERIOD_TYPES: list[str] | None = None
DIFFICULTY_LEVELS: list[int] | None = None
RECORD_IDS: list[str] | None = None
MAX_RECORDS: int | None = None
OPENROUTER_API_KEY_ENV = "OPENROUTER_API_KEY"
TEMPERATURE = 0.0
MAX_OUTPUT_TOKENS = 12000
TIMEOUT_SECONDS = 300
OVERWRITE_EXISTING_RUN = True
WORST_CASE_COUNT = 25


def _safe_model_slug(model: str) -> str:
    return model.replace("/", "_").replace(":", "_")


def _load_jsonl_rows(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _metric_table(summary: dict[str, Any]) -> list[tuple[str, Any]]:
    return [
        ("Records Evaluated", summary["records_evaluated"]),
        ("Standard Records", summary["standard_records"]),
        ("Inconsistency Records", summary["inconsistency_records"]),
        ("Parse Success", summary["parse_success_rate"]),
        ("Journal Entries Matched (Exact)", summary["journal_entries_exact_record_match_rate"]),
        ("Journal Entries Matched (Ignoring Document References)", summary["journal_entries_accounting_record_match_rate"]),
        ("Entry Exact Posting Rate", summary["entry_exact_posting_rate"]),
        ("Entry Accounting Posting Rate", summary["entry_accounting_posting_rate"]),
        ("Final Balance Sheet Matched", summary["final_balance_sheet_matches_rate"]),
        ("Final Balance Sheet and Journal Entries Both Matched", summary["final_balance_sheet_and_journal_entries_match_rate"]),
        ("Entries Correct but Final Balance Sheet Wrong", summary["entries_correct_but_final_balance_sheet_wrong_rate"]),
        ("Entries Accounting-Correct but Document References Wrong", summary["entries_accounting_correct_but_doc_refs_wrong_rate"]),
        ("Predicted Entries Reconstruct Correct Final Balance Sheet", summary["predicted_entries_reconstruct_correct_final_balance_sheet_rate"]),
        ("Reported Balance Sheet Matches Reconstructed Balance Sheet", summary["predicted_balance_sheet_matches_reconstructed_balance_sheet_rate"]),
        ("False Inconsistency Alarm", summary["false_inconsistency_alarm_rate"]),
        ("Inconsistency Flag Matched", summary["inconsistency_flag_match_rate"]),
        ("Inconsistency Code Matched", summary["inconsistency_code_match_rate"]),
        ("Inconsistency Empty-Answer Contract Matched", summary["inconsistency_empty_answer_rate"]),
        ("Missed Inconsistency", summary["missed_inconsistency_rate"]),
        ("Average Missing Entries per Standard Record", summary["average_missing_entries_per_standard_record"]),
        ("Average Extra Entries per Standard Record", summary["average_extra_entries_per_standard_record"]),
        ("Total Cost", summary["cost_total"]),
        ("Average Cost per Record", summary["cost_average_per_record"]),
    ]


def _format_value(value: Any) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(_format_value(cell) for cell in row) + " |")
    return "\n".join(lines)


def _summary_rows(grouped: dict[str, dict[str, Any]], *, limit: int | None = None) -> list[list[Any]]:
    ordered = sorted(
        grouped.items(),
        key=lambda item: (
            item[1].get("journal_entries_exact_record_match_rate", 0.0),
            item[1].get("final_balance_sheet_matches_rate", 0.0),
        ),
    )
    if limit is not None:
        ordered = ordered[:limit]
    rows: list[list[Any]] = []
    for group, summary in ordered:
        rows.append(
            [
                group,
                summary["records_evaluated"],
                summary["journal_entries_exact_record_match_rate"],
                summary["journal_entries_accounting_record_match_rate"],
                summary["final_balance_sheet_matches_rate"],
                summary["entries_correct_but_final_balance_sheet_wrong_rate"],
                summary["false_inconsistency_alarm_rate"],
                summary["inconsistency_flag_match_rate"],
            ]
        )
    return rows


def _top_failure_rows(
    grouped: dict[str, dict[str, Any]],
    *,
    primary_key: str,
    secondary_key: str | None = None,
    limit: int = 10,
) -> list[list[Any]]:
    ordered = sorted(
        grouped.items(),
        key=lambda item: (
            item[1].get(primary_key, 0.0),
            item[1].get(secondary_key, 0.0) if secondary_key else 0.0,
            -item[1].get("records_evaluated", 0),
        ),
    )[:limit]
    rows: list[list[Any]] = []
    for group, summary in ordered:
        rows.append(
            [
                group,
                summary["records_evaluated"],
                summary["journal_entries_exact_record_match_rate"],
                summary["journal_entries_accounting_record_match_rate"],
                summary["final_balance_sheet_matches_rate"],
                summary["inconsistency_flag_match_rate"],
            ]
        )
    return rows


def _write_summary_csv(path: Path, grouped: dict[str, dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    headers = [
        "group",
        "records_evaluated",
        "standard_records",
        "inconsistency_records",
        "parse_success_rate",
        "journal_entries_exact_record_match_rate",
        "journal_entries_accounting_record_match_rate",
        "entry_exact_posting_rate",
        "entry_accounting_posting_rate",
        "final_balance_sheet_matches_rate",
        "final_balance_sheet_and_journal_entries_match_rate",
        "entries_correct_but_final_balance_sheet_wrong_rate",
        "entries_accounting_correct_but_doc_refs_wrong_rate",
        "predicted_entries_reconstruct_correct_final_balance_sheet_rate",
        "predicted_balance_sheet_matches_reconstructed_balance_sheet_rate",
        "false_inconsistency_alarm_rate",
        "inconsistency_flag_match_rate",
        "inconsistency_code_match_rate",
        "inconsistency_empty_answer_rate",
        "missed_inconsistency_rate",
        "average_missing_entries_per_standard_record",
        "average_extra_entries_per_standard_record",
        "cost_total",
        "cost_average_per_record",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        for group, summary in sorted(grouped.items()):
            row = {"group": group}
            row.update({key: summary.get(key) for key in headers if key != "group"})
            writer.writerow(row)


def _write_expected_entry_csv(path: Path, grouped: dict[str, dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    headers = [
        "group",
        "expected_entries",
        "exact_entry_rate",
        "accounting_entry_rate",
        "doc_refs_mismatch_rate",
        "wrong_amount_rate",
        "wrong_account_rate",
        "missing_rate",
        "parse_or_output_failure_rate",
        "doc_ref_linking_failure_rate",
        "direct_doc_reasoning_failure_rate",
        "derived_reasoning_failure_rate",
        "exact_entry_count",
        "doc_refs_mismatch_count",
        "wrong_amount_count",
        "wrong_account_count",
        "missing_count",
        "parse_or_output_failure_count",
        "doc_ref_linking_failure_count",
        "direct_doc_reasoning_failure_count",
        "derived_reasoning_failure_count",
        "dominant_failure_mode",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        for group, summary in sorted(grouped.items()):
            row = {"group": group}
            row.update({key: summary.get(key) for key in headers if key != "group"})
            writer.writerow(row)


def _worst_case_score(result: dict[str, Any]) -> tuple[int, int, int, int]:
    metrics = result["metrics"]
    if metrics["expected_inconsistency"]:
        return (
            1 if metrics["missed_inconsistency"] else 0,
            1 if not metrics["inconsistency_code_matches"] else 0,
            0,
            0,
        )
    return (
        1 if not metrics["parse_success"] else 0,
        metrics["missing_entry_count"] + metrics["extra_entry_count"],
        metrics["wrong_account_count"] + metrics["wrong_amount_count"],
        1 if not metrics["final_balance_sheet_matches"] else 0,
    )


def _build_run_summary(evaluation: dict[str, Any]) -> dict[str, Any]:
    results = evaluation["results"]
    return {
        "overall": summarize_result_subset(results),
        "by_industry": group_results_by_field(results, "industry"),
        "by_period_type": group_results_by_field(results, "period_type"),
        "by_difficulty": group_results_by_field(results, "difficulty_level"),
        "by_tax_regime": group_results_by_field(results, "tax_regime"),
        "by_currency_code": group_results_by_field(results, "currency_code"),
        "by_date_format": group_results_by_field(results, "date_format"),
        "by_expected_inconsistency_code": group_results_by_field(results, "expected_inconsistency_code"),
        "by_feature_flag": group_results_by_feature_flags(results),
        "by_scenario": group_results_by_membership(results, "scenario_sequence"),
        "by_doc_type": group_results_by_membership(results, "doc_types_present"),
        "by_doc_role": group_results_by_membership(results, "doc_roles_present"),
        "by_posting_label": group_results_by_membership(results, "posting_labels_present"),
        "by_ledger_family": group_results_by_membership(results, "ledger_families_present"),
        "expected_entries_by_posting_label": summarize_expected_entry_groups(results, "posting_label"),
        "expected_entries_by_ledger_family": summarize_expected_entry_groups(results, "ledger_family"),
        "expected_entries_by_doc_type": summarize_expected_entry_groups(results, "doc_type"),
    }


def _write_summary_markdown(path: Path, model: str, dataset_path: Path, summary: dict[str, Any]) -> None:
    overall = summary["overall"]
    inconsistency_groups = {
        group: values
        for group, values in summary["by_expected_inconsistency_code"].items()
        if group != "none"
    }
    lines = [
        f"# docs_benchmark Summary: `{model}`",
        "",
        f"- Dataset: `{dataset_path}`",
        f"- Records evaluated: `{overall['records_evaluated']}`",
        f"- Standard records: `{overall['standard_records']}`",
        f"- Inconsistency records: `{overall['inconsistency_records']}`",
        f"- Total cost: `{overall['cost_total']}`",
        "",
        "## Overall Metrics",
        "",
        _markdown_table(
            ["Metric", "Value"],
            [[label, value] for label, value in _metric_table(overall)],
        ),
        "",
        "## By Industry",
        "",
        "_Worst exact journal-entry match rate first._",
        "",
        _markdown_table(
            [
                "Industry",
                "Records",
                "JE Exact",
                "JE Accounting",
                "BS Exact",
                "Entries Exact but BS Wrong",
                "False Inconsistency Alarm",
                "Inconsistency Flag Match",
            ],
            _summary_rows(summary["by_industry"]),
        ),
        "",
        "## By Period Type",
        "",
        "_Worst exact journal-entry match rate first._",
        "",
        _markdown_table(
            [
                "Period",
                "Records",
                "JE Exact",
                "JE Accounting",
                "BS Exact",
                "Entries Exact but BS Wrong",
                "False Inconsistency Alarm",
                "Inconsistency Flag Match",
            ],
            _summary_rows(summary["by_period_type"]),
        ),
        "",
        "## By Difficulty",
        "",
        "_Worst exact journal-entry match rate first._",
        "",
        _markdown_table(
            [
                "Difficulty",
                "Records",
                "JE Exact",
                "JE Accounting",
                "BS Exact",
                "Entries Exact but BS Wrong",
                "False Inconsistency Alarm",
                "Inconsistency Flag Match",
            ],
            _summary_rows(summary["by_difficulty"]),
        ),
        "",
        "## By Tax Regime",
        "",
        _markdown_table(
            [
                "Tax Regime",
                "Records",
                "JE Exact",
                "JE Accounting",
                "BS Exact",
                "Entries Exact but BS Wrong",
                "False Inconsistency Alarm",
                "Inconsistency Flag Match",
            ],
            _summary_rows(summary["by_tax_regime"]),
        ),
        "",
        "## By Currency / Date Format",
        "",
        "### Currency",
        "",
        _markdown_table(
            [
                "Currency",
                "Records",
                "JE Exact",
                "JE Accounting",
                "BS Exact",
                "Entries Exact but BS Wrong",
                "False Inconsistency Alarm",
                "Inconsistency Flag Match",
            ],
            _summary_rows(summary["by_currency_code"]),
        ),
        "",
        "### Date Format",
        "",
        _markdown_table(
            [
                "Date Format",
                "Records",
                "JE Exact",
                "JE Accounting",
                "BS Exact",
                "Entries Exact but BS Wrong",
                "False Inconsistency Alarm",
                "Inconsistency Flag Match",
            ],
            _summary_rows(summary["by_date_format"]),
        ),
        "",
        "## Where The Model Fails",
        "",
        f"- Entries correct but final balance sheet wrong: `{overall['entries_correct_but_final_balance_sheet_wrong_rate']:.2%}`",
        f"- Entries accounting-correct but document references wrong: `{overall['entries_accounting_correct_but_doc_refs_wrong_rate']:.2%}`",
        f"- Predicted entries reconstruct the correct final balance sheet: `{overall['predicted_entries_reconstruct_correct_final_balance_sheet_rate']:.2%}`",
        f"- Reported balance sheet matches reconstructed balance sheet: `{overall['predicted_balance_sheet_matches_reconstructed_balance_sheet_rate']:.2%}`",
        f"- False inconsistency alarms on clean records: `{overall['false_inconsistency_alarm_rate']:.2%}`",
        f"- Missed inconsistencies on negative controls: `{overall['missed_inconsistency_rate']:.2%}`",
        "",
        "## Inconsistency Detection",
        "",
        _markdown_table(
            [
                "Inconsistency Code",
                "Records",
                "JE Exact",
                "JE Accounting",
                "BS Exact",
                "Inconsistency Flag Match",
            ],
            _top_failure_rows(
                inconsistency_groups,
                primary_key="inconsistency_flag_match_rate",
                secondary_key="inconsistency_code_match_rate",
            ),
        ),
        "",
        "## Worst Scenario Slices",
        "",
        "_Scenario slices overlap. A record can appear in multiple scenario rows._",
        "",
        _markdown_table(
            [
                "Scenario",
                "Records",
                "JE Exact",
                "JE Accounting",
                "BS Exact",
                "Inconsistency Flag Match",
            ],
            _top_failure_rows(
                summary["by_scenario"],
                primary_key="journal_entries_exact_record_match_rate",
                secondary_key="final_balance_sheet_matches_rate",
            ),
        ),
        "",
        "## Worst Document Types",
        "",
        _markdown_table(
            [
                "Document Type",
                "Records",
                "JE Exact",
                "JE Accounting",
                "BS Exact",
                "Inconsistency Flag Match",
            ],
            _top_failure_rows(
                summary["by_doc_type"],
                primary_key="journal_entries_exact_record_match_rate",
                secondary_key="final_balance_sheet_matches_rate",
            ),
        ),
        "",
        "## Worst Ledger Families",
        "",
        _markdown_table(
            [
                "Ledger Family",
                "Records",
                "JE Exact",
                "JE Accounting",
                "BS Exact",
                "Inconsistency Flag Match",
            ],
            _top_failure_rows(
                summary["by_ledger_family"],
                primary_key="journal_entries_exact_record_match_rate",
                secondary_key="final_balance_sheet_matches_rate",
            ),
        ),
        "",
        "## Worst Posting Labels",
        "",
        "_These rows now include the dominant failure mode for the missed expected entries._",
        "",
        _markdown_table(
            [
                "Posting Label",
                "Expected Entries",
                "Exact Entry Rate",
                "Accounting Entry Rate",
                "Dominant Failure Mode",
                "Doc Ref Linking",
                "Direct Reasoning",
                "Derived Reasoning",
                "Parse / Output",
            ],
            [
                [
                    group,
                    values["expected_entries"],
                    values["exact_entry_rate"],
                    values["accounting_entry_rate"],
                    values["dominant_failure_mode"],
                    values["doc_ref_linking_failure_rate"],
                    values["direct_doc_reasoning_failure_rate"],
                    values["derived_reasoning_failure_rate"],
                    values["parse_or_output_failure_rate"],
                ]
                for group, values in sorted(
                    summary["expected_entries_by_posting_label"].items(),
                    key=lambda item: item[1]["exact_entry_rate"],
                )[:10]
            ],
        ),
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_per_record_jsonl(path: Path, results: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for result in results:
            handle.write(json.dumps(result, ensure_ascii=True) + "\n")


def _write_worst_cases(path: Path, results: list[dict[str, Any]], record_lookup: dict[str, Any]) -> None:
    ranked = sorted(results, key=_worst_case_score, reverse=True)[:WORST_CASE_COUNT]
    payload: list[dict[str, Any]] = []
    for result in ranked:
        record = record_lookup[result["record_id"]]
        payload.append(
            {
                "record_id": result["record_id"],
                "industry": result["industry"],
                "period_type": result["period_type"],
                "difficulty_level": result["difficulty_level"],
                "record_features": result["record_features"],
                "metrics": result["metrics"],
                "parsed_submission": result["parsed_submission"],
                "reconstructed_balance_sheet": result["reconstructed_balance_sheet"],
                "expected_entries": [posting.__dict__ for posting in record.expected_entries],
                "expected_balance_sheet": record.expected_balance_sheet.flat(),
                "expected_balance_sheet_sections": {
                    "assets": record.expected_balance_sheet.assets,
                    "liabilities": record.expected_balance_sheet.liabilities,
                    "equity": record.expected_balance_sheet.equity,
                },
                "expected_inconsistency": record.expected_inconsistency,
                "expected_inconsistency_codes": record.expected_inconsistency_codes,
                "entry_diagnostics": result["entry_diagnostics"],
                "raw_response": result["raw_response"],
                "usage": result["usage"],
                "cost": result["cost"],
            }
        )
    _write_per_record_jsonl(path, payload)


def _write_cost_summary(path: Path, results: list[dict[str, Any]]) -> None:
    total_cost = round(sum(result.get("cost", 0.0) for result in results), 6)
    summary = {
        "records": len(results),
        "total_cost": total_cost,
        "average_cost_per_record": round(total_cost / len(results), 6) if results else 0.0,
        "prompt_tokens_total": sum(result.get("prompt_tokens", 0) for result in results),
        "completion_tokens_total": sum(result.get("completion_tokens", 0) for result in results),
        "total_tokens": sum(result.get("total_tokens", 0) for result in results),
        "most_expensive_records": sorted(
            [
                {
                    "record_id": result["record_id"],
                    "cost": result["cost"],
                    "prompt_tokens": result["prompt_tokens"],
                    "completion_tokens": result["completion_tokens"],
                }
                for result in results
            ],
            key=lambda item: item["cost"],
            reverse=True,
        )[:10],
    }
    path.write_text(json.dumps(summary, indent=2), encoding="utf-8")


def _write_model_outputs(model_dir: Path, dataset_path: Path, evaluation: dict[str, Any], summary: dict[str, Any], record_lookup: dict[str, Any]) -> None:
    model_dir.mkdir(parents=True, exist_ok=True)
    (model_dir / "evaluation.json").write_text(json.dumps(evaluation, indent=2), encoding="utf-8")
    (model_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    _write_summary_markdown(model_dir / "summary.md", evaluation["model"], dataset_path, summary)
    _write_per_record_jsonl(model_dir / "per_record_results.jsonl", evaluation["results"])
    _write_worst_cases(model_dir / "worst_cases.jsonl", evaluation["results"], record_lookup)
    _write_cost_summary(model_dir / "cost_summary.json", evaluation["results"])

    slice_dir = model_dir / "slice_tables"
    _write_summary_csv(slice_dir / "by_industry.csv", summary["by_industry"])
    _write_summary_csv(slice_dir / "by_period_type.csv", summary["by_period_type"])
    _write_summary_csv(slice_dir / "by_difficulty.csv", summary["by_difficulty"])
    _write_summary_csv(slice_dir / "by_tax_regime.csv", summary["by_tax_regime"])
    _write_summary_csv(slice_dir / "by_currency_code.csv", summary["by_currency_code"])
    _write_summary_csv(slice_dir / "by_date_format.csv", summary["by_date_format"])
    _write_summary_csv(slice_dir / "by_expected_inconsistency_code.csv", summary["by_expected_inconsistency_code"])
    _write_summary_csv(slice_dir / "by_feature_flag.csv", summary["by_feature_flag"])
    _write_summary_csv(slice_dir / "by_scenario.csv", summary["by_scenario"])
    _write_summary_csv(slice_dir / "by_doc_type.csv", summary["by_doc_type"])
    _write_summary_csv(slice_dir / "by_doc_role.csv", summary["by_doc_role"])
    _write_summary_csv(slice_dir / "by_posting_label.csv", summary["by_posting_label"])
    _write_summary_csv(slice_dir / "by_ledger_family.csv", summary["by_ledger_family"])
    _write_expected_entry_csv(slice_dir / "expected_entries_by_posting_label.csv", summary["expected_entries_by_posting_label"])
    _write_expected_entry_csv(slice_dir / "expected_entries_by_ledger_family.csv", summary["expected_entries_by_ledger_family"])
    _write_expected_entry_csv(slice_dir / "expected_entries_by_doc_type.csv", summary["expected_entries_by_doc_type"])


def _write_run_overview(path: Path, model_summaries: list[tuple[str, dict[str, Any]]]) -> None:
    rows = []
    for model, summary in model_summaries:
        overall = summary["overall"]
        rows.append(
            [
                model,
                overall["records_evaluated"],
                overall["journal_entries_exact_record_match_rate"],
                overall["journal_entries_accounting_record_match_rate"],
                overall["final_balance_sheet_matches_rate"],
                overall["inconsistency_flag_match_rate"],
                overall["cost_total"],
            ]
        )
    lines = [
        "# docs_benchmark Run Overview",
        "",
        _markdown_table(
            [
                "Model",
                "Records",
                "JE Exact",
                "JE Accounting",
                "BS Exact",
                "Inconsistency Flag Match",
                "Cost",
            ],
            rows,
        ),
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if not MODELS:
        raise SystemExit("Set MODELS at the top of scripts/evaluate_docs_benchmark.py before running.")

    api_key = os.environ.get(OPENROUTER_API_KEY_ENV)
    if not api_key:
        raise SystemExit(f"Missing {OPENROUTER_API_KEY_ENV} in the environment.")

    dataset_path = Path(DATASET_RECORDS_PATH)
    records = filter_records(
        load_records(dataset_path),
        industries=INDUSTRIES,
        period_types=PERIOD_TYPES,
        levels=DIFFICULTY_LEVELS,
        record_ids=RECORD_IDS,
        max_records=MAX_RECORDS,
    )
    if not records:
        raise SystemExit("No records matched the configured dataset filters.")

    results_root = PROJECT_ROOT / "docs_benchmark" / "results" / DATASET_NAME / RUN_LABEL
    if OVERWRITE_EXISTING_RUN and results_root.exists():
        shutil.rmtree(results_root)
    results_root.mkdir(parents=True, exist_ok=True)

    record_lookup = {record.record_id: record for record in records}
    model_summaries: list[tuple[str, dict[str, Any]]] = []

    print(f"Dataset: {dataset_path}")
    print(f"Records selected: {len(records)}")

    for model in MODELS:
        print(f"\nRunning model: {model}")
        client = OpenRouterClient(api_key=api_key, model=model)
        evaluation = run_openrouter_evaluation(
            records,
            client=client,
            dataset_path=str(dataset_path),
            temperature=TEMPERATURE,
            max_tokens=MAX_OUTPUT_TOKENS,
            timeout=TIMEOUT_SECONDS,
        )
        summary = _build_run_summary(evaluation)
        model_dir = results_root / _safe_model_slug(model)
        _write_model_outputs(model_dir, dataset_path, evaluation, summary, record_lookup)
        model_summaries.append((model, summary))

        overall = summary["overall"]
        print(f"  Parse Success: {_format_value(overall['parse_success_rate'])}")
        print(f"  Journal Entries Matched (Exact): {_format_value(overall['journal_entries_exact_record_match_rate'])}")
        print(
            "  Journal Entries Matched (Ignoring Document References): "
            f"{_format_value(overall['journal_entries_accounting_record_match_rate'])}"
        )
        print(f"  Final Balance Sheet Matched: {_format_value(overall['final_balance_sheet_matches_rate'])}")
        print(f"  Inconsistency Flag Matched: {_format_value(overall['inconsistency_flag_match_rate'])}")
        print(f"  Total Cost: {_format_value(overall['cost_total'])}")

    _write_run_overview(results_root / "run_overview.md", model_summaries)
    (results_root / "run_config.json").write_text(
        json.dumps(
            {
                "dataset_path": str(dataset_path),
                "models": MODELS,
                "industries": INDUSTRIES,
                "period_types": PERIOD_TYPES,
                "difficulty_levels": DIFFICULTY_LEVELS,
                "record_ids": RECORD_IDS,
                "max_records": MAX_RECORDS,
                "temperature": TEMPERATURE,
                "max_output_tokens": MAX_OUTPUT_TOKENS,
                "timeout_seconds": TIMEOUT_SECONDS,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"\nSaved benchmark results under {results_root}")


if __name__ == "__main__":
    main()
