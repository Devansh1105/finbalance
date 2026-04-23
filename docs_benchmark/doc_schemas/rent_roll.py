from docs_benchmark.doc_schemas.base import kv, listing, req, schema


SCHEMA = schema(
    doc_type="rent_roll",
    title="Rent Roll",
    role="posting_doc",
    description="Monthly rent bill summary by tenant and unit.",
    required_fields=(
        req("roll_number", "string", "Rent roll id"),
        req("property_name", "string", "Property"),
        req("period_label", "string", "Period label"),
        req("lines", "list", "Tenant rent rows"),
        req("total_amount", "number", "Total rent billed"),
    ),
    sections=(
        kv(
            "Rent Roll Summary",
            ("Roll Number", "roll_number"),
            ("Property", "property_name"),
            ("Period", "period_label"),
            ("Total Rent", "total_amount"),
        ),
        listing("Tenant Rows", "Rows", "lines"),
    ),
    list_field_orders={"lines": ("unit", "tenant", "amount")},
    visible_fields=("roll_number", "property_name", "total_amount"),
    template_variants=("formal", "compact", "portfolio"),
    cosmetic_blocks=("issuer_block", "reference_block", "footer_block"),
)
