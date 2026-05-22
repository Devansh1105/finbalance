from finbalance.doc_schemas.base import DocSchemaVariant, kv, listing, opt, req, schema


SCHEMA = schema(
    doc_type="supplier_invoice",
    title="Supplier Invoice",
    role="posting_doc",
    description="Supplier bill for inventory, materials, repair parts, or subcontract support.",
    required_fields=(
        req("number", "string", "Supplier invoice number"),
        req("vendor", "string", "Supplier name"),
        req("due_date", "date", "Payment due date"),
        req("total", "number", "Total bill amount"),
        req("line_items", "list", "Supplier invoice lines"),
    ),
    optional_fields=(
        opt("goods_receipt_ref", "string", "Linked goods receipt note"),
        opt("expense_account_label", "string", "Internal expense classification"),
        opt("document_currency", "string", "Document currency code"),
        opt("subtotal", "number", "Amount before indirect tax"),
        opt("tax_label", "string", "Indirect tax label"),
        opt("tax_rate", "number", "Indirect tax rate"),
        opt("tax_amount", "number", "Indirect tax amount"),
        opt("cgst_amount", "number", "India GST central component"),
        opt("sgst_amount", "number", "India GST state component"),
        opt("igst_amount", "number", "India GST integrated component"),
    ),
    sections=(
        kv(
            "Supplier Header",
            ("Supplier", "vendor"),
            ("Goods Receipt Ref", "goods_receipt_ref"),
            ("Expense Category", "expense_account_label"),
            ("Currency", "document_currency"),
        ),
        kv(
            "Supplier Bill Details",
            ("Invoice Number", "number"),
            ("Due Date", "due_date"),
            ("Subtotal", "subtotal"),
            ("Tax Label", "tax_label"),
            ("Tax Rate", "tax_rate"),
            ("Tax Amount", "tax_amount"),
            ("CGST Amount", "cgst_amount"),
            ("SGST Amount", "sgst_amount"),
            ("IGST Amount", "igst_amount"),
            ("Total", "total"),
        ),
        listing("Supplier Bill Lines", "Lines", "line_items"),
    ),
    list_field_orders={"line_items": ("description", "quantity", "unit_cost", "amount")},
    visible_fields=("number", "vendor", "total"),
    template_variants=("formal", "compact", "warehouse"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "terms_block", "footer_block"),
    variants={
        "wholesale_distribution": DocSchemaVariant(
            extra_required_fields=(req("goods_receipt_ref", "string", "Goods receipt reference"),),
            template_variants=("warehouse", "formal", "compact"),
        )
    },
)
