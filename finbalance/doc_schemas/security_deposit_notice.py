from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="security_deposit_notice",
    title="Security Deposit Notice",
    role="posting_doc",
    description="Notice for tenant security deposit receipt or refund.",
    required_fields=(
        req("notice_number", "string", "Deposit notice number"),
        req("tenant_name", "string", "Tenant"),
        req("unit_id", "string", "Unit"),
        req("amount", "number", "Deposit amount"),
        req("due_date", "date", "Payment or refund date"),
    ),
    sections=(
        kv(
            "Security Deposit",
            ("Notice Number", "notice_number"),
            ("Tenant", "tenant_name"),
            ("Unit", "unit_id"),
            ("Amount", "amount"),
            ("Due Date", "due_date"),
        ),
    ),
    visible_fields=("notice_number", "tenant_name", "amount"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "footer_block"),
)
