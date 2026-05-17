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
    "tax_total_mismatch": "Subtotal, indirect tax, and total do not reconcile on the document.",
    "tax_rate_mismatch": "Shown indirect tax amount does not reconcile with the shown tax rate and basis.",
    "input_tax_mismatch": "Recoverable input tax fields do not reconcile with the underlying bill amounts.",
    "jurisdiction_tax_mismatch": "Jurisdiction-specific tax treatment does not reconcile with the applicable support documents.",
    "tax_exemption_conflict": "Tax exemption certificate evidence conflicts with the invoice tax treatment.",
    "ssp_allocation_mismatch": "ASC 606 allocation does not reconcile transaction price to standalone selling prices.",
    "performance_obligation_release_mismatch": "Performance obligation release evidence does not reconcile to the recognition schedule.",
    "asset_disposal_mismatch": "Fixed asset disposal support does not reconcile cost, accumulated depreciation, NBV, proceeds, and gain or loss.",
    "deferred_tax_rollforward_mismatch": "Deferred tax rollforward does not reconcile the opening liability, current movement, and ending liability.",
    "lease_schedule_mismatch": "Lease amortization schedule does not reconcile payment, interest, principal, and ending liability.",
    "lease_remeasurement_mismatch": "Lease modification support does not reconcile liability remeasurement and equal ROU asset adjustment.",
    "exchange_rate_mismatch": "Exchange-rate support does not reconcile the foreign amount into the stated functional amount.",
    "fx_settlement_mismatch": "Foreign-currency settlement support does not reconcile booked amount, paid amount, and FX difference.",
    "remeasurement_mismatch": "Closing-rate remeasurement does not reconcile the open foreign balance to the stated functional amount.",
}

INCONSISTENCY_CODES = tuple(INCONSISTENCY_CODE_DETAILS.keys())


def inconsistency_description(code: str) -> str:
    if code not in INCONSISTENCY_CODE_DETAILS:
        raise KeyError(f"Unknown inconsistency code '{code}'")
    return INCONSISTENCY_CODE_DETAILS[code]
