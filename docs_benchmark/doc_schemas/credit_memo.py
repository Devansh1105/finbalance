from docs_benchmark.doc_schemas.base import kv, opt, req, schema


SCHEMA = schema(
    doc_type="credit_memo",
    title="Credit Memo",
    role="posting_doc",
    description="Credit note reducing a bill, invoice, or deferred balance.",
    required_fields=(
        req("memo_number", "string", "Credit memo number"),
        req("counterparty", "string", "Customer or supplier"),
        req("reference", "string", "Related invoice or contract"),
        req("reason", "string", "Reason for credit"),
        req("amount", "number", "Credit amount"),
    ),
    optional_fields=(
        opt("document_currency", "string", "Document currency code"),
        opt("tax_label", "string", "Indirect tax label"),
        opt("tax_rate", "number", "Indirect tax rate"),
        opt("tax_amount", "number", "Indirect tax amount"),
    ),
    sections=(
        kv(
            "Credit Memo",
            ("Memo Number", "memo_number"),
            ("Counterparty", "counterparty"),
            ("Currency", "document_currency"),
            ("Reference", "reference"),
            ("Reason", "reason"),
            ("Tax Label", "tax_label"),
            ("Tax Rate", "tax_rate"),
            ("Tax Amount", "tax_amount"),
            ("Amount", "amount"),
        ),
    ),
    visible_fields=("memo_number", "counterparty", "amount"),
    template_variants=("formal", "compact", "approval"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "approval_block", "footer_block"),
)
