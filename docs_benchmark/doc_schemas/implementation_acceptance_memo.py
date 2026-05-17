from docs_benchmark.doc_schemas.base import kv, narrative, req, schema


SCHEMA = schema(
    doc_type="implementation_acceptance_memo",
    title="Implementation Acceptance Memo",
    role="support_doc",
    description="Acceptance evidence for implementation performance obligation revenue release.",
    required_fields=(
        req("memo_id", "string", "Memo id"),
        req("contract_reference", "string", "Contract reference"),
        req("customer", "string", "Customer"),
        req("acceptance_date", "date", "Acceptance date"),
        req("accepted_obligation", "string", "Accepted performance obligation"),
        req("accepted_amount", "number", "Allocated amount released on acceptance"),
        req("narrative", "string", "Memo narrative"),
    ),
    sections=(
        kv(
            "Acceptance",
            ("Memo ID", "memo_id"),
            ("Contract Reference", "contract_reference"),
            ("Customer", "customer"),
            ("Acceptance Date", "acceptance_date"),
            ("Accepted Obligation", "accepted_obligation"),
            ("Accepted Amount", "accepted_amount"),
        ),
        narrative("Narrative", "Details", "narrative"),
    ),
    visible_fields=("memo_id", "contract_reference", "accepted_amount"),
    template_variants=("formal", "contract"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "approval_block", "footer_block"),
)
