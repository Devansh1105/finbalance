"""
All evaluation metrics from the FinBalance research plan.

Metrics implemented:
  BA   – Balance Accuracy         (hard constraint: Assets = L + E)
  ALA  – Account-Level Accuracy   (per-account correctness)
  TPA  – Transaction Processing Accuracy (via intermediate states)
  NE   – Numerical Error          (MAE, MAPE, RMSE)
  CSR  – Constraint Satisfaction Rate
  FBS  – FinBalance Score         (weighted aggregate)
"""

import math
from dataclasses import dataclass, field
from typing import Optional

from finbalance.data.schemas import BalanceSheet, IntermediateState, Problem

EPSILON = 1.0          # tolerance for balance equation (1 currency unit)
ACCOUNT_TOLERANCE_ABS  = 10.0   # ALA absolute floor: within ±$10
ACCOUNT_TOLERANCE_PCT  = 0.01   # ALA percentage: within ±1% of expected value
                                  # Hybrid (default): max($10, 1% of expected)

# Weights for FBS when all components are available (TPA requires CoT/self_refine)
FBS_WEIGHTS = {
    "BA":  0.30,
    "ALA": 0.25,
    "TPA": 0.20,
    "CSR": 0.15,
    "NE":  0.10,
}

# Weights when TPA is unavailable (zero_shot / few_shot produce no intermediate states).
# TPA's 0.20 weight is redistributed proportionally across the remaining components.
FBS_WEIGHTS_NO_TPA = {
    "BA":  0.375,   # 0.30 / 0.80
    "ALA": 0.3125,  # 0.25 / 0.80
    "CSR": 0.1875,  # 0.15 / 0.80
    "NE":  0.125,   # 0.10 / 0.80
}

DIFFICULTY_WEIGHTS = {1: 0.10, 2: 0.20, 3: 0.30, 4: 0.30, 5: 0.10}


# ---------------------------------------------------------------------------
# Per-problem result
# ---------------------------------------------------------------------------

@dataclass
class ProblemMetrics:
    problem_id:   str
    difficulty:   int

    # Primary
    BA:   float = 0.0   # 0 or 1
    ALA:  float = 0.0   # 0-1
    TPA:  float = 0.0   # 0-1
    CSR:  float = 0.0   # 0-1

    # Numerical error
    MAE:  float = 0.0
    MAPE: Optional[float] = None
    RMSE: float = 0.0

    # Aggregate
    FBS:  float = 0.0

    # Extras
    n_accounts_expected:  int = 0
    n_accounts_correct:   int = 0
    assets_predicted:     float = 0.0
    liabilities_predicted: float = 0.0
    equity_predicted:     float = 0.0
    assets_expected:      float = 0.0
    parse_error:          bool = False
    constraint_details:   dict = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _normalise_account_name(name: str) -> str:
    """Lowercase + strip for fuzzy matching."""
    return name.lower().strip()


def _match_accounts(
    predicted: dict[str, float], expected: dict[str, float]
) -> dict[str, tuple[Optional[float], float]]:
    """
    Match predicted accounts to expected accounts.
    Returns {expected_account: (predicted_value_or_None, expected_value)}.
    Uses exact match first, then case-insensitive fallback.
    """
    result = {}
    pred_lower = {_normalise_account_name(k): v for k, v in predicted.items()}
    for exp_acc, exp_val in expected.items():
        pred_val = predicted.get(exp_acc)
        if pred_val is None:
            pred_val = pred_lower.get(_normalise_account_name(exp_acc))
        result[exp_acc] = (pred_val, exp_val)
    return result


def _flat_expected(expected_bs: BalanceSheet) -> dict[str, float]:
    """Merge all sections into one flat dict, excluding zero-value accounts."""
    flat = {}
    for section in (expected_bs.assets, expected_bs.liabilities, expected_bs.equity):
        for acc, val in section.items():
            if abs(val) > 0.01:
                flat[acc] = val
    return flat


def _flat_predicted(predicted: dict) -> tuple[dict[str, float], dict[str, float], dict[str, float], float, float, float]:
    """Extract per-section dicts and totals from a parsed model response."""
    assets      = predicted.get("assets", {})
    liabilities = predicted.get("liabilities", {})
    equity      = predicted.get("equity", {})

    def _sum(d):
        return sum(float(v) for v in d.values() if isinstance(v, (int, float)))

    return assets, liabilities, equity, _sum(assets), _sum(liabilities), _sum(equity)


# ---------------------------------------------------------------------------
# Metric functions
# ---------------------------------------------------------------------------

def balance_accuracy(pred_assets: float, pred_liabilities: float, pred_equity: float) -> float:
    """BA: 1.0 if the accounting equation holds within EPSILON."""
    return 1.0 if abs(pred_assets - (pred_liabilities + pred_equity)) <= EPSILON else 0.0


def account_level_accuracy(
    predicted: dict, expected_bs: BalanceSheet, strict: bool = False
) -> tuple[float, int, int]:
    """
    ALA: fraction of expected accounts predicted within tolerance.
    Returns (ALA, n_correct, n_total).

    Tolerance (default hybrid, strict=False):
        max(ACCOUNT_TOLERANCE_ABS, expected_value * ACCOUNT_TOLERANCE_PCT)
        i.e. max($10, 1% of expected) — scale-invariant across difficulty levels.

    Strict mode (strict=True): flat ±$10 regardless of account magnitude.
    """
    expected_flat = _flat_expected(expected_bs)
    if not expected_flat:
        return 1.0, 0, 0

    pred_flat: dict[str, float] = {}
    for section in ("assets", "liabilities", "equity"):
        for k, v in predicted.get(section, {}).items():
            if isinstance(v, (int, float)):
                pred_flat[k] = float(v)

    matched = _match_accounts(pred_flat, expected_flat)
    n_correct = 0
    for exp_acc, (pred_val, exp_val) in matched.items():
        if pred_val is None:
            continue
        tol = ACCOUNT_TOLERANCE_ABS if strict else max(ACCOUNT_TOLERANCE_ABS, abs(exp_val) * ACCOUNT_TOLERANCE_PCT)
        if abs(pred_val - exp_val) <= tol:
            n_correct += 1

    return n_correct / len(expected_flat), n_correct, len(expected_flat)


def transaction_processing_accuracy(
    predicted_states: list[dict],   # list of {after_tx_id, assets, liabilities, equity}
    expected_states: list[IntermediateState],
) -> float:
    """
    TPA: fraction of intermediate snapshots within tolerance.
    Only applicable when models output step-by-step reasoning + states.
    Returns 0.0 if no states provided.
    """
    if not predicted_states or not expected_states:
        return 0.0

    n = min(len(predicted_states), len(expected_states))
    correct = 0
    for ps, es in zip(predicted_states[:n], expected_states[:n]):
        pa = ps.get("assets_total", 0.0)
        pl = ps.get("liabilities_total", 0.0)
        pe = ps.get("equity_total", 0.0)
        if (
            abs(pa - es.assets_total) <= EPSILON
            and abs(pl - es.liabilities_total) <= EPSILON
            and abs(pe - es.equity_total) <= EPSILON
        ):
            correct += 1
    return correct / n


def numerical_errors(
    predicted: dict, expected_bs: BalanceSheet
) -> tuple[float, Optional[float], float]:
    """
    Returns (MAE, MAPE, RMSE) across all expected account values.
    MAPE is None if any expected value is zero.
    """
    expected_flat = _flat_expected(expected_bs)
    if not expected_flat:
        return 0.0, None, 0.0

    pred_flat: dict[str, float] = {}
    for section in ("assets", "liabilities", "equity"):
        for k, v in predicted.get(section, {}).items():
            if isinstance(v, (int, float)):
                pred_flat[k] = float(v)

    matched = _match_accounts(pred_flat, expected_flat)
    errors = []
    pct_errors = []
    has_zero = False

    for exp_acc, (pred_val, exp_val) in matched.items():
        pv = pred_val if pred_val is not None else 0.0
        err = abs(pv - exp_val)
        errors.append(err)
        if abs(exp_val) > 0.01:
            pct_errors.append(err / abs(exp_val) * 100)
        else:
            has_zero = True

    mae  = sum(errors) / len(errors) if errors else 0.0
    rmse = math.sqrt(sum(e**2 for e in errors) / len(errors)) if errors else 0.0
    mape = (sum(pct_errors) / len(pct_errors)) if pct_errors and not has_zero else None

    return round(mae, 2), (round(mape, 2) if mape else None), round(rmse, 2)


def constraint_satisfaction_rate(
    predicted: dict, expected_bs: BalanceSheet
) -> tuple[float, dict]:
    """
    CSR: fraction of accounting constraints satisfied.
    Returns (rate, {constraint_name: bool}).
    """
    checks: dict[str, bool] = {}

    assets, liabilities, equity, ta, tl, te = _flat_predicted(predicted)

    # 1. Balance equation
    checks["balance_equation"] = abs(ta - (tl + te)) <= EPSILON

    # 2. Non-negativity of asset accounts (contra-assets are expected to be negative)
    from finbalance.data.schemas import ACCOUNT_TYPE
    for acc, val in assets.items():
        if isinstance(val, (int, float)):
            if ACCOUNT_TYPE.get(acc, "asset") != "contra_asset":
                checks[f"non_negative_{acc}"] = float(val) >= -EPSILON

    # 3. Contra-asset rule: accumulated depr ≤ gross asset (simplified check)
    accum_depr = float(assets.get("Accumulated Depreciation", 0.0))
    equipment  = float(assets.get("Equipment", 0.0))
    furniture  = float(assets.get("Furniture", 0.0))
    vehicles   = float(assets.get("Vehicles", 0.0))
    gross_depreciable = abs(equipment) + abs(furniture) + abs(vehicles)
    if accum_depr != 0.0 or gross_depreciable > 0:
        checks["contra_asset_rule"] = abs(accum_depr) <= gross_depreciable + EPSILON

    # 4. Total assets ≥ 0
    checks["total_assets_positive"] = ta >= 0

    # 5. Expected account presence (completeness)
    expected_flat = _flat_expected(expected_bs)
    pred_flat = {**assets, **liabilities, **equity}
    missing = [k for k in expected_flat if k not in pred_flat
               and _normalise_account_name(k) not in {_normalise_account_name(p) for p in pred_flat}]
    checks["completeness"] = len(missing) == 0

    total = len(checks)
    satisfied = sum(1 for v in checks.values() if v)
    return round(satisfied / total, 4) if total else 1.0, checks


def _normalise_account_name(name: str) -> str:
    return name.lower().strip()


def finbalance_score(
    ba: float,
    ala: float,
    tpa: float,
    csr: float,
    mae: float,
    max_mae: float = 50_000.0,
    tpa_available: bool = False,
) -> float:
    """
    FBS: weighted aggregate on 0-100 scale.
    NE component = 1 - normalised MAE (capped at max_mae).

    tpa_available: set True only when the model outputs intermediate ledger states
                   (i.e. CoT / self_refine strategies). For zero_shot and few_shot,
                   TPA is structurally 0, so its weight is redistributed across the
                   remaining components (FBS_WEIGHTS_NO_TPA) to avoid systematic
                   deflation of scores across strategies.
    """
    ne_norm = 1.0 - min(mae / max_mae, 1.0)
    if tpa_available:
        w = FBS_WEIGHTS
        raw = (
            w["BA"]  * ba
            + w["ALA"] * ala
            + w["TPA"] * tpa
            + w["CSR"] * csr
            + w["NE"]  * ne_norm
        )
    else:
        w = FBS_WEIGHTS_NO_TPA
        raw = (
            w["BA"]  * ba
            + w["ALA"] * ala
            + w["CSR"] * csr
            + w["NE"]  * ne_norm
        )
    return round(raw * 100, 2)


# ---------------------------------------------------------------------------
# Main evaluation entry point
# ---------------------------------------------------------------------------

def evaluate_problem(
    problem: Problem,
    predicted: dict,            # parsed model JSON response
    predicted_states: Optional[list[dict]] = None,
) -> ProblemMetrics:
    """
    Compute all metrics for a single problem.

    Args:
        problem:          ground-truth Problem object
        predicted:        model output as dict {assets:{}, liabilities:{}, equity:{}}
        predicted_states: optional list of intermediate state dicts (for TPA).
                          Pass only for CoT / self_refine strategies. When None or
                          empty, TPA weight is redistributed in FBS (see finbalance_score).
    """
    m = ProblemMetrics(problem_id=problem.problem_id, difficulty=problem.difficulty_level)

    _, _, _, pa, pl, pe = _flat_predicted(predicted)
    m.assets_predicted      = round(pa, 2)
    m.liabilities_predicted = round(pl, 2)
    m.equity_predicted      = round(pe, 2)
    m.assets_expected       = problem.expected.total_assets

    tpa_available = bool(predicted_states)
    m.BA  = balance_accuracy(pa, pl, pe)
    m.ALA, m.n_accounts_correct, m.n_accounts_expected = account_level_accuracy(predicted, problem.expected)
    m.TPA = transaction_processing_accuracy(predicted_states or [], problem.intermediate_states)
    m.CSR, m.constraint_details = constraint_satisfaction_rate(predicted, problem.expected)
    m.MAE, m.MAPE, m.RMSE = numerical_errors(predicted, problem.expected)
    m.FBS = finbalance_score(m.BA, m.ALA, m.TPA, m.CSR, m.MAE, tpa_available=tpa_available)

    return m


# ---------------------------------------------------------------------------
# Aggregate across many problems
# ---------------------------------------------------------------------------

@dataclass
class AggregateMetrics:
    n_problems:   int = 0
    BA:           float = 0.0
    ALA:          float = 0.0
    TPA:          float = 0.0
    CSR:          float = 0.0
    MAE:          float = 0.0
    RMSE:         float = 0.0
    FBS:          float = 0.0
    FBS_weighted: float = 0.0   # difficulty-weighted
    by_difficulty: dict = field(default_factory=dict)
    parse_error_rate: float = 0.0


def aggregate(results: list[ProblemMetrics]) -> AggregateMetrics:
    if not results:
        return AggregateMetrics()

    agg = AggregateMetrics(n_problems=len(results))
    fields = ["BA", "ALA", "TPA", "CSR", "MAE", "RMSE", "FBS"]
    for f in fields:
        setattr(agg, f, round(sum(getattr(r, f) for r in results) / len(results), 4))

    # Difficulty-weighted FBS
    by_diff: dict[int, list[ProblemMetrics]] = {}
    for r in results:
        by_diff.setdefault(r.difficulty, []).append(r)

    weighted_sum = 0.0
    weight_total = 0.0
    for lvl, lvl_results in by_diff.items():
        w = DIFFICULTY_WEIGHTS.get(lvl, 0.0)
        lvl_fbs = sum(r.FBS for r in lvl_results) / len(lvl_results)
        weighted_sum += w * lvl_fbs
        weight_total += w
        agg.by_difficulty[lvl] = {
            "n": len(lvl_results),
            "BA":  round(sum(r.BA  for r in lvl_results) / len(lvl_results), 4),
            "ALA": round(sum(r.ALA for r in lvl_results) / len(lvl_results), 4),
            "FBS": round(lvl_fbs, 2),
        }

    agg.FBS_weighted = round(weighted_sum / weight_total if weight_total else 0.0, 2)
    agg.parse_error_rate = round(sum(1 for r in results if r.parse_error) / len(results), 4)

    return agg
