from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="secondary_copy",
    title="Secondary Copy",
    role="distractor_doc",
    description="A second scan or forwarded copy of a billing document already present elsewhere in the packet.",
    required_fields=(
        req("copy_id", "string", "Secondary copy id"),
        req("source_reference", "string", "Original billing reference"),
        req("counterparty", "string", "Counterparty name"),
        req("total", "number", "Billing total"),
        req("copy_context", "string", "Why this copy appears in the packet"),
    ),
    sections=(
        kv(
            "Copy Summary",
            ("Copy ID", "copy_id"),
            ("Source Reference", "source_reference"),
            ("Counterparty", "counterparty"),
            ("Total", "total"),
            ("Copy Context", "copy_context"),
        ),
    ),
    visible_fields=("copy_id", "source_reference", "total"),
    template_variants=("formal", "compact"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "footer_block"),
)
