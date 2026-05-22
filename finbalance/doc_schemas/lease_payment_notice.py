from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="lease_payment_notice",
    title="Lease Payment Notice",
    role="support_doc",
    description="Lease payment notice supporting cash, interest, and principal split.",
    required_fields=(
        req("notice_number", "string", "Notice number"),
        req("agreement_number", "string", "Lease agreement number"),
        req("payment_date", "date", "Payment date"),
        req("payment_amount", "number", "Payment amount"),
        req("interest_amount", "number", "Interest component"),
        req("principal_amount", "number", "Principal component"),
    ),
    sections=(
        kv(
            "Payment",
            ("Notice Number", "notice_number"),
            ("Agreement Number", "agreement_number"),
            ("Payment Date", "payment_date"),
            ("Payment Amount", "payment_amount"),
            ("Interest Amount", "interest_amount"),
            ("Principal Amount", "principal_amount"),
        ),
    ),
    visible_fields=("notice_number", "agreement_number", "payment_amount"),
    template_variants=("formal", "remittance"),
    cosmetic_blocks=("issuer_block", "reference_block", "footer_block"),
)
