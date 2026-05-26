"""Data loaders for FinBalance paper figures."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from finbalance.figures.style import ABLATION_LABELS, MODEL_LABELS


@dataclass(frozen=True)
class ResultRun:
    label: str
    ablation_name: str
    model_id: str
    path: Path
    summary: dict[str, Any]
    evaluation: dict[str, Any]

    @property
    def records(self) -> int:
        return int(self.summary.get("records_evaluated") or 0)

    def metric(self, key: str) -> float:
        value = self.summary.get(key)
        return float(value) if value is not None else 0.0


DEFAULT_BASELINE_RUNS: tuple[tuple[str, str], ...] = (
    ("Gemini 3 Flash", "gemini3flash_main710/prompt_baseline"),
    ("GPT-5", "gpt5_main710/prompt_baseline"),
    ("Claude Haiku 4.5", "claude_haiku45_main710/prompt_baseline"),
    ("Grok 4.3", "grok43_main710/prompt_baseline"),
    ("Qwen3 235B", "qwen3_235b_main710/prompt_baseline"),
    ("DeepSeek Chat", "deepseek_chat_main710/prompt_baseline"),
)

DEFAULT_VERIFIER_MODEL_DIRS: tuple[tuple[str, str], ...] = (
    ("Gemini 3 Flash", "gemini3flash_promoted_coverage_full_clean"),
    ("DeepSeek V3.2", "deepseek_v32_sweep"),
    ("Qwen3 235B", "qwen3_235b_sweep_baseline"),
    ("Claude Haiku 4.5", "claude_haiku45_sweep_baseline"),
)

DEFAULT_GEMINI_ABLATION_DIRS: tuple[str, ...] = (
    "gemini3flash_ablation_coverage",
    "gemini3flash_promoted_coverage_full_clean",
)

DEFAULT_SELF_CONSISTENCY_RUN = "gemini3flash_self_consistency_gap/self_consistency_k3"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def load_result_run(path: Path, *, label: str | None = None) -> ResultRun | None:
    summary_path = path / "summary.json"
    evaluation_path = path / "evaluation.json"
    if not summary_path.exists() or not evaluation_path.exists():
        return None
    summary = load_json(summary_path)
    evaluation = load_json(evaluation_path)
    model_id = str(evaluation.get("model") or "")
    ablation_name = str(evaluation.get("ablation_name") or path.name)
    display = label or MODEL_LABELS.get(model_id) or ABLATION_LABELS.get(ablation_name) or ablation_name
    return ResultRun(
        label=display,
        ablation_name=ablation_name,
        model_id=model_id,
        path=path,
        summary=summary,
        evaluation=evaluation,
    )


def load_default_baselines(results_dir: Path, *, min_records: int = 100) -> list[ResultRun]:
    runs: list[ResultRun] = []
    for label, relative in DEFAULT_BASELINE_RUNS:
        run = load_result_run(results_dir / relative, label=label)
        if run and run.records >= min_records:
            runs.append(run)
    return runs


def load_ablation_group(results_dir: Path, relative_dir: str) -> dict[str, ResultRun]:
    root = results_dir / relative_dir
    if not root.exists():
        return {}
    runs: dict[str, ResultRun] = {}
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        run = load_result_run(child, label=ABLATION_LABELS.get(child.name))
        if run:
            runs[run.ablation_name] = run
    return runs


def load_default_gemini_ablation_rows(results_dir: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for group in DEFAULT_GEMINI_ABLATION_DIRS:
        runs = load_ablation_group(results_dir, group)
        baseline = runs.get("prompt_baseline")
        if not baseline:
            continue
        for name, run in runs.items():
            if name == "prompt_baseline":
                continue
            key = (name, group)
            if key in seen:
                continue
            seen.add(key)
            rows.append({"ablation": name, "run": run, "baseline": baseline, "group": group})

    self_consistency = load_result_run(
        results_dir / DEFAULT_SELF_CONSISTENCY_RUN,
        label=ABLATION_LABELS.get("self_consistency_k3"),
    )
    promoted = load_ablation_group(results_dir, "gemini3flash_promoted_coverage_full_clean")
    baseline = promoted.get("prompt_baseline")
    if self_consistency and baseline:
        subset_baseline = subset_baseline_for_run(baseline, self_consistency) or baseline
        rows.append(
            {
                "ablation": self_consistency.ablation_name,
                "run": self_consistency,
                "baseline": subset_baseline,
                "group": "gemini3flash_self_consistency_gap",
            }
        )
    return rows


def load_verifier_pairs(results_dir: Path, *, min_records: int = 100) -> list[tuple[str, ResultRun, ResultRun]]:
    pairs: list[tuple[str, ResultRun, ResultRun]] = []
    for label, relative in DEFAULT_VERIFIER_MODEL_DIRS:
        baseline = load_result_run(results_dir / relative / "prompt_baseline", label=label)
        verifier = load_result_run(results_dir / relative / "forced_ledger_verifier", label=label)
        if baseline and verifier and baseline.records >= min_records and verifier.records >= min_records:
            pairs.append((label, baseline, verifier))
    return pairs


def load_records(dataset_path: Path) -> list[dict[str, Any]]:
    return load_jsonl(dataset_path)


def load_bootstrap_comparisons(results_dir: Path, relative_dir: str) -> dict[tuple[str, str], dict[str, Any]]:
    path = results_dir / relative_dir / "bootstrap_summary.json"
    if not path.exists():
        return {}
    data = load_json(path)
    comparisons: dict[tuple[str, str], dict[str, Any]] = {}
    for row in data.get("comparisons", []):
        comparisons[(str(row.get("ablation_name")), str(row.get("metric")))] = row
    return comparisons


def subset_baseline_for_run(baseline: ResultRun, target: ResultRun) -> ResultRun | None:
    target_rows_path = target.path / "per_record_results.jsonl"
    if not target_rows_path.exists():
        return None
    target_ids = {row["record_id"] for row in load_jsonl(target_rows_path) if row.get("record_id")}
    if not target_ids:
        return None
    return subset_run_for_record_ids(baseline, target_ids, label=f"{baseline.label} subset")


def subset_run_for_record_ids(
    run: ResultRun,
    record_ids: set[str],
    *,
    label: str | None = None,
) -> ResultRun | None:
    rows_path = run.path / "per_record_results.jsonl"
    if not rows_path.exists() or not record_ids:
        return None
    rows = [row for row in load_jsonl(rows_path) if row.get("record_id") in record_ids]
    if not rows:
        return None
    summary = _summarize_per_record_rows(rows)
    evaluation = dict(run.evaluation)
    evaluation["summary"] = summary
    return ResultRun(
        label=label or f"{run.label} subset",
        ablation_name=run.ablation_name,
        model_id=run.model_id,
        path=run.path,
        summary=summary,
        evaluation=evaluation,
    )


def record_ids_for_run(run: ResultRun) -> set[str]:
    rows_path = run.path / "per_record_results.jsonl"
    if not rows_path.exists():
        return set()
    return {row["record_id"] for row in load_jsonl(rows_path) if row.get("record_id")}


def doc_ref_mismatch_rate(run: ResultRun) -> float:
    expected = float(run.summary.get("expected_entry_count") or 0.0)
    if expected <= 0:
        return float(run.summary.get("entries_accounting_correct_but_doc_refs_wrong_rate") or 0.0)
    return float(run.summary.get("doc_refs_mismatch_count") or 0.0) / expected


def _summarize_per_record_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    metric_rows = [row.get("metrics", {}) for row in rows]
    standard = [metrics for metrics in metric_rows if not metrics.get("expected_inconsistency")]
    inconsistency = [metrics for metrics in metric_rows if metrics.get("expected_inconsistency")]

    def rate(metric: str, population: list[dict[str, Any]] | None = None) -> float:
        selected = population if population is not None else standard
        if not selected:
            return 0.0
        return round(sum(1 for metrics in selected if metrics.get(metric)) / len(selected), 4)

    return {
        "records_evaluated": len(rows),
        "standard_records": len(standard),
        "inconsistency_records": len(inconsistency),
        "parse_success_count": sum(1 for metrics in metric_rows if metrics.get("parse_success")),
        "parse_success_rate": rate("parse_success", metric_rows),
        "predicted_entries_reconstruct_correct_final_balance_sheet_rate": rate(
            "predicted_entries_reconstruct_correct_final_balance_sheet"
        ),
        "final_balance_sheet_matches_rate": rate("final_balance_sheet_matches"),
        "final_journal_entries_match_no_doc_refs_rate": rate("final_journal_entries_match_no_doc_refs"),
        "final_balance_sheet_and_journal_entries_match_rate": rate(
            "final_balance_sheet_and_journal_entries_match"
        ),
        "inconsistency_code_match_rate": rate("inconsistency_code_matches", inconsistency),
        "cost_total": round(sum(float(row.get("cost") or 0.0) for row in rows), 6),
    }
