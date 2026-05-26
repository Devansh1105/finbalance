#!/usr/bin/env python3
"""Regenerate the canonical FinBalance coverage and main datasets."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from finbalance.cli import regenerate_standard_datasets


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Regenerate data/coverage and data/main with manifests.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--base-dir", default="data", help="Base directory that will contain coverage/ and main/")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--records-per-combo", type=int, default=4, help="Main split records per industry x period x difficulty cell, including coverage")
    parser.add_argument("--negative-controls-per-code", type=int, default=10, help="Main split forced inconsistency records per code, including coverage")
    parser.add_argument(
        "--main-only",
        action="store_true",
        help="Regenerate only main/ as an extension of existing coverage/",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Required when coverage/ or main/ already exists under --base-dir",
    )
    args = parser.parse_args()

    base_dir = Path(args.base_dir)
    existing = [path for path in ((base_dir / "main",) if args.main_only else (base_dir / "coverage", base_dir / "main")) if path.exists()]
    if existing and not args.overwrite:
        formatted = ", ".join(str(path) for path in existing)
        raise SystemExit(f"Refusing to overwrite existing dataset directories: {formatted}. Re-run with --overwrite.")

    if args.main_only:
        from finbalance.cli import regenerate_main_dataset_from_existing_coverage

        summary = regenerate_main_dataset_from_existing_coverage(
            base_dir=base_dir,
            seed=args.seed,
            records_per_combo=args.records_per_combo,
            negative_controls_per_code=args.negative_controls_per_code,
        )
    else:
        summary = regenerate_standard_datasets(
            base_dir=base_dir,
            seed=args.seed,
            records_per_combo=args.records_per_combo,
            negative_controls_per_code=args.negative_controls_per_code,
        )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
