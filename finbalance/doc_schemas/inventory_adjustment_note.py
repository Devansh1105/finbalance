from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="inventory_adjustment_note",
    title="Inventory Adjustment Note",
    role="adjustment_doc",
    description="Month-end note that records a stock difference.",
    required_fields=(
        req("note_id", "string", "Adjustment note id"),
        req("reason", "string", "Reason for adjustment"),
        req("amount", "number", "Inventory adjustment amount"),
        req("reference_sheet_id", "string", "Linked stock count sheet"),
    ),
    sections=(
        kv(
            "Adjustment Summary",
            ("Note ID", "note_id"),
            ("Reason", "reason"),
            ("Amount", "amount"),
            ("Reference Sheet", "reference_sheet_id"),
        ),
    ),
    visible_fields=("note_id", "amount", "reference_sheet_id"),
)
