from docs_benchmark.doc_schemas.base import kv, narrative, req, schema


SCHEMA = schema(
    doc_type="lease_modification_notice",
    title="Lease Modification Notice",
    role="adjustment_doc",
    description="Lease modification notice for remeasuring liability and adjusting ROU asset.",
    required_fields=(
        req("modification_number", "string", "Modification number"),
        req("agreement_number", "string", "Lease agreement number"),
        req("modification_date", "date", "Modification date"),
        req("old_liability_balance", "number", "Old lease liability"),
        req("remeasured_liability_balance", "number", "Remeasured lease liability"),
        req("liability_remeasurement_delta_amount", "number", "Remeasurement delta"),
        req("rou_asset_adjustment_amount", "number", "ROU asset adjustment"),
        req("narrative", "string", "Modification narrative"),
    ),
    sections=(
        kv(
            "Remeasurement",
            ("Modification Number", "modification_number"),
            ("Agreement Number", "agreement_number"),
            ("Modification Date", "modification_date"),
            ("Old Liability Balance", "old_liability_balance"),
            ("Remeasured Liability Balance", "remeasured_liability_balance"),
            ("Liability Remeasurement Delta Amount", "liability_remeasurement_delta_amount"),
            ("ROU Asset Adjustment Amount", "rou_asset_adjustment_amount"),
        ),
        narrative("Narrative", "Details", "narrative"),
    ),
    visible_fields=("modification_number", "agreement_number", "liability_remeasurement_delta_amount"),
    template_variants=("formal", "contract", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
