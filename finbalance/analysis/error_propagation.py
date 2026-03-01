"""
Error Propagation Simulator
===========================
Sends an increasing prefix of transactions (K = 1, 2, ..., N) to the model
and compares the predicted intermediate balance sheet against the ground-truth
ledger state computed by replaying journal entries.

This exposes:
  - First error onset transaction (which TX triggered the first deviation)
  - Error growth trajectory (MAE vs K)
  - Account-level error map per checkpoint
  - Whether specific tx_types (cogs, mixed_funding, derived_interest, …) are
    the systematic error triggers

Usage:
    from finbalance.analysis.error_propagation import PropagationSimulator
    from finbalance.evaluation.models.anthropic_model import AnthropicModel
    from finbalance.evaluation.models.base import ModelConfig

    model = AnthropicModel(ModelConfig(model_id="claude-3-haiku-20240307"))
    sim   = PropagationSimulator(model, checkpoint_every=1)
    trace = sim.simulate(problem)
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field, asdict
from typing import Optional

from finbalance.data.schemas import (
    ACCOUNT_TYPE,
    JournalEntry,
    Problem,
    Transaction,
)
from finbalance.evaluation.runner import parse_response

# ---------------------------------------------------------------------------
# Normal-balance side lookup (used to compute true running balance)
# ---------------------------------------------------------------------------

# Debit-normal: increases on debit
_DEBIT_NORMAL = {"asset", "expense"}
# Credit-normal: increases on credit  (contra_asset also credit-normal)
_CREDIT_NORMAL = {"liability", "equity", "revenue", "contra_asset"}


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class AccountError:
    """Error on a single account at a checkpoint."""
    account:    str
    true_value: float
    pred_value: float
    abs_error:  float
    rel_error:  float   # abs_error / max(1, true_value)
    is_new: bool        # True if this account was absent in prior checkpoint errors


@dataclass
class PropagationCheckpoint:
    """All data captured after the model sees the first k transactions."""
    k:               int           # transactions seen
    transaction_id:  str
    tx_type:         str
    tx_description:  str

    # ---- Ground truth at step k ----
    true_accounts:          dict[str, float]
    true_assets_total:      float
    true_liabilities_total: float
    true_equity_total:      float

    # ---- Model prediction ----
    pred_accounts:          dict[str, float]
    pred_assets_total:      float
    pred_liabilities_total: float
    pred_equity_total:      float
    pred_balanced:          bool        # does assets = liab + equity in prediction?
    parse_failed:           bool

    # ---- Error metrics ----
    mae:                  float         # mean |pred - true| across union of accounts
    max_abs_error:        float
    account_errors:       list[dict]    # serializable AccountError list
    error_count:          int           # accounts with abs_error > ERROR_THRESHOLD
    delta_mae:            float         # MAE(k) - MAE(k-1)
    balance_equation_err: float         # |assets - (liab + equity)| in prediction

    # ---- Meta ----
    latency_s:   float
    raw_response: str


@dataclass
class PropagationTrace:
    """Full propagation trace for one problem."""
    problem_id:           str
    difficulty:           int
    model_id:             str
    n_transactions:       int
    n_checkpoints:        int

    # Error onset
    first_error_k:            Optional[int]    # checkpoint index of first error
    first_error_tx_type:      Optional[str]
    first_error_transaction:  Optional[str]    # transaction_id
    first_error_accounts:     list[str]        # which accounts were wrong first

    # Summary
    final_mae:              float
    peak_mae:               float
    mae_trajectory:         list[float]        # MAE at each checkpoint
    error_counts:           list[int]          # error_count at each checkpoint
    first_balance_fail_k:   Optional[int]      # when balanced equation first fails

    # Raw checkpoints
    checkpoints: list[dict]   # serialised PropagationCheckpoints


# ---------------------------------------------------------------------------
# Ground-truth replay
# ---------------------------------------------------------------------------

ERROR_THRESHOLD = 1.0   # $1 tolerance for "account is wrong"


def _account_type(account: str) -> str:
    """Return the account type string, defaulting to 'asset' if unknown."""
    return ACCOUNT_TYPE.get(account, "asset")


def _apply_entry(balances: dict[str, float], entry: JournalEntry) -> None:
    """Update running balances for one journal entry, in-place."""
    atype = _account_type(entry.account)
    if atype in _DEBIT_NORMAL:
        balances[entry.account] = balances.get(entry.account, 0.0) + entry.debit - entry.credit
    else:
        balances[entry.account] = balances.get(entry.account, 0.0) + entry.credit - entry.debit


def compute_partial_balance(problem: Problem, k: int) -> dict[str, float]:
    """
    Replay opening balance + first k transactions.
    Revenue/expense accounts are NOT closed to Retained Earnings.
    Returns flat {account: value} dict (all values non-negative for normal-balance items).
    """
    balances: dict[str, float] = {}

    # Opening balance
    ob = problem.opening_balance
    for acc, val in {**ob.assets, **ob.liabilities, **ob.equity}.items():
        balances[acc] = val

    # Replay first k transactions
    for tx in problem.transactions[:k]:
        for entry in tx.entries:
            _apply_entry(balances, entry)

    # Remove zero-balance accounts (cleaner diff)
    return {acc: round(val, 2) for acc, val in balances.items() if abs(val) > 0.01}


def _section_totals(balances: dict[str, float]) -> tuple[float, float, float]:
    """Return (assets_total, liabilities_total, equity_total) from a flat balance dict.
    Revenue/expense are included in equity for this check (as net income)."""
    assets = liab = equity = 0.0
    for acc, val in balances.items():
        atype = _account_type(acc)
        if atype == "asset":
            assets += val
        elif atype == "contra_asset":
            assets -= val        # contra reduces assets
        elif atype == "liability":
            liab += val
        elif atype in ("equity", "revenue"):
            equity += val
        elif atype == "expense":
            equity -= val        # expenses reduce equity
    return round(assets, 2), round(liab, 2), round(equity, 2)


# ---------------------------------------------------------------------------
# Prompt builder for intermediate state
# ---------------------------------------------------------------------------

_OUTPUT_FORMAT = """{
  "assets":      {"<account name>": <amount>, ...},
  "liabilities": {"<account name>": <amount>, ...},
  "equity":      {"<account name>": <amount>, ...}
}"""


def _build_intermediate_prompt(problem: Problem, k: int) -> str:
    """
    Build a prompt that shows only the first k transactions (no adjustments).
    Ask the model for the balance sheet as-of that point.
    """
    ob = problem.opening_balance

    # Opening balance section
    ob_lines = [f"Opening balances as of {ob.date}:"]
    for acc, val in {**ob.assets, **ob.liabilities, **ob.equity}.items():
        ob_lines.append(f"  {acc}: {val:,.0f}")
    ob_str = "\n".join(ob_lines)

    # First k transactions
    tx_lines = ["Transactions (apply in order):"]
    for tx in problem.transactions[:k]:
        for entry in tx.entries:
            side = "Dr" if entry.debit else "Cr"
            amt  = entry.debit or entry.credit
            tx_lines.append(
                f"  {tx.date} | {tx.description:<40} | {side} {entry.account:<25} {amt:>10,.0f}"
            )
    tx_str = "\n".join(tx_lines)

    last_date = problem.transactions[k - 1].date if k > 0 else ob.date

    return f"""You are an expert accountant preparing an INTERIM balance sheet.

{ob_str}

{tx_str}

Task: Prepare the balance sheet as of {last_date} after applying ALL the transactions above.
Do NOT apply any period-end adjustments.
Do NOT close revenue/expense accounts into Retained Earnings.
Revenue and expense accounts should appear in the equity section as separate line items.

IMPORTANT: assets = liabilities + equity. Verify this before responding.

Respond ONLY with a JSON object (no markdown, no explanation):

{_OUTPUT_FORMAT}"""


# ---------------------------------------------------------------------------
# Comparison helpers
# ---------------------------------------------------------------------------

def _flatten_prediction(parsed: dict) -> dict[str, float]:
    """Merge assets/liabilities/equity sections into one flat dict."""
    flat: dict[str, float] = {}
    for section in ("assets", "liabilities", "equity"):
        sec = parsed.get(section, {})
        if isinstance(sec, dict):
            for k, v in sec.items():
                try:
                    flat[k] = float(v)
                except (TypeError, ValueError):
                    flat[k] = 0.0
    return flat


def _compute_pred_totals(parsed: dict) -> tuple[float, float, float]:
    """Return (assets_total, liabilities_total, equity_total) from parsed dict."""
    def _sum_section(sec: dict) -> float:
        return sum(float(v) for v in sec.values() if isinstance(v, (int, float)))
    a = _sum_section(parsed.get("assets", {}))
    l = _sum_section(parsed.get("liabilities", {}))
    e = _sum_section(parsed.get("equity", {}))
    return round(a, 2), round(l, 2), round(e, 2)


def _compute_mae_and_errors(
    true: dict[str, float],
    pred: dict[str, float],
    prev_error_accounts: set[str],
) -> tuple[float, float, list[AccountError]]:
    """Compute MAE and per-account errors over the union of both account sets."""
    all_accounts = set(true.keys()) | set(pred.keys())
    errors: list[AccountError] = []
    total_error = 0.0
    max_err = 0.0

    for acc in all_accounts:
        t = true.get(acc, 0.0)
        p = pred.get(acc, 0.0)
        ae = abs(p - t)
        total_error += ae
        if ae > max_err:
            max_err = ae
        if ae > ERROR_THRESHOLD:
            errors.append(AccountError(
                account=acc,
                true_value=t,
                pred_value=p,
                abs_error=ae,
                rel_error=round(ae / max(1.0, abs(t)), 4),
                is_new=(acc not in prev_error_accounts),
            ))

    mae = round(total_error / max(1, len(all_accounts)), 2)
    return mae, round(max_err, 2), errors


# ---------------------------------------------------------------------------
# Simulator
# ---------------------------------------------------------------------------

class PropagationSimulator:
    """
    Sends the model an increasing prefix of transactions and records the
    per-checkpoint prediction error.

    Parameters
    ----------
    model              : a BaseModel (any backend)
    checkpoint_every   : how many transactions between API calls (1 = every single TX)
    max_checkpoints    : cap to avoid cost explosion on long problems (0 = no cap)
    sleep_between      : seconds to sleep between API calls (rate-limit safety)
    verbose            : print progress
    """

    def __init__(
        self,
        model,
        checkpoint_every: int = 1,
        max_checkpoints: int = 0,
        sleep_between: float = 0.5,
        verbose: bool = True,
    ):
        self.model           = model
        self.checkpoint_every = max(1, checkpoint_every)
        self.max_checkpoints = max_checkpoints
        self.sleep_between   = sleep_between
        self.verbose         = verbose

    def _log(self, msg: str):
        if self.verbose:
            print(msg)

    # ------------------------------------------------------------------ #
    # Core: simulate one problem
    # ------------------------------------------------------------------ #

    def simulate(self, problem: Problem) -> PropagationTrace:
        n_tx = len(problem.transactions)

        # Build list of checkpoint indices (1-based transactions seen)
        checkpoints_k = list(range(self.checkpoint_every, n_tx + 1, self.checkpoint_every))
        if not checkpoints_k or checkpoints_k[-1] != n_tx:
            checkpoints_k.append(n_tx)   # always include the final state
        if self.max_checkpoints > 0:
            checkpoints_k = checkpoints_k[:self.max_checkpoints]

        self._log(
            f"\n[Propagation] {problem.problem_id} L{problem.difficulty_level} | "
            f"{n_tx} txs, {len(checkpoints_k)} checkpoints"
        )

        checkpoints: list[PropagationCheckpoint] = []
        prev_mae = 0.0
        prev_error_accounts: set[str] = set()
        first_error_k: Optional[int] = None
        first_error_tx_type: Optional[str] = None
        first_error_transaction: Optional[str] = None
        first_error_accounts_list: list[str] = []
        first_balance_fail_k: Optional[int] = None
        mae_trajectory: list[float] = []
        error_counts: list[int] = []

        for ck, k in enumerate(checkpoints_k):
            tx = problem.transactions[k - 1]   # the transaction that was just added

            # --- Ground truth ---
            true_accounts = compute_partial_balance(problem, k)
            ta, tl, te = _section_totals(true_accounts)

            # --- Prompt & model call ---
            prompt = _build_intermediate_prompt(problem, k)
            t0 = time.perf_counter()
            try:
                raw = self.model.complete(prompt)
            except Exception as exc:
                raw = ""
                self._log(f"  [API ERROR] k={k}: {exc}")
            latency = round(time.perf_counter() - t0, 2)

            # --- Parse ---
            parsed = parse_response(raw)
            parse_failed = parsed is None

            if not parse_failed:
                pred_accounts = _flatten_prediction(parsed)
                pa, pl, pe = _compute_pred_totals(parsed)
                pred_balanced = abs(pa - (pl + pe)) < 2.0
            else:
                pred_accounts = {}
                pa = pl = pe = 0.0
                pred_balanced = False

            balance_eq_err = round(abs(pa - (pl + pe)), 2) if not parse_failed else float("inf")

            # --- Error metrics ---
            mae, max_ae, account_errors = _compute_mae_and_errors(
                true_accounts, pred_accounts, prev_error_accounts
            )
            delta_mae = round(mae - prev_mae, 2)

            # Track first error onset
            if first_error_k is None and (mae > ERROR_THRESHOLD or parse_failed):
                first_error_k = k
                first_error_tx_type = tx.tx_type
                first_error_transaction = tx.transaction_id
                first_error_accounts_list = [e.account for e in account_errors if e.is_new]

            if first_balance_fail_k is None and not pred_balanced and not parse_failed:
                first_balance_fail_k = k

            # Update tracking
            prev_mae = mae
            prev_error_accounts = {e.account for e in account_errors}
            mae_trajectory.append(mae)
            error_counts.append(len(account_errors))

            cp = PropagationCheckpoint(
                k=k,
                transaction_id=tx.transaction_id,
                tx_type=tx.tx_type,
                tx_description=tx.description,
                true_accounts=true_accounts,
                true_assets_total=ta,
                true_liabilities_total=tl,
                true_equity_total=te,
                pred_accounts=pred_accounts,
                pred_assets_total=pa,
                pred_liabilities_total=pl,
                pred_equity_total=pe,
                pred_balanced=pred_balanced,
                parse_failed=parse_failed,
                mae=mae,
                max_abs_error=max_ae,
                account_errors=[asdict(e) for e in account_errors],
                error_count=len(account_errors),
                delta_mae=delta_mae,
                balance_equation_err=balance_eq_err,
                latency_s=latency,
                raw_response=raw,
            )
            checkpoints.append(cp)

            self._log(
                f"  k={k:2d} | {tx.tx_type:<30} | MAE={mae:>8,.0f} Δ={delta_mae:>+8,.0f} "
                f"| errors={len(account_errors)} balanced={'✓' if pred_balanced else '✗'}"
            )

            if self.sleep_between > 0 and ck < len(checkpoints_k) - 1:
                time.sleep(self.sleep_between)

        return PropagationTrace(
            problem_id=problem.problem_id,
            difficulty=problem.difficulty_level,
            model_id=str(self.model),
            n_transactions=n_tx,
            n_checkpoints=len(checkpoints),
            first_error_k=first_error_k,
            first_error_tx_type=first_error_tx_type,
            first_error_transaction=first_error_transaction,
            first_error_accounts=first_error_accounts_list,
            final_mae=mae_trajectory[-1] if mae_trajectory else 0.0,
            peak_mae=max(mae_trajectory) if mae_trajectory else 0.0,
            mae_trajectory=mae_trajectory,
            error_counts=error_counts,
            first_balance_fail_k=first_balance_fail_k,
            checkpoints=[asdict(cp) for cp in checkpoints],
        )

    # ------------------------------------------------------------------ #
    # Batch simulation
    # ------------------------------------------------------------------ #

    def simulate_batch(
        self,
        problems: list[Problem],
        save_path: Optional[str] = None,
    ) -> list[PropagationTrace]:
        traces = []
        for i, p in enumerate(problems, 1):
            self._log(f"\n[{i}/{len(problems)}]")
            trace = self.simulate(p)
            traces.append(trace)
            if save_path:
                _save_traces(traces, save_path)
        return traces


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def _save_traces(traces: list[PropagationTrace], path: str) -> None:
    with open(path, "w") as f:
        json.dump([asdict(t) for t in traces], f, indent=2)


def save_traces(traces: list[PropagationTrace], path: str) -> None:
    _save_traces(traces, path)
    print(f"Saved {len(traces)} traces → {path}")


def load_traces(path: str) -> list[dict]:
    with open(path) as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Analysis helpers (call separately or from the CLI)
# ---------------------------------------------------------------------------

def summarize_traces(traces: list[dict]) -> dict:
    """
    Aggregate across traces to produce paper-ready statistics:
      - error_onset_distribution: {tx_type: count}
      - mae_by_checkpoint_index:  [mean_mae at relative position 0%, 25%, 50%, 75%, 100%]
      - error_propagation_shape:  'immediate' | 'gradual' | 'late' (based on onset k / n_tx)
      - problem_level_breakdown:  {L1: {mean_onset_k, mean_final_mae}, ...}
    """
    from collections import defaultdict
    import statistics

    onset_tx_types: dict[str, int] = defaultdict(int)
    onset_fractions: list[float] = []
    final_maes: list[float] = []
    by_level: dict[int, list] = defaultdict(list)

    for t in traces:
        n_tx = t["n_transactions"]
        lvl  = t["difficulty"]
        fmae = t["final_mae"]
        final_maes.append(fmae)
        by_level[lvl].append(t)

        if t["first_error_k"] is not None:
            otype = t["first_error_tx_type"] or "unknown"
            onset_tx_types[otype] += 1
            onset_fractions.append(t["first_error_k"] / max(1, n_tx))

    # MAE trajectory averaged across problems (normalised to 5 quantile points)
    def _quantile_mae(t: dict, q: float) -> float:
        traj = t["mae_trajectory"]
        if not traj:
            return 0.0
        idx = min(int(q * len(traj)), len(traj) - 1)
        return traj[idx]

    quantile_points = [0.0, 0.25, 0.5, 0.75, 1.0]
    mae_by_quantile = []
    for q in quantile_points:
        vals = [_quantile_mae(t, q) for t in traces]
        mae_by_quantile.append(round(statistics.mean(vals), 2) if vals else 0.0)

    # Error propagation shape
    if onset_fractions:
        mean_onset = statistics.mean(onset_fractions)
        if mean_onset < 0.25:
            shape = "immediate"
        elif mean_onset < 0.6:
            shape = "gradual"
        else:
            shape = "late"
    else:
        shape = "none"

    # Per-level summary
    level_summary = {}
    for lvl, ts in by_level.items():
        onset_ks = [t["first_error_k"] for t in ts if t["first_error_k"] is not None]
        fmaes    = [t["final_mae"] for t in ts]
        level_summary[lvl] = {
            "n": len(ts),
            "mean_onset_k": round(statistics.mean(onset_ks), 1) if onset_ks else None,
            "mean_onset_fraction": round(
                statistics.mean(o / max(1, t["n_transactions"]) for o, t in zip(onset_ks, ts)), 3
            ) if onset_ks else None,
            "mean_final_mae": round(statistics.mean(fmaes), 2) if fmaes else 0.0,
            "errors_at_first_cp": round(
                statistics.mean(
                    t["checkpoints"][0]["error_count"] for t in ts if t["checkpoints"]
                ), 2
            ) if any(t["checkpoints"] for t in ts) else 0.0,
        }

    return {
        "n_problems": len(traces),
        "error_onset_tx_type_distribution": dict(
            sorted(onset_tx_types.items(), key=lambda x: -x[1])
        ),
        "mean_onset_fraction": round(statistics.mean(onset_fractions), 3) if onset_fractions else None,
        "error_propagation_shape": shape,
        "mean_final_mae": round(statistics.mean(final_maes), 2) if final_maes else 0.0,
        "mae_at_quantiles": dict(zip([f"q{int(q*100)}" for q in quantile_points], mae_by_quantile)),
        "by_level": dict(sorted(level_summary.items())),
    }
