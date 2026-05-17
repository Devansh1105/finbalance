from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="lease_amortization_schedule",
    title="Lease Amortization Schedule",
    role="adjustment_doc",
    description="Lease liability and ROU amortization schedule.",
    required_fields=(
        req("schedule_id", "string", "Schedule id"),
        req("agreement_number", "string", "Lease agreement number"),
        req("opening_liability_balance", "number", "Opening lease liability"),
        req("payment_amount", "number", "Cash payment"),
        req("interest_amount", "number", "Interest component"),
        req("principal_amount", "number", "Principal component"),
        req("ending_liability_balance", "number", "Ending lease liability"),
        req("rou_amortization_amount", "number", "ROU asset amortization"),
    ),
    sections=(
        kv(
            "Lease Schedule",
            ("Schedule ID", "schedule_id"),
            ("Agreement Number", "agreement_number"),
            ("Opening Liability Balance", "opening_liability_balance"),
            ("Payment Amount", "payment_amount"),
            ("Interest Amount", "interest_amount"),
            ("Principal Amount", "principal_amount"),
            ("Ending Liability Balance", "ending_liability_balance"),
            ("ROU Amortization Amount", "rou_amortization_amount"),
        ),
    ),
    visible_fields=("schedule_id", "agreement_number", "ending_liability_balance"),
    template_variants=("formal", "schedule", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
