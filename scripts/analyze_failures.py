#!/usr/bin/env python3
"""
Failure analysis CLI for FinBalance.

Usage:
  python scripts/analyze_failures.py \\
      --results results/claude-3-haiku-20240307_zero_shot.json \\
      --dataset data/sample.jsonl

  # Save full JSON report
  python scripts/analyze_failures.py \\
      --results results/claude-3-haiku-20240307_zero_shot.json \\
      --dataset data/sample.jsonl \\
      --output results/failure_analysis_haiku_zero_shot.json
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.run_evaluation import load_dataset
from finbalance.analysis.failure_analysis import (
    FailureAnalysisReport,
    run_failure_analysis,
)


# ──────────────────────────────────────────────────────────────────────────────
# Pretty-print helpers
# ──────────────────────────────────────────────────────────────────────────────

W = 70

def _header(title: str):
    print()
    print("=" * W)
    print(f"  {title}")
    print("=" * W)

def _subheader(title: str):
    print()
    print(f"  ── {title} ──")

def _row(label: str, value, width: int = 40):
    print(f"  {label:<{width}} {value}")


def print_report(r: FailureAnalysisReport):
    print()
    print("=" * W)
    print(f"  FinBalance Failure Analysis")
    print(f"  Model:    {r.model_id}")
    print(f"  Strategy: {r.strategy}")
    print(f"  Problems: {r.n_problems}")
    print("=" * W)

    # ── 1. Complexity Drivers ────────────────────────────────────────────────
    _header("1. Complexity Driver Analysis  (sorted: most harmful → least)")
    print(f"  {'Feature':<25} {'N':>5}  {'FBS':>6}  {'ALA':>6}  {'ΔFBS':>7}  {'ΔALA':>7}  {'BA%':>6}")
    print(f"  {'-'*25}  {'-'*5}  {'-'*6}  {'-'*6}  {'-'*7}  {'-'*7}  {'-'*6}")
    for fg in r.complexity_drivers.features:
        delta_fbs_str = f"{fg.fbs_delta:+.1f}"
        delta_ala_str = f"{fg.ala_delta:+.3f}"
        print(
            f"  {fg.feature:<25}  {fg.n_problems:>5}"
            f"  {fg.avg_fbs:>6.1f}  {fg.avg_ala:>6.3f}"
            f"  {delta_fbs_str:>7}  {delta_ala_str:>7}"
            f"  {fg.ba_rate * 100:>5.1f}%"
        )

    # ── 2. Account Miss Rates ────────────────────────────────────────────────
    _header("2. Account-Level Miss Rate Analysis")

    _subheader("Most Omitted Accounts  (omission_rate = missed / times expected)")
    print(f"  {'Account':<35} {'Type':<15} {'Expected':>8}  {'Omit%':>6}  {'Arith%':>7}")
    print(f"  {'-'*35}  {'-'*15}  {'-'*8}  {'-'*6}  {'-'*7}")
    shown = sorted(
        [s for s in r.account_miss_rates.accounts if s.n_expected >= 2],
        key=lambda s: -s.omission_rate
    )[:12]
    for s in shown:
        print(
            f"  {s.account:<35}  {s.account_type:<15}"
            f"  {s.n_expected:>8}"
            f"  {s.omission_rate * 100:>5.1f}%"
            f"  {s.arithmetic_rate * 100:>6.1f}%"
        )

    _subheader("Most Arithmetic Errors  (among accounts that ARE present)")
    shown_ae = sorted(
        [s for s in r.account_miss_rates.accounts if s.n_expected >= 2 and s.omission_rate < 0.9],
        key=lambda s: -s.arithmetic_rate
    )[:10]
    for s in shown_ae:
        print(
            f"  {s.account:<35}  avg_err={s.avg_abs_error:>10,.0f}"
            f"  arith%={s.arithmetic_rate * 100:>5.1f}%"
        )

    # ── 3. Balance Equation Failure Causes ───────────────────────────────────
    _header("3. Balance Equation Failure Root Causes")
    bf = r.balance_failures
    print(f"  Problems with BA=0:  {bf.n_failures} / {r.n_problems}")
    if bf.n_failures > 0:
        print()
        print(f"  Cause breakdown:")
        for cause, cnt in sorted(bf.cause_summary.items(), key=lambda x: -x[1]):
            pct = cnt / bf.n_failures * 100
            print(f"    {cause:<30}  {cnt:>3}  ({pct:.0f}%)")
        print()
        print(f"  {'Problem':<20} {'Lvl':>4} {'Imbalance':>12}  Cause")
        print(f"  {'-'*20}  {'-'*4}  {'-'*12}  {'-'*30}")
        for c in bf.causes:
            print(
                f"  {c.problem_id:<20}  L{c.difficulty}"
                f"  {c.imbalance:>12,.0f}  {c.cause}: {c.description[:45]}"
            )

    # ── 4. Hallucination Catalog ─────────────────────────────────────────────
    _header("4. Hallucination Catalog  (accounts model invented)")
    hc = r.hallucinations
    print(f"  Total hallucination instances: {hc.total_hallucinations}")
    print(f"  Real-accounting-account rate:  {hc.schema_known_rate * 100:.1f}%")
    print(f"  (In-schema = classification confusion; out-of-schema = fabrication)")
    if hc.entries:
        print()
        print(f"  {'Account':<40} {'Freq':>5}  {'In Schema':>10}  {'Type'}")
        print(f"  {'-'*40}  {'-'*5}  {'-'*10}  {'-'*15}")
        for e in hc.entries[:20]:
            schema_str = "YES" if e.in_schema else "NO"
            atype = e.account_type or "—"
            print(f"  {e.account_name:<40}  {e.frequency:>5}  {schema_str:>10}  {atype}")

    # ── 5. Difficulty Gradient ───────────────────────────────────────────────
    _header("5. Difficulty Gradient")
    print(f"  {'Level':>5}  {'N':>4}  {'BA%':>6}  {'ALA':>6}  {'FBS':>6}  {'AvgErr':>7}  Top Error Categories")
    print(f"  {'-'*5}  {'-'*4}  {'-'*6}  {'-'*6}  {'-'*6}  {'-'*7}  {'-'*30}")
    for lp in r.difficulty_gradient.levels:
        top_cats = ", ".join(
            f"{cat}={pct*100:.0f}%"
            for cat, pct in list(lp.error_composition.items())[:3]
        )
        print(
            f"  {lp.level:>5}  {lp.n_problems:>4}"
            f"  {lp.ba_rate * 100:>5.1f}%"
            f"  {lp.avg_ala:>6.3f}"
            f"  {lp.avg_fbs:>6.1f}"
            f"  {lp.avg_n_errors:>7.1f}"
            f"  {top_cats}"
        )

    _subheader("Feature presence rate by level")
    all_features = sorted({
        f for lp in r.difficulty_gradient.levels for f in lp.feature_rates
    })
    header_cols = "".join(f"  L{lp.level}" for lp in r.difficulty_gradient.levels)
    print(f"  {'Feature':<25} {header_cols}")
    for feat in all_features:
        rates = "".join(
            f"  {lp.feature_rates.get(feat, 0.0) * 100:>4.0f}%"
            for lp in r.difficulty_gradient.levels
        )
        print(f"  {feat:<25} {rates}")

    print()
    print("=" * W)


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────

def report_to_dict(r: FailureAnalysisReport) -> dict:
    """Serialize to a plain dict for JSON output."""
    import dataclasses
    def _dc(obj):
        if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
            return {k: _dc(v) for k, v in dataclasses.asdict(obj).items()}
        if isinstance(obj, list):
            return [_dc(x) for x in obj]
        if isinstance(obj, dict):
            return {k: _dc(v) for k, v in obj.items()}
        return obj
    return _dc(r)


def main():
    ap = argparse.ArgumentParser(description="FinBalance failure analysis")
    ap.add_argument("--results", required=True, help="Path to results JSON (from run_evaluation.py)")
    ap.add_argument("--dataset", required=True, help="Path to dataset JSONL")
    ap.add_argument("--output",  default=None,  help="Optional: save full analysis as JSON")
    args = ap.parse_args()

    print(f"Loading dataset from {args.dataset}...")
    problems = load_dataset(args.dataset)
    print(f"  {len(problems)} problems loaded.")

    print(f"Loading results from {args.results}...")
    with open(args.results) as f:
        results = json.load(f)
    print(f"  {len(results)} results loaded.")

    print("Running failure analysis...")
    report = run_failure_analysis(problems, results)

    print_report(report)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(report_to_dict(report), f, indent=2)
        print(f"\nFull analysis saved to {args.output}")


if __name__ == "__main__":
    main()
