# Verification Packet — COV_SUB_M3_0107

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 3
- **Period type:** month
- **Period label:** May 2024
- **Period start → end:** 2024-05-01 → 2024-05-31
- **Entity:** Beacon Retail Group
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 12
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-05-01_

**Assets**
- Cash: 97,896.40
- Accounts Receivable: 8,394.55
- Prepaid Insurance: 3,869.88
- Office Supplies: 774.99

**Liabilities**
- Accounts Payable: 4,017.14
- Accrued Expenses: 2,334.75
- Unearned Revenue: 16,780.22

**Equity**
- Retained Earnings: 8,478.32
- Share Capital: 79,325.39


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-05-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/05/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 97,896.40
  - Section assets | Account Accounts Receivable | Amount GBP 8,394.55
  - Section assets | Account Prepaid Insurance | Amount GBP 3,869.88
  - Section assets | Account Office Supplies | Amount GBP 774.99
  - Section liabilities | Account Accounts Payable | Amount GBP 4,017.14
  - Section liabilities | Account Accrued Expenses | Amount GBP 2,334.75
  - Section liabilities | Account Unearned Revenue | Amount GBP 16,780.22
  - Section equity | Account Retained Earnings | Amount GBP 8,478.32
  - Section equity | Account Share Capital | Amount GBP 79,325.39

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D011 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2024-05-01

```
MEMO
====

From
----
Beacon Retail Group
220 Lake View Road, Bengaluru
Document Date: 01/05/2024

Reference Box
-------------
Document ID: D011
Document Type: memo
Period: May 2024

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0001
Subject: Quarter-end packet routing note
Audience: Operations Team

Memo Body
---------
Narrative: The packet may include supporting correspondence gathered during the close 
review.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-05-02

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Beacon Retail Group
220 Lake View Road, Bengaluru
Date: 02/05/2024

To
--
Riverfront Group
Customer account on file

Terms
-----
Contract Start: 02/05/2024

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: SOF-0001
Customer: Riverfront Group
Plan Name: Enterprise License
Term Months: 12
Contract Start: 02/05/2024
Contract Value: GBP 107,241.51

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-02

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Beacon Retail Group
220 Lake View Road, Bengaluru
Date: 02/05/2024

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: May 2024
Contract Ref: SOF-0001

Terms
-----
Due Date: 12/05/2024

Parties
-------
Customer: Riverfront Group
Contract Ref: SOF-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 12/05/2024
Subtotal: GBP 102,134.77
Tax Label: India GST
Tax Rate: 5.00%
Tax Amount: GBP 5,106.74
CGST Amount: GBP 2,553.37
SGST Amount: GBP 2,553.37
Total: GBP 107,241.51

Line Items
----------
Items:
  - Description Business Suite | Amount GBP 29,668.27
  - Description Service coverage under contract | Amount GBP 72,466.50

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D009 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-05-02

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Beacon Retail Group
220 Lake View Road, Bengaluru
Date: 02/05/2024

To
--
Metro Edge Partners
Customer account on file

Terms
-----
Contract Start: 02/05/2024

Approval / Context
------------------
Plan Name: Team Support Plan

Order Summary
-------------
Form Number: SOF-0002
Customer: Metro Edge Partners
Plan Name: Team Support Plan
Term Months: 6
Contract Start: 02/05/2024
Contract Value: GBP 23,037.55

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D010 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-02

```
CUSTOMER INVOICE
================

From
----
Beacon Retail Group
220 Lake View Road, Bengaluru
Document Date: 02/05/2024

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D010
Document Type: customer_invoice
Period: May 2024
Contract Ref: SOF-0002

Terms
-----
Due Date: 12/05/2024

Parties
-------
Customer: Metro Edge Partners
Contract Ref: SOF-0002
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 12/05/2024
Subtotal: GBP 19,523.35
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 3,514.20
CGST Amount: GBP 1,757.10
SGST Amount: GBP 1,757.10
Total: GBP 23,037.55

Line Items
----------
Items:
  - Description Business Suite | Amount GBP 8,646.36
  - Description Service coverage under contract | Amount GBP 10,876.99

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-04

```
VENDOR INVOICE
==============

From
----
Beacon Retail Group
220 Lake View Road, Bengaluru
Document Date: 04/05/2024

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: May 2024

Terms
-----
Due Date: 20/05/2024

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Utilities Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 20/05/2024
Subtotal: GBP 13,813.11
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 1,657.57
Total: GBP 15,470.68

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 4,829.85
  - Description Support fee | Amount GBP 8,983.26

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-05-21

```
PAYMENT ADVICE
==============

From
----
Beacon Retail Group
220 Lake View Road, Bengaluru
Document Date: 21/05/2024

To
--
Riverfront Group

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: May 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: GBP 107,241.51
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-05-24

```
PAYMENT ADVICE
==============

From
----
Beacon Retail Group
220 Lake View Road, Bengaluru
Document Date: 24/05/2024

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: May 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: GBP 15,470.68
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-05-24

```
PAYROLL SUMMARY
===============

From
----
Beacon Retail Group
220 Lake View Road, Bengaluru
Document Date: 24/05/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: May 2024
Headcount: 11
Gross Pay: GBP 12,688.94
Employer Tax: 1,403.36
Cash Outflow: GBP 14,092.30

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-05-31

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Beacon Retail Group
220 Lake View Road, Bengaluru
Date: 31/05/2024

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: May 2024

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: May 2024
Opening Deferred: GBP 102,134.77
Added Deferred: GBP 0.00
Released This Period: 8,511.23
Ending Deferred: GBP 93,623.54

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D012 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-05-31

```
BANK STATEMENT
==============

From
----
Beacon Retail Group
220 Lake View Road, Bengaluru
Date: 31/05/2024

Reference Box
-------------
Document ID: D012
Document Type: bank_statement
Period: May 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0107
Statement Currency: GBP
Opening Balance: GBP 97,896.40
Closing Balance: GBP 198,612.48

Statement Rows
--------------
Rows:
  - Date 02/05/2024 | Description Advance collection INV-0002 | Amount GBP 23,037.55 | 
Running Balance GBP 120,933.95
  - Date 21/05/2024 | Description Customer settlement INV-0001 | Amount GBP 107,241.51 | 
Running Balance GBP 228,175.46
  - Date 24/05/2024 | Description Payroll PAYRUN-0001 | Amount GBP -14,092.30 | Running 
Balance GBP 214,083.16
  - Date 24/05/2024 | Description Supplier settlement BILL-0001 | Amount GBP -15,470.68 | 
Running Balance GBP 198,612.48

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
| 1 | Accounts Receivable | Unearned Revenue | 102,134.77 | D002, D003 | 2024-05-02 | subscription_invoice |
| 2 | Accounts Receivable | CGST Payable | 2,553.37 | D002, D003 | 2024-05-02 | subscription_invoice_tax_cgst |
| 3 | Accounts Receivable | SGST Payable | 2,553.37 | D002, D003 | 2024-05-02 | subscription_invoice_tax_sgst |
| 4 | Unearned Revenue | Service Revenue | 8,511.23 | D004, D003 | 2024-05-31 | revenue_release |
| 5 | Cash | Accounts Receivable | 107,241.51 | D005, D003 | 2024-05-21 | customer_payment |
| 6 | Utilities Expense | Accounts Payable | 13,813.11 | D006 | 2024-05-04 | hosting_bill |
| 7 | Input CGST Receivable | Accounts Payable | 828.78 | D006 | 2024-05-04 | hosting_bill_tax_cgst |
| 8 | Input SGST Receivable | Accounts Payable | 828.79 | D006 | 2024-05-04 | hosting_bill_tax_sgst |
| 9 | Accounts Payable | Cash | 15,470.68 | D007, D006 | 2024-05-24 | vendor_payment |
| 10 | Salaries Expense | Cash | 12,688.94 | D008 | 2024-05-24 | payroll_gross |
| 11 | Payroll Tax Expense | Cash | 1,403.36 | D008 | 2024-05-24 | payroll_tax |
| 12 | Cash | Unearned Revenue | 19,523.35 | D009, D010 | 2024-05-02 | subscription_cash_invoice |
| 13 | Cash | CGST Payable | 1,757.10 | D009, D010 | 2024-05-02 | subscription_cash_invoice_tax_cgst |
| 14 | Cash | SGST Payable | 1,757.10 | D009, D010 | 2024-05-02 | subscription_cash_invoice_tax_sgst |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 198,612.48
- Accounts Receivable: 8,394.55
- Prepaid Insurance: 3,869.88
- Office Supplies: 774.99
- Input CGST Receivable: 828.78
- Input SGST Receivable: 828.79

**Liabilities**
- Accounts Payable: 4,017.14
- Accrued Expenses: 2,334.75
- Unearned Revenue: 129,927.11
- CGST Payable: 4,310.47
- SGST Payable: 4,310.47

**Equity**
- Retained Earnings: -10,915.86
- Share Capital: 79,325.39

**Totals:** Assets = 213,309.47; Liabilities = 144,899.94; Equity = 68,409.53
**Balanced (A = L + E):** True

---

## 7. Verification Form

_Fill in your judgement below. For each question, mark one box and add notes where applicable._

### Q1 — Document analogy to real paperwork
We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?
- [ ] Yes — analogous to what an accountant would receive
- [x] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes: SaaS contract refs are sparse but the allocation inputs are present.

### Q2 — Are the expected journal entries correct?
Given only the documents in section 4 (and the opening trial balance), would you book exactly the entries in section 5?
- [x] Yes — entries match what I would book
- [ ] Mostly — minor account / amount issues (please describe)
- [ ] No — significant errors (missing entries, wrong entries, wrong amounts)
- Notes:

### Q3 — Are entries complete?
Are there any entries you would book that are MISSING from section 5? Or any entries in section 5 that should NOT be there?
- [x] Complete and exact
- [ ] Missing entries (list them in notes)
- [ ] Extra entries that should not be booked (list them)
- Notes:

### Q4 — Are document references correct?
For each expected entry, is `doc_refs` the set of documents that actually support that posting?
- [x] Yes, doc_refs are correct
- [ ] Mostly correct with minor mismatches
- [ ] Doc_refs are systematically wrong
- Notes:

### Q5 — Difficulty calibration
Is the difficulty level (section 1) appropriately calibrated for this packet? L1=trivial, L5=hardest.
- [x] Calibration feels right
- [ ] Too easy for this level
- [ ] Too hard for this level
- Notes:

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
