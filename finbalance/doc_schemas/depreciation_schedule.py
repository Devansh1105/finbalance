from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="depreciation_schedule",
    title="Depreciation Schedule",
    role="adjustment_doc",
    description="Monthly depreciation support for a fixed asset.",
    required_fields=(
        req("schedule_id", "string", "Schedule id"),
        req("asset_name", "string", "Asset name"),
        req("asset_tag", "string", "Asset tag"),
        req("cost", "number", "Original cost"),
        req("useful_life_months", "number", "Useful life"),
        req("current_period_charge", "number", "Current month depreciation"),
        req("accumulated_depreciation", "number", "Accumulated depreciation"),
    ),
    sections=(
        kv(
            "Depreciation Schedule",
            ("Schedule ID", "schedule_id"),
            ("Asset Name", "asset_name"),
            ("Asset Tag", "asset_tag"),
            ("Cost", "cost"),
            ("Useful Life Months", "useful_life_months"),
            ("Current Period Charge", "current_period_charge"),
            ("Accumulated Depreciation", "accumulated_depreciation"),
        ),
    ),
    visible_fields=("schedule_id", "asset_name", "current_period_charge"),
)
