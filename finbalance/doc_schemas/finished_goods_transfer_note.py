from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="finished_goods_transfer_note",
    title="Finished Goods Transfer Note",
    role="posting_doc",
    description="Transfer note moving completed production into finished goods.",
    required_fields=(
        req("transfer_number", "string", "Transfer number"),
        req("batch_id", "string", "Production batch"),
        req("product_name", "string", "Product"),
        req("units_completed", "number", "Completed units"),
        req("transfer_value", "number", "Transfer value"),
    ),
    sections=(
        kv(
            "Transfer Summary",
            ("Transfer Number", "transfer_number"),
            ("Batch ID", "batch_id"),
            ("Product", "product_name"),
            ("Units Completed", "units_completed"),
            ("Transfer Value", "transfer_value"),
        ),
    ),
    visible_fields=("transfer_number", "batch_id", "transfer_value"),
    template_variants=("formal", "warehouse", "shop_floor"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
