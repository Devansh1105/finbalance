from finbalance.doc_schemas.base import kv, narrative, req, schema


SCHEMA = schema(
    doc_type="overhead_accrual_memo",
    title="Overhead Accrual Memo",
    role="adjustment_doc",
    description="Period-end memo showing accrued overhead moved into work in process.",
    required_fields=(
        req("batch_id", "string", "Batch id"),
        req("product_name", "string", "Product name"),
        req("planned_units", "number", "Planned units"),
        req("overhead_value", "number", "Overhead charged"),
        req("accrued_amount", "number", "Accrued overhead amount"),
        req("narrative", "string", "Explanation of the accrual"),
    ),
    sections=(
        kv(
            "Overhead Summary",
            ("Batch ID", "batch_id"),
            ("Product", "product_name"),
            ("Planned Units", "planned_units"),
            ("Overhead Value", "overhead_value"),
            ("Accrued Overhead", "accrued_amount"),
        ),
        narrative("Explanation", "Narrative", "narrative"),
    ),
    visible_fields=("batch_id", "product_name", "overhead_value", "accrued_amount"),
    template_variants=("formal", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
