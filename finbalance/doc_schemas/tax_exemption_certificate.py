from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="tax_exemption_certificate",
    title="Tax Exemption Certificate",
    role="support_doc",
    description="Customer or vendor exemption certificate that overrides default tax treatment.",
    required_fields=(
        req("certificate_number", "string", "Certificate number"),
        req("counterparty", "string", "Counterparty"),
        req("tax_regime", "string", "Tax regime"),
        req("effective_date", "date", "Effective date"),
        req("expiration_date", "date", "Expiration date"),
        req("exemption_status", "string", "Exemption status"),
        req("exempt_reason", "string", "Reason for exemption"),
    ),
    sections=(
        kv(
            "Certificate",
            ("Certificate Number", "certificate_number"),
            ("Counterparty", "counterparty"),
            ("Tax Regime", "tax_regime"),
            ("Effective Date", "effective_date"),
            ("Expiration Date", "expiration_date"),
            ("Exemption Status", "exemption_status"),
            ("Exempt Reason", "exempt_reason"),
        ),
    ),
    visible_fields=("certificate_number", "counterparty", "exemption_status"),
    template_variants=("formal", "summary"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "footer_block"),
)
