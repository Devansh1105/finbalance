from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="copay_receipt",
    title="Copay Receipt",
    role="posting_doc",
    description="Receipt for patient copay collection.",
    required_fields=(
        req("receipt_number", "string", "Copay receipt number"),
        req("patient_name", "string", "Patient"),
        req("amount", "number", "Amount collected"),
        req("reference", "string", "Linked patient invoice"),
        req("payment_method", "string", "Payment method"),
    ),
    sections=(
        kv(
            "Copay Receipt",
            ("Receipt Number", "receipt_number"),
            ("Patient", "patient_name"),
            ("Amount", "amount"),
            ("Reference Invoice", "reference"),
            ("Payment Method", "payment_method"),
        ),
    ),
    visible_fields=("receipt_number", "amount", "reference"),
    cosmetic_blocks=("issuer_block", "recipient_block", "footer_block"),
)
