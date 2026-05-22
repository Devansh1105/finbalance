"""
Create stratified dev/test splits from full.jsonl.

  dev:  10 problems per level  =  50 total  (public, for prompt tuning)
  test: 20 problems per level  = 100 total  (held-out, for paper results)

Usage:
  python scripts/create_splits.py --input data/full.jsonl --seed 42
"""

import argparse
import json
import random
from collections import defaultdict
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input",    default="data/full.jsonl")
    ap.add_argument("--dev-n",   type=int, default=10, help="Problems per level for dev")
    ap.add_argument("--test-n",  type=int, default=20, help="Problems per level for test")
    ap.add_argument("--seed",    type=int, default=42)
    ap.add_argument("--out-dir", default="data")
    args = ap.parse_args()

    # Load all problems grouped by level
    by_level = defaultdict(list)
    with open(args.input) as f:
        for line in f:
            line = line.strip()
            if line:
                d = json.loads(line)
                by_level[d["difficulty_level"]].append(d)

    rng = random.Random(args.seed)
    dev_problems, test_problems = [], []

    for lvl in sorted(by_level):
        pool = by_level[lvl][:]
        rng.shuffle(pool)
        need = args.dev_n + args.test_n
        if len(pool) < need:
            raise ValueError(f"Level {lvl}: only {len(pool)} problems, need {need}")
        dev_problems.extend(pool[:args.dev_n])
        test_problems.extend(pool[args.dev_n:args.dev_n + args.test_n])

    out_dir = Path(args.out_dir)

    dev_path = out_dir / "dev.jsonl"
    with open(dev_path, "w") as f:
        for p in dev_problems:
            f.write(json.dumps(p) + "\n")

    test_path = out_dir / "test.jsonl"
    with open(test_path, "w") as f:
        for p in test_problems:
            f.write(json.dumps(p) + "\n")

    print(f"Dev  ({len(dev_problems)} problems) -> {dev_path}")
    print(f"Test ({len(test_problems)} problems) -> {test_path}")
    print(f"\nLevel breakdown:")
    from collections import Counter
    dev_lvls  = Counter(p["difficulty_level"] for p in dev_problems)
    test_lvls = Counter(p["difficulty_level"] for p in test_problems)
    for lvl in sorted(dev_lvls):
        print(f"  L{lvl}  dev={dev_lvls[lvl]}  test={test_lvls[lvl]}")


if __name__ == "__main__":
    main()
