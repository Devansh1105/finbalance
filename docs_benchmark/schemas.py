"""Core dataclasses for the document benchmark."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class OpeningBalance:
    date: str
    assets: dict[str, float] = field(default_factory=dict)
    liabilities: dict[str, float] = field(default_factory=dict)
    equity: dict[str, float] = field(default_factory=dict)


@dataclass
class Posting:
    doc_refs: list[str]
    debit_account: str
    credit_account: str
    amount: float
    posting_date: str
    label: str = ""

    def key(self, amount_tol: float = 0.0) -> tuple[Any, ...]:
        rounded_amount = self.amount if amount_tol <= 0 else round(self.amount / amount_tol) * amount_tol
        return (
            tuple(sorted(self.doc_refs)),
            self.debit_account,
            self.credit_account,
            rounded_amount,
        )


@dataclass
class BalanceSheet:
    date: str
    assets: dict[str, float]
    liabilities: dict[str, float]
    equity: dict[str, float]
    total_assets: float
    total_liabilities: float
    total_equity: float
    balanced: bool

    def flat(self) -> dict[str, float]:
        return {**self.assets, **self.liabilities, **self.equity}


@dataclass
class DocumentAsset:
    doc_id: str
    doc_type: str
    role: str
    title: str
    date: str
    asset_path: str
    ocr_text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class DocumentSeed:
    doc_id: str
    doc_type: str
    role: str
    title: str
    date: str
    fields: dict[str, Any]
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class DocumentRecord:
    record_id: str
    industry: str
    difficulty_level: int
    period_start: str
    period_end: str
    opening_balance: OpeningBalance
    allowed_accounts: list[str]
    documents: list[DocumentAsset]
    expected_entries: list[Posting]
    expected_balance_sheet: BalanceSheet
    expected_inconsistency: bool = False
    expected_inconsistency_codes: list[str] = field(default_factory=list)
    inconsistency_reasons: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ParsedSubmission:
    entries: list[Posting]
    balance_sheet: dict[str, dict[str, float]]
    has_inconsistency: bool
    inconsistency_codes: list[str]
    inconsistency_notes: list[str]
    raw: dict[str, Any]


def ensure_parent(path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
