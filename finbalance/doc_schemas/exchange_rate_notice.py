from finbalance.doc_schemas.base import kv, opt, req, schema


SCHEMA = schema(
    doc_type="exchange_rate_notice",
    title="Exchange Rate Notice",
    role="support_doc",
    description="Support document showing the exchange rate used to convert a foreign-currency amount into functional currency.",
    required_fields=(
        req("notice_number", "string", "Rate notice number"),
        req("reference", "string", "Linked invoice or payment reference"),
        req("source_currency", "string", "Foreign source currency"),
        req("functional_currency", "string", "Functional currency"),
        req("exchange_rate", "number", "Applied exchange rate"),
        req("source_amount", "number", "Foreign-currency amount"),
        req("functional_amount", "number", "Converted functional amount"),
        req("rate_date", "date", "Rate date"),
    ),
    optional_fields=(opt("rate_type", "string", "Spot or closing rate description"),),
    sections=(
        kv(
            "Rate Summary",
            ("Notice Number", "notice_number"),
            ("Reference", "reference"),
            ("Rate Date", "rate_date"),
            ("Rate Type", "rate_type"),
        ),
        kv(
            "Conversion Details",
            ("Source Currency", "source_currency"),
            ("Source Amount", "source_amount"),
            ("Functional Currency", "functional_currency"),
            ("Exchange Rate", "exchange_rate"),
            ("Functional Amount", "functional_amount"),
        ),
    ),
    visible_fields=("notice_number", "reference", "source_currency", "functional_currency", "exchange_rate"),
    template_variants=("formal", "summary", "bank_transfer"),
    cosmetic_blocks=("issuer_block", "reference_block", "footer_block"),
)
