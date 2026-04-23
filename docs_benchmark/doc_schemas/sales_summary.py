from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="sales_summary",
    title="Sales Summary",
    role="posting_doc",
    description="Retail day or period sales summary.",
    required_fields=(
        req("report_id", "string", "Sales report id"),
        req("store_name", "string", "Store name"),
        req("gross_sales", "number", "Gross sales"),
        req("returns", "number", "Returns"),
        req("net_sales", "number", "Net sales"),
        req("cash_sales", "number", "Cash sales"),
        req("card_sales", "number", "Card sales"),
        req("units_sold", "number", "Units sold"),
    ),
    sections=(
        kv(
            "Sales Summary",
            ("Report ID", "report_id"),
            ("Store Name", "store_name"),
            ("Gross Sales", "gross_sales"),
            ("Returns", "returns"),
            ("Net Sales", "net_sales"),
            ("Cash Sales", "cash_sales"),
            ("Card Sales", "card_sales"),
            ("Units Sold", "units_sold"),
        ),
    ),
    visible_fields=("report_id", "net_sales", "card_sales"),
)
