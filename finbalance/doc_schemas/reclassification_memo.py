from finbalance.doc_schemas.base import kv, narrative, req, schema


SCHEMA = schema(
    doc_type="reclassification_memo",
    title="Reclassification Memo",
    role="adjustment_doc",
    description="Internal memo approving a correcting entry that moves an amount between expense accounts.",
    required_fields=(
        req("memo_id", "string", "Memo id"),
        req("original_reference", "string", "Original source reference"),
        req("from_account", "string", "Account to credit"),
        req("to_account", "string", "Account to debit"),
        req("amount", "number", "Reclassification amount"),
        req("narrative", "string", "Reason for the correction"),
    ),
    sections=(
        kv(
            "Correction Summary",
            ("Memo ID", "memo_id"),
            ("Original Reference", "original_reference"),
            ("From Account", "from_account"),
            ("To Account", "to_account"),
            ("Amount", "amount"),
        ),
        narrative("Explanation", "Narrative", "narrative"),
    ),
    visible_fields=("memo_id", "original_reference", "from_account", "to_account", "amount"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
