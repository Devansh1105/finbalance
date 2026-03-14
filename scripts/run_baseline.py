"""
Run the rule-based oracle baseline and optionally compute weight-sensitivity
and bootstrap CIs on existing model results.

Usage examples:

  # Run oracle baseline on the sample dataset
  python scripts/run_baseline.py --dataset data/sample.jsonl

  # Also compute bootstrap CIs + weight sensitivity on a saved model result
  python scripts/run_baseline.py \\
      --dataset data/sample.jsonl \\
      --model-results results/claude-3-haiku-20240307_zero_shot.json \\
      --output results/baseline_rule_based.json

  # Bootstrap CIs only (no baseline run)
  python scripts/run_baseline.py \\
      --model-results results/claude-3-haiku-20240307_zero_shot.json \\
      --stats-only
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from finbalance.baselines.rule_based import RuleBasedSolver
from finbalance.data.schemas import Problem
from finbalance.evaluation.metrics.core import evaluate_problem, aggregate, ProblemMetrics
from finbalance.evaluation.metrics.stats import bootstrap_metrics, fbs_sensitivity


# ---------------------------------------------------------------------------
# Dataset loading (mirrors run_evaluation.py)
# ---------------------------------------------------------------------------

def load_problems(path: str) -> list[Problem]:
    import dataclasses
    problems = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            problems.append(_dict_to_problem(d))
    return problems


def _dict_to_problem(d: dict) -> Problem:
    from finbalance.data.schemas import (
        OpeningBalance, Transaction, JournalEntry,
        Adjustment, BalanceSheet, IntermediateState,
    )

    def _je(e):
        return JournalEntry(account=e["account"], debit=e.get("debit", 0.0), credit=e.get("credit", 0.0))

    ob = d["opening_balance"]
    opening = OpeningBalance(
        date=ob["date"],
        assets=ob.get("assets", {}),
        liabilities=ob.get("liabilities", {}),
        equity=ob.get("equity", {}),
    )

    transactions = []
    for t in d.get("transactions", []):
        transactions.append(Transaction(
            transaction_id=t["transaction_id"],
            date=t["date"],
            description=t["description"],
            entries=[_je(e) for e in t["entries"]],
            tx_type=t.get("tx_type", ""),
            complexity_factors=t.get("complexity_factors", []),
        ))

    adjustments = []
    for a in d.get("adjustments", []):
        adjustments.append(Adjustment(
            adjustment_id=a["adjustment_id"],
            date=a["date"],
            description=a["description"],
            adj_type=a["adj_type"],
            entries=[_je(e) for e in a["entries"]],
            calculation=a.get("calculation"),
        ))

    exp = d["expected"]
    expected = BalanceSheet(
        date=exp["date"],
        assets=exp["assets"],
        liabilities=exp["liabilities"],
        equity=exp["equity"],
        total_assets=exp["total_assets"],
        total_liabilities=exp["total_liabilities"],
        total_equity=exp["total_equity"],
        balanced=exp["balanced"],
    )

    states = []
    for s in d.get("intermediate_states", []):
        states.append(IntermediateState(
            after_transaction_id=s["after_transaction_id"],
            assets_total=s["assets_total"],
            liabilities_total=s["liabilities_total"],
            equity_total=s["equity_total"],
        ))

    return Problem(
        problem_id=d["problem_id"],
        difficulty_level=d["difficulty_level"],
        opening_balance=opening,
        transactions=transactions,
        adjustments=adjustments,
        expected=expected,
        intermediate_states=states,
        metadata=d.get("metadata", {}),
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_baseline(problems: list[Problem], verbose: bool = True) -> list[ProblemMetrics]:
    solver = RuleBasedSolver()
    all_metrics = []

    for i, problem in enumerate(problems, 1):
        predicted = solver.solve(problem)
        m = evaluate_problem(problem, predicted)
        all_metrics.append(m)
        if verbose:
            print(
                f"  [{i}/{len(problems)}] {problem.problem_id} L{problem.difficulty_level} | "
                f"BA={m.BA:.0f} ALA={m.ALA:.3f} FBS={m.FBS:.1f}"
            )

    return all_metrics


def print_aggregate(metrics: list[ProblemMetrics], label: str = ""):
    agg = aggregate(metrics)
    print(f"\n{'='*55}")
    print(f"  {label or 'Results'}  (n={agg.n_problems})")
    print(f"{'='*55}")
    print(f"  BA  (Balance Accuracy)       : {agg.BA:.4f}  ({agg.BA*100:.1f}%)")
    print(f"  ALA (Account-Level Accuracy) : {agg.ALA:.4f}")
    print(f"  FBS (FinBalance Score)       : {agg.FBS:.2f} / 100")
    print(f"  CSR (Constraint Sat. Rate)   : {agg.CSR:.4f}")
    print(f"  MAE (Mean Abs Error $)       : {agg.MAE:.0f}")
    print(f"\n  By difficulty level:")
    for lvl, lvl_data in sorted(agg.by_difficulty.items()):
        print(f"    L{lvl}  n={lvl_data['n']:3d}  BA={lvl_data['BA']:.2f}  ALA={lvl_data['ALA']:.3f}  FBS={lvl_data['FBS']:.1f}")


def main():
    parser = argparse.ArgumentParser(description="FinBalance rule-based baseline + statistical analysis")
    parser.add_argument("--dataset",        type=str, help="Path to .jsonl dataset")
    parser.add_argument("--model-results",  type=str, help="Path to saved model results JSON (for stats)")
    parser.add_argument("--output",         type=str, default=None, help="Save baseline results to JSON")
    parser.add_argument("--stats-only",     action="store_true", help="Skip baseline, only run stats on --model-results")
    parser.add_argument("--n-boot",         type=int, default=2000, help="Bootstrap resamples (default 2000)")
    parser.add_argument("--no-bootstrap",   action="store_true", help="Skip bootstrap CIs")
    parser.add_argument("--no-sensitivity", action="store_true", help="Skip weight sensitivity analysis")
    args = parser.parse_args()

    if not args.stats_only and not args.dataset:
        parser.error("--dataset is required unless --stats-only is set")

    # ── 1. Oracle baseline ────────────────────────────────────────────────
    baseline_metrics: list[ProblemMetrics] = []
    if not args.stats_only and args.dataset:
        print(f"\nLoading dataset: {args.dataset}")
        problems = load_problems(args.dataset)
        print(f"  {len(problems)} problems loaded")

        print(f"\nRunning rule-based oracle baseline...")
        baseline_metrics = run_baseline(problems, verbose=True)
        print_aggregate(baseline_metrics, label="Rule-Based Oracle Baseline")

        if args.output:
            import dataclasses
            rows = [dataclasses.asdict(m) for m in baseline_metrics]
            with open(args.output, "w") as f:
                json.dump(rows, f, indent=2)
            print(f"\n  Saved to {args.output}")

    # ── 2. Stats on model results (optional) ─────────────────────────────
    model_metrics: list[ProblemMetrics] = []
    if args.model_results:
        print(f"\nLoading model results: {args.model_results}")
        with open(args.model_results) as f:
            rows = json.load(f)

        for r in rows:
            m = ProblemMetrics(problem_id=r["problem_id"], difficulty=r["difficulty"])
            for field in ["BA", "ALA", "TPA", "CSR", "MAE", "RMSE", "FBS",
                          "n_accounts_expected", "n_accounts_correct", "parse_error"]:
                if field in r:
                    setattr(m, field, r[field])
            model_metrics.append(m)

        print_aggregate(model_metrics, label=f"Model Results ({os.path.basename(args.model_results)})")

    # ── 3. Bootstrap CIs ─────────────────────────────────────────────────
    for label, metrics in [("Oracle Baseline", baseline_metrics), ("Model Results", model_metrics)]:
        if not metrics or args.no_bootstrap:
            continue
        print(f"\n{'-'*55}")
        boot = bootstrap_metrics(metrics, n_boot=args.n_boot)
        boot.print_summary()

    # ── 4. Weight sensitivity (model results only) ────────────────────────
    # Skipped for the oracle baseline: near-perfect scores make Spearman
    # rank correlation degenerate (tiny floating-point differences dominate).
    if model_metrics and not args.no_sensitivity:
        print(f"\n{'-'*55}")
        print("Weight Sensitivity -- Model Results")
        sens = fbs_sensitivity(model_metrics)
        sens.print_summary()

    # ── 5. Side-by-side comparison ────────────────────────────────────────
    if baseline_metrics and model_metrics:
        print(f"\n{'='*55}")
        print("  Baseline vs Model Comparison")
        print(f"{'='*55}")
        b_agg = aggregate(baseline_metrics)
        m_agg = aggregate(model_metrics)
        print(f"  {'Metric':<10}  {'Baseline':>10}  {'Model':>10}  {'Gap':>10}")
        print(f"  {'-'*45}")
        for attr, label in [("BA","BA"), ("ALA","ALA"), ("FBS","FBS"), ("MAE","MAE ($)")]:
            bv = getattr(b_agg, attr)
            mv = getattr(m_agg, attr)
            gap = mv - bv
            print(f"  {label:<10}  {bv:>10.4f}  {mv:>10.4f}  {gap:>+10.4f}")


if __name__ == "__main__":
    main()
