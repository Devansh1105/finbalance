from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="tax_depreciation_schedule",
    title="Tax Depreciation Schedule",
    role="support_doc",
    description="Tax-basis depreciation support for deferred tax computation.",
    required_fields=(
        req("schedule_id", "string", "Schedule id"),
        req("asset_tag", "string", "Asset tag"),
        req("book_depreciation_amount", "number", "Book depreciation"),
        req("tax_depreciation_amount", "number", "Tax depreciation"),
        req("temporary_difference_amount", "number", "Temporary difference"),
        req("tax_rate", "number", "Tax rate"),
    ),
    sections=(
        kv(
            "Book Tax Difference",
            ("Schedule ID", "schedule_id"),
            ("Asset Tag", "asset_tag"),
            ("Book Depreciation Amount", "book_depreciation_amount"),
            ("Tax Depreciation Amount", "tax_depreciation_amount"),
            ("Temporary Difference Amount", "temporary_difference_amount"),
            ("Tax Rate", "tax_rate"),
        ),
    ),
    visible_fields=("schedule_id", "asset_tag", "temporary_difference_amount"),
    template_variants=("formal", "schedule", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
