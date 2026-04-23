from docs_benchmark.doc_schemas.base import kv, listing, req, schema


SCHEMA = schema(
    doc_type="utilities_statement",
    title="Utilities Statement",
    role="posting_doc",
    description="Utility provider statement for the selected accounting period.",
    required_fields=(
        req("statement_number", "string", "Statement number"),
        req("provider", "string", "Provider name"),
        req("service_period", "string", "Service period"),
        req("due_date", "date", "Due date"),
        req("total", "number", "Total amount due"),
        req("line_items", "list", "Statement charges"),
    ),
    sections=(
        kv(
            "Statement Summary",
            ("Statement Number", "statement_number"),
            ("Provider", "provider"),
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
