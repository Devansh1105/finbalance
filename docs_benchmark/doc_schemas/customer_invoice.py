from docs_benchmark.doc_schemas.base import DocSchemaVariant, kv, listing, opt, req, schema


SCHEMA = schema(
    doc_type="customer_invoice",
    title="Customer Invoice",
    role="posting_doc",
    description="Bill sent to a customer for delivered goods or services.",
    required_fields=(
        req("number", "string", "Invoice number"),
        req("customer", "string", "Customer name"),
        req("due_date", "date", "Invoice due date"),
        req("total", "number", "Total amount"),
        req("line_items", "list", "Invoice lines"),
    ),
    optional_fields=(
        opt("contract_ref", "string", "Underlying contract reference"),
        opt("job_code", "string", "Job or work code"),
        opt("shipment_ref", "string", "Shipment or delivery reference"),
        opt("document_currency", "string", "Document currency code"),
        opt("subtotal", "number", "Amount before indirect tax"),
        opt("tax_label", "string", "Indirect tax label"),
        opt("tax_rate", "number", "Indirect tax rate"),
        opt("tax_amount", "number", "Indirect tax amount"),
    ),
    sections=(
        kv("Parties", ("Customer", "customer"), ("Contract Ref", "contract_ref"), ("Currency", "document_currency")),
        kv(
            "Invoice Details",
            ("Invoice Number", "number"),
            ("Due Date", "due_date"),
            ("Subtotal", "subtotal"),
            ("Tax Label", "tax_label"),
            ("Tax Rate", "tax_rate"),
            ("Tax Amount", "tax_amount"),
            ("Total", "total"),
        ),
        listing("Line Items", "Items", "line_items"),
    ),
    list_field_orders={"line_items": ("description", "amount")},
    visible_fields=("number", "customer", "total"),
    template_variants=("formal", "compact", "remittance"),
    cosmetic_blocks=("issuer_block", "recipient_block", "reference_block", "terms_block", "footer_block"),
    variants={
        "field_services": DocSchemaVariant(
            extra_required_fields=(req("job_code", "string", "Field job code"),),
            extra_sections=(kv("Field Job", ("Job Code", "job_code")),),
            template_variants=("formal", "work_ordered", "compact"),
        ),
        "wholesale_distribution": DocSchemaVariant(
            extra_optional_fields=(opt("shipment_ref", "string", "Related delivery note"),),
            extra_sections=(kv("Shipment Link", ("Shipment Ref", "shipment_ref")),),
            template_variants=("formal", "shipment", "compact"),
        ),
    },
)
