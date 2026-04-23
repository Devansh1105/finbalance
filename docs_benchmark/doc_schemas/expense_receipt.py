from docs_benchmark.doc_schemas.base import kv, listing, opt, req, schema


SCHEMA = schema(
    doc_type="expense_receipt",
    title="Expense Receipt",
    role="posting_doc",
    description="Small cash or card expense receipt.",
    required_fields=(
        req("receipt_number", "string", "Receipt number"),
        req("merchant", "string", "Merchant name"),
        req("total", "number", "Receipt total"),
        req("line_items", "list", "Receipt lines"),
    ),
    optional_fields=(opt("payment_method", "string", "How it was paid"),),
    sections=(
        kv(
            "Receipt Details",
            ("Receipt Number", "receipt_number"),
            ("Merchant", "merchant"),
            ("Total", "total"),
            ("Payment Method", "payment_method"),
        ),
        listing("Receipt Lines", "Lines", "line_items"),
    ),
    list_field_orders={"line_items": ("description", "amount")},
    visible_fields=("receipt_number", "merchant", "total"),
)
