from docs_benchmark.doc_schemas.base import kv, listing, opt, req, schema


SCHEMA = schema(
    doc_type="vendor_invoice",
    title="Vendor Invoice",
    role="posting_doc",
    description="Supplier bill for overhead or service costs.",
    required_fields=(
        req("number", "string", "Vendor invoice number"),
        req("vendor", "string", "Vendor name"),
        req("due_date", "date", "Payment due date"),
        req("total", "number", "Total bill amount"),
        req("line_items", "list", "Bill lines"),
    ),
    optional_fields=(opt("expense_account_label", "string", "Intended expense bucket"),),
    sections=(
        kv("Supplier Header", ("Vendor", "vendor"), ("Expense Label", "expense_account_label")),
        kv(
            "Bill Details",
            ("Invoice Number", "number"),
            ("Due Date", "due_date"),
            ("Total", "total"),
        ),
        listing("Bill Lines", "Lines", "line_items"),
    ),
    list_field_orders={"line_items": ("description", "amount")},
    visible_fields=("number", "vendor", "total"),
    template_variants=("formal", "compact", "statement"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "terms_block", "approval_block", "footer_block"),
)
