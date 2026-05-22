from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="pos_batch_report",
    title="POS Batch Report",
    role="support_doc",
    description="Batch report from a card terminal or POS system.",
    required_fields=(
        req("batch_id", "string", "Batch id"),
        req("processor", "string", "Payment processor"),
        req("batch_total", "number", "Batch total"),
        req("fee_amount", "number", "Fees"),
        req("expected_deposit", "number", "Expected deposit"),
        req("terminal_id", "string", "Terminal id"),
    ),
    sections=(
        kv(
            "Batch Summary",
            ("Batch ID", "batch_id"),
            ("Processor", "processor"),
            ("Batch Total", "batch_total"),
            ("Fee Amount", "fee_amount"),
            ("Expected Deposit", "expected_deposit"),
            ("Terminal ID", "terminal_id"),
        ),
    ),
    visible_fields=("batch_id", "expected_deposit"),
)
