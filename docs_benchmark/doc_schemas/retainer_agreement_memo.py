from docs_benchmark.doc_schemas.base import kv, narrative, req, schema


SCHEMA = schema(
    doc_type="retainer_agreement_memo",
    title="Retainer Agreement Memo",
    role="support_doc",
    description="Support memo describing a retainer contract before revenue is earned.",
    required_fields=(
        req("memo_id", "string", "Memo id"),
        req("subject", "string", "Memo subject"),
        req("reference", "string", "Linked contract reference"),
        req("contract_months", "number", "Contract length in months"),
        req("total_contract_value", "number", "Total retainer value"),
        req("narrative", "string", "Contract explanation"),
    ),
    sections=(
        kv(
            "Memo Summary",
            ("Memo ID", "memo_id"),
            ("Subject", "subject"),
            ("Reference", "reference"),
            ("Contract Months", "contract_months"),
            ("Total Contract Value", "total_contract_value"),
        ),
        narrative("Explanation", "Narrative", "narrative"),
    ),
    visible_fields=("memo_id", "reference", "contract_months", "total_contract_value"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
