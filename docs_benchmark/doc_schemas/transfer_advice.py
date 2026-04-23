from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="transfer_advice",
    title="Transfer Advice",
    role="support_doc",
    description="Internal bank transfer instruction between two company-controlled cash accounts.",
    required_fields=(
        req("transfer_number", "string", "Transfer advice number"),
        req("from_account", "string", "Source cash account"),
        req("to_account", "string", "Destination cash account"),
        req("amount", "number", "Transfer amount"),
        req("transfer_date", "date", "Transfer date"),
        req("reference", "string", "Transfer reference"),
    ),
    sections=(
        kv(
            "Transfer Details",
            ("Transfer Number", "transfer_number"),
            ("From Account", "from_account"),
            ("To Account", "to_account"),
            ("Amount", "amount"),
            ("Transfer Date", "transfer_date"),
            ("Reference", "reference"),
        ),
    ),
    visible_fields=("transfer_number", "from_account", "to_account", "amount"),
    template_variants=("formal", "bank_transfer"),
    cosmetic_blocks=("issuer_block", "reference_block", "footer_block"),
)
