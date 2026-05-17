from docs_benchmark.doc_schemas.base import kv, listing, req, schema


SCHEMA = schema(
    doc_type="performance_obligation_schedule",
    title="Performance Obligation Schedule",
    role="adjustment_doc",
    description="ASC 606 allocation and release schedule for bundled contracts.",
    required_fields=(
        req("schedule_id", "string", "Schedule id"),
        req("contract_reference", "string", "Contract reference"),
        req("transaction_price", "number", "Total contract transaction price"),
        req("total_ssp", "number", "Total standalone selling price"),
        req("allocation_total", "number", "Total allocated transaction price"),
        req("released_this_period", "number", "Revenue released this period"),
        req("ending_deferred", "number", "Ending deferred revenue"),
        req("obligations", "list", "Allocated performance obligations"),
    ),
    sections=(
        kv(
            "Allocation Summary",
            ("Schedule ID", "schedule_id"),
            ("Contract Reference", "contract_reference"),
            ("Transaction Price", "transaction_price"),
            ("Total SSP", "total_ssp"),
            ("Allocation Total", "allocation_total"),
            ("Released This Period", "released_this_period"),
            ("Ending Deferred", "ending_deferred"),
        ),
        listing("Performance Obligations", "Obligations", "obligations"),
    ),
    list_field_orders={
        "obligations": (
            "obligation",
            "ssp_amount",
            "invoice_line_amount",
            "allocated_transaction_price",
            "release_pattern",
            "released_this_period",
        )
    },
    visible_fields=("schedule_id", "contract_reference", "allocation_total"),
    template_variants=("formal", "contract", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "approval_block", "footer_block"),
)
