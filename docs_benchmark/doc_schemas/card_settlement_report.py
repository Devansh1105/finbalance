from docs_benchmark.doc_schemas.base import kv, listing, req, schema


SCHEMA = schema(
    doc_type="card_settlement_report",
    title="Card Settlement Report",
    role="posting_doc",
    description="Processor settlement report that clears card batches into cash.",
    required_fields=(
        req("settlement_id", "string", "Settlement id"),
        req("processor", "string", "Processor"),
        req("batch_refs", "list", "Batch references"),
        req("gross_amount", "number", "Gross settled amount"),
        req("fees", "number", "Processor fees"),
        req("net_deposit", "number", "Net cash deposit"),
        req("deposit_date", "date", "Deposit date"),
    ),
    sections=(
        kv(
            "Settlement Summary",
            ("Settlement ID", "settlement_id"),
            ("Processor", "processor"),
            ("Gross Amount", "gross_amount"),
            ("Fees", "fees"),
            ("Net Deposit", "net_deposit"),
            ("Deposit Date", "deposit_date"),
        ),
        listing("Linked Batches", "Batch References", "batch_refs"),
    ),
    visible_fields=("settlement_id", "net_deposit"),
)
