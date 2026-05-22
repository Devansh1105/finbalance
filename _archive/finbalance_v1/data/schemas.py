"""
Core data structures for the FinBalance benchmark.
All monetary values are stored as plain floats (no currency symbol).
"""

from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Account taxonomy
# ---------------------------------------------------------------------------

# Normal balance side for each account type:
#   asset / expense   -> debit  (increase on debit)
#   liability / equity / revenue -> credit (increase on credit)

ACCOUNT_TYPE = {
    # Assets
    "Cash":                      "asset",
    "Accounts Receivable":       "asset",
    "Inventory":                 "asset",
    "Equipment":                 "asset",
    "Furniture":                 "asset",
    "Vehicles":                  "asset",
    "Prepaid Rent":              "asset",
    "Prepaid Insurance":         "asset",
    "Accumulated Depreciation":           "contra_asset",   # contra: reduces assets
    "Allowance for Doubtful Accounts":    "contra_asset",   # contra: reduces receivables
    # Liabilities
    "Accounts Payable":          "liability",
    "Loans Payable":             "liability",
    "Notes Payable":             "liability",
    "Accrued Expenses":          "liability",
    "Accrued Interest Payable":  "liability",
    "Unearned Revenue":          "liability",
    # Equity
    "Owner's Equity":            "equity",
    "Share Capital":             "equity",
    "Retained Earnings":         "equity",
    # Revenue & expenses (closed to Retained Earnings for balance sheet)
    "Revenue":                   "revenue",
    "Sales Revenue":             "revenue",
    "Cost of Goods Sold":        "expense",
    "Operating Expenses":        "expense",
    "Salaries Expense":          "expense",
    "Rent Expense":              "expense",
    "Insurance Expense":         "expense",
    "Depreciation Expense":      "expense",
    "Interest Expense":          "expense",
    "Bad Debt Expense":          "expense",
    "Utilities Expense":         "expense",
}

BALANCE_SHEET_SECTION = {
    "asset":        "assets",
    "contra_asset": "assets",   # shown as negative
    "liability":    "liabilities",
    "equity":       "equity",
    # revenue/expense are collapsed into equity (Retained Earnings)
}


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class JournalEntry:
    """A single debit/credit line within a transaction."""
    account: str
    debit:  float = 0.0
    credit: float = 0.0


@dataclass
class Transaction:
    transaction_id: str
    date:           str
    description:    str
    entries:        list[JournalEntry]
    tx_type:        str = ""          # e.g. "cash_sale", "credit_purchase"
    complexity_factors: list[str] = field(default_factory=list)


@dataclass
class Adjustment:
    """Period-end adjusting entry (depreciation, accruals, etc.)."""
    adjustment_id: str
    date:          str
    description:   str
    adj_type:      str                # "depreciation" | "prepaid" | "accrual"
    entries:       list[JournalEntry]
    calculation:   Optional[dict] = None


@dataclass
class IntermediateState:
    """Snapshot of running totals after a transaction."""
    after_transaction_id: str
    assets_total:         float
    liabilities_total:    float
    equity_total:         float       # includes net income to date


@dataclass
class BalanceSheet:
    date:            str
    assets:          dict[str, float]   # account -> value (positive)
    liabilities:     dict[str, float]
    equity:          dict[str, float]
    total_assets:    float
    total_liabilities: float
    total_equity:    float
    balanced:        bool              # True iff |assets - (liab + equity)| < 1

    def to_flat_dict(self) -> dict[str, float]:
        """Merge all sections for easy comparison."""
        return {**self.assets, **self.liabilities, **self.equity}


@dataclass
class OpeningBalance:
    date:        str
    assets:      dict[str, float] = field(default_factory=dict)
    liabilities: dict[str, float] = field(default_factory=dict)
    equity:      dict[str, float] = field(default_factory=dict)


@dataclass
class Problem:
    problem_id:     str
    difficulty_level: int             # 1-5
    opening_balance: OpeningBalance
    transactions:    list[Transaction]
    adjustments:     list[Adjustment]
    expected:        BalanceSheet
    intermediate_states: list[IntermediateState]
    metadata:        dict             # num_transactions, industry, etc.

    def to_dict(self) -> dict:
        """Serialize to JSON-compatible dict."""
        import dataclasses
        return dataclasses.asdict(self)
