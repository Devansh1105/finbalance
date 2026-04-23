from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="fixed_asset_rollforward",
    title="Fixed Asset Rollforward",
    role="adjustment_doc",
    description="Rollforward of fixed asset balances for a longer accounting period.",
    required_fields=(
        req("schedule_id", "string", "Schedule id"),
        req("asset_name", "string", "Asset name"),
        req("asset_tag", "string", "Asset tag"),
        req("cost", "number", "Cost"),
        req("useful_life_months", "number", "Useful life in months"),
        req("current_period_charge", "number", "Current period depreciation"),
        req("accumulated_depreciation", "number", "Accumulated depreciation"),
        req("opening_balance", "number", "Opening balance"),
        req("additions", "number", "Additions"),
        req("disposals", "number", "Disposals"),
        req("ending_balance", "number", "Ending balance"),
    ),
    sections=(
        kv(
            "Asset Rollforward",
            ("Schedule ID", "schedule_id"),
            ("Asset Name", "asset_name"),
            ("Asset Tag", "asset_tag"),
            ("Cost", "cost"),
            ("Useful Life", "useful_life_months"),
            ("Current Charge", "current_period_charge"),
            ("Accumulated Depreciation", "accumulated_depreciation"),
            ("Opening Balance", "opening_balance"),
            ("Additions", "additions"),
            ("Disposals", "disposals"),
            ("Ending Balance", "ending_balance"),
        ),
    ),
    visible_fields=("schedule_id", "asset_name", "current_period_charge"),
    template_variants=("formal", "schedule", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
