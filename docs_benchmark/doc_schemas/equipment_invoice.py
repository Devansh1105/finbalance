from docs_benchmark.doc_schemas.base import kv, opt, req, schema


SCHEMA = schema(
    doc_type="equipment_invoice",
    title="Equipment Invoice",
    role="posting_doc",
    description="Invoice for a fixed-asset purchase.",
    required_fields=(
        req("number", "string", "Equipment invoice number"),
        req("vendor", "string", "Vendor"),
        req("asset_name", "string", "Asset purchased"),
        req("asset_tag", "string", "Asset tag"),
        req("useful_life_months", "number", "Useful life"),
        req("total", "number", "Total asset cost"),
        req("paid_cash", "number", "Cash paid now"),
        req("financed_amount", "number", "Amount financed"),
    ),
    optional_fields=(
        opt("note_reference", "string", "Promissory note reference"),
        opt("financing_instrument", "string", "Financing instrument description"),
    ),
    sections=(
        kv(
            "Asset Purchase",
            ("Invoice Number", "number"),
            ("Vendor", "vendor"),
            ("Asset Name", "asset_name"),
            ("Asset Tag", "asset_tag"),
            ("Useful Life Months", "useful_life_months"),
            ("Total", "total"),
            ("Paid Cash", "paid_cash"),
            ("Financed Amount", "financed_amount"),
            ("Note Reference", "note_reference"),
            ("Financing Instrument", "financing_instrument"),
        ),
    ),
    visible_fields=("number", "asset_name", "total"),
)
