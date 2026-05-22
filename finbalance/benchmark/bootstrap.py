"""Bootstrap comparison helpers for ablation result directories."""

from __future__ import annotations

import csv
import json
import random
from pathlib import Path
from typing import Any, Callable

from finbalance.schemas import ensure_parent


MetricFn = Callable[[list[dict[str, Any]]], float]


def analyze_ablation_bootstrap(
    results_dir: str | Path,
    *,
    baseline_name: str = "prompt_baseline",
    iterations: int = 5000,
    confidence: float = 0.95,
    seed: int = 1,
    output_dir: str | Path | None = None,
) -> dict[str, Any]:
    root = Path(results_dir)
    results_by_ablation = _load_ablation_results(root)
    if baseline_name not in results_by_ablation:
        raise ValueError(f"Baseline ablation '{baseline_name}' not found in {root}")

    baseline_by_id = {
        result["record_id"]: result for result in results_by_ablation[baseline_name]
    }
    rows: list[dict[str, Any]] = []
    rng = random.Random(seed)
    for ablation_name, results in sorted(results_by_ablation.items()):
        if ablation_name == baseline_name:
            continue
        ablation_by_id = {result["record_id"]: result for result in results}
        matched_ids = sorted(set(baseline_by_id) & set(ablation_by_id))
        if not matched_ids:
            continue
        baseline_results = [baseline_by_id[record_id] for record_id in matched_ids]
        ablation_results = [ablation_by_id[record_id] for record_id in matched_ids]
        for metric_name, metric_fn in _metric_functions().items():
            baseline_rate = metric_fn(baseline_results)
            ablation_rate = metric_fn(ablation_results)
            diffs = _bootstrap_diffs(
                baseline_results,
                ablation_results,
                metric_fn,
                iterations=iterations,
                confidence=confidence,
                rng=rng,
            )
            rows.append(
                {
                    "baseline_ablation": baseline_name,
                    "ablation_name": ablation_name,
                    "metric": metric_name,
                    "matched_records": len(matched_ids),
                    "baseline_rate": round(baseline_rate, 6),
                    "ablation_rate": round(ablation_rate, 6),
                    "diff": round(ablation_rate - baseline_rate, 6),
                    "ci_low": round(diffs["ci_low"], 6),
                    "ci_high": round(diffs["ci_high"], 6),
                    "iterations": int(iterations),
                    "confidence": float(confidence),
                }
            )

    summary = {
        "results_dir": str(root),
        "baseline_ablation": baseline_name,
        "iterations": int(iterations),
        "confidence": float(confidence),
        "seed": int(seed),
        "comparisons": rows,
    }
    if output_dir is not None:
        write_bootstrap_outputs(summary, output_dir)
    else:
        write_bootstrap_outputs(summary, root)
    return summary


def write_bootstrap_outputs(summary: dict[str, Any], output_dir: str | Path) -> None:
    output_root = Path(output_dir)
    ensure_parent(output_root / "bootstrap_summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )
    rows = summary.get("comparisons", [])
    path = ensure_parent(output_root / "bootstrap_summary.csv")
    fieldnames = [
        "baseline_ablation",
        "ablation_name",
        "metric",
        "matched_records",
        "baseline_rate",
        "ablation_rate",
        "diff",
        "ci_low",
        "ci_high",
        "iterations",
        "confidence",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _load_ablation_results(root: Path) -> dict[str, list[dict[str, Any]]]:
    results: dict[str, list[dict[str, Any]]] = {}
    for path in sorted(root.iterdir()):
        if not path.is_dir():
            continue
        records_path = path / "per_record_results.jsonl"
        if not records_path.exists():
            continue
        records = []
        with records_path.open(encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if line:
                    records.append(json.loads(line))
        results[path.name] = records
    return results


def _metric_functions() -> dict[str, MetricFn]:
    return {
        "predicted_entries_reconstruct_correct_final_balance_sheet_rate": _standard_bool_rate(
            "predicted_entries_reconstruct_correct_final_balance_sheet"
        ),
        "final_balance_sheet_matches_rate": _standard_bool_rate("final_balance_sheet_matches"),
        "final_journal_entries_match_no_doc_refs_rate": _standard_bool_rate(
            "final_journal_entries_match_no_doc_refs"
        ),
        "final_balance_sheet_and_journal_entries_match_rate": _standard_bool_rate(
            "final_balance_sheet_and_journal_entries_match"
        ),
        "inconsistency_code_match_rate": _inconsistency_bool_rate("inconsistency_code_matches"),
        "strict_doc_ref_mismatch_rate": _strict_doc_ref_mismatch_rate,
    }


def _standard_bool_rate(metric_key: str) -> MetricFn:
    def rate(results: list[dict[str, Any]]) -> float:
        subset = [
            result
            for result in results
            if not result.get("metrics", {}).get("expected_inconsistency")
        ]
        return _safe_rate(
            sum(1 for result in subset if result.get("metrics", {}).get(metric_key)),
            len(subset),
        )

    return rate


def _inconsistency_bool_rate(metric_key: str) -> MetricFn:
    def rate(results: list[dict[str, Any]]) -> float:
        subset = [
            result
            for result in results
            if result.get("metrics", {}).get("expected_inconsistency")
        ]
        return _safe_rate(
            sum(1 for result in subset if result.get("metrics", {}).get(metric_key)),
            len(subset),
        )

    return rate


def _strict_doc_ref_mismatch_rate(results: list[dict[str, Any]]) -> float:
    subset = [
        result
        for result in results
        if not result.get("metrics", {}).get("expected_inconsistency")
    ]
    numerator = sum(int(result.get("metrics", {}).get("doc_refs_mismatch_count", 0)) for result in subset)
    denominator = sum(int(result.get("metrics", {}).get("expected_entry_count", 0)) for result in subset)
    return _safe_rate(numerator, denominator)


def _bootstrap_diffs(
    baseline_results: list[dict[str, Any]],
    ablation_results: list[dict[str, Any]],
    metric_fn: MetricFn,
    *,
    iterations: int,
    confidence: float,
    rng: random.Random,
) -> dict[str, float]:
    if not baseline_results or not ablation_results:
        return {"ci_low": 0.0, "ci_high": 0.0}
    iterations = max(1, int(iterations))
    n = len(baseline_results)
    diffs: list[float] = []
    for _ in range(iterations):
        indices = [rng.randrange(n) for _ in range(n)]
        baseline_sample = [baseline_results[index] for index in indices]
        ablation_sample = [ablation_results[index] for index in indices]
        diffs.append(metric_fn(ablation_sample) - metric_fn(baseline_sample))
    diffs.sort()
    alpha = max(0.0, min(1.0, 1.0 - confidence))
    low_index = min(int((alpha / 2.0) * iterations), iterations - 1)
    high_index = min(int((1.0 - alpha / 2.0) * iterations), iterations - 1)
    return {"ci_low": diffs[low_index], "ci_high": diffs[high_index]}


def _safe_rate(numerator: int, denominator: int) -> float:
    if denominator <= 0:
        return 0.0
    return numerator / denominator
