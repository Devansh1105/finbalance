"""
Statistical utilities for FinBalance evaluation results.

  bootstrap_ci          – percentile bootstrap for a single metric
  bootstrap_metrics     – bootstrap CIs for all ProblemMetrics fields
  fbs_sensitivity       – FBS under alternative weight schemes
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Optional

from finbalance.evaluation.metrics.core import (
    ProblemMetrics,
    FBS_WEIGHTS_NO_TPA,
    finbalance_score,
)


# ---------------------------------------------------------------------------
# Bootstrap CI
# ---------------------------------------------------------------------------

def bootstrap_ci(
    values: list[float],
    n_boot: int = 2000,
    alpha: float = 0.05,
    seed: int = 42,
) -> tuple[float, float, float]:
    """
    Percentile bootstrap confidence interval for the mean of `values`.

    Returns:
        (mean, lower_bound, upper_bound) at (1-alpha) confidence level.
    """
    if not values:
        return 0.0, 0.0, 0.0
    rng = random.Random(seed)
    n = len(values)
    boot_means = []
    for _ in range(n_boot):
        sample = [rng.choice(values) for _ in range(n)]
        boot_means.append(sum(sample) / n)
    boot_means.sort()
    lo_idx = int((alpha / 2) * n_boot)
    hi_idx = int((1 - alpha / 2) * n_boot) - 1
    mean = sum(values) / n
    return round(mean, 4), round(boot_means[lo_idx], 4), round(boot_means[hi_idx], 4)


# ---------------------------------------------------------------------------
# Per-metric bootstrap across a set of results
# ---------------------------------------------------------------------------

BOOTSTRAP_METRICS = ["BA", "ALA", "FBS", "CSR", "MAE"]


@dataclass
class MetricCI:
    metric:  str
    mean:    float
    lower:   float
    upper:   float
    n:       int

    def __str__(self) -> str:
        return f"{self.metric}: {self.mean:.4f}  95% CI [{self.lower:.4f}, {self.upper:.4f}]  (n={self.n})"


@dataclass
class BootstrapReport:
    n_problems:  int
    alpha:       float
    n_boot:      int
    metrics:     list[MetricCI] = field(default_factory=list)
    by_difficulty: dict[int, list[MetricCI]] = field(default_factory=dict)

    def print_summary(self):
        print(f"\nBootstrap CIs  (n={self.n_problems}, {int((1-self.alpha)*100)}% CI, {self.n_boot} resamples)")
        print("-" * 55)
        for m in self.metrics:
            print(f"  {m}")
        for lvl, lvl_metrics in sorted(self.by_difficulty.items()):
            print(f"\n  Level {lvl}:")
            for m in lvl_metrics:
                print(f"    {m}")


def bootstrap_metrics(
    results: list[ProblemMetrics],
    n_boot: int = 2000,
    alpha: float = 0.05,
    seed: int = 42,
) -> BootstrapReport:
    """
    Compute bootstrap CIs for all key metrics, overall and per difficulty level.

    Args:
        results:  list of ProblemMetrics from evaluate_problem()
        n_boot:   number of bootstrap resamples
        alpha:    significance level (0.05 → 95% CI)
        seed:     random seed for reproducibility
    """
    report = BootstrapReport(n_problems=len(results), alpha=alpha, n_boot=n_boot)

    # Overall CIs
    for metric in BOOTSTRAP_METRICS:
        vals = [getattr(r, metric) for r in results]
        mean, lo, hi = bootstrap_ci(vals, n_boot=n_boot, alpha=alpha, seed=seed)
        report.metrics.append(MetricCI(metric=metric, mean=mean, lower=lo, upper=hi, n=len(vals)))

    # Per-difficulty CIs
    by_diff: dict[int, list[ProblemMetrics]] = {}
    for r in results:
        by_diff.setdefault(r.difficulty, []).append(r)

    for lvl, lvl_results in sorted(by_diff.items()):
        lvl_cis = []
        for metric in BOOTSTRAP_METRICS:
            vals = [getattr(r, metric) for r in lvl_results]
            mean, lo, hi = bootstrap_ci(vals, n_boot=n_boot, alpha=alpha, seed=seed)
            lvl_cis.append(MetricCI(metric=metric, mean=mean, lower=lo, upper=hi, n=len(vals)))
        report.by_difficulty[lvl] = lvl_cis

    return report


# ---------------------------------------------------------------------------
# FBS weight sensitivity
# ---------------------------------------------------------------------------

# Alternative weight schemes to test (all for the no-TPA case, weights sum to 1)
WEIGHT_SCHEMES: dict[str, dict[str, float]] = {
    "default": FBS_WEIGHTS_NO_TPA,
    "ba_heavy": {
        "BA": 0.50, "ALA": 0.20, "CSR": 0.20, "NE": 0.10,
    },
    "ala_heavy": {
        "BA": 0.20, "ALA": 0.50, "CSR": 0.20, "NE": 0.10,
    },
    "uniform": {
        "BA": 0.25, "ALA": 0.25, "CSR": 0.25, "NE": 0.25,
    },
    "ba_ala_only": {
        "BA": 0.50, "ALA": 0.50, "CSR": 0.00, "NE": 0.00,
    },
}


@dataclass
class WeightSchemeResult:
    scheme_name: str
    weights:     dict[str, float]
    mean_fbs:    float
    by_difficulty: dict[int, float] = field(default_factory=dict)
    # Spearman rank correlation with default scheme (1.0 = identical ordinal ranking)
    rank_corr_with_default: Optional[float] = None


@dataclass
class SensitivityReport:
    """
    FBS computed under multiple weight schemes.

    If ordinal rankings are stable across schemes (high rank correlations),
    the default weights are defensible as a design choice rather than an
    arbitrary one that determines conclusions.
    """
    schemes: list[WeightSchemeResult] = field(default_factory=list)
    rankings_stable: bool = False  # True if all rank correlations > 0.95

    def print_summary(self):
        print("\nFBS Weight Sensitivity Analysis")
        print("-" * 55)
        header = f"{'Scheme':<15}" + "".join(f"  L{i}" for i in range(1, 6)) + "  Overall  RankCorr"
        print(header)
        for s in self.schemes:
            lvl_str = "".join(f"  {s.by_difficulty.get(i, 0.0):5.1f}" for i in range(1, 6))
            rho = f"  {s.rank_corr_with_default:.3f}" if s.rank_corr_with_default is not None else "   ref  "
            print(f"  {s.scheme_name:<13}{lvl_str}  {s.mean_fbs:7.1f}{rho}")
        status = "STABLE (ordinal rankings robust to weight choices)" if self.rankings_stable else "UNSTABLE -- weights affect conclusions"
        print(f"\n  Rank stability: {status}")


def _spearman(x: list[float], y: list[float]) -> float:
    """Spearman rank correlation between two lists of equal length."""
    n = len(x)
    if n < 2:
        return 1.0

    def _ranks(vals: list[float]) -> list[float]:
        sorted_vals = sorted(enumerate(vals), key=lambda kv: kv[1])
        ranks = [0.0] * n
        for rank, (idx, _) in enumerate(sorted_vals, 1):
            ranks[idx] = float(rank)
        return ranks

    rx, ry = _ranks(x), _ranks(y)
    d2 = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return round(1 - (6 * d2) / (n * (n * n - 1)), 4)


def fbs_sensitivity(
    results: list[ProblemMetrics],
    max_mae: float = 50_000.0,
) -> SensitivityReport:
    """
    Compute FBS for each problem under each weight scheme in WEIGHT_SCHEMES.
    Report mean FBS overall and per difficulty, plus Spearman rank correlation
    with the default scheme.

    A rank_corr > 0.95 with default across all alternative schemes means the
    default weights don't determine ordinal conclusions — defensible for ACL.
    """
    report = SensitivityReport()

    # Compute per-problem NE (needed to recompute FBS from scratch per scheme)
    def _ne(r: ProblemMetrics) -> float:
        return 1.0 - min(r.MAE / max_mae, 1.0)

    # Default FBS scores per problem (for rank correlation reference)
    default_fbs_per_problem = [r.FBS for r in results]

    scheme_results: list[WeightSchemeResult] = []
    for scheme_name, weights in WEIGHT_SCHEMES.items():
        per_problem_fbs = []
        for r in results:
            ne = _ne(r)
            raw = (
                weights.get("BA", 0)  * r.BA
                + weights.get("ALA", 0) * r.ALA
                + weights.get("CSR", 0) * r.CSR
                + weights.get("NE", 0)  * ne
                # TPA omitted — these schemes are all for no-TPA evaluation
            )
            per_problem_fbs.append(round(raw * 100, 2))

        mean_fbs = round(sum(per_problem_fbs) / len(per_problem_fbs), 2) if per_problem_fbs else 0.0

        by_diff: dict[int, list[float]] = {}
        for r, fbs in zip(results, per_problem_fbs):
            by_diff.setdefault(r.difficulty, []).append(fbs)
        by_diff_means = {lvl: round(sum(v) / len(v), 2) for lvl, v in by_diff.items()}

        rho = None if scheme_name == "default" else _spearman(default_fbs_per_problem, per_problem_fbs)

        scheme_results.append(WeightSchemeResult(
            scheme_name=scheme_name,
            weights=weights,
            mean_fbs=mean_fbs,
            by_difficulty=by_diff_means,
            rank_corr_with_default=rho,
        ))

    report.schemes = scheme_results
    non_default_rhos = [s.rank_corr_with_default for s in scheme_results if s.rank_corr_with_default is not None]
    report.rankings_stable = bool(non_default_rhos) and all(r >= 0.95 for r in non_default_rhos)
    return report
