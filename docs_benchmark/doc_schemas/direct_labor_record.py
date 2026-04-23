from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="direct_labor_record",
    title="Direct Labor Record",
    role="posting_doc",
    description="Production labor record showing labor cash paid into work in process.",
    required_fields=(
        req("batch_id", "string", "Batch id"),
        req("product_name", "string", "Product name"),
        req("planned_units", "number", "Planned units"),
        req("labor_value", "number", "Direct labor charged"),
        req("cash_paid", "number", "Cash paid for direct labor"),
    ),
    sections=(
        kv(
            "Labor Summary",
            ("Batch ID", "batch_id"),
            ("Product", "product_name"),
            ("Planned Units", "planned_units"),
            ("Labor Value", "labor_value"),
            ("Labor Cash Paid", "cash_paid"),
        ),
    ),
    visible_fields=("batch_id", "product_name", "labor_value", "cash_paid"),
    template_variants=("formal", "shop_floor", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
