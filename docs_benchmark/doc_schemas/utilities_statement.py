from docs_benchmark.doc_schemas.base import kv, listing, opt, req, schema


SCHEMA = schema(
    doc_type="utilities_statement",
    title="Utility Invoice",
    role="posting_doc",
    description="Utility provider invoice for the selected accounting period.",
    required_fields=(
        req("statement_number", "string", "Statement number"),
        req("provider", "string", "Provider name"),
        req("service_period", "string", "Service period"),
        req("due_date", "date", "Due date"),
        req("total", "number", "Total amount due"),
        req("line_items", "list", "Statement charges"),
    ),
    optional_fields=(
        opt("invoice_number", "string", "Utility invoice number"),
        opt("pay_to", "string", "Utility provider payee"),
    ),
    sections=(
        kv(
            "Invoice Summary",
            ("Statement Number", "statement_number"),
            ("Invoice Number", "invoice_number"),
            ("Provider", "provider"),
            ("Pay To", "pay_to"),
            ("Service Period", "service_period"),
            ("Due Date", "due_date"),
            ("Total", "total"),
        ),
        listing("Charges", "Charges", "line_items"),
    ),
    list_field_orders={"line_items": ("description", "amount")},
    visible_fields=("statement_number", "provider", "total"),
    template_variants=("formal", "metered", "compact"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "terms_block", "footer_block"),
)
