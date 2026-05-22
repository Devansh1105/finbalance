#!/usr/bin/env python3
"""
Generate the FinBalance dataset.

Usage:
  python scripts/generate_dataset.py --output data/dataset.jsonl
  python scripts/generate_dataset.py --counts 1:50,2:75,3:75 --output data/small.jsonl
  python scripts/generate_dataset.py --counts 1:500,2:750,3:750,4:400,5:100 --output data/full.jsonl
"""

import argparse
import json
import sys
from pathlib import Path

# Allow running from repo root
sys.path.insert(0, str(Path(__file__).parent.parent))

from finbalance.data.generation.generator import ProblemGenerator


def parse_counts(s: str) -> dict[int, int]:
    """Parse '1:5,2:7,3:7' into {1: 5, 2: 7, 3: 7}."""
    result = {}
    for part in s.split(","):
        level, n = part.strip().split(":")
        result[int(level)] = int(n)
    return result


def main():
    parser = argparse.ArgumentParser(description="Generate FinBalance dataset")
    parser.add_argument("--counts", default="1:20,2:30,3:30",
                        help="Problems per level, e.g. 1:500,2:750,3:750,4:400,5:100")
    parser.add_argument("--output", default="data/dataset.jsonl",
                        help="Output JSONL file path")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for reproducibility")
    args = parser.parse_args()

    counts = parse_counts(args.counts)
    total = sum(counts.values())
    print(f"Generating {total} problems: {counts}")

    generator = ProblemGenerator(seed=args.seed)
    problems = generator.generate_dataset(counts)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w") as f:
        for p in problems:
            f.write(json.dumps(p.to_dict()) + "\n")

    print(f"Saved {len(problems)} problems to {out_path}")

    # Print summary statistics
    by_level: dict[int, list] = {}
    for p in problems:
        by_level.setdefault(p.difficulty_level, []).append(p)

    print("\nDataset summary:")
    print(f"  {'Level':<8} {'N':>6} {'Avg Tx':>8} {'Avg Accts':>10} {'With Adj':>10}")
    for lvl in sorted(by_level):
        ps = by_level[lvl]
        avg_tx = sum(p.metadata["num_transactions"] for p in ps) / len(ps)
        avg_ac = sum(p.metadata["num_accounts"] for p in ps) / len(ps)
        with_adj = sum(1 for p in ps if p.metadata["has_adjustments"])
        print(f"  {lvl:<8} {len(ps):>6} {avg_tx:>8.1f} {avg_ac:>10.1f} {with_adj:>9}/{len(ps)}")


if __name__ == "__main__":
    main()
