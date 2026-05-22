from finbalance.doc_schemas.base import kv, opt, req, schema


SCHEMA = schema(
    doc_type="loan_statement",
    title="Loan Statement",
    role="posting_doc",
    description="Loan draw or repayment statement.",
    required_fields=(
        req("loan_number", "string", "Loan account number"),
        req("lender", "string", "Lender name"),
        req("opening_principal", "number", "Opening principal"),
        req("draw_amount", "number", "New funds drawn"),
        req("principal_paid", "number", "Principal repaid"),
        req("interest_paid", "number", "Interest paid"),
        req("ending_principal", "number", "Ending principal"),
    ),
    optional_fields=(opt("note", "string", "Loan narrative"),),
    sections=(
        kv(
            "Loan Activity",
            ("Loan Number", "loan_number"),
            ("Lender", "lender"),
            ("Opening Principal", "opening_principal"),
            ("Draw Amount", "draw_amount"),
            ("Principal Paid", "principal_paid"),
            ("Interest Paid", "interest_paid"),
            ("Ending Principal", "ending_principal"),
            ("Note", "note"),
        ),
    ),
    visible_fields=("loan_number", "lender", "ending_principal"),
)
