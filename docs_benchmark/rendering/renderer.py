"""Schema-driven rendering for documents."""

from __future__ import annotations

import random
from pathlib import Path
from typing import Any

from docs_benchmark.doc_schemas import get_doc_schema
from docs_benchmark.render import make_ocr_text, write_text_pdf
from docs_benchmark.schemas import DocumentAsset, DocumentSeed


def render_document(seed: DocumentSeed, asset_dir: str | Path, rng: random.Random, industry: str) -> DocumentAsset:
    schema = get_doc_schema(seed.doc_type)
    variant = seed.metadata.get("template_variant") or rng.choice(schema.template_variants_for(industry))
    lines = render_lines_for_seed(seed, rng, industry, template_variant=variant)
    asset_dir = Path(asset_dir)
    asset_path = asset_dir / f"{seed.doc_id}_{seed.doc_type}.pdf"
    write_text_pdf(asset_path, lines)
    metadata = dict(seed.metadata)
    metadata["template_variant"] = variant
    return DocumentAsset(
        doc_id=seed.doc_id,
        doc_type=seed.doc_type,
        role=seed.role,
        title=seed.title,
        date=seed.date,
        asset_path=str(asset_path),
        ocr_text=make_ocr_text(lines),
        metadata=metadata,
    )


def render_lines_for_seed(
    seed: DocumentSeed,
    rng: random.Random,
    industry: str,
    template_variant: str | None = None,
) -> list[str]:
    schema = get_doc_schema(seed.doc_type)
    variant = template_variant or rng.choice(schema.template_variants_for(industry))
    blocks = schema.cosmetic_blocks_for(industry)
    title_line = _title_line(schema.title_for(industry), variant)
    lines = [title_line, "=" * min(len(title_line), 72), ""]

    if "issuer_block" in blocks:
        lines.extend(_issuer_block(seed, variant))
    if "recipient_block" in blocks:
        recipient_lines = _recipient_block(seed)
        if recipient_lines:
            lines.extend(recipient_lines)
    if "reference_block" in blocks:
        lines.extend(_reference_block(seed))
    if "terms_block" in blocks:
        term_lines = _terms_block(seed)
        if term_lines:
            lines.extend(term_lines)
    if "approval_block" in blocks:
        approval_lines = _approval_block(seed)
        if approval_lines:
            lines.extend(approval_lines)

    for section in schema.sections_for(industry):
        section_lines: list[str] = []
        for label, field_name in section.entries:
            value = seed.fields.get(field_name)
            if value is None:
                continue
            section_lines.extend(_render_field(label, field_name, value, schema.list_field_orders, section.kind, seed.metadata))
        if not section_lines:
            continue
        lines.append(section.title)
        lines.append("-" * min(len(section.title), 72))
        lines.extend(section_lines)
        lines.append("")

    narrative = seed.metadata.get("footer_note")
    if narrative:
        lines.extend(["Notes", "-----", narrative, ""])
    if "footer_block" in blocks:
        lines.extend(_footer_block(seed, variant))
    return lines


def _title_line(title: str, variant: str) -> str:
    if variant in {"compact", "summary"}:
        return title.upper()
    if variant in {"remittance", "contract", "coverage"}:
        return f"{title} / Reference Copy".upper()
    return title.upper()


def _issuer_block(seed: DocumentSeed, variant: str) -> list[str]:
    issuer_name = seed.metadata.get("issuer_name", "Northwind Synthetic Holdings")
    issuer_address = seed.metadata.get("issuer_address", "")
    lines = ["From", "----", issuer_name]
    if issuer_address:
        lines.append(issuer_address)
    if variant in {"formal", "contract", "coverage"}:
        lines.append(f"Document Date: {format_scalar(seed.date, 'date', seed.metadata)}")
    else:
        lines.append(f"Date: {format_scalar(seed.date, 'date', seed.metadata)}")
    lines.append("")
    return lines


def _recipient_block(seed: DocumentSeed) -> list[str]:
    recipient = _counterparty(seed)
    if not recipient:
        return []
    lines = ["To", "--", recipient]
    if seed.fields.get("customer"):
        lines.append("Customer account on file")
    elif seed.fields.get("vendor") or seed.fields.get("provider"):
        lines.append("Vendor remittance address on file")
    elif seed.fields.get("patient_name"):
        lines.append("Patient billing contact")
    lines.append("")
    return lines


def _reference_block(seed: DocumentSeed) -> list[str]:
    common_fields = [
        ("Document ID", seed.doc_id),
        ("Document Type", seed.doc_type),
        ("Period", seed.metadata.get("period_label")),
    ]
    detail_fields = [
        ("Reference", seed.fields.get("reference")),
        ("Contract Ref", seed.fields.get("contract_ref")),
        ("Job Code", seed.fields.get("job_code")),
        ("Shipment Ref", seed.fields.get("shipment_ref")),
    ]
    lines = ["Reference Box", "-------------"]
    for label, value in [*common_fields, *detail_fields]:
        if value:
            lines.append(f"{label}: {format_scalar(value, label.lower().replace(' ', '_'), seed.metadata)}")
    lines.append("")
    return lines


def _terms_block(seed: DocumentSeed) -> list[str]:
    candidates = [
        ("Due Date", seed.fields.get("due_date")),
        ("Service Start", seed.fields.get("service_start")),
        ("Service End", seed.fields.get("service_end")),
        ("Contract Start", seed.fields.get("contract_start")),
        ("Renewal Start", seed.fields.get("renewal_start")),
    ]
    lines = [f"{label}: {format_scalar(value, label.lower().replace(' ', '_'), seed.metadata)}" for label, value in candidates if value]
    if not lines:
        return []
    return ["Terms", "-----", *lines, ""]


def _approval_block(seed: DocumentSeed) -> list[str]:
    candidates = [
        ("Prepared By", seed.fields.get("prepared_by")),
        ("Subject", seed.fields.get("subject")),
        ("Reason", seed.fields.get("reason")),
        ("Plan Name", seed.fields.get("plan_name")),
    ]
    lines = [f"{label}: {format_scalar(value, label.lower().replace(' ', '_'), seed.metadata)}" for label, value in candidates if value]
    if not lines:
        return []
    return ["Approval / Context", "------------------", *lines, ""]


def _footer_block(seed: DocumentSeed, variant: str) -> list[str]:
    lines = ["Footer", "------"]
    if variant in {"formal", "contract", "coverage"}:
        lines.append("Generated for synthetic accounting research use.")
    else:
        lines.append("Internal document packet copy.")
    lines.append(f"Page marker: {seed.doc_id}")
    lines.append("")
    return lines


def _counterparty(seed: DocumentSeed) -> str | None:
    for key in (
        "customer",
        "vendor",
        "counterparty",
        "provider",
        "patient_name",
        "tenant_name",
        "supplier",
        "payer_name",
    ):
        value = seed.fields.get(key)
        if value:
            return str(value)
    return seed.metadata.get("counterparty_name")


def _render_field(
    label: str,
    field_name: str,
    value: Any,
    list_field_orders: dict[str, tuple[str, ...]],
    kind: str,
    metadata: dict[str, Any],
) -> list[str]:
    if kind == "narrative":
        return [f"{label}: {format_scalar(value, field_name, metadata)}"] if isinstance(value, (str, int, float)) else [f"{label}: {value}"]
    if isinstance(value, list):
        if not value:
            return [f"{label}: None"]
        lines = [f"{label}:"]
        order = list_field_orders.get(field_name, ())
        for item in value:
            if isinstance(item, dict):
                parts = []
                keys = order or tuple(item.keys())
                for key in keys:
                    if key in item:
                        parts.append(f"{_pretty_label(key)} {format_scalar(item[key], key, metadata)}")
                lines.append(f"  - {' | '.join(parts)}")
            else:
                lines.append(f"  - {item}")
        return lines
    if isinstance(value, dict):
        return [f"{label}: {', '.join(f'{_pretty_label(k)} {format_scalar(v, k, metadata)}' for k, v in value.items())}"]
    return [f"{label}: {format_scalar(value, field_name, metadata)}"]

def format_scalar(value: Any, field_name: str, metadata: dict[str, Any] | None = None) -> str:
    metadata = metadata or {}
    if isinstance(value, float):
        return _format_numeric(value, field_name, metadata)
    if isinstance(value, int):
        if _is_money_field(field_name):
            return _format_numeric(float(value), field_name, metadata)
        return str(value)
    if isinstance(value, bool):
        return "Yes" if value else "No"
    if value is None:
        return ""
    name = field_name.lower()
    if isinstance(value, str) and _looks_like_iso_date(value) and any(token in name for token in ("date", "start", "end", "due", "deposit")):
        return _format_date_value(value, metadata)
    if isinstance(value, str) and _is_money_field(name):
        try:
            return _format_numeric(float(value), field_name, metadata)
        except ValueError:
            return value
    return str(value)


def _format_numeric(value: float, field_name: str, metadata: dict[str, Any]) -> str:
    raw = f"{value:,.2f}"
    if metadata.get("currency_format") == "symbol_prefix_eu":
        raw = raw.replace(",", "_").replace(".", ",").replace("_", ".")
    symbol = metadata.get("currency_symbol", "$") if _is_money_field(field_name) else ""
    return f"{symbol}{raw}".strip()


def _format_date_value(value: str, metadata: dict[str, Any]) -> str:
    if metadata.get("date_format") == "DD/MM/YYYY":
        year, month, day = value.split("-")
        return f"{day}/{month}/{year}"
    return value


def _is_money_field(field_name: str) -> bool:
    name = field_name.lower()
    return any(
        token in name
        for token in (
            "amount",
            "total",
            "sales",
            "charge",
            "rent",
            "deposit",
            "paid",
            "balance",
            "gross",
            "net",
            "fee",
            "value",
            "cost",
            "price",
            "deferred",
            "revenue",
            "pay",
            "payment",
            "cash",
            "principal",
            "interest",
        )
    )


def _looks_like_iso_date(value: str) -> bool:
    return len(value) == 10 and value[4] == "-" and value[7] == "-"


def _pretty_label(value: str) -> str:
    return value.replace("_", " ").title()
