from docs_benchmark.doc_schemas.base import kv, opt, req, schema


SCHEMA = schema(
    doc_type="fx_remeasurement_memo",
    title="FX Remeasurement Memo",
    role="adjustment_doc",
    description="Period-end memo remeasuring an open foreign-currency balance at the closing rate.",
    required_fields=(
        req("memo_id", "string", "Memo id"),
        req("reference", "string", "Linked open item reference"),
        req("source_currency", "string", "Foreign source currency"),
        req("functional_currency", "string", "Functional currency"),
        req("source_amount", "number", "Open foreign amount"),
        req("booked_amount", "number", "Originally booked functional amount"),
        req("closing_rate", "number", "Closing exchange rate"),
        req("remeasured_amount", "number", "Closing functional amount"),
        req("difference_amount", "number", "FX gain or loss recognized"),
    ),
    optional_fields=(opt("narrative", "string", "Reason for the remeasurement"),),
    sections=(
        kv(
            "Remeasurement Details",
            ("Memo ID", "memo_id"),
            ("Reference", "reference"),
            ("Source Currency", "source_currency"),
            ("Functional Currency", "functional_currency"),
            ("Source Amount", "source_amount"),
            ("Booked Amount", "booked_amount"),
            ("Closing Rate", "closing_rate"),
            ("Remeasured Amount", "remeasured_amount"),
            ("Difference Amount", "difference_amount"),
            ("Narrative", "narrative"),
        ),
    ),
    visible_fields=("memo_id", "reference", "closing_rate", "difference_amount"),
    template_variants=("formal", "summary", "approval"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
