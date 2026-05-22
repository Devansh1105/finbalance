from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="revenue_recognition_schedule",
    title="Revenue Recognition Schedule",
    role="adjustment_doc",
    description="Schedule releasing deferred revenue into earned revenue.",
    required_fields=(
        req("schedule_id", "string", "Schedule id"),
        req("contract_reference", "string", "Contract reference"),
        req("period_label", "string", "Period label"),
        req("opening_deferred", "number", "Opening deferred balance"),
        req("added_deferred", "number", "Added deferred revenue"),
        req("released_this_period", "number", "Revenue released"),
        req("ending_deferred", "number", "Ending deferred balance"),
    ),
    sections=(
        kv(
            "Recognition Summary",
            ("Schedule ID", "schedule_id"),
            ("Contract Reference", "contract_reference"),
            ("Period", "period_label"),
            ("Opening Deferred", "opening_deferred"),
            ("Added Deferred", "added_deferred"),
            ("Released This Period", "released_this_period"),
            ("Ending Deferred", "ending_deferred"),
        ),
    ),
    visible_fields=("schedule_id", "contract_reference", "released_this_period"),
    template_variants=("formal", "summary", "contract"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
