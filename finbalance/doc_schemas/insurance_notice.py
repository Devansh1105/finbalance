from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="insurance_notice",
    title="Insurance Notice",
    role="posting_doc",
    description="Notice for insurance coverage paid in advance.",
    required_fields=(
        req("number", "string", "Notice number"),
        req("vendor", "string", "Insurance carrier"),
        req("property_name", "string", "Covered business or location"),
        req("service_start", "date", "Coverage start date"),
        req("service_end", "date", "Coverage end date"),
        req("total", "number", "Total premium"),
        req("monthly_amount", "number", "Monthly coverage amount"),
    ),
    sections=(
        kv(
            "Coverage Notice",
            ("Notice Number", "number"),
            ("Carrier", "vendor"),
            ("Covered Item", "property_name"),
            ("Coverage Start", "service_start"),
            ("Coverage End", "service_end"),
            ("Total Premium", "total"),
            ("Monthly Amount", "monthly_amount"),
        ),
    ),
    visible_fields=("number", "vendor", "total"),
    template_variants=("formal", "compact", "coverage"),
    cosmetic_blocks=("issuer_block", "recipient_block", "terms_block", "footer_block"),
)
