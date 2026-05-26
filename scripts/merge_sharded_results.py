#!/usr/bin/env python3
"""Merge sharded ablation outputs into one canonical result directory."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from finbalance.benchmark.ablations import summarize_ablation_results, write_ablation_outputs


def _dataset_order(path: Path) -> list[str]:
    order: list[str] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                order.append(str(json.loads(line)["record_id"]))
    return order


def _load_rows(path: Path) -> list[dict]:
    rows_path = path / "per_record_results.jsonl"
    if not rows_path.exists():
        return []
    rows: list[dict] = []
    with rows_path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _row_rank(row: dict) -> tuple[int, int]:
    """Prefer successful parses, then non-empty completions, when merging retries."""
    metrics = row.get("metrics") or {}
    parse_success = 1 if metrics.get("parse_success") else 0
    has_completion = 1 if str(row.get("raw_completion") or "").strip() else 0
    return (parse_success, has_completion)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", default="data/main/records.jsonl")
    parser.add_argument("--results-dir", default="results")
    parser.add_argument("--target", required=True, help="Canonical output group under results-dir")
    parser.add_argument("--sources", nargs="+", required=True, help="Source groups under results-dir")
    parser.add_argument("--ablation", default="prompt_baseline")
    parser.add_argument(
        "--prefer-best-duplicates",
        action="store_true",
        help="Allow duplicate record IDs from retry dirs and keep the best parsed row",
    )
    args = parser.parse_args()

    results_dir = Path(args.results_dir)
    order = _dataset_order(Path(args.dataset))
    order_index = {record_id: idx for idx, record_id in enumerate(order)}
    rows_by_id: dict[str, dict] = {}
    metadata: dict | None = None

    for source in args.sources:
        ablation_dir = results_dir / source / args.ablation
        evaluation_path = ablation_dir / "evaluation.json"
        if metadata is None and evaluation_path.exists():
            metadata = json.loads(evaluation_path.read_text(encoding="utf-8"))
        for row in _load_rows(ablation_dir):
            record_id = str(row.get("record_id"))
            if record_id in rows_by_id:
                if not args.prefer_best_duplicates:
                    raise SystemExit(f"duplicate record_id {record_id} from {source}")
                if _row_rank(row) > _row_rank(rows_by_id[record_id]):
                    rows_by_id[record_id] = row
                continue
            rows_by_id[record_id] = row

    missing = [record_id for record_id in order if record_id not in rows_by_id]
    extra = [record_id for record_id in rows_by_id if record_id not in order_index]
    if missing or extra:
        raise SystemExit(f"cannot merge: missing={len(missing)} extra={len(extra)}")
    if metadata is None:
        raise SystemExit("no evaluation metadata found in sources")

    rows = [rows_by_id[record_id] for record_id in order]
    evaluation = dict(metadata)
    evaluation.update(
        {
            "dataset_path": args.dataset,
            "run_completed_at": datetime.now(timezone.utc).isoformat(),
            "summary": summarize_ablation_results(rows),
            "results": rows,
        }
    )
    output = write_ablation_outputs(evaluation, results_dir / args.target)
    parsed = sum(1 for row in rows if row.get("metrics", {}).get("parse_success"))
    print(json.dumps({"output": str(output), "rows": len(rows), "parse_success": parsed, "errors": len(rows) - parsed}, indent=2))


if __name__ == "__main__":
    main()
