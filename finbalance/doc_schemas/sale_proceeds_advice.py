from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="sale_proceeds_advice",
    title="Sale Proceeds Advice",
    role="support_doc",
    description="Cash proceeds advice for a fixed asset disposal.",
    required_fields=(
        req("advice_number", "string", "Advice number"),
        req("buyer", "string", "Buyer"),
        req("asset_tag", "string", "Asset tag"),
        req("proceeds_amount", "number", "Sale proceeds"),
        req("settlement_date", "date", "Settlement date"),
        req("payment_reference", "string", "Payment reference"),
    ),
    sections=(
        kv(
            "Proceeds",
            ("Advice Number", "advice_number"),
            ("Buyer", "buyer"),
            ("Asset Tag", "asset_tag"),
            ("Proceeds Amount", "proceeds_amount"),
            ("Settlement Date", "settlement_date"),
            ("Payment Reference", "payment_reference"),
        ),
    ),
    visible_fields=("advice_number", "asset_tag", "proceeds_amount"),
    template_variants=("formal", "remittance"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "footer_block"),
)
