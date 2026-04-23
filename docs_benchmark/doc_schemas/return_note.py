from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="return_note",
    title="Return Note",
    role="posting_doc",
    description="Return or refund note tied to a prior sale.",
    required_fields=(
        req("return_id", "string", "Return id"),
        req("reason", "string", "Reason"),
        req("amount", "number", "Return amount"),
        req("reference", "string", "Related sale"),
    ),
    sections=(
        kv(
            "Return Summary",
            ("Return ID", "return_id"),
            ("Reason", "reason"),
            ("Amount", "amount"),
            ("Reference", "reference"),
        ),
    ),
    visible_fields=("return_id", "amount", "reference"),
)
