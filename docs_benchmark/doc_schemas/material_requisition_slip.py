from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="material_requisition_slip",
    title="Material Requisition Slip",
    role="posting_doc",
    description="Issue slip for raw materials moved into production.",
    required_fields=(
        req("slip_number", "string", "Slip number"),
        req("batch_id", "string", "Production batch"),
        req("material", "string", "Material name"),
        req("quantity_issued", "number", "Quantity issued"),
        req("issue_value", "number", "Value issued"),
        req("warehouse", "string", "Warehouse or store"),
    ),
    sections=(
        kv(
            "Material Issue",
            ("Slip Number", "slip_number"),
            ("Batch ID", "batch_id"),
            ("Material", "material"),
            ("Quantity Issued", "quantity_issued"),
            ("Issue Value", "issue_value"),
            ("Warehouse", "warehouse"),
        ),
    ),
    visible_fields=("slip_number", "batch_id", "issue_value"),
    template_variants=("formal", "warehouse", "shop_floor"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
