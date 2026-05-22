#!/usr/bin/env python3
"""Generate a custom FinBalance dataset bundle.

Example:
    python scripts/generate_dataset.py \
      --output-dir data/custom_retail \
      --records 50 \
      --industries retail subscription_saas \
      --period-types month quarter \
      --levels 2 3 4 \
      --negative-control-rate 0.10
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from finbalance.generation.helpers import PERIOD_TYPES
from finbalance.generation.user_dataset import DIFFICULTY_LEVELS, UserDatasetConfig, generate_user_dataset
from finbalance.industry_schemas import INDUSTRIES


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate an easy custom FinBalance dataset bundle.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--output-dir", default="data/custom", help="Directory for records.jsonl, assets, and manifests")
    parser.add_argument("--dataset-name", default="custom", help="Name stored in manifest.json")

    size = parser.add_mutually_exclusive_group()
    size.add_argument("--records", type=int, default=24, help="Exact number of records to generate")
    size.add_argument("--records-per-combo", type=int, help="Records per selected industry x period x difficulty cell")

    parser.add_argument("--industries", nargs="+", choices=INDUSTRIES, default=list(INDUSTRIES))
    parser.add_argument("--period-types", nargs="+", choices=PERIOD_TYPES, default=list(PERIOD_TYPES))
    parser.add_argument("--levels", nargs="+", type=int, choices=DIFFICULTY_LEVELS, default=list(DIFFICULTY_LEVELS))
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--negative-control-rate", type=float, default=0.05)
    parser.add_argument("--clean-only", action="store_true", help="Shortcut for --negative-control-rate 0.0")
    parser.add_argument("--overwrite", action="store_true", help="Delete an existing non-empty output directory first")
    args = parser.parse_args()

    negative_control_rate = 0.0 if args.clean_only else args.negative_control_rate
    config = UserDatasetConfig(
        output_dir=args.output_dir,
        dataset_name=args.dataset_name,
        records=None if args.records_per_combo is not None else args.records,
        records_per_combo=args.records_per_combo,
        industries=tuple(args.industries),
        period_types=tuple(args.period_types),
        levels=tuple(args.levels),
        seed=args.seed,
        negative_control_rate=negative_control_rate,
        overwrite=args.overwrite,
    )
    summary = generate_user_dataset(config)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
