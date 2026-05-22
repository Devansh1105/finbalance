"""Dataset helpers for the PydanticAI/OpenRouter evaluation script."""

import json
import random
from collections import defaultdict
from pathlib import Path

from finbalance.data.schemas import Problem


def load_dataset(path: str | Path) -> list[Problem]:
    """Load problems from a JSONL dataset file."""
    problems: list[Problem] = []
    with open(path) as handle:
        for line in handle:
            line = line.strip()
            if line:
                problems.append(_dict_to_problem(json.loads(line)))
    return problems


def sample_stratified_subset(
    problems: list[Problem],
    subset_size: int,
    seed: int,
) -> list[Problem]:
    """Draw a stratified subset with as-even-as-possible allocation per level."""
    if subset_size <= 0 or subset_size >= len(problems):
        return list(problems)

    by_level: dict[int, list[Problem]] = defaultdict(list)
    for problem in problems:
        by_level[problem.difficulty_level].append(problem)

    levels = sorted(by_level)
    rng = random.Random(seed)
    for level in levels:
        rng.shuffle(by_level[level])

    per_level, remainder = divmod(subset_size, len(levels))
    counts = {level: per_level for level in levels}
    for level in levels[:remainder]:
        counts[level] += 1

    for level, needed in counts.items():
        available = len(by_level[level])
        if available < needed:
            raise ValueError(
                f"Difficulty level {level} only has {available} problems, but {needed} were requested."
            )

    subset: list[Problem] = []
    for level in levels:
        subset.extend(by_level[level][: counts[level]])
    rng.shuffle(subset)
    return subset


def _dict_to_problem(d: dict) -> Problem:
    """Reconstruct a Problem dataclass from serialized JSON."""
    from finbalance.data.schemas import (
        Adjustment,
        BalanceSheet,
        IntermediateState,
        JournalEntry,
        OpeningBalance,
        Transaction,
    )

    def _entries(rows: list[dict]) -> list[JournalEntry]:
        return [JournalEntry(**row) for row in rows]

    transactions = [
        Transaction(
            transaction_id=transaction["transaction_id"],
            date=transaction["date"],
            description=transaction["description"],
            entries=_entries(transaction["entries"]),
            tx_type=transaction.get("tx_type", ""),
            complexity_factors=transaction.get("complexity_factors", []),
        )
        for transaction in d["transactions"]
    ]
    adjustments = [
        Adjustment(
            adjustment_id=adjustment["adjustment_id"],
            date=adjustment["date"],
            description=adjustment["description"],
            adj_type=adjustment["adj_type"],
            entries=_entries(adjustment["entries"]),
            calculation=adjustment.get("calculation"),
        )
        for adjustment in d["adjustments"]
    ]
    expected = BalanceSheet(
        **{
            key: d["expected"][key]
            for key in (
                "date",
                "assets",
                "liabilities",
                "equity",
                "total_assets",
                "total_liabilities",
                "total_equity",
                "balanced",
            )
        }
    )
    states = [IntermediateState(**state) for state in d["intermediate_states"]]
    opening_balance = OpeningBalance(**d["opening_balance"])

    return Problem(
        problem_id=d["problem_id"],
        difficulty_level=d["difficulty_level"],
        opening_balance=opening_balance,
        transactions=transactions,
        adjustments=adjustments,
        expected=expected,
        intermediate_states=states,
        metadata=d["metadata"],
    )
