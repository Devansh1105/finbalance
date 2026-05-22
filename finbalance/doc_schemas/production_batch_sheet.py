from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="production_batch_sheet",
    title="Production Batch Sheet",
    role="support_doc",
    description="Batch sheet summarising production cost loaded into WIP.",
    required_fields=(
        req("batch_id", "string", "Batch id"),
        req("product_name", "string", "Product name"),
        req("planned_units", "number", "Planned units"),
        req("material_value", "number", "Material cost"),
        req("labor_value", "number", "Labor cost"),
        req("overhead_value", "number", "Overhead cost"),
    ),
    sections=(
        kv(
            "Batch Summary",
            ("Batch ID", "batch_id"),
            ("Product", "product_name"),
            ("Planned Units", "planned_units"),
            ("Material Value", "material_value"),
            ("Labor Value", "labor_value"),
            ("Overhead Value", "overhead_value"),
        ),
    ),
    visible_fields=("batch_id", "product_name"),
    template_variants=("formal", "shop_floor", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
