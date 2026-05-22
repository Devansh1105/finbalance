from finbalance.doc_schemas.base import kv, listing, req, schema


SCHEMA = schema(
    doc_type="ssp_rate_card",
    title="SSP Rate Card",
    role="support_doc",
    description="Standalone selling prices used for ASC 606 transaction price allocation.",
    required_fields=(
        req("rate_card_id", "string", "Rate card id"),
        req("contract_reference", "string", "Contract reference"),
        req("effective_date", "date", "Effective date"),
        req("obligations", "list", "Performance obligations and SSPs"),
        req("total_ssp", "number", "Total standalone selling price"),
    ),
    sections=(
        kv(
            "Rate Card",
            ("Rate Card ID", "rate_card_id"),
            ("Contract Reference", "contract_reference"),
            ("Effective Date", "effective_date"),
            ("Total SSP", "total_ssp"),
        ),
        listing("Standalone Selling Prices", "Obligations", "obligations"),
    ),
    list_field_orders={"obligations": ("obligation", "ssp_amount")},
    visible_fields=("rate_card_id", "contract_reference", "total_ssp"),
    template_variants=("formal", "contract", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
