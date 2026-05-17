from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="customer_tax_profile",
    title="Customer Tax Profile",
    role="support_doc",
    description="Customer tax jurisdiction and exemption profile.",
    required_fields=(
        req("profile_id", "string", "Profile id"),
        req("customer", "string", "Customer"),
        req("customer_jurisdiction", "string", "Customer jurisdiction"),
        req("company_jurisdiction", "string", "Company jurisdiction"),
        req("same_state", "bool", "Whether both parties are in the same state"),
        req("exemption_certificate", "string", "Linked exemption certificate"),
    ),
    sections=(
        kv(
            "Tax Profile",
            ("Profile ID", "profile_id"),
            ("Customer", "customer"),
            ("Customer Jurisdiction", "customer_jurisdiction"),
            ("Company Jurisdiction", "company_jurisdiction"),
            ("Same State", "same_state"),
            ("Exemption Certificate", "exemption_certificate"),
        ),
    ),
    visible_fields=("profile_id", "customer", "customer_jurisdiction"),
    template_variants=("formal", "summary"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "footer_block"),
)
