#!/usr/bin/env python3
"""Generate paper-ready FinBalance figures and diagrams."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from finbalance.figures import generate_all_figures


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results-dir", default="results", help="Directory containing evaluation result folders.")
    parser.add_argument("--dataset", default="data/coverage/records.jsonl", help="Dataset JSONL used for composition plots.")
    parser.add_argument("--output-dir", default="paper/figures", help="Directory for generated PDF/PNG figures.")
    parser.add_argument(
        "--min-model-records",
        type=int,
        default=100,
        help="Minimum evaluated records required for inclusion in model-comparison plots.",
    )
    args = parser.parse_args()

    generated = generate_all_figures(
        results_dir=args.results_dir,
        dataset_path=args.dataset,
        output_dir=args.output_dir,
        min_model_records=args.min_model_records,
    )
    print(json.dumps(generated, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

