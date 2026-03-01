"""
Error detection and taxonomy for the FinBalance benchmark.

Eight error categories (from the research plan):
  AE  – Arithmetic Errors
  CE  – Classification Errors
  OE  – Omission Errors
  CO  – Commission Errors (hallucinations)
  CV  – Constraint Violation Errors
  PE  – Propagation Errors
  FE  – Format / Parsing Errors
  CNE – Conceptual Errors
"""

from dataclasses import dataclass, field
from typing import Optional

from finbalance.data.schemas import BalanceSheet, IntermediateState, Problem

EPSILON = 1.0
LARGE_ERROR_PCT = 0.10   # >10% of account value = "large" arithmetic error


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class DetectedError:
    category:    str        # AE | CE | OE | CO | CV | PE | FE | CNE
    subcategory: str        # e.g. AE-Add, CE-Account
    severity:    str        # Critical | High | Medium | Low
    account:     Optional[str] = None
    description: str = ""
    predicted:   Optional[float] = None
    expected:    Optional[float] = None
    difference:  Optional[float] = None


@dataclass
class ErrorReport:
    problem_id: str
    errors:     list[DetectedError] = field(default_factory=list)
    parse_failed: bool = False

    # Summary counts per category
    @property
    def by_category(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for e in self.errors:
            counts[e.category] = counts.get(e.category, 0) + 1
        return counts

    @property
    def has_critical(self) -> bool:
        return any(e.severity == "Critical" for e in self.errors)

    @property
    def total_errors(self) -> int:
        return len(self.errors)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _norm(name: str) -> str:
    return name.lower().strip()


def _flat(section_dict: dict) -> dict[str, float]:
    return {k: float(v) for k, v in section_dict.items() if isinstance(v, (int, float))}


def _flat_pred(predicted: dict) -> dict[str, float]:
    out = {}
    for sec in ("assets", "liabilities", "equity"):
        out.update(_flat(predicted.get(sec, {})))
    return out


def _flat_exp(expected_bs: BalanceSheet) -> dict[str, float]:
    out = {}
    for sec in (expected_bs.assets, expected_bs.liabilities, expected_bs.equity):
        out.update({k: v for k, v in sec.items() if abs(v) > 0.01})
    return out


def _find_expected_account(pred_acc: str, expected_flat: dict[str, float]) -> Optional[str]:
    """Try to find expected account matching pred_acc (case-insensitive)."""
    if pred_acc in expected_flat:
        return pred_acc
    pn = _norm(pred_acc)
    for exp_acc in expected_flat:
        if _norm(exp_acc) == pn:
            return exp_acc
    return None


def _section_of(account: str, predicted: dict) -> Optional[str]:
    for sec in ("assets", "liabilities", "equity"):
        if account in predicted.get(sec, {}):
            return sec
    return None


def _expected_section(account: str, expected_bs: BalanceSheet) -> Optional[str]:
    if account in expected_bs.assets:
        return "assets"
    if account in expected_bs.liabilities:
        return "liabilities"
    if account in expected_bs.equity:
        return "equity"
    return None


# ---------------------------------------------------------------------------
# Error detectors
# ---------------------------------------------------------------------------

def _check_format(predicted) -> list[DetectedError]:
    errors = []
    if not isinstance(predicted, dict):
        errors.append(DetectedError("FE", "FE-Structure", "Critical",
                                    description="Response is not a JSON object"))
        return errors
    for sec in ("assets", "liabilities", "equity"):
        if sec not in predicted:
            errors.append(DetectedError("FE", "FE-Missing", "Critical",
                                        description=f"Missing required section '{sec}'"))
        elif not isinstance(predicted[sec], dict):
            errors.append(DetectedError("FE", "FE-Type", "High",
                                        description=f"Section '{sec}' is not an object"))
        else:
            for k, v in predicted[sec].items():
                if not isinstance(v, (int, float)):
                    errors.append(DetectedError("FE", "FE-Type", "Medium", account=k,
                                                description=f"Account '{k}' value is not numeric: {v!r}"))
    return errors


def _check_constraint_violations(predicted: dict) -> list[DetectedError]:
    errors = []
    assets = _flat(predicted.get("assets", {}))
    liabs  = _flat(predicted.get("liabilities", {}))
    equity = _flat(predicted.get("equity", {}))
    ta = sum(assets.values())
    tl = sum(liabs.values())
    te = sum(equity.values())

    if abs(ta - (tl + te)) > EPSILON:
        diff = ta - (tl + te)
        errors.append(DetectedError("CV", "CV-Balance", "Critical",
                                    description=f"Assets({ta:.0f}) != L+E({tl+te:.0f}), diff={diff:.0f}"))

    for acc, val in assets.items():
        if val < -EPSILON and "Depreciation" not in acc:
            errors.append(DetectedError("CV", "CV-Negative", "High", account=acc,
                                        description=f"Unexpected negative asset: {val:.0f}"))

    accum = abs(assets.get("Accumulated Depreciation", 0.0))
    gross = abs(assets.get("Equipment", 0.0)) + abs(assets.get("Furniture", 0.0)) + abs(assets.get("Vehicles", 0.0))
    if accum > gross + EPSILON and gross > 0:
        errors.append(DetectedError("CV", "CV-Contra", "High",
                                    description=f"Accumulated depreciation ({accum:.0f}) > gross assets ({gross:.0f})"))

    return errors


def _check_omissions(predicted: dict, expected_bs: BalanceSheet) -> list[DetectedError]:
    errors = []
    expected_flat = _flat_exp(expected_bs)
    pred_flat = _flat_pred(predicted)
    pred_norms = {_norm(k) for k in pred_flat}

    for exp_acc in expected_flat:
        if exp_acc not in pred_flat and _norm(exp_acc) not in pred_norms:
            errors.append(DetectedError("OE", "OE-Account", "High", account=exp_acc,
                                        description=f"Expected account '{exp_acc}' missing from response",
                                        expected=expected_flat[exp_acc]))
    return errors


def _check_commissions(predicted: dict, expected_bs: BalanceSheet) -> list[DetectedError]:
    errors = []
    expected_flat = _flat_exp(expected_bs)
    exp_norms = {_norm(k) for k in expected_flat}

    for sec in ("assets", "liabilities", "equity"):
        for pred_acc in predicted.get(sec, {}):
            if _norm(pred_acc) not in exp_norms:
                errors.append(DetectedError("CO", "CO-Account", "Medium", account=pred_acc,
                                            description=f"Hallucinated account '{pred_acc}' not in expected output",
                                            predicted=predicted[sec].get(pred_acc)))
    return errors


def _check_arithmetic(predicted: dict, expected_bs: BalanceSheet) -> list[DetectedError]:
    errors = []
    expected_flat = _flat_exp(expected_bs)
    pred_flat = _flat_pred(predicted)

    for exp_acc, exp_val in expected_flat.items():
        # Find the predicted value for this account
        pred_val = pred_flat.get(exp_acc)
        if pred_val is None:
            pn = _norm(exp_acc)
            for k, v in pred_flat.items():
                if _norm(k) == pn:
                    pred_val = v
                    break

        if pred_val is None:
            continue   # omission — handled separately

        diff = abs(pred_val - exp_val)
        if diff > EPSILON:
            pct_err = diff / abs(exp_val) if abs(exp_val) > 0.01 else 1.0
            severity = "High" if pct_err > LARGE_ERROR_PCT else "Medium"
            errors.append(DetectedError("AE", "AE", severity, account=exp_acc,
                                        description=f"Numerical error on '{exp_acc}'",
                                        predicted=pred_val,
                                        expected=exp_val,
                                        difference=pred_val - exp_val))
    return errors


def _check_classification(predicted: dict, expected_bs: BalanceSheet) -> list[DetectedError]:
    """
    Classification error: account exists but is in the wrong section.
    """
    errors = []
    for exp_acc, exp_val in _flat_exp(expected_bs).items():
        expected_sec = _expected_section(exp_acc, expected_bs)
        pred_sec = _section_of(exp_acc, predicted)

        if pred_sec is None:
            # Try case-insensitive
            pn = _norm(exp_acc)
            for sec in ("assets", "liabilities", "equity"):
                for k in predicted.get(sec, {}):
                    if _norm(k) == pn:
                        pred_sec = sec
                        break
                if pred_sec:
                    break

        if pred_sec and pred_sec != expected_sec:
            errors.append(DetectedError("CE", "CE-Account", "High", account=exp_acc,
                                        description=f"'{exp_acc}' placed in '{pred_sec}', expected '{expected_sec}'",
                                        expected=exp_val))
    return errors


def _check_propagation(
    predicted_states: list[dict],
    expected_states: list[IntermediateState],
) -> list[DetectedError]:
    """
    Detect error propagation: an intermediate state is wrong and subsequent states
    continue to be wrong, suggesting a cascade rather than independent errors.
    """
    if not predicted_states or not expected_states:
        return []

    errors = []
    n = min(len(predicted_states), len(expected_states))
    first_error_idx = None

    for i, (ps, es) in enumerate(zip(predicted_states[:n], expected_states[:n])):
        pa = ps.get("assets_total", 0.0)
        if abs(pa - es.assets_total) > EPSILON:
            if first_error_idx is None:
                first_error_idx = i
            elif first_error_idx is not None:
                errors.append(DetectedError("PE", "PE-Cascade", "High",
                                            description=f"Error at step {i+1} likely propagated from step {first_error_idx+1}",
                                            difference=pa - es.assets_total))

    return errors


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def detect_errors(
    problem: Problem,
    predicted,                    # raw parsed model response (may be dict or garbage)
    predicted_states: Optional[list[dict]] = None,
) -> ErrorReport:
    """
    Run all error checks and return an ErrorReport.

    Args:
        problem:          ground-truth Problem
        predicted:        parsed model output (or None if parse failed)
        predicted_states: optional intermediate state dicts for propagation analysis
    """
    report = ErrorReport(problem_id=problem.problem_id)

    # FE: format/parse errors first
    if predicted is None:
        report.parse_failed = True
        report.errors.append(DetectedError("FE", "FE-Structure", "Critical",
                                           description="Model response could not be parsed as JSON"))
        return report

    fmt_errors = _check_format(predicted)
    report.errors.extend(fmt_errors)
    if any(e.subcategory == "FE-Structure" for e in fmt_errors):
        return report   # can't do deeper checks without valid structure

    # CV: constraint violations
    report.errors.extend(_check_constraint_violations(predicted))

    # CE: classification errors
    report.errors.extend(_check_classification(predicted, problem.expected))

    # AE: arithmetic errors (only on non-classification-errored accounts to avoid double count)
    ae = _check_arithmetic(predicted, problem.expected)
    ce_accounts = {e.account for e in report.errors if e.category == "CE"}
    ae = [e for e in ae if e.account not in ce_accounts]
    report.errors.extend(ae)

    # OE: omission errors
    report.errors.extend(_check_omissions(predicted, problem.expected))

    # CO: commission errors (hallucinations)
    report.errors.extend(_check_commissions(predicted, problem.expected))

    # PE: propagation errors (only if intermediate states provided)
    if predicted_states:
        report.errors.extend(_check_propagation(predicted_states, problem.intermediate_states))

    return report


# ---------------------------------------------------------------------------
# Aggregate error statistics
# ---------------------------------------------------------------------------

@dataclass
class ErrorStats:
    total_problems: int = 0
    total_errors:   int = 0
    by_category:    dict = field(default_factory=dict)
    critical_rate:  float = 0.0
    parse_fail_rate: float = 0.0
    error_rate_by_difficulty: dict = field(default_factory=dict)


def aggregate_errors(reports: list[ErrorReport], difficulties: list[int]) -> ErrorStats:
    stats = ErrorStats(total_problems=len(reports))
    stats.total_errors = sum(r.total_errors for r in reports)
    stats.critical_rate = sum(1 for r in reports if r.has_critical) / len(reports) if reports else 0.0
    stats.parse_fail_rate = sum(1 for r in reports if r.parse_failed) / len(reports) if reports else 0.0

    category_counts: dict[str, int] = {}
    for r in reports:
        for cat, cnt in r.by_category.items():
            category_counts[cat] = category_counts.get(cat, 0) + cnt
    total = sum(category_counts.values()) or 1
    stats.by_category = {cat: {"count": cnt, "pct": round(cnt / total * 100, 1)}
                         for cat, cnt in sorted(category_counts.items(), key=lambda x: -x[1])}

    # Per difficulty
    diff_buckets: dict[int, list[ErrorReport]] = {}
    for r, d in zip(reports, difficulties):
        diff_buckets.setdefault(d, []).append(r)
    for d, bucket in diff_buckets.items():
        stats.error_rate_by_difficulty[d] = round(
            sum(r.total_errors for r in bucket) / len(bucket), 2
        )

    return stats
