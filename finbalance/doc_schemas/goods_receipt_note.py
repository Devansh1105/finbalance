from finbalance.doc_schemas.base import kv, listing, req, schema


SCHEMA = schema(
    doc_type="goods_receipt_note",
    title="Goods Receipt Note",
    role="support_doc",
    description="Warehouse receipt showing goods received from a supplier.",
    required_fields=(
        req("grn_number", "string", "Goods receipt number"),
        req("supplier", "string", "Supplier"),
        req("purchase_ref", "string", "Purchase reference"),
        req("items", "list", "Received items"),
        req("total_quantity", "number", "Total quantity received"),
    ),
    sections=(
        kv(
            "Receipt Summary",
            ("GRN Number", "grn_number"),
            ("Supplier", "supplier"),
            ("Purchase Ref", "purchase_ref"),
            ("Total Quantity", "total_quantity"),
        ),
        listing("Received Items", "Items", "items"),
    ),
    list_field_orders={"items": ("sku", "description", "quantity", "unit_cost")},
    visible_fields=("grn_number", "supplier"),
)
