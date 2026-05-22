from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="duplicate_invoice_copy",
    title="Duplicate Invoice Copy",
    role="distractor_doc",
    description="Duplicate scan or copy of an invoice already included elsewhere in the packet.",
    required_fields=(
        req("copy_id", "string", "Duplicate copy id"),
        req("source_reference", "string", "Original invoice number"),
        req("counterparty", "string", "Counterparty name"),
        req("total", "number", "Invoice total"),
        req("note", "string", "Duplicate note"),
    ),
    sections=(
        kv(
            "Duplicate Copy",
            ("Copy ID", "copy_id"),
            ("Original Invoice", "source_reference"),
            ("Counterparty", "counterparty"),
            ("Total", "total"),
            ("Note", "note"),
        ),
    ),
    visible_fields=("copy_id", "source_reference", "total"),
    template_variants=("formal", "compact"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "footer_block"),
)
