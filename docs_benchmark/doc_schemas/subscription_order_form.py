from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="subscription_order_form",
    title="Subscription Order Form",
    role="support_doc",
    description="Order form for a deferred-revenue subscription contract.",
    required_fields=(
        req("form_number", "string", "Order form number"),
        req("customer", "string", "Customer name"),
        req("plan_name", "string", "Plan name"),
        req("term_months", "number", "Term length in months"),
        req("contract_start", "date", "Contract start"),
        req("total_contract_value", "number", "Total contract value"),
    ),
    sections=(
        kv(
            "Order Summary",
            ("Form Number", "form_number"),
            ("Customer", "customer"),
            ("Plan Name", "plan_name"),
            ("Term Months", "term_months"),
            ("Contract Start", "contract_start"),
            ("Contract Value", "total_contract_value"),
        ),
    ),
    visible_fields=("form_number", "customer", "total_contract_value"),
    template_variants=("formal", "compact", "sales"),
    cosmetic_blocks=("issuer_block", "recipient_block", "terms_block", "approval_block", "footer_block"),
)
