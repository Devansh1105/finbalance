from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="inventory_rollforward",
    title="Inventory Rollforward",
    role="adjustment_doc",
    description="Inventory movement summary over the selected period.",
    required_fields=(
        req("rollforward_id", "string", "Rollforward id"),
        req("opening_balance", "number", "Opening inventory"),
        req("additions", "number", "Purchases or production"),
        req("usage_or_sales", "number", "Issues or sales"),
        req("write_down", "number", "Write-down"),
        req("ending_balance", "number", "Ending inventory"),
    ),
    sections=(
        kv(
            "Inventory Rollforward",
            ("Rollforward ID", "rollforward_id"),
            ("Opening Balance", "opening_balance"),
            ("Additions", "additions"),
            ("Usage Or Sales", "usage_or_sales"),
            ("Write Down", "write_down"),
            ("Ending Balance", "ending_balance"),
        ),
    ),
    visible_fields=("rollforward_id", "opening_balance", "ending_balance"),
    template_variants=("formal", "summary", "warehouse"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
