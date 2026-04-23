from docs_benchmark.doc_schemas.base import kv, narrative, req, schema


SCHEMA = schema(
    doc_type="cancellation_note",
    title="Cancellation Note",
    role="distractor_doc",
    description="Administrative note showing that an earlier billing reference was withdrawn or superseded.",
    required_fields=(
        req("note_number", "string", "Cancellation note number"),
        req("withdrawn_reference", "string", "Withdrawn billing reference"),
        req("replacement_reference", "string", "Replacement billing reference"),
        req("reason", "string", "Cancellation narrative"),
    ),
    sections=(
        kv(
            "Cancellation Summary",
            ("Note Number", "note_number"),
            ("Withdrawn Reference", "withdrawn_reference"),
            ("Replacement Reference", "replacement_reference"),
        ),
        narrative("Background", "Narrative", "reason"),
    ),
    visible_fields=("note_number", "withdrawn_reference", "replacement_reference"),
    template_variants=("formal", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "footer_block"),
)
