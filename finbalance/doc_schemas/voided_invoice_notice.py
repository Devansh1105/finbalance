from finbalance.doc_schemas.base import kv, narrative, req, schema


SCHEMA = schema(
    doc_type="voided_invoice_notice",
    title="Voided Invoice Notice",
    role="distractor_doc",
    description="Notice that an invoice was voided and should not be posted again.",
    required_fields=(
        req("notice_number", "string", "Notice number"),
        req("voided_reference", "string", "Voided invoice reference"),
        req("replacement_reference", "string", "Replacement invoice reference"),
        req("reason", "string", "Void reason"),
    ),
    sections=(
        kv(
            "Void Notice",
            ("Notice Number", "notice_number"),
            ("Voided Invoice", "voided_reference"),
            ("Replacement Invoice", "replacement_reference"),
        ),
        narrative("Reason", "Narrative", "reason"),
    ),
    visible_fields=("notice_number", "voided_reference", "replacement_reference"),
    template_variants=("formal", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "footer_block"),
)
