from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="scrap_report",
    title="Scrap Report",
    role="adjustment_doc",
    description="Report documenting damaged or obsolete production output.",
    required_fields=(
        req("report_number", "string", "Report number"),
        req("batch_or_lot_ref", "string", "Batch or lot reference"),
        req("reason", "string", "Reason for scrap"),
        req("write_down_amount", "number", "Write-down amount"),
    ),
    sections=(
        kv(
            "Scrap Summary",
            ("Report Number", "report_number"),
            ("Batch Or Lot", "batch_or_lot_ref"),
            ("Reason", "reason"),
            ("Write Down", "write_down_amount"),
        ),
    ),
    visible_fields=("report_number", "batch_or_lot_ref", "write_down_amount"),
    template_variants=("formal", "quality", "compact"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
