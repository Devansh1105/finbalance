#!/usr/bin/env python3
"""Create a fixed stratified subset JSONL for repeatable multi-model runs."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from finbalance.evaluation.pydantic_ai import load_dataset, sample_stratified_subset


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a fixed FinBalance subset JSONL")
    parser.add_argument("--input", default="data/full.jsonl", help="Source dataset JSONL")
    parser.add_argument("--output", default="data/large500.jsonl", help="Output subset JSONL")
    parser.add_argument("--size", type=int, default=500, help="Subset size")
    parser.add_argument("--seed", type=int, default=42, help="Subset RNG seed")
    args = parser.parse_args()

    problems = load_dataset(args.input)
    subset = sample_stratified_subset(problems, args.size, args.seed)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as handle:
        for problem in subset:
            handle.write(json.dumps(problem.to_dict()) + "\n")

    counts = Counter(problem.difficulty_level for problem in subset)
    print(f"Wrote {len(subset)} problems to {output_path}")
    print("Breakdown:", ", ".join(f"L{level}={counts[level]}" for level in sorted(counts)))


if __name__ == "__main__":
    main()
