from finbalance.doc_schemas.base import kv, narrative, req, schema


SCHEMA = schema(
    doc_type="service_period_memo",
    title="Service Period Memo",
    role="adjustment_doc",
    description="Memo that explains month-end recognition for a period-based cost.",
    required_fields=(
        req("memo_id", "string", "Memo id"),
        req("subject", "string", "Memo subject"),
        req("reference", "string", "Linked document reference"),
        req("recognized_amount", "number", "Amount to recognize this month"),
        req("narrative", "string", "Recognition explanation"),
    ),
    sections=(
        kv(
            "Memo Summary",
            ("Memo ID", "memo_id"),
            ("Subject", "subject"),
            ("Reference", "reference"),
            ("Recognized Amount", "recognized_amount"),
        ),
        narrative("Explanation", "Narrative", "narrative"),
    ),
    visible_fields=("memo_id", "reference", "recognized_amount"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
