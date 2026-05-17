from docs_benchmark.doc_schemas.base import kv, narrative, req, schema


SCHEMA = schema(
    doc_type="deferred_tax_memo",
    title="Deferred Tax Memo",
    role="adjustment_doc",
    description="Deferred tax liability rollforward from book/tax depreciation differences.",
    required_fields=(
        req("memo_id", "string", "Memo id"),
        req("asset_tag", "string", "Asset tag"),
        req("opening_deferred_tax_liability", "number", "Opening deferred tax liability"),
        req("current_period_deferred_tax_movement", "number", "Current period deferred tax movement"),
        req("deferred_tax_liability_ending", "number", "Ending deferred tax liability"),
        req("deferred_tax_expense_amount", "number", "Deferred tax expense amount"),
        req("narrative", "string", "Memo narrative"),
    ),
    sections=(
        kv(
            "Deferred Tax Rollforward",
            ("Memo ID", "memo_id"),
            ("Asset Tag", "asset_tag"),
            ("Opening Deferred Tax Liability", "opening_deferred_tax_liability"),
            ("Current Period Deferred Tax Movement", "current_period_deferred_tax_movement"),
            ("Deferred Tax Liability Ending", "deferred_tax_liability_ending"),
            ("Deferred Tax Expense Amount", "deferred_tax_expense_amount"),
        ),
        narrative("Narrative", "Details", "narrative"),
    ),
    visible_fields=("memo_id", "asset_tag", "deferred_tax_liability_ending"),
    template_variants=("formal", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
