"""Common state and assembly helpers for generation."""

from __future__ import annotations

import calendar
import random
from datetime import date, datetime, timedelta
from typing import Any

from docs_benchmark.schemas import DocumentSeed, Posting
from docs_benchmark.types import BusinessState, PeriodSpec


PERIOD_TYPES = ("month", "quarter", "year")
PERIOD_DOC_RANGES = {
    "month": {
        1: (5, 8),
        2: (8, 11),
        3: (10, 15),
        4: (14, 20),
        5: (18, 28),
    },
    "quarter": {
        1: (7, 11),
        2: (10, 14),
        3: (13, 18),
        4: (17, 24),
        5: (22, 32),
    },
    "year": {
        1: (9, 13),
        2: (13, 18),
        3: (17, 23),
        4: (22, 30),
        5: (28, 40),
    },
}

DISPLAY_PROFILES = (
    {
        "currency_code": "USD",
        "currency_symbol": "$",
        "currency_format": "symbol_prefix_comma",
        "date_format": "YYYY-MM-DD",
    },
    {
        "currency_code": "EUR",
        "currency_symbol": "EUR ",
        "currency_format": "symbol_prefix_eu",
        "date_format": "DD/MM/YYYY",
    },
    {
        "currency_code": "GBP",
        "currency_symbol": "GBP ",
        "currency_format": "symbol_prefix_comma",
        "date_format": "DD/MM/YYYY",
    },
)

INDUSTRY_AMOUNT_SCALES = {
    "professional_services": {"month": 1.0, "quarter": 2.2, "year": 5.5},
    "field_services": {"month": 1.3, "quarter": 3.0, "year": 7.0},
    "retail": {"month": 1.1, "quarter": 2.3, "year": 4.8},
    "wholesale_distribution": {"month": 1.6, "quarter": 3.6, "year": 8.5},
    "healthcare_clinic": {"month": 1.4, "quarter": 3.0, "year": 6.2},
    "property_management": {"month": 1.5, "quarter": 3.1, "year": 7.2},
    "manufacturing": {"month": 2.0, "quarter": 5.0, "year": 11.5},
    "subscription_saas": {"month": 3.0, "quarter": 8.0, "year": 24.0},
}

DIFFICULTY_AMOUNT_BOOST = {1: 0.9, 2: 1.0, 3: 1.15, 4: 1.35, 5: 1.6}
AMOUNT_BUCKET_BOOST = {
    "micro": 0.12,
    "small": 0.32,
    "operating": 1.0,
    "inventory": 1.35,
    "payroll": 1.15,
    "contract": 1.9,
    "capital": 2.0,
    "financing": 2.8,
}


def doc_seed(
    state: BusinessState,
    doc_type: str,
    title: str,
    date: str,
    fields: dict[str, Any],
    role: str,
    metadata: dict[str, Any] | None = None,
) -> DocumentSeed:
    extra = metadata.copy() if metadata else {}
    extra.setdefault("issuer_name", state.entity_name)
    extra.setdefault("issuer_address", state.entity_address)
    extra.setdefault("industry", state.industry)
    extra.setdefault("industry_label", state.master_data.get("industry_label", state.industry.replace("_", " ").title()))
    extra.setdefault("role_label", role.replace("_", " ").title())
    extra.setdefault("period_label", state.period_spec.label)
    extra.setdefault("period_type", state.period_spec.period_type)
    extra.setdefault("currency_code", state.currency_code)
    extra.setdefault("currency_symbol", state.currency_symbol)
    extra.setdefault("currency_format", state.currency_format)
    extra.setdefault("date_format", state.date_format)
    return DocumentSeed(
        doc_id=state.next_doc_id(),
        doc_type=doc_type,
        role=role,
        title=title,
        date=date,
        fields=fields,
        metadata=extra,
    )


def posting(doc_refs: list[str], debit: str, credit: str, amount: float, posting_date: str, label: str) -> Posting:
    return Posting(
        doc_refs=doc_refs,
        debit_account=debit,
        credit_account=credit,
        amount=round(float(amount), 2),
        posting_date=posting_date,
        label=label,
    )


def amount(rng: random.Random, lo: int | float, hi: int | float) -> float:
    return round(rng.uniform(lo, hi), 2)


def choose_display_profile(rng: random.Random) -> dict[str, str]:
    if rng.random() < 0.05:
        return dict(rng.choice(DISPLAY_PROFILES[1:]))
    return dict(DISPLAY_PROFILES[0])


def choose_nonstandard_display_profile(rng: random.Random) -> dict[str, str]:
    return dict(rng.choice(DISPLAY_PROFILES[1:]))


def amount_scale(industry: str, period_type: str, difficulty_level: int, bucket: str = "operating") -> float:
    industry_scale = INDUSTRY_AMOUNT_SCALES.get(industry, {"month": 1.0, "quarter": 2.0, "year": 4.0})
    return industry_scale[period_type] * DIFFICULTY_AMOUNT_BOOST[difficulty_level] * AMOUNT_BUCKET_BOOST.get(bucket, 1.0)


def period_rank(period_type: str) -> int:
    return {"month": 0, "quarter": 1, "year": 2}[period_type]


def choose_period_spec(rng: random.Random, period_type: str) -> PeriodSpec:
    if period_type not in PERIOD_TYPES:
        raise ValueError(f"Unsupported period type '{period_type}'")
    fiscal_start_month = rng.choice((1, 4))
    if period_type == "month":
        year = rng.choice((2024, 2025))
        month = rng.randint(1, 12)
        start = date(year, month, 1)
        end = date(year, month, calendar.monthrange(year, month)[1])
        label = start.strftime("%B %Y")
        return PeriodSpec(period_type=period_type, start_date=start.isoformat(), end_date=end.isoformat(), label=label, month_count=1, fiscal_start_month=fiscal_start_month)

    if period_type == "quarter":
        fiscal_year_start = rng.choice((2024, 2025))
        quarter_index = rng.randint(0, 3)
        start = _add_months(date(fiscal_year_start, fiscal_start_month, 1), quarter_index * 3)
        end = _add_months(start, 3) - timedelta(days=1)
        fiscal_year_label = _fiscal_year_label(start, fiscal_start_month)
        quarter_number = quarter_index + 1
        label = f"Q{quarter_number} {fiscal_year_label}"
        return PeriodSpec(period_type=period_type, start_date=start.isoformat(), end_date=end.isoformat(), label=label, month_count=3, fiscal_start_month=fiscal_start_month)

    fiscal_year_start = rng.choice((2024, 2025))
    start = date(fiscal_year_start, fiscal_start_month, 1)
    end = _add_months(start, 12) - timedelta(days=1)
    label = _fiscal_year_label(start, fiscal_start_month)
    return PeriodSpec(period_type=period_type, start_date=start.isoformat(), end_date=end.isoformat(), label=label, month_count=12, fiscal_start_month=fiscal_start_month)


def pick_date(period_spec: PeriodSpec, rng: random.Random, window: str = "mid") -> str:
    start = _parse_date(period_spec.start_date)
    end = _parse_date(period_spec.end_date)
    total_days = max((end - start).days, 1)
    ranges = {
        "opening": (0.0, 0.08),
        "early": (0.05, 0.28),
        "mid": (0.32, 0.68),
        "late": (0.68, 0.9),
        "closing": (0.9, 1.0),
    }
    low_ratio, high_ratio = ranges.get(window, ranges["mid"])
    low_offset = int(total_days * low_ratio)
    high_offset = max(low_offset, int(total_days * high_ratio))
    offset = rng.randint(low_offset, high_offset)
    return (start + timedelta(days=offset)).isoformat()


def due_date(issue_date: str, rng: random.Random, days_low: int = 10, days_high: int = 30) -> str:
    return (_parse_date(issue_date) + timedelta(days=rng.randint(days_low, days_high))).isoformat()


def date_plus_days(value: str, days: int) -> str:
    return (_parse_date(value) + timedelta(days=days)).isoformat()


def add_months_to_date(value: str, months: int) -> str:
    return _add_months(_parse_date(value), months).isoformat()


def bank_row(date: str, description: str, amount_value: float, account: str = "Cash") -> dict[str, Any]:
    return {
        "date": date,
        "description": description,
        "amount": round(float(amount_value), 2),
        "account": account,
    }


def line_items(total: float, descriptions: list[str], rng: random.Random) -> list[dict[str, Any]]:
    if len(descriptions) == 1:
        return [{"description": descriptions[0], "amount": round(total, 2)}]
    remainder = round(total, 2)
    rows: list[dict[str, Any]] = []
    for description in descriptions[:-1]:
        share = round(total * rng.uniform(0.2, 0.45), 2)
        share = min(share, remainder)
        rows.append({"description": description, "amount": share})
        remainder = round(remainder - share, 2)
    rows.append({"description": descriptions[-1], "amount": round(remainder, 2)})
    return rows


def quantity_line_items(
    total: float,
    descriptions: list[str],
    rng: random.Random,
    qty_low: int = 2,
    qty_high: int = 30,
) -> list[dict[str, Any]]:
    rows = line_items(total, descriptions, rng)
    detailed: list[dict[str, Any]] = []
    for row in rows:
        quantity = rng.randint(qty_low, qty_high)
        unit_cost = round(row["amount"] / quantity, 2)
        detailed.append(
            {
                "description": row["description"],
                "quantity": quantity,
                "unit_cost": unit_cost,
                "amount": row["amount"],
            }
        )
    return detailed


def pay_period_label(period_spec: PeriodSpec) -> str:
    if period_spec.period_type == "month":
        return period_spec.label
    if period_spec.period_type == "quarter":
        return f"Payroll for {period_spec.label}"
    return f"Annual payroll summary for {period_spec.label}"


def ensure_period_doc_range(period_type: str, difficulty_level: int) -> tuple[int, int]:
    return PERIOD_DOC_RANGES[period_type][difficulty_level]


def _parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def _add_months(value: date, months: int) -> date:
    month = value.month - 1 + months
    year = value.year + month // 12
    month = month % 12 + 1
    day = min(value.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


def _fiscal_year_label(start: date, fiscal_start_month: int) -> str:
    if fiscal_start_month == 1:
        return f"FY {start.year}"
    return f"FY {start.year}-{str((start.year + 1) % 100).zfill(2)}"
