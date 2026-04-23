from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="renewal_notice",
    title="Renewal Notice",
    role="support_doc",
    description="Notice sent before a subscription or contract renewal.",
    required_fields=(
        req("notice_number", "string", "Notice number"),
        req("customer", "string", "Customer"),
        req("contract_reference", "string", "Contract reference"),
        req("renewal_start", "date", "Renewal start"),
        req("renewal_amount", "number", "Renewal amount"),
    ),
    sections=(
        kv(
            "Renewal Summary",
            ("Notice Number", "notice_number"),
            ("Customer", "customer"),
            ("Contract Reference", "contract_reference"),
            ("Renewal Start", "renewal_start"),
            ("Renewal Amount", "renewal_amount"),
        ),
    ),
    visible_fields=("notice_number", "customer", "renewal_amount"),
    template_variants=("formal", "compact", "contract"),
    cosmetic_blocks=("issuer_block", "recipient_block", "terms_block", "footer_block"),
)
