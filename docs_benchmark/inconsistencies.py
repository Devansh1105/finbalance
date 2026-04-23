"""Deterministic inconsistency codes used by negative-control records."""

from __future__ import annotations


INCONSISTENCY_CODE_DETAILS = {
    "invoice_total_mismatch": "Invoice total does not match the visible line items.",
    "bank_closing_mismatch": "Bank statement closing balance does not reconcile with the listed movements.",
    "statement_balance_mismatch": "Statement closing balance does not reconcile with the listed open lines.",
    "payment_allocation_mismatch": "Payment advice amount does not reconcile with the listed invoice allocations.",
    "duplicate_reference_conflict": "Two documents show the same reference with conflicting totals or status.",
    "schedule_rollforward_mismatch": "Schedule opening, additions, and releases do not roll forward to the stated ending balance.",
    "inventory_rollforward_mismatch": "Inventory rollforward does not reconcile from opening through ending balance.",
    "transfer_mismatch": "Inter-bank transfer support does not reconcile between the advice and bank evidence.",
    "reclassification_support_mismatch": "Correction memo details do not reconcile with the linked original posting support.",
}

INCONSISTENCY_CODES = tuple(INCONSISTENCY_CODE_DETAILS.keys())


def inconsistency_description(code: str) -> str:
    if code not in INCONSISTENCY_CODE_DETAILS:
        raise KeyError(f"Unknown inconsistency code '{code}'")
    return INCONSISTENCY_CODE_DETAILS[code]
