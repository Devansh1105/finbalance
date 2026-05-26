# Verification Packet — COV_SUB_Q2_0111

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 2
- **Period type:** quarter
- **Period label:** Q1 FY 2024-25
- **Period start → end:** 2024-04-01 → 2024-06-30
- **Entity:** Cedar Operations
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 12
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 198,046.52
- Accounts Receivable: 33,794.66
- Prepaid Insurance: 9,047.54
- Office Supplies: 2,590.46

**Liabilities**
- Accounts Payable: 19,441.96
- Accrued Expenses: 7,749.29
- Unearned Revenue: 39,587.40

**Equity**
- Retained Earnings: 39,591.15
- Share Capital: 137,109.38


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-04-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-04-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $198,046.52
  - Section assets | Account Accounts Receivable | Amount $33,794.66
  - Section assets | Account Prepaid Insurance | Amount $9,047.54
  - Section assets | Account Office Supplies | Amount $2,590.46
  - Section liabilities | Account Accounts Payable | Amount $19,441.96
  - Section liabilities | Account Accrued Expenses | Amount $7,749.29
  - Section liabilities | Account Unearned Revenue | Amount $39,587.40
  - Section equity | Account Retained Earnings | Amount $39,591.15
  - Section equity | Account Share Capital | Amount $137,109.38

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D009 — Renewal Notice

- **Type:** `renewal_notice`
- **Role:** `support_doc`
- **Date:** 2024-04-01

```
RENEWAL NOTICE
==============

From
----
Cedar Operations
90 Hill Park, Hyderabad
Date: 2024-04-01

To
--
Crescent Labs
Customer account on file

Terms
-----
Renewal Start: 2024-04-11

Renewal Summary
---------------
Notice Number: RENEW-0001
Customer: Crescent Labs
Contract Reference: SOF-0002
Renewal Start: 2024-04-11
Renewal Amount: $79,985.14

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-10

```
VENDOR INVOICE
==============

From
----
Cedar Operations
90 Hill Park, Hyderabad
Date: 2024-04-10

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: Q1 FY 2024-25

Terms
-----
Due Date: 2024-04-26

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Utilities Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-04-26
Subtotal: $26,036.96
Tax Label: GST
Tax Rate: 7.00%
Tax Amount: $1,822.59
Total: $27,859.55

Bill Lines
----------
Lines:
  - Description Support package | Amount $6,286.25
  - Description Support fee | Amount $19,750.71

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D008 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-04-11

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Cedar Operations
90 Hill Park, Hyderabad
Document Date: 2024-04-11

To
--
Crescent Labs
Customer account on file

Terms
-----
Contract Start: 2024-04-11

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: SOF-0002
Customer: Crescent Labs
Plan Name: Enterprise License
Term Months: 6
Contract Start: 2024-04-11
Contract Value: $79,985.14

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D010 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-11

```
CUSTOMER INVOICE
================

From
----
Cedar Operations
90 Hill Park, Hyderabad
Document Date: 2024-04-11

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D010
Document Type: customer_invoice
Period: Q1 FY 2024-25
Contract Ref: SOF-0002

Terms
-----
Due Date: 2024-04-29

Parties
-------
Customer: Crescent Labs
Contract Ref: SOF-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2024-04-29
Subtotal: $72,713.76
Tax Label: GST
Tax Rate: 10.00%
Tax Amount: $7,271.38
Total: $79,985.14

Line Items
----------
Items:
  - Description Enterprise License | Amount $24,527.77
  - Description Service coverage under contract | Amount $48,185.99

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D011 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-04-11

```
CANCELLATION NOTE
=================

From
----
Cedar Operations
90 Hill Park, Hyderabad
Date: 2024-04-11

Reference Box
-------------
Document ID: D011
Document Type: cancellation_note
Period: Q1 FY 2024-25

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0002-OLD
Replacement Reference: INV-0002

Background
----------
Narrative: INV-0002-OLD is withdrawn and must not be posted. Use INV-0002 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-04-25

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Cedar Operations
90 Hill Park, Hyderabad
Date: 2024-04-25

To
--
Crescent Labs
Customer account on file

Terms
-----
Contract Start: 2024-04-25

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: SOF-0001
Customer: Crescent Labs
Plan Name: Enterprise License
Term Months: 6
Contract Start: 2024-04-25
Contract Value: $213,883.48

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-25

```
CUSTOMER INVOICE
================

From
----
Cedar Operations
90 Hill Park, Hyderabad
Date: 2024-04-25

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: Q1 FY 2024-25
Contract Ref: SOF-0001

Terms
-----
Due Date: 2024-05-02

Parties
-------
Customer: Crescent Labs
Contract Ref: SOF-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-05-02
Subtotal: $199,891.10
Tax Label: GST
Tax Rate: 7.00%
Tax Amount: $13,992.38
Total: $213,883.48

Line Items
----------
Items:
  - Description Enterprise License | Amount $74,342.42
  - Description Service coverage under contract | Amount $125,548.68

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-02

```
PAYMENT ADVICE
==============

From
----
Cedar Operations
90 Hill Park, Hyderabad
Date: 2024-06-02

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: Q1 FY 2024-25
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: $27,859.55
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-16

```
PAYMENT ADVICE
==============

From
----
Cedar Operations
90 Hill Park, Hyderabad
Document Date: 2024-06-16

To
--
Crescent Labs

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q1 FY 2024-25
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Crescent Labs
Amount: $213,883.48
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-30

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Cedar Operations
90 Hill Park, Hyderabad
Date: 2024-06-30

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: Q1 FY 2024-25

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: Q1 FY 2024-25
Opening Deferred: $199,891.10
Added Deferred: $0.00
Released This Period: 99,945.55
Ending Deferred: $99,945.55

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D012 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
BANK STATEMENT
==============

From
----
Cedar Operations
90 Hill Park, Hyderabad
Date: 2024-06-30

Reference Box
-------------
Document ID: D012
Document Type: bank_statement
Period: Q1 FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0111
Statement Currency: USD
Opening Balance: $198,046.52
Closing Balance: $384,070.45

Statement Rows
--------------
Rows:
  - Date 2024-06-02 | Description Supplier settlement BILL-0001 | Amount $-27,859.55 | 
Running Balance $170,186.97
  - Date 2024-06-16 | Description Customer settlement INV-0001 | Amount $213,883.48 | 
Running Balance $384,070.45

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D012
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Unearned Revenue | 199,891.10 | D002, D003 | 2024-04-25 | subscription_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 13,992.38 | D002, D003 | 2024-04-25 | subscription_invoice_tax |
| 3 | Unearned Revenue | Service Revenue | 99,945.55 | D004, D003 | 2024-06-30 | revenue_release |
| 4 | Cash | Accounts Receivable | 213,883.48 | D005, D003 | 2024-06-16 | customer_payment |
| 5 | Utilities Expense | Accounts Payable | 26,036.96 | D006 | 2024-04-10 | hosting_bill |
| 6 | Input Tax Receivable | Accounts Payable | 1,822.59 | D006 | 2024-04-10 | hosting_bill_tax |
| 7 | Accounts Payable | Cash | 27,859.55 | D007, D006 | 2024-06-02 | vendor_payment |
| 8 | Accounts Receivable | Unearned Revenue | 72,713.76 | D009, D008, D010 | 2024-04-11 | renewal_invoice |
| 9 | Accounts Receivable | Sales Tax Payable | 7,271.38 | D009, D008, D010 | 2024-04-11 | renewal_invoice_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 384,070.45
- Accounts Receivable: 113,779.80
- Prepaid Insurance: 9,047.54
- Office Supplies: 2,590.46
- Input Tax Receivable: 1,822.59

**Liabilities**
- Accounts Payable: 19,441.96
- Accrued Expenses: 7,749.29
- Unearned Revenue: 212,246.71
- Sales Tax Payable: 21,263.76

**Equity**
- Retained Earnings: 113,499.74
- Share Capital: 137,109.38

**Totals:** Assets = 511,310.84; Liabilities = 260,701.72; Equity = 250,609.12
**Balanced (A = L + E):** True

---

## 7. Verification Form

_Fill in your judgement below. For each question, mark one box and add notes where applicable._

### Q1 — Document analogy to real paperwork
We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?
- [ ] Yes — analogous to what an accountant would receive
- [ ] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes:

### Q2 — Are the expected journal entries correct?
Given only the documents in section 4 (and the opening trial balance), would you book exactly the entries in section 5?
- [ ] Yes — entries match what I would book
- [ ] Mostly — minor account / amount issues (please describe)
- [ ] No — significant errors (missing entries, wrong entries, wrong amounts)
- Notes:

### Q3 — Are entries complete?
Are there any entries you would book that are MISSING from section 5? Or any entries in section 5 that should NOT be there?
- [ ] Complete and exact
- [ ] Missing entries (list them in notes)
- [ ] Extra entries that should not be booked (list them)
- Notes:

### Q4 — Are document references correct?
For each expected entry, is `doc_refs` the set of documents that actually support that posting?
- [ ] Yes, doc_refs are correct
- [ ] Mostly correct with minor mismatches
- [ ] Doc_refs are systematically wrong
- Notes:

### Q5 — Difficulty calibration
Is the difficulty level (section 1) appropriately calibrated for this packet? L1=trivial, L5=hardest.
- [ ] Calibration feels right
- [ ] Too easy for this level
- [ ] Too hard for this level
- Notes:

### Q7 — Overall verdict
- [ ] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
