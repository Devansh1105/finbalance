"""
Paired permutation tests for pairwise model comparisons on the FinBalance test set.

For two models A and B that both evaluated the same 100 problems, we test:
  H0: mean(FBS_A) == mean(FBS_B)
using a one-sided permutation test (A > B) with n_perm=10,000 permutations.

Since both models evaluated the same problem IDs, we align by problem_id
and compute per-problem FBS differences — this removes problem-level variance
and greatly increases statistical power.

Also reports bootstrap 95% CIs for FBS/BA/ALA for each model×strategy.

Output: results/significance_tests.json  +  printed table

Usage:
    python scripts/permutation_tests.py
    python scripts/permutation_tests.py --metric FBS --n-perm 10000
"""

import argparse
import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_primary_results(results_dir: Path) -> dict:
    """Returns {(model_id, strategy): {problem_id: result_dict}}."""
    skip = {"failure_analysis", "propagation", "leaderboard", "significance"}
    groups = {}
    for path in sorted(results_dir.glob("*.json")):
        if any(s in path.name for s in skip):
            continue
        try:
            with open(path) as f:
                data = json.load(f)
        except Exception:
            continue
        if not isinstance(data, list) or len(data) < 90:
            continue
        if not data or "FBS" not in data[0]:
            continue
        model_id = data[0].get("model_id", "unknown")
        strategy = data[0].get("strategy", "unknown")
        key = (model_id, strategy)
        groups[key] = {r["problem_id"]: r for r in data if "problem_id" in r}
    return groups


def bootstrap_ci(values: np.ndarray, n_boot: int = 2000, alpha: float = 0.05):
    means = [np.mean(np.random.choice(values, size=len(values), replace=True))
             for _ in range(n_boot)]
    return np.percentile(means, 100 * alpha / 2), np.percentile(means, 100 * (1 - alpha / 2))


def permutation_test(a: np.ndarray, b: np.ndarray, n_perm: int = 10000) -> tuple[float, float]:
    """
    Paired one-sided permutation test: H1: mean(a) > mean(b).
    Returns (observed_delta, p_value).
    """
    diff = a - b
    observed = np.mean(diff)
    count = 0
    for _ in range(n_perm):
        signs = np.random.choice([-1, 1], size=len(diff))
        if np.mean(signs * diff) >= observed:
            count += 1
    return round(float(observed), 4), round(count / n_perm, 4)


def p_stars(p: float) -> str:
    if p < 0.001:
        return "***"
    elif p < 0.01:
        return "**"
    elif p < 0.05:
        return "*"
    elif p < 0.10:
        return "†"
    return "n.s."


def display_name(model_id: str, strategy: str) -> str:
    short = {
        "openai/gpt-5.2":                    "GPT-5.2",
        "google/gemini-3-flash-preview":     "Gemini3Flash",
        "meta-llama/llama-3.3-70b-instruct": "Llama3.3-70B",
    }
    m = short.get(model_id, model_id.split("/")[-1])
    s = {"zero_shot": "ZS", "cot": "CoT"}.get(strategy, strategy)
    return f"{m}-{s}"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results-dir", default="results")
    ap.add_argument("--metric",      default="FBS", help="Primary metric for pairwise tests")
    ap.add_argument("--n-perm",      type=int, default=10000)
    ap.add_argument("--seed",        type=int, default=42)
    args = ap.parse_args()

    np.random.seed(args.seed)
    groups = load_primary_results(Path(args.results_dir))

    if not groups:
        print("No primary result files found.")
        return

    keys = sorted(groups.keys())
    print(f"Found {len(keys)} model×strategy combinations:\n")
    for k in keys:
        print(f"  {display_name(*k)}  (n={len(groups[k])})")
    print()

    # -----------------------------------------------------------------------
    # Per-model bootstrap CIs
    # -----------------------------------------------------------------------
    ci_results = {}
    print("=== Bootstrap 95% CIs ===")
    print(f"{'Model-Strategy':<25} {'FBS mean':>9} {'95% CI':>16} {'BA%':>7} {'ALA':>7}")
    print("-" * 68)

    for key in keys:
        pid_map = groups[key]
        fbs_vals  = np.array([r.get("FBS", 0)   for r in pid_map.values()])
        ba_vals   = np.array([r.get("BA", 0)*100 for r in pid_map.values()])
        ala_vals  = np.array([r.get("ALA", 0)    for r in pid_map.values()])

        fbs_lo, fbs_hi = bootstrap_ci(fbs_vals)
        ci_results[display_name(*key)] = {
            "FBS_mean": round(float(np.mean(fbs_vals)), 2),
            "FBS_ci":   [round(fbs_lo, 2), round(fbs_hi, 2)],
            "BA_mean":  round(float(np.mean(ba_vals)), 1),
            "ALA_mean": round(float(np.mean(ala_vals)), 3),
        }
        name = display_name(*key)
        print(f"{name:<25} {np.mean(fbs_vals):>9.2f} [{fbs_lo:>6.2f}, {fbs_hi:>6.2f}]"
              f"  {np.mean(ba_vals):>5.1f}%  {np.mean(ala_vals):>6.3f}")

    # -----------------------------------------------------------------------
    # Pairwise permutation tests
    # -----------------------------------------------------------------------
    print(f"\n=== Pairwise Permutation Tests (metric={args.metric}, n_perm={args.n_perm}) ===")
    print(f"{'Model A':<25} {'Model B':<25} {'Delta':>8} {'p (A>B)':>10} {'sig':>5}")
    print("-" * 75)

    pair_results = []
    for key_a, key_b in combinations(keys, 2):
        pid_a = groups[key_a]
        pid_b = groups[key_b]
        shared_ids = sorted(set(pid_a.keys()) & set(pid_b.keys()))
        if len(shared_ids) < 20:
            continue

        metric = args.metric
        a_vals = np.array([pid_a[pid].get(metric, 0) for pid in shared_ids])
        b_vals = np.array([pid_b[pid].get(metric, 0) for pid in shared_ids])

        delta, p = permutation_test(a_vals, b_vals, args.n_perm)
        # Also test reverse direction for two-sided reporting
        _, p_rev = permutation_test(b_vals, a_vals, args.n_perm)
        p_two = min(p, p_rev) * 2  # approximate two-sided

        name_a = display_name(*key_a)
        name_b = display_name(*key_b)
        stars = p_stars(p_two)
        print(f"{name_a:<25} {name_b:<25} {delta:>+8.3f}  {p_two:>9.4f}  {stars:>5}")

        pair_results.append({
            "model_a": display_name(*key_a),
            "model_b": display_name(*key_b),
            "metric":  metric,
            "n_shared": len(shared_ids),
            "delta":    delta,
            "p_one_sided": p,
            "p_two_sided": round(p_two, 4),
            "significant_0.05": p_two < 0.05,
        })

    # -----------------------------------------------------------------------
    # Save
    # -----------------------------------------------------------------------
    out = {
        "bootstrap_cis": ci_results,
        "pairwise_tests": pair_results,
        "n_permutations": args.n_perm,
        "metric": args.metric,
    }
    out_path = Path(args.results_dir) / "significance_tests.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nResults saved to {out_path}")
    print("\n*** p<0.001  ** p<0.01  * p<0.05  † p<0.10  n.s. not significant")


if __name__ == "__main__":
    main()
