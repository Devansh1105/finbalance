from docs_benchmark.doc_schemas.base import kv, opt, req, schema


SCHEMA = schema(
    doc_type="payment_advice",
    title="Payment Advice",
    role="support_doc",
    description="Payment instruction or confirmation used to support a settlement.",
    required_fields=(
        req("number", "string", "Payment advice number"),
        req("counterparty", "string", "Who the payment is for"),
        req("amount", "number", "Payment amount"),
        req("reference", "string", "Reference invoice or bill"),
        req("payment_method", "string", "Settlement method"),
    ),
    optional_fields=(
        opt("payment_for", "string", "Narrative for the payment"),
        opt("allocations", "list", "Allocation lines for one payment against multiple references"),
    ),
    sections=(
        kv(
            "Payment Details",
            ("Advice Number", "number"),
            ("Counterparty", "counterparty"),
            ("Amount", "amount"),
            ("Reference", "reference"),
            ("Payment Method", "payment_method"),
            ("Payment For", "payment_for"),
        ),
        kv(
            "Allocation Details",
            ("Allocations", "allocations"),
        ),
    ),
    list_field_orders={"allocations": ("reference", "allocated_amount", "status")},
    visible_fields=("number", "counterparty", "amount", "reference"),
    template_variants=("formal", "compact", "bank_transfer"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "footer_block"),
)
