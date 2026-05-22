from finbalance.doc_schemas.base import kv, listing, opt, req, schema


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
    optional_fields=(
        opt("expense_account_label", "string", "Intended expense bucket"),
        opt("document_currency", "string", "Document currency code"),
        opt("subtotal", "number", "Amount before indirect tax"),
        opt("tax_label", "string", "Indirect tax label"),
        opt("tax_rate", "number", "Indirect tax rate"),
        opt("tax_amount", "number", "Indirect tax amount"),
    ),
    sections=(
        kv("Supplier Header", ("Vendor", "vendor"), ("Expense Label", "expense_account_label"), ("Currency", "document_currency")),
        kv(
            "Bill Details",
            ("Invoice Number", "number"),
            ("Due Date", "due_date"),
            ("Subtotal", "subtotal"),
            ("Tax Label", "tax_label"),
            ("Tax Rate", "tax_rate"),
            ("Tax Amount", "tax_amount"),
            ("Total", "total"),
        ),
        listing("Bill Lines", "Lines", "line_items"),
    ),
    list_field_orders={"line_items": ("description", "amount")},
    visible_fields=("number", "vendor", "total"),
    template_variants=("formal", "compact", "statement"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "terms_block", "approval_block", "footer_block"),
)
