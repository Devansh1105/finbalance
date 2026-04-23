from docs_benchmark.doc_schemas.base import kv, listing, req, schema


SCHEMA = schema(
    doc_type="patient_invoice",
    title="Patient Invoice",
    role="posting_doc",
    description="Clinic invoice that splits patient and insurer responsibility.",
    required_fields=(
        req("invoice_number", "string", "Patient invoice number"),
        req("patient_name", "string", "Patient"),
        req("payer_name", "string", "Insurer"),
        req("service_date", "date", "Service date"),
        req("total", "number", "Gross charge"),
        req("patient_due", "number", "Patient copay"),
        req("insurer_due", "number", "Insurer share"),
    ),
    sections=(
        kv(
            "Invoice Summary",
            ("Invoice Number", "invoice_number"),
            ("Patient", "patient_name"),
            ("Payer", "payer_name"),
            ("Service Date", "service_date"),
            ("Gross Charge", "total"),
            ("Patient Due", "patient_due"),
            ("Insurer Due", "insurer_due"),
        ),
    ),
    visible_fields=("invoice_number", "patient_name", "total"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "footer_block"),
)
