# Verification Packet — COV_SUB_Q3_0112

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 3
- **Period type:** quarter
- **Period label:** Q4 FY 2025
- **Period start → end:** 2025-10-01 → 2025-12-31
- **Entity:** Summit Manufacturing
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 16
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-10-01_

**Assets**
- Cash: 203,591.20
- Accounts Receivable: 23,196.39
- Prepaid Insurance: 8,505.01
- Office Supplies: 5,245.46

**Liabilities**
- Accounts Payable: 20,891.81
- Accrued Expenses: 5,611.28
- Unearned Revenue: 64,391.71

**Equity**
- Retained Earnings: 47,100.30
- Share Capital: 102,542.96


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-10-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/10/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 203.591,20
  - Section assets | Account Accounts Receivable | Amount EUR 23.196,39
  - Section assets | Account Prepaid Insurance | Amount EUR 8.505,01
  - Section assets | Account Office Supplies | Amount EUR 5.245,46
  - Section liabilities | Account Accounts Payable | Amount EUR 20.891,81
  - Section liabilities | Account Accrued Expenses | Amount EUR 5.611,28
  - Section liabilities | Account Unearned Revenue | Amount EUR 64.391,71
  - Section equity | Account Retained Earnings | Amount EUR 47.100,30
  - Section equity | Account Share Capital | Amount EUR 102.542,96

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D013 — Renewal Notice

- **Type:** `renewal_notice`
- **Role:** `support_doc`
- **Date:** 2025-10-01

```
RENEWAL NOTICE
==============

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Document Date: 01/10/2025

To
--
Oak Harbor Foods
Customer account on file

Terms
-----
Renewal Start: 12/10/2025

Renewal Summary
---------------
Notice Number: RENEW-0001
Customer: Oak Harbor Foods
Contract Reference: SOF-0003
Renewal Start: 12/10/2025
Renewal Amount: EUR 285.350,93

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-10

```
VENDOR INVOICE
==============

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Document Date: 10/10/2025

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 27/10/2025

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Utilities Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 27/10/2025
Subtotal: EUR 29.865,50
Tax Label: US Sales Tax
Tax Rate: 6.25%
Tax Amount: EUR 1.866,59
Total: EUR 31.732,09

Bill Lines
----------
Lines:
  - Description Support package | Amount EUR 6.698,05
  - Description Support fee | Amount EUR 23.167,45

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D012 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-10-12

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Date: 12/10/2025

To
--
Oak Harbor Foods
Customer account on file

Terms
-----
Contract Start: 12/10/2025

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: SOF-0003
Customer: Oak Harbor Foods
Plan Name: Enterprise License
Term Months: 12
Contract Start: 12/10/2025
Contract Value: EUR 285.350,93

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D014 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-12

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Date: 12/10/2025

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D014
Document Type: customer_invoice
Period: Q4 FY 2025
Contract Ref: SOF-0003

Terms
-----
Due Date: 20/10/2025

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: SOF-0003
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 20/10/2025
Subtotal: EUR 260.594,46
Tax Label: US Sales Tax
Tax Rate: 9.50%
Tax Amount: EUR 24.756,47
Total: EUR 285.350,93

Line Items
----------
Items:
  - Description Business Suite | Amount EUR 109.919,05
  - Description Service coverage under contract | Amount EUR 150.675,41

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-10-14

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Document Date: 14/10/2025

To
--
Metro Edge Partners
Customer account on file

Terms
-----
Contract Start: 14/10/2025

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Metro Edge Partners
Plan Name: Annual Growth Plan
Term Months: 3
Contract Start: 14/10/2025
Contract Value: EUR 136.153,03

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-14

```
CUSTOMER INVOICE
================

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Document Date: 14/10/2025

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: Q4 FY 2025
Contract Ref: SOF-0001

Terms
-----
Due Date: 31/10/2025

Parties
-------
Customer: Metro Edge Partners
Contract Ref: SOF-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 31/10/2025
Subtotal: EUR 125.776,47
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 10.376,56
Total: EUR 136.153,03

Line Items
----------
Items:
  - Description Team Support Plan | Amount EUR 30.854,94
  - Description Service coverage under contract | Amount EUR 94.921,53

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D010 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-10-25

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Document Date: 25/10/2025

To
--
Metro Edge Partners
Customer account on file

Terms
-----
Contract Start: 25/10/2025

Approval / Context
------------------
Plan Name: Business Suite

Order Summary
-------------
Form Number: SOF-0002
Customer: Metro Edge Partners
Plan Name: Business Suite
Term Months: 3
Contract Start: 25/10/2025
Contract Value: EUR 71.431,95

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-25

```
CUSTOMER INVOICE
================

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Document Date: 25/10/2025

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: Q4 FY 2025
Contract Ref: SOF-0002

Terms
-----
Due Date: 03/11/2025

Parties
-------
Customer: Metro Edge Partners
Contract Ref: SOF-0002
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 03/11/2025
Subtotal: EUR 65.234,66
Tax Label: US Sales Tax
Tax Rate: 9.50%
Tax Amount: EUR 6.197,29
Total: EUR 71.431,95

Line Items
----------
Items:
  - Description Enterprise License | Amount EUR 26.720,29
  - Description Service coverage under contract | Amount EUR 38.514,37

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-12-01

```
PAYROLL SUMMARY
===============

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Date: 01/12/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q4 FY 2025
Headcount: 8
Gross Pay: EUR 47.295,56
Employer Tax: 3.826,88
Cash Outflow: EUR 51.122,44

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-09

```
PAYMENT ADVICE
==============

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Date: 09/12/2025

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q4 FY 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Metro Edge Partners
Amount: EUR 136.153,03
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-13

```
PAYMENT ADVICE
==============

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Date: 13/12/2025

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: Q4 FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: EUR 31.732,09
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
REVENUE RECOGNITION SCHEDULE / REFERENCE COPY
=============================================

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: Q4 FY 2025

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: Q4 FY 2025
Opening Deferred: EUR 125.776,47
Added Deferred: EUR 0,00
Released This Period: 125.776,47
Ending Deferred: EUR 0,00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: Q4 FY 2025
Reference: Q4 FY 2025

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: Q4 FY 2025
Recognized Amount: EUR 15.399,88

Explanation
-----------
Narrative: Accrue unpaid utilities expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D015 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D015
Document Type: memo
Period: Q4 FY 2025

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0001
Subject: Quarter-end packet routing note
Audience: All Staff

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D016 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Summit Manufacturing
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D016
Document Type: bank_statement
Period: Q4 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0112
Statement Currency: EUR
Opening Balance: EUR 203.591,20
Closing Balance: EUR 328.321,65

Statement Rows
--------------
Rows:
  - Date 25/10/2025 | Description Advance collection INV-0002 | Amount EUR 71.431,95 | 
Running Balance EUR 275.023,15
  - Date 01/12/2025 | Description Payroll PAYRUN-0001 | Amount EUR -51.122,44 | Running 
Balance EUR 223.900,71
  - Date 09/12/2025 | Description Customer settlement INV-0001 | Amount EUR 136.153,03 | 
Running Balance EUR 360.053,74
  - Date 13/12/2025 | Description Supplier settlement BILL-0001 | Amount EUR -31.732,09 | 
Running Balance EUR 328.321,65

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Unearned Revenue | 125,776.47 | D002, D003 | 2025-10-14 | subscription_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 10,376.56 | D002, D003 | 2025-10-14 | subscription_invoice_tax |
| 3 | Unearned Revenue | Service Revenue | 125,776.47 | D004, D003 | 2025-12-31 | revenue_release |
| 4 | Cash | Accounts Receivable | 136,153.03 | D005, D003 | 2025-12-09 | customer_payment |
| 5 | Utilities Expense | Accounts Payable | 29,865.50 | D006 | 2025-10-10 | hosting_bill |
| 6 | Input Tax Receivable | Accounts Payable | 1,866.59 | D006 | 2025-10-10 | hosting_bill_tax |
| 7 | Accounts Payable | Cash | 31,732.09 | D007, D006 | 2025-12-13 | vendor_payment |
| 8 | Salaries Expense | Cash | 47,295.56 | D008 | 2025-12-01 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 3,826.88 | D008 | 2025-12-01 | payroll_tax |
| 10 | Utilities Expense | Accrued Expenses | 15,399.88 | D009 | 2025-12-31 | expense_accrual |
| 11 | Cash | Unearned Revenue | 65,234.66 | D010, D011 | 2025-10-25 | subscription_cash_invoice |
| 12 | Cash | Sales Tax Payable | 6,197.29 | D010, D011 | 2025-10-25 | subscription_cash_invoice_tax |
| 13 | Accounts Receivable | Unearned Revenue | 260,594.46 | D013, D012, D014 | 2025-10-12 | renewal_invoice |
| 14 | Accounts Receivable | Sales Tax Payable | 24,756.47 | D013, D012, D014 | 2025-10-12 | renewal_invoice_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 328,321.65
- Accounts Receivable: 308,547.32
- Prepaid Insurance: 8,505.01
- Office Supplies: 5,245.46
- Input Tax Receivable: 1,866.59

**Liabilities**
- Accounts Payable: 20,891.81
- Accrued Expenses: 21,011.16
- Unearned Revenue: 390,220.83
- Sales Tax Payable: 41,330.32

**Equity**
- Retained Earnings: 76,488.95
- Share Capital: 102,542.96

**Totals:** Assets = 652,486.03; Liabilities = 473,454.12; Equity = 179,031.91
**Balanced (A = L + E):** True

---

## 7. Verification Form

_Fill in your judgement below. For each question, mark one box and add notes where applicable._

### Q1 — Document analogy to real paperwork
We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?
- [x] Yes — analogous to what an accountant would receive
- [ ] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes:

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
- Notes: Checks out.
