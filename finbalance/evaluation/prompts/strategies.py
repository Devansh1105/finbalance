"""
Prompting strategies: zero-shot, few-shot, chain-of-thought, self-refine.

All strategies produce a single string prompt. The expected model output
is always a JSON object with keys: assets, liabilities, equity.
"""

from finbalance.data.schemas import Problem

OUTPUT_FORMAT = """{
  "assets":      {"<account name>": <amount>, ...},
  "liabilities": {"<account name>": <amount>, ...},
  "equity":      {"<account name>": <amount>, ...}
}"""
OUTPUT_KEYS = ["assets", "liabilities", "equity"]

CONSTRAINT_REMINDER = (
    "IMPORTANT: The balance sheet MUST satisfy: "
    "sum(assets) = sum(liabilities) + sum(equity). "
    "Double-check this before outputting."
)


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _format_opening(problem: Problem) -> str:
    ob = problem.opening_balance
    lines = [f"Opening balances as of {ob.date}:"]
    for acc, val in {**ob.assets, **ob.liabilities, **ob.equity}.items():
        lines.append(f"  {acc}: {val:,.0f}")
    return "\n".join(lines)


def _format_transactions(problem: Problem) -> str:
    lines = ["Transactions:"]
    for tx in problem.transactions:
        for entry in tx.entries:
            side = "Dr" if entry.debit else "Cr"
            amt  = entry.debit or entry.credit
            lines.append(
                f"  {tx.date} | {tx.description:<40} | {side} {entry.account:<25} {amt:>10,.0f}"
            )
    return "\n".join(lines)


def _format_adjustments(problem: Problem) -> str:
    if not problem.adjustments:
        return ""
    lines = ["Period-end adjustments (apply before preparing balance sheet):"]
    for adj in problem.adjustments:
        lines.append(f"  {adj.date} | {adj.description}")
        for entry in adj.entries:
            side = "Dr" if entry.debit else "Cr"
            amt  = entry.debit or entry.credit
            lines.append(f"             {side} {entry.account:<25} {amt:>10,.0f}")
    return "\n".join(lines)


def _body(problem: Problem) -> str:
    parts = [_format_opening(problem), _format_transactions(problem)]
    adj = _format_adjustments(problem)
    if adj:
        parts.append(adj)
    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# Strategy 1: Zero-Shot
# ---------------------------------------------------------------------------

def zero_shot(problem: Problem, with_constraint_reminder: bool = True) -> str:
    constraint = f"\n\n{CONSTRAINT_REMINDER}" if with_constraint_reminder else ""
    return f"""You are an expert accountant. Prepare a balance sheet from the transactions below.

{_body(problem)}

Respond ONLY with a JSON object in this exact format (no markdown, no explanation):{constraint}

{OUTPUT_FORMAT}"""


# ---------------------------------------------------------------------------
# Strategy 2: Few-Shot
# ---------------------------------------------------------------------------

_FEW_SHOT_EXAMPLE = """Example:
Opening: Cash 10000, Owner's Equity 10000
T1: Owner invested cash 5000  -> Dr Cash 5000 / Cr Owner's Equity 5000
T2: Bought equipment for cash 3000 -> Dr Equipment 3000 / Cr Cash 3000

Expected output:
{
  "assets":      {"Cash": 12000, "Equipment": 3000},
  "liabilities": {},
  "equity":      {"Owner's Equity": 15000}
}
Verification: Assets(15000) = Liabilities(0) + Equity(15000) ✓
"""


def few_shot(problem: Problem, n_examples: int = 1) -> str:
    examples = _FEW_SHOT_EXAMPLE   # In full system, sample from dataset
    return f"""You are an expert accountant. Study the example, then prepare a balance sheet.

{examples}
---
Now solve this problem:

{_body(problem)}

Respond ONLY with a JSON object (no markdown, no explanation):

{OUTPUT_FORMAT}"""


# ---------------------------------------------------------------------------
# Strategy 3: Chain-of-Thought
# ---------------------------------------------------------------------------

def chain_of_thought(problem: Problem) -> str:
    return f"""You are an expert accountant. Prepare a balance sheet step by step.

{_body(problem)}

Think through this carefully:
1. Start with the opening balances.
2. Process each transaction: identify accounts debited/credited and update running balances.
3. Apply any period-end adjustments.
4. Organize accounts into Assets, Liabilities, and Equity.
5. Verify: Assets = Liabilities + Equity.

Show your reasoning, then end with a line "FINAL ANSWER:" followed by the JSON object only:

{OUTPUT_FORMAT}"""


# ---------------------------------------------------------------------------
# Strategy 4: Self-Refine  (two-stage: generate then critique + correct)
# ---------------------------------------------------------------------------

def self_refine_stage1(problem: Problem) -> str:
    return zero_shot(problem)


def self_refine_stage2(stage1_output: str, problem: Problem) -> str:
    return f"""You prepared this balance sheet:

{stage1_output}

Review it critically:
- Does Assets = Liabilities + Equity?
- Are all transactions reflected?
- Are accounts in the correct section?
- Are all values correct?

If correct, output it unchanged. If there are errors, output a corrected version.

Respond ONLY with the final JSON object (no markdown, no explanation):

{OUTPUT_FORMAT}"""


# ---------------------------------------------------------------------------
# Strategy dispatcher
# ---------------------------------------------------------------------------

STRATEGIES = {
    "zero_shot":   zero_shot,
    "few_shot":    few_shot,
    "cot":         chain_of_thought,
    "self_refine": self_refine_stage1,
}

STRATEGY_METADATA = {
    "zero_shot": {
        "label": "Zero-shot",
        "description": "Single-pass direct balance-sheet generation with a balance-equation reminder.",
        "reasoning_style": "direct_json",
        "n_stages": 1,
        "uses_examples": False,
        "uses_final_answer_marker": False,
        "response_format": "json_only",
        "output_keys": OUTPUT_KEYS,
    },
    "few_shot": {
        "label": "Few-shot",
        "description": "Single-pass generation after studying an in-prompt worked example.",
        "reasoning_style": "example_conditioned_json",
        "n_stages": 1,
        "uses_examples": True,
        "uses_final_answer_marker": False,
        "response_format": "json_only",
        "output_keys": OUTPUT_KEYS,
    },
    "cot": {
        "label": "Chain-of-thought",
        "description": "Step-by-step reasoning followed by a FINAL ANSWER JSON block.",
        "reasoning_style": "step_by_step_then_json",
        "n_stages": 1,
        "uses_examples": False,
        "uses_final_answer_marker": True,
        "final_answer_marker": "FINAL ANSWER:",
        "response_format": "reasoning_plus_final_json",
        "output_keys": OUTPUT_KEYS,
    },
    "self_refine": {
        "label": "Self-refine",
        "description": "Two-stage generation: initial zero-shot JSON, then critique and correction pass.",
        "reasoning_style": "two_pass_refinement",
        "n_stages": 2,
        "uses_examples": False,
        "uses_final_answer_marker": False,
        "response_format": "json_only_after_refinement",
        "output_keys": OUTPUT_KEYS,
    },
}


def build_prompt(problem: Problem, strategy: str) -> str:
    if strategy not in STRATEGIES:
        raise ValueError(f"Unknown strategy '{strategy}'. Choose from: {list(STRATEGIES)}")
    return STRATEGIES[strategy](problem)


def describe_strategy(strategy: str) -> dict:
    """Return structured metadata for a configured prompting strategy."""
    if strategy not in STRATEGY_METADATA:
        return {
            "strategy_id": strategy,
            "label": strategy,
            "description": "Unknown strategy metadata.",
        }
    return {
        "strategy_id": strategy,
        **STRATEGY_METADATA[strategy],
    }
