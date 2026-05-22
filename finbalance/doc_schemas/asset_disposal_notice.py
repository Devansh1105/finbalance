from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="asset_disposal_notice",
    title="Asset Disposal Notice",
    role="adjustment_doc",
    description="Fixed asset disposal support showing NBV and gain or loss.",
    required_fields=(
        req("notice_number", "string", "Notice number"),
        req("asset_name", "string", "Asset name"),
        req("asset_tag", "string", "Asset tag"),
        req("original_cost", "number", "Original cost"),
        req("accumulated_depreciation", "number", "Accumulated depreciation removed"),
        req("net_book_value", "number", "Net book value"),
        req("proceeds_amount", "number", "Sale proceeds"),
        req("gain_loss_amount", "number", "Gain or loss amount"),
        req("gain_loss_type", "string", "Gain or loss type"),
    ),
    sections=(
        kv(
            "Disposal Computation",
            ("Notice Number", "notice_number"),
            ("Asset Name", "asset_name"),
            ("Asset Tag", "asset_tag"),
            ("Original Cost", "original_cost"),
            ("Accumulated Depreciation", "accumulated_depreciation"),
            ("Net Book Value", "net_book_value"),
            ("Proceeds Amount", "proceeds_amount"),
            ("Gain Loss Amount", "gain_loss_amount"),
            ("Gain Loss Type", "gain_loss_type"),
        ),
    ),
    visible_fields=("notice_number", "asset_tag", "net_book_value"),
    template_variants=("formal", "schedule", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
