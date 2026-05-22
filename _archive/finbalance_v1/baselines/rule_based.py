"""
Rule-based balance sheet solver (oracle baseline).

This baseline reads the structured journal entries from a Problem object —
the same information the LLM receives as formatted text — and applies
double-entry bookkeeping rules deterministically via the Ledger engine.

Purpose for ACL:
    Establishes the performance ceiling: a solver with perfect transaction
    parsing should score ~100% BA on every problem. The LLM's failure to
    match this ceiling isolates the gap as a reasoning deficit (closing entries,
    contra-account handling, arithmetic accumulation) rather than task
    ambiguity or annotation noise.

Usage:
    from finbalance.baselines.rule_based import RuleBasedSolver
    solver = RuleBasedSolver()
    predicted = solver.solve(problem)   # returns dict like model output
    metrics   = evaluate_problem(problem, predicted)
"""

from finbalance.data.schemas import ACCOUNT_TYPE, Problem
from finbalance.data.generation.generator import Ledger


class RuleBasedSolver:
    """
    Deterministic balance sheet solver.

    Replays all JournalEntry objects from the Problem directly through the
    Ledger engine, then builds a GAAP-compliant balance sheet.  No natural-
    language parsing is involved — the solver operates on the same structured
    data that was used to generate the problem.

    This is the *oracle* baseline: it answers the question "what score does
    a system achieve if it applies accounting rules perfectly on the structured
    input?".  Comparing LLM scores against this ceiling contextualises the
    magnitude of the reasoning gap.
    """

    def solve(self, problem: Problem) -> dict:
        """
        Produce a balance sheet dict in the same format as model output:
            {"assets": {...}, "liabilities": {...}, "equity": {...}}

        Steps:
            1. Seed the Ledger with opening balances.
            2. Apply every JournalEntry in each Transaction.
            3. Apply every JournalEntry in each Adjustment.
            4. Build and return the closing balance sheet.
        """
        ledger = Ledger()

        # 1. Opening balances — directly write known values into the ledger.
        #    Opening balance accounts are always assets/liabilities/equity
        #    (normal-sign convention: stored positive).
        ob = problem.opening_balance
        for acc, val in ob.assets.items():
            ledger.balances[acc] = float(val)
        for acc, val in ob.liabilities.items():
            ledger.balances[acc] = float(val)
        for acc, val in ob.equity.items():
            ledger.balances[acc] = float(val)

        # 2. Transactions
        for tx in problem.transactions:
            self._apply_entries(ledger, tx.entries)

        # 3. Period-end adjustments
        for adj in problem.adjustments:
            self._apply_entries(ledger, adj.entries)

        # 4. Build GAAP balance sheet (closes Revenue/Expense into Retained Earnings)
        bs = ledger.build_balance_sheet(date=problem.expected.date)
        return {
            "assets":      bs.assets,
            "liabilities": bs.liabilities,
            "equity":      bs.equity,
        }

    @staticmethod
    def _apply_entries(ledger: Ledger, entries) -> None:
        """
        Apply a list of JournalEntry objects to the ledger.

        Each entry carries either a debit or a credit amount (never both).
        We apply the correct balance-side effect for the account type:
          - Debit  → increases asset/expense, decreases liability/equity/revenue
          - Credit → increases liability/equity/revenue, decreases asset/expense
        """
        for entry in entries:
            acc = entry.account
            if entry.debit:
                delta = ledger.debit_effect(acc, entry.debit)
            elif entry.credit:
                delta = ledger.credit_effect(acc, entry.credit)
            else:
                continue
            ledger.balances[acc] = ledger.balances.get(acc, 0.0) + delta
