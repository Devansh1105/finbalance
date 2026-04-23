from docs_benchmark.doc_schemas.base import kv, listing, req, schema


SCHEMA = schema(
    doc_type="vendor_statement",
    title="Vendor Statement",
    role="distractor_doc",
    description="Vendor account statement that overlaps invoices already present in the packet.",
    required_fields=(
        req("statement_number", "string", "Statement number"),
        req("vendor", "string", "Vendor name"),
        req("closing_balance", "number", "Statement closing balance"),
        req("lines", "list", "Statement lines"),
    ),
    sections=(
        kv(
            "Statement Header",
            ("Statement Number", "statement_number"),
            ("Vendor", "vendor"),
            ("Closing Balance", "closing_balance"),
        ),
        listing("Statement Lines", "Lines", "lines"),
    ),
    list_field_orders={"lines": ("reference", "document_type", "amount", "status")},
    visible_fields=("statement_number", "vendor", "closing_balance"),
    template_variants=("formal", "summary"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "footer_block"),
)
