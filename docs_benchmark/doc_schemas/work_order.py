from docs_benchmark.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="work_order",
    title="Work Order",
    role="support_doc",
    description="Approved work order that supports a field-service invoice.",
    required_fields=(
        req("work_order_number", "string", "Work order number"),
        req("customer", "string", "Customer"),
        req("job_site", "string", "Job site"),
        req("scope", "string", "Work scope"),
        req("approved_amount", "number", "Approved amount"),
    ),
    sections=(
        kv(
            "Work Order Details",
            ("Work Order Number", "work_order_number"),
            ("Customer", "customer"),
            ("Job Site", "job_site"),
            ("Scope", "scope"),
            ("Approved Amount", "approved_amount"),
        ),
    ),
    visible_fields=("work_order_number", "customer", "approved_amount"),
)
