from docs_benchmark.doc_schemas.base import kv, narrative, req, schema


SCHEMA = schema(
    doc_type="memo",
    title="Memo",
    role="distractor_doc",
    description="Administrative memo included in the scanned packet.",
    required_fields=(
        req("memo_id", "string", "Memo id"),
        req("subject", "string", "Memo subject"),
        req("audience", "string", "Memo audience"),
        req("narrative", "string", "Memo body"),
    ),
    sections=(
        kv("Memo Summary", ("Memo ID", "memo_id"), ("Subject", "subject"), ("Audience", "audience")),
        narrative("Memo Body", "Narrative", "narrative"),
    ),
    visible_fields=("memo_id", "subject"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
