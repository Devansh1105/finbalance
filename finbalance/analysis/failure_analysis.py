"""
FinBalance Failure Analysis
============================
Produces structured, paper-ready failure diagnostics by connecting raw model
outputs to the ground-truth problems.

Five analysis dimensions:
  1. ComplexityDrivers   — which transaction/adjustment features correlate with failure
  2. AccountMissRates    — per-account omission / arithmetic / hallucination rates
  3. BalanceFailureCauses— root-cause breakdown when BA = 0
  4. HallucinationCatalog— most frequent fabricated accounts
  5. DifficultyGradient  — how error composition shifts across levels 1-5
"""

from __future__ import annotations
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Optional

from finbalance.data.schemas import ACCOUNT_TYPE, BalanceSheet, Problem


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def _norm(name: str) -> str:
    return name.lower().strip()


def _flat_pred(predicted: dict) -> dict[str, float]:
    out: dict[str, float] = {}
    for sec in ("assets", "liabilities", "equity"):
        for k, v in predicted.get(sec, {}).items():
            if isinstance(v, (int, float)):
                out[k] = float(v)
    return out


def _flat_exp(bs: BalanceSheet) -> dict[str, float]:
    out: dict[str, float] = {}
    for sec in (bs.assets, bs.liabilities, bs.equity):
        out.update({k: v for k, v in sec.items() if abs(v) > 0.01})
    return out


def _match(pred_key: str, expected_flat: dict[str, float]) -> Optional[str]:
    if pred_key in expected_flat:
        return pred_key
    pn = _norm(pred_key)
    for k in expected_flat:
        if _norm(k) == pn:
            return k
    return None


def _expected_section(account: str, bs: BalanceSheet) -> Optional[str]:
    if account in bs.assets:        return "assets"
    if account in bs.liabilities:   return "liabilities"
    if account in bs.equity:        return "equity"
    return None


EPSILON = 1.0


# ──────────────────────────────────────────────────────────────────────────────
# 1. Complexity Driver Analysis
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class FeatureGroup:
    feature:          str
    n_problems:       int = 0
    avg_fbs:          float = 0.0
    avg_ala:          float = 0.0
    avg_errors:       float = 0.0
    ba_rate:          float = 0.0   # fraction where balance equation holds
    # Compared to problems WITHOUT this feature
    fbs_delta:        float = 0.0   # avg_fbs(with) - avg_fbs(without)
    ala_delta:        float = 0.0


@dataclass
class ComplexityDriverReport:
    features: list[FeatureGroup] = field(default_factory=list)


def analyze_complexity_drivers(
    problems:   list[Problem],
    metrics:    list[dict],          # list of metric dicts (from results JSON)
    error_counts: list[dict],        # list of error_categories dicts
) -> ComplexityDriverReport:
    """
    For each complexity factor (cogs, mixed_funding, derived_interest, etc.)
    compare FBS / ALA / error rate on problems that HAVE the factor vs. those
    that DON'T.
    """
    # Collect all observed complexity factors
    all_factors: set[str] = set()
    for p in problems:
        for tx in p.transactions:
            all_factors.update(tx.complexity_factors)

    # Map problem_id -> metrics
    metrics_by_id = {m["problem_id"]: m for m in metrics}

    groups: list[FeatureGroup] = []
    for feature in sorted(all_factors):
        with_ids  = set()
        without_ids = set()
        for p in problems:
            has = any(feature in tx.complexity_factors for tx in p.transactions)
            if has:
                with_ids.add(p.problem_id)
            else:
                without_ids.add(p.problem_id)

        def _avg(ids: set, key: str) -> float:
            vals = [metrics_by_id[pid][key] for pid in ids if pid in metrics_by_id]
            return sum(vals) / len(vals) if vals else 0.0

        def _avg_errs(ids: set) -> float:
            vals = [metrics_by_id[pid].get("n_errors", 0) for pid in ids if pid in metrics_by_id]
            return sum(vals) / len(vals) if vals else 0.0

        def _ba_rate(ids: set) -> float:
            vals = [metrics_by_id[pid]["BA"] for pid in ids if pid in metrics_by_id]
            return sum(vals) / len(vals) if vals else 0.0

        fg = FeatureGroup(
            feature     = feature,
            n_problems  = len(with_ids),
            avg_fbs     = round(_avg(with_ids, "FBS"), 2),
            avg_ala     = round(_avg(with_ids, "ALA"), 4),
            avg_errors  = round(_avg_errs(with_ids), 2),
            ba_rate     = round(_ba_rate(with_ids), 4),
        )
        fg.fbs_delta = round(fg.avg_fbs - _avg(without_ids, "FBS"), 2)
        fg.ala_delta = round(fg.avg_ala - _avg(without_ids, "ALA"), 4)
        groups.append(fg)

    # Sort by fbs_delta (most harmful feature first)
    groups.sort(key=lambda g: g.fbs_delta)
    return ComplexityDriverReport(features=groups)


# ──────────────────────────────────────────────────────────────────────────────
# 2. Account-Level Miss Rate
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class AccountStats:
    account:         str
    account_type:    str
    n_expected:      int = 0   # problems where this account is in ground truth
    n_omitted:       int = 0   # model misses it entirely
    n_arithmetic:    int = 0   # model has it but value is wrong
    n_correct:       int = 0   # model has correct value
    n_hallucinated:  int = 0   # model adds it when NOT in ground truth
    # Rates
    omission_rate:   float = 0.0
    arithmetic_rate: float = 0.0
    hallucination_rate: float = 0.0   # per problem WHERE it is not expected
    avg_abs_error:   float = 0.0


@dataclass
class AccountMissRateReport:
    accounts: list[AccountStats] = field(default_factory=list)
    # Top offenders
    most_omitted:     list[tuple[str, float]] = field(default_factory=list)
    most_arithmetic:  list[tuple[str, float]] = field(default_factory=list)
    most_hallucinated: list[tuple[str, float]] = field(default_factory=list)


def analyze_account_miss_rates(
    problems:  list[Problem],
    responses: list[Optional[dict]],   # parsed model outputs (None if parse failed)
) -> AccountMissRateReport:
    """Per-account breakdown of omission, arithmetic error, and hallucination."""

    stats: dict[str, AccountStats] = {}
    # Track how many problems each account appeared in ground truth vs not
    n_not_expected: Counter = Counter()
    abs_errors: dict[str, list[float]] = defaultdict(list)

    for problem, pred in zip(problems, responses):
        if pred is None:
            continue
        exp_flat  = _flat_exp(problem.expected)
        pred_flat = _flat_pred(pred)
        pred_norms = {_norm(k): k for k in pred_flat}

        # Initialise stats entries for expected accounts
        for acc, exp_val in exp_flat.items():
            if acc not in stats:
                stats[acc] = AccountStats(
                    account=acc,
                    account_type=ACCOUNT_TYPE.get(acc, "unknown"),
                )
            s = stats[acc]
            s.n_expected += 1

            pred_val = pred_flat.get(acc)
            if pred_val is None:
                pred_val_norm = pred_norms.get(_norm(acc))
                if pred_val_norm is not None:
                    pred_val = pred_flat[pred_val_norm]

            if pred_val is None:
                s.n_omitted += 1
            elif abs(pred_val - exp_val) <= EPSILON:
                s.n_correct += 1
            else:
                s.n_arithmetic += 1
                abs_errors[acc].append(abs(pred_val - exp_val))

        # Hallucinations: accounts in prediction NOT in expected
        exp_norms = {_norm(k) for k in exp_flat}
        for pred_acc in pred_flat:
            if _norm(pred_acc) not in exp_norms:
                if pred_acc not in stats:
                    stats[pred_acc] = AccountStats(
                        account=pred_acc,
                        account_type=ACCOUNT_TYPE.get(pred_acc, "unknown"),
                    )
                stats[pred_acc].n_hallucinated += 1
            else:
                n_not_expected[pred_acc]  # not incremented here — handled below

        # Track n_not_expected for hallucination rate denominator
        for acc in stats:
            if acc not in exp_flat:
                n_not_expected[acc] += 1

    # Compute rates
    n_problems_with_output = sum(1 for r in responses if r is not None)
    for acc, s in stats.items():
        if s.n_expected > 0:
            s.omission_rate   = round(s.n_omitted    / s.n_expected, 4)
            s.arithmetic_rate = round(s.n_arithmetic / s.n_expected, 4)
        if n_not_expected[acc] > 0:
            s.hallucination_rate = round(s.n_hallucinated / n_not_expected[acc], 4)
        if abs_errors[acc]:
            s.avg_abs_error = round(sum(abs_errors[acc]) / len(abs_errors[acc]), 2)

    account_list = sorted(stats.values(), key=lambda x: -x.n_expected)

    report = AccountMissRateReport(accounts=account_list)
    report.most_omitted = sorted(
        [(s.account, s.omission_rate) for s in account_list if s.n_expected >= 2],
        key=lambda x: -x[1]
    )[:10]
    report.most_arithmetic = sorted(
        [(s.account, s.arithmetic_rate) for s in account_list if s.n_expected >= 2],
        key=lambda x: -x[1]
    )[:10]
    report.most_hallucinated = sorted(
        [(s.account, s.hallucination_rate) for s in account_list if s.n_hallucinated >= 1],
        key=lambda x: -x[1]
    )[:10]

    return report


# ──────────────────────────────────────────────────────────────────────────────
# 3. Balance Equation Failure Root Cause
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class BalanceFailureCause:
    """Root cause classification for a single BA=0 problem."""
    problem_id:    str
    difficulty:    int
    cause:         str          # see CAUSE_ constants below
    description:   str
    imbalance:     float        # Assets - (L + E) in model output
    missing_accounts: list[str] = field(default_factory=list)
    misclassified:    list[str] = field(default_factory=list)


# Cause taxonomy
CAUSE_MISCLASSIFIED    = "misclassified_account"   # account in wrong section
CAUSE_OMITTED_KEY      = "omitted_key_account"     # important account missing
CAUSE_ARITHMETIC       = "arithmetic_error"        # present but wrong value
CAUSE_HALLUCINATED     = "hallucinated_account"    # invented account distorts total
CAUSE_MISSING_SECTION  = "missing_section"         # entire section absent
CAUSE_UNKNOWN          = "unknown"


@dataclass
class BalanceFailureReport:
    n_failures:    int = 0
    causes:        list[BalanceFailureCause] = field(default_factory=list)
    cause_summary: dict[str, int] = field(default_factory=dict)


def analyze_balance_failures(
    problems:  list[Problem],
    responses: list[Optional[dict]],
) -> BalanceFailureReport:
    """Root-cause each BA=0 failure."""

    report = BalanceFailureReport()

    for problem, pred in zip(problems, responses):
        if pred is None:
            continue

        assets_d     = pred.get("assets",      {})
        liabs_d      = pred.get("liabilities", {})
        equity_d     = pred.get("equity",      {})
        ta = sum(float(v) for v in assets_d.values()  if isinstance(v, (int, float)))
        tl = sum(float(v) for v in liabs_d.values()   if isinstance(v, (int, float)))
        te = sum(float(v) for v in equity_d.values()  if isinstance(v, (int, float)))
        imbalance = ta - (tl + te)

        if abs(imbalance) <= EPSILON:
            continue   # balanced — skip

        report.n_failures += 1
        exp_flat = _flat_exp(problem.expected)
        pred_flat = _flat_pred(pred)

        cause = CAUSE_UNKNOWN
        missing: list[str] = []
        misclassified: list[str] = []
        description = ""

        # Test 1: missing section
        if not assets_d or not liabs_d or not equity_d:
            cause = CAUSE_MISSING_SECTION
            missing_secs = [s for s in ("assets","liabilities","equity") if not pred.get(s)]
            description = f"Missing sections: {missing_secs}"

        else:
            # Test 2: misclassified accounts (e.g. liability put under assets)
            for acc, val in pred_flat.items():
                exp_acc = _match(acc, exp_flat)
                if exp_acc is None:
                    continue
                exp_sec = _expected_section(exp_acc, problem.expected)
                pred_sec_actual = None
                for sec in ("assets", "liabilities", "equity"):
                    if acc in pred.get(sec, {}) or _norm(acc) in {_norm(k) for k in pred.get(sec, {})}:
                        pred_sec_actual = sec
                        break
                if exp_sec and pred_sec_actual and exp_sec != pred_sec_actual:
                    misclassified.append(acc)

            # Test 3: omitted high-value accounts
            for acc, exp_val in exp_flat.items():
                if _match(acc, pred_flat) is None:
                    missing.append(acc)

            if misclassified:
                cause = CAUSE_MISCLASSIFIED
                description = (
                    f"Account(s) in wrong section: {misclassified[:3]}"
                    + (f" (+{len(misclassified)-3} more)" if len(misclassified) > 3 else "")
                )
            elif missing:
                # Check if a key structural account is missing (largest absolute value)
                key_missing = sorted(missing, key=lambda a: abs(exp_flat.get(a, 0)), reverse=True)
                cause = CAUSE_OMITTED_KEY
                description = (
                    f"Key account(s) missing: {key_missing[:3]}"
                    + (f" (+{len(key_missing)-3} more)" if len(key_missing) > 3 else "")
                )
            else:
                # Everything present — must be arithmetic error
                cause = CAUSE_ARITHMETIC
                worst = max(exp_flat.items(),
                            key=lambda kv: abs((pred_flat.get(kv[0]) or 0.0) - kv[1]))
                description = (
                    f"Arithmetic error on '{worst[0]}': "
                    f"predicted={(pred_flat.get(worst[0]) or 0.0):.0f} "
                    f"expected={worst[1]:.0f}"
                )

        report.causes.append(BalanceFailureCause(
            problem_id  = problem.problem_id,
            difficulty  = problem.difficulty_level,
            cause       = cause,
            description = description,
            imbalance   = round(imbalance, 2),
            missing_accounts = missing,
            misclassified    = misclassified,
        ))

    # Summarise
    report.cause_summary = dict(Counter(c.cause for c in report.causes))
    return report


# ──────────────────────────────────────────────────────────────────────────────
# 4. Hallucination Catalog
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class HallucinationEntry:
    account_name:    str
    frequency:       int    # how many times it appeared in predictions
    in_schema:       bool   # is it a real accounting account (in ACCOUNT_TYPE)?
    account_type:    Optional[str]   # if in schema


@dataclass
class HallucinationCatalog:
    entries: list[HallucinationEntry] = field(default_factory=list)
    total_hallucinations: int = 0
    schema_known_rate: float = 0.0   # fraction of hallucinations that ARE real accounts
    # In-schema hallucinations indicate classification confusion, not invention
    # Out-of-schema hallucinations indicate pure fabrication


def analyze_hallucinations(
    problems:  list[Problem],
    responses: list[Optional[dict]],
) -> HallucinationCatalog:
    hallucination_counts: Counter = Counter()

    for problem, pred in zip(problems, responses):
        if pred is None:
            continue
        exp_flat   = _flat_exp(problem.expected)
        exp_norms  = {_norm(k) for k in exp_flat}

        for sec in ("assets", "liabilities", "equity"):
            for acc in pred.get(sec, {}):
                if _norm(acc) not in exp_norms:
                    hallucination_counts[acc] += 1

    catalog = HallucinationCatalog()
    catalog.total_hallucinations = sum(hallucination_counts.values())

    entries = []
    for acc, freq in hallucination_counts.most_common():
        in_schema = acc in ACCOUNT_TYPE
        entries.append(HallucinationEntry(
            account_name = acc,
            frequency    = freq,
            in_schema    = in_schema,
            account_type = ACCOUNT_TYPE.get(acc),
        ))
    catalog.entries = entries

    if entries:
        catalog.schema_known_rate = round(
            sum(1 for e in entries if e.in_schema) / len(entries), 4
        )
    return catalog


# ──────────────────────────────────────────────────────────────────────────────
# 5. Difficulty Gradient — error composition per level
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class LevelProfile:
    level:           int
    n_problems:      int
    avg_fbs:         float
    avg_ala:         float
    ba_rate:         float
    avg_n_errors:    float
    error_composition: dict[str, float]   # category -> fraction of total errors
    avg_n_accounts_expected: float
    avg_n_accounts_correct:  float
    # Feature presence rates
    feature_rates:   dict[str, float] = field(default_factory=dict)


@dataclass
class DifficultyGradientReport:
    levels: list[LevelProfile] = field(default_factory=list)


def analyze_difficulty_gradient(
    problems:   list[Problem],
    metrics:    list[dict],
    error_reports: list[list[dict]],   # each: list of {category, subcategory, ...} dicts
) -> DifficultyGradientReport:
    """
    For each difficulty level: aggregate metrics, error composition,
    account coverage, and feature presence.
    """
    buckets: dict[int, list[int]] = defaultdict(list)
    for i, p in enumerate(problems):
        buckets[p.difficulty_level].append(i)

    metrics_by_pid = {m["problem_id"]: m for m in metrics}

    levels = []
    for lvl in sorted(buckets):
        idxs = buckets[lvl]
        lvl_problems = [problems[i] for i in idxs]
        lvl_metrics  = [metrics_by_pid.get(p.problem_id, {}) for p in lvl_problems]
        lvl_errors   = [error_reports[i] for i in idxs]

        def _mean(key: str) -> float:
            vals = [m.get(key, 0.0) for m in lvl_metrics if m]
            return round(sum(vals) / len(vals), 4) if vals else 0.0

        # Error composition
        cat_counts: Counter = Counter()
        total_errors = 0
        for err_list in lvl_errors:
            for e in err_list:
                cat_counts[e.get("category", "?")] += 1
                total_errors += 1
        error_comp = {
            cat: round(cnt / total_errors, 4)
            for cat, cnt in cat_counts.most_common()
        } if total_errors else {}

        # Feature presence rates
        feature_flags: dict[str, list[int]] = defaultdict(list)
        for p in lvl_problems:
            seen = set()
            for tx in p.transactions:
                for f in tx.complexity_factors:
                    seen.add(f)
            for f in seen:
                feature_flags[f].append(1)
            # Also mark features NOT seen
            all_feats = {"cogs", "mixed_funding", "derived_interest", "debt",
                         "prepaid", "credit_transaction", "depreciable_asset"}
            for f in all_feats - seen:
                feature_flags[f].append(0)

        feature_rates = {
            f: round(sum(v) / len(v), 3)
            for f, v in feature_flags.items()
        }

        avg_exp = _mean("n_accounts_expected")
        avg_cor = _mean("n_accounts_correct")

        levels.append(LevelProfile(
            level           = lvl,
            n_problems      = len(idxs),
            avg_fbs         = _mean("FBS"),
            avg_ala         = _mean("ALA"),
            ba_rate         = _mean("BA"),
            avg_n_errors    = sum(len(e) for e in lvl_errors) / len(lvl_errors),
            error_composition = error_comp,
            avg_n_accounts_expected = avg_exp,
            avg_n_accounts_correct  = avg_cor,
            feature_rates   = feature_rates,
        ))

    return DifficultyGradientReport(levels=levels)


# ──────────────────────────────────────────────────────────────────────────────
# Master runner
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class FailureAnalysisReport:
    model_id:            str
    strategy:            str
    n_problems:          int
    complexity_drivers:  ComplexityDriverReport
    account_miss_rates:  AccountMissRateReport
    balance_failures:    BalanceFailureReport
    hallucinations:      HallucinationCatalog
    difficulty_gradient: DifficultyGradientReport


def run_failure_analysis(
    problems:   list[Problem],
    results:    list[dict],     # raw dicts from the results JSON
) -> FailureAnalysisReport:
    """
    Run all five failure analyses.

    Args:
        problems: ground-truth Problem objects (must match result order)
        results:  list of result dicts as saved by EvaluationRunner.save_results()
    """
    # Align by problem_id
    pid_to_problem = {p.problem_id: p for p in problems}
    aligned_problems: list[Problem] = []
    aligned_responses: list[Optional[dict]] = []
    aligned_metrics:   list[dict] = []
    aligned_errors:    list[list[dict]] = []

    for r in results:
        pid = r["problem_id"]
        if pid not in pid_to_problem:
            continue
        aligned_problems.append(pid_to_problem[pid])
        # raw_response field added in our fix; parse it fresh for full fidelity
        from finbalance.evaluation.runner import parse_response
        raw = r.get("raw_response", "")
        aligned_responses.append(parse_response(raw) if raw else None)
        aligned_metrics.append(r)

        # Rebuild per-error list from stored error_categories + error_detection
        from finbalance.analysis.error_detection import detect_errors
        parsed = aligned_responses[-1]
        err_report = detect_errors(pid_to_problem[pid], parsed)
        aligned_errors.append([
            {"category": e.category, "subcategory": e.subcategory,
             "severity": e.severity, "account": e.account,
             "description": e.description, "predicted": e.predicted,
             "expected": e.expected, "difference": e.difference}
            for e in err_report.errors
        ])

    model_id  = results[0].get("model_id",  "unknown") if results else "unknown"
    strategy  = results[0].get("strategy",  "unknown") if results else "unknown"

    return FailureAnalysisReport(
        model_id   = model_id,
        strategy   = strategy,
        n_problems = len(aligned_problems),
        complexity_drivers  = analyze_complexity_drivers(aligned_problems, aligned_metrics, aligned_errors),
        account_miss_rates  = analyze_account_miss_rates(aligned_problems, aligned_responses),
        balance_failures    = analyze_balance_failures(aligned_problems, aligned_responses),
        hallucinations      = analyze_hallucinations(aligned_problems, aligned_responses),
        difficulty_gradient = analyze_difficulty_gradient(aligned_problems, aligned_metrics, aligned_errors),
    )
