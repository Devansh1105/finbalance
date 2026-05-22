from finbalance.doc_schemas.base import kv, req, schema


SCHEMA = schema(
    doc_type="payroll_summary",
    title="Payroll Summary",
    role="posting_doc",
    description="Payroll run showing gross pay, tax, and cash paid.",
    required_fields=(
        req("run_number", "string", "Payroll run number"),
        req("pay_period", "string", "Payroll period"),
        req("headcount", "number", "Number of employees paid"),
        req("gross_pay", "number", "Gross pay"),
        req("employer_tax", "number", "Employer tax cost"),
        req("cash_outflow", "number", "Cash paid"),
    ),
    sections=(
        kv(
            "Payroll Summary",
            ("Run Number", "run_number"),
            ("Pay Period", "pay_period"),
            ("Headcount", "headcount"),
            ("Gross Pay", "gross_pay"),
            ("Employer Tax", "employer_tax"),
            ("Cash Outflow", "cash_outflow"),
        ),
    ),
    visible_fields=("run_number", "pay_period", "cash_outflow"),
    template_variants=("formal", "register", "summary"),
    cosmetic_blocks=("issuer_block", "approval_block", "footer_block"),
)
