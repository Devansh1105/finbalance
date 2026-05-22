from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="rent_notice",
    title="Rent Notice",
    role="posting_doc",
    description="Notice for rent paid or billed in advance.",
    required_fields=(
        req("number", "string", "Rent notice number"),
        req("vendor", "string", "Landlord or property manager"),
        req("property_name", "string", "Property name"),
        req("service_start", "date", "Service start date"),
        req("service_end", "date", "Service end date"),
        req("total", "number", "Total prepaid amount"),
        req("monthly_amount", "number", "One month amount"),
    ),
    sections=(
        kv(
            "Rent Notice",
            ("Notice Number", "number"),
            ("Vendor", "vendor"),
            ("Property", "property_name"),
            ("Service Start", "service_start"),
            ("Service End", "service_end"),
            ("Total", "total"),
            ("Monthly Amount", "monthly_amount"),
        ),
    ),
    visible_fields=("number", "property_name", "total"),
)
