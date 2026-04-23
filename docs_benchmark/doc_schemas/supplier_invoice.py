from docs_benchmark.doc_schemas.base import DocSchemaVariant, kv, listing, opt, req, schema


SCHEMA = schema(
    doc_type="supplier_invoice",
    title="Supplier Invoice",
    role="posting_doc",
    description="Supplier bill used mainly for inventory or stock purchases.",
    required_fields=(
        req("number", "string", "Supplier invoice number"),
        req("vendor", "string", "Supplier name"),
        req("due_date", "date", "Payment due date"),
        req("total", "number", "Total bill amount"),
        req("line_items", "list", "Supplier invoice lines"),
    ),
    optional_fields=(opt("goods_receipt_ref", "string", "Linked goods receipt note"),),
    sections=(
        kv("Supplier Header", ("Supplier", "vendor"), ("Goods Receipt Ref", "goods_receipt_ref")),
        kv(
            "Supplier Bill Details",
            ("Invoice Number", "number"),
            ("Due Date", "due_date"),
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
