"""
Error Propagation Simulator — CLI
==================================
Runs the PropagationSimulator on selected problems and saves results.

Usage examples
--------------
# One specific problem (by problem_id)
python scripts/simulate_propagation.py \
    --dataset data/sample.jsonl \
    --model  claude-3-haiku-20240307 \
    --problem-ids P001_L1 P002_L2

# First N problems of each difficulty level
python scripts/simulate_propagation.py \
    --dataset data/sample.jsonl \
    --model  claude-3-haiku-20240307 \
    --n-per-level 1

# Every-other-transaction checkpoint (halves API calls)
python scripts/simulate_propagation.py \
    --dataset data/sample.jsonl \
    --model  claude-3-haiku-20240307 \
    --n-per-level 2 \
    --checkpoint-every 2 \
    --output results/propagation_haiku.json
"""

import argparse
import json
import os
import sys
from pathlib import Path

# ── resolve repo root so imports work from any cwd ──────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from finbalance.data.schemas import Problem
from finbalance.evaluation.models.anthropic_model import AnthropicModel
from finbalance.evaluation.models.base import ModelConfig
from finbalance.analysis.error_propagation import (
    PropagationSimulator,
    summarize_traces,
    save_traces,
    load_traces,
)


# ---------------------------------------------------------------------------
# Dataset loader
# ---------------------------------------------------------------------------

def _load_problems(path: str) -> list[Problem]:
    import dataclasses

    def _make(d: dict) -> Problem:
        from finbalance.data.schemas import (
            OpeningBalance, Transaction, Adjustment, BalanceSheet,
            IntermediateState, JournalEntry,
        )
        from dataclasses import fields

        def to_je(e: dict) -> JournalEntry:
            return JournalEntry(**{f.name: e.get(f.name, 0.0) for f in fields(JournalEntry)})

        def to_tx(t: dict) -> Transaction:
            return Transaction(
                transaction_id=t["transaction_id"],
                date=t["date"],
                description=t["description"],
                entries=[to_je(e) for e in t["entries"]],
                tx_type=t.get("tx_type", ""),
                complexity_factors=t.get("complexity_factors", []),
            )

        def to_adj(a: dict) -> Adjustment:
            return Adjustment(
                adjustment_id=a["adjustment_id"],
                date=a["date"],
                description=a["description"],
                adj_type=a["adj_type"],
                entries=[to_je(e) for e in a["entries"]],
                calculation=a.get("calculation"),
            )

        def to_ob(o: dict) -> OpeningBalance:
            return OpeningBalance(**{f.name: o.get(f.name, {} if f.name != "date" else "") for f in fields(OpeningBalance)})

        def to_bs(b: dict) -> BalanceSheet:
            return BalanceSheet(**{f.name: b[f.name] for f in fields(BalanceSheet)})

        def to_is(s: dict) -> IntermediateState:
            return IntermediateState(**{f.name: s[f.name] for f in fields(IntermediateState)})

        return Problem(
            problem_id=d["problem_id"],
            difficulty_level=d["difficulty_level"],
            opening_balance=to_ob(d["opening_balance"]),
            transactions=[to_tx(t) for t in d["transactions"]],
            adjustments=[to_adj(a) for a in d.get("adjustments", [])],
            expected=to_bs(d["expected"]),
            intermediate_states=[to_is(s) for s in d.get("intermediate_states", [])],
            metadata=d.get("metadata", {}),
        )

    problems = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                problems.append(_make(json.loads(line)))
    return problems


# ---------------------------------------------------------------------------
# Pretty-print summary
# ---------------------------------------------------------------------------

def _print_summary(summary: dict) -> None:
    print("\n" + "=" * 60)
    print("ERROR PROPAGATION SUMMARY")
    print("=" * 60)
    print(f"  Problems analysed:   {summary['n_problems']}")
    print(f"  Propagation shape:   {summary['error_propagation_shape'].upper()}")
    print(f"  Mean onset fraction: {summary.get('mean_onset_fraction', 'N/A')} "
          f"(0=first tx, 1=last tx)")
    print(f"  Mean final MAE:      ${summary['mean_final_mae']:,.0f}")

    print("\n  MAE trajectory (normalised checkpoints):")
    for k, v in summary["mae_at_quantiles"].items():
        bar = "█" * min(40, int(v / max(1, summary["mean_final_mae"]) * 40))
        print(f"    {k:4s}  ${v:>10,.0f}  {bar}")

    print("\n  Error onset by transaction type:")
    for ttype, cnt in summary["error_onset_tx_type_distribution"].items():
        print(f"    {ttype:<35} {cnt:3d}")

    print("\n  By difficulty level:")
    for lvl, info in summary["by_level"].items():
        onset_info = (
            f"onset@k={info['mean_onset_k']:.1f} ({info['mean_onset_fraction']:.0%})"
            if info.get("mean_onset_k") else "no error"
        )
        print(
            f"    L{lvl} (n={info['n']:2d})  "
            f"finalMAE=${info['mean_final_mae']:>8,.0f}  "
            f"{onset_info}"
        )
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Run error propagation simulation")
    ap.add_argument("--dataset",          required=True,  help="Path to .jsonl dataset")
    ap.add_argument("--model",            default="claude-3-haiku-20240307")
    ap.add_argument("--api-key",          default=None,   help="Anthropic API key (overrides env)")
    ap.add_argument("--problem-ids",      nargs="+",      help="Select specific problem IDs")
    ap.add_argument("--n-per-level",      type=int, default=1,
                    help="Number of problems to pick per difficulty level (default: 1)")
    ap.add_argument("--levels",           nargs="+", type=int, default=[1, 2, 3, 4, 5])
    ap.add_argument("--checkpoint-every", type=int, default=1,
                    help="Transactions between checkpoints (1=every tx, 2=every other, …)")
    ap.add_argument("--max-checkpoints",  type=int, default=0,
                    help="Cap checkpoints per problem (0=no cap)")
    ap.add_argument("--sleep",            type=float, default=0.5,
                    help="Seconds to sleep between API calls")
    ap.add_argument("--output",           default=None,
                    help="Save traces to this JSON file")
    ap.add_argument("--summary-only",     action="store_true",
                    help="Load existing --output and print summary without running new API calls")

    args = ap.parse_args()

    # ── summary-only mode ──
    if args.summary_only:
        if not args.output or not os.path.exists(args.output):
            print("ERROR: --summary-only requires --output pointing to an existing file")
            sys.exit(1)
        traces = load_traces(args.output)
        summary = summarize_traces(traces)
        _print_summary(summary)
        return

    # ── load dataset ──
    print(f"Loading dataset: {args.dataset}")
    all_problems = _load_problems(args.dataset)
    print(f"  {len(all_problems)} problems loaded")

    # ── select problems ──
    if args.problem_ids:
        selected = [p for p in all_problems if p.problem_id in set(args.problem_ids)]
        if not selected:
            print(f"ERROR: none of {args.problem_ids} found in dataset")
            sys.exit(1)
    else:
        from collections import defaultdict
        by_level: dict[int, list] = defaultdict(list)
        for p in all_problems:
            by_level[p.difficulty_level].append(p)
        selected = []
        for lvl in args.levels:
            selected.extend(by_level[lvl][: args.n_per_level])

    print(f"  Running simulation on {len(selected)} problems: "
          f"{[p.problem_id for p in selected]}")

    # ── build model ──
    api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("ERROR: set ANTHROPIC_API_KEY or pass --api-key")
        sys.exit(1)

    model = AnthropicModel(
        ModelConfig(model_id=args.model, temperature=0),
        api_key=api_key,
    )

    # ── run simulator ──
    sim = PropagationSimulator(
        model=model,
        checkpoint_every=args.checkpoint_every,
        max_checkpoints=args.max_checkpoints,
        sleep_between=args.sleep,
        verbose=True,
    )

    output_path = args.output or f"results/propagation_{args.model.replace('/', '_')}.json"
    traces = sim.simulate_batch(selected, save_path=output_path)

    # ── summary ──
    import dataclasses
    summary = summarize_traces([dataclasses.asdict(t) for t in traces])
    _print_summary(summary)

    # Append summary to output file
    summary_path = output_path.replace(".json", "_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary saved → {summary_path}")


if __name__ == "__main__":
    main()
