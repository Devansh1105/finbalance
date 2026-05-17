from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="tax_regime_notice",
    title="Tax Regime Notice",
    role="support_doc",
    description="Jurisdiction-specific indirect tax rule notice for the packet.",
    required_fields=(
        req("notice_number", "string", "Notice number"),
        req("tax_regime", "string", "Tax regime"),
        req("company_jurisdiction", "string", "Company jurisdiction"),
        req("counterparty_jurisdiction", "string", "Counterparty jurisdiction"),
        req("tax_rate", "number", "Applicable tax rate"),
        req("jurisdiction_tax_amount", "number", "Jurisdiction tax amount"),
        req("treatment", "string", "Tax treatment"),
    ),
    sections=(
        kv(
            "Tax Rule",
            ("Notice Number", "notice_number"),
            ("Tax Regime", "tax_regime"),
            ("Company Jurisdiction", "company_jurisdiction"),
            ("Counterparty Jurisdiction", "counterparty_jurisdiction"),
            ("Tax Rate", "tax_rate"),
            ("Jurisdiction Tax Amount", "jurisdiction_tax_amount"),
            ("Treatment", "treatment"),
        ),
    ),
    visible_fields=("notice_number", "tax_regime", "treatment"),
    template_variants=("formal", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "footer_block"),
)
