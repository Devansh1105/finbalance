from docs_benchmark.doc_schemas.base import kv, listing, req, schema


SCHEMA = schema(
    doc_type="stock_count_sheet",
    title="Stock Count Sheet",
    role="support_doc",
    description="Physical stock count used for reconciliation.",
    required_fields=(
        req("sheet_id", "string", "Stock count id"),
        req("location", "string", "Store or warehouse location"),
        req("items", "list", "Counted items"),
    ),
    sections=(
        kv("Count Summary", ("Sheet ID", "sheet_id"), ("Location", "location")),
        listing("Counted Items", "Items", "items"),
    ),
    list_field_orders={"items": ("sku", "description", "system_qty", "counted_qty", "unit_cost")},
    visible_fields=("sheet_id", "location"),
)
