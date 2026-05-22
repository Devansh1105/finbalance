from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="lease_agreement",
    title="Lease Agreement",
    role="posting_doc",
    description="Lease agreement used to recognize ROU asset and lease liability.",
    required_fields=(
        req("agreement_number", "string", "Agreement number"),
        req("lessor", "string", "Lessor"),
        req("commencement_date", "date", "Lease commencement date"),
        req("term_months", "number", "Lease term"),
        req("monthly_payment_amount", "number", "Monthly payment amount"),
        req("incremental_borrowing_rate", "number", "Annual borrowing rate"),
        req("rou_asset_amount", "number", "ROU asset amount"),
        req("lease_liability_amount", "number", "Lease liability amount"),
    ),
    sections=(
        kv(
            "Lease Terms",
            ("Agreement Number", "agreement_number"),
            ("Lessor", "lessor"),
            ("Commencement Date", "commencement_date"),
            ("Term Months", "term_months"),
            ("Monthly Payment Amount", "monthly_payment_amount"),
            ("Incremental Borrowing Rate", "incremental_borrowing_rate"),
            ("ROU Asset Amount", "rou_asset_amount"),
            ("Lease Liability Amount", "lease_liability_amount"),
        ),
    ),
    visible_fields=("agreement_number", "lessor", "lease_liability_amount"),
    template_variants=("formal", "contract"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "terms_block", "footer_block"),
)
