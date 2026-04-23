from docs_benchmark.doc_schemas.base import kv, listing, req, schema


SCHEMA = schema(
    doc_type="ar_aging_summary",
    title="AR Aging Summary",
    role="support_doc",
    description="Summary of open receivables grouped by age bucket.",
    required_fields=(
        req("summary_id", "string", "Summary id"),
        req("period_label", "string", "Period label"),
        req("lines", "list", "Aging lines"),
        req("total_amount", "number", "Total open receivables"),
    ),
    sections=(
        kv(
            "Aging Summary",
            ("Summary ID", "summary_id"),
            ("Period", "period_label"),
            ("Total Open", "total_amount"),
        ),
        listing("Customer Lines", "Lines", "lines"),
    ),
    list_field_orders={"lines": ("customer", "reference", "current", "past_due")},
    visible_fields=("summary_id", "period_label", "total_amount"),
    template_variants=("formal", "summary", "portfolio"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
