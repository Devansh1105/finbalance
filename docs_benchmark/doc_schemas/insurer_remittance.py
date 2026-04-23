from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="insurer_remittance",
    title="Insurer Remittance",
    role="posting_doc",
    description="Payment advice from an insurer against a patient invoice.",
    required_fields=(
        req("remittance_number", "string", "Remittance number"),
        req("payer_name", "string", "Insurer"),
        req("claim_reference", "string", "Linked patient invoice"),
        req("approved_amount", "number", "Approved amount"),
        req("paid_amount", "number", "Cash paid"),
        req("payment_date", "date", "Payment date"),
    ),
    sections=(
        kv(
            "Remittance Summary",
            ("Remittance Number", "remittance_number"),
            ("Payer", "payer_name"),
            ("Claim Reference", "claim_reference"),
            ("Approved Amount", "approved_amount"),
            ("Paid Amount", "paid_amount"),
            ("Payment Date", "payment_date"),
        ),
    ),
    visible_fields=("remittance_number", "paid_amount", "claim_reference"),
    cosmetic_blocks=("issuer_block", "reference_block", "footer_block"),
)
