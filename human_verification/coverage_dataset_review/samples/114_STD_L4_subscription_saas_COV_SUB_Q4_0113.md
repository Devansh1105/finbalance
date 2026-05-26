# Verification Packet — COV_SUB_Q4_0113

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 4
- **Period type:** quarter
- **Period label:** Q4 FY 2026-27
- **Period start → end:** 2026-01-01 → 2026-03-31
- **Entity:** Silverline Clinic
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 20
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2026-01-01_

**Assets**
- Cash: 320,276.45
- Accounts Receivable: 42,210.26
- Prepaid Insurance: 6,017.48
- Equipment: 26,791.98
- Office Supplies: 1,814.33

**Liabilities**
- Accounts Payable: 13,982.78
- Accrued Expenses: 7,443.34
- Unearned Revenue: 65,828.19
- Loans Payable: 14,798.96

**Equity**
- Retained Earnings: 39,570.21
- Share Capital: 255,487.02


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2026-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/01/2026
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 320,276.45
  - Section assets | Account Accounts Receivable | Amount GBP 42,210.26
  - Section assets | Account Prepaid Insurance | Amount GBP 6,017.48
  - Section assets | Account Equipment | Amount GBP 26,791.98
  - Section assets | Account Office Supplies | Amount GBP 1,814.33
  - Section liabilities | Account Accounts Payable | Amount GBP 13,982.78
  - Section liabilities | Account Accrued Expenses | Amount GBP 7,443.34
  - Section liabilities | Account Unearned Revenue | Amount GBP 65,828.19
  - Section liabilities | Account Loans Payable | Amount GBP 14,798.96
  - Section equity | Account Retained Earnings | Amount GBP 39,570.21
  - Section equity | Account Share Capital | Amount GBP 255,487.02

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-01-12

```
VENDOR INVOICE
==============

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Document Date: 12/01/2026

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: Q4 FY 2026-27

Terms
-----
Due Date: 27/01/2026

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Utilities Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 27/01/2026
Subtotal: GBP 22,295.30
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 2,675.44
Total: GBP 24,970.74

Bill Lines
----------
Lines:
  - Description Review pack | Amount GBP 9,202.81
  - Description Support fee | Amount GBP 13,092.49

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D010 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2026-01-12

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Date: 12/01/2026

To
--
Blue Finch Holdings
Customer account on file

Terms
-----
Contract Start: 12/01/2026

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: ASC606-0001
Customer: Blue Finch Holdings
Plan Name: Enterprise License
Term Months: 12
Contract Start: 12/01/2026
Contract Value: GBP 875,109.19

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-01-12

```
CUSTOMER INVOICE
================

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Document Date: 12/01/2026

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: Q4 FY 2026-27
Contract Ref: ASC606-0001

Terms
-----
Due Date: 28/01/2026

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: ASC606-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 28/01/2026
Total: GBP 875,109.19

Line Items
----------
Items:
  - Description Implementation invoice line | Amount GBP 131,266.38
  - Description Platform access invoice line | Amount GBP 743,842.81

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D012 — SSP Rate Card

- **Type:** `ssp_rate_card`
- **Role:** `support_doc`
- **Date:** 2026-01-12

```
SSP RATE CARD
=============

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Date: 12/01/2026

Reference Box
-------------
Document ID: D012
Document Type: ssp_rate_card
Period: Q4 FY 2026-27

Rate Card
---------
Rate Card ID: SSP-0001
Contract Reference: ASC606-0001
Effective Date: 12/01/2026
Total SSP: GBP 1,028,070.88

Standalone Selling Prices
-------------------------
Obligations:
  - Obligation Implementation | Ssp Amount GBP 342,258.21
  - Obligation Platform access | Ssp Amount GBP 685,812.67

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D018 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2026-01-12

```
CANCELLATION NOTE
=================

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Document Date: 12/01/2026

Reference Box
-------------
Document ID: D018
Document Type: cancellation_note
Period: Q4 FY 2026-27

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
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2026-01-21

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Date: 21/01/2026

To
--
Riverfront Group
Customer account on file

Terms
-----
Contract Start: 21/01/2026

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Riverfront Group
Plan Name: Annual Growth Plan
Term Months: 12
Contract Start: 21/01/2026
Contract Value: GBP 253,955.28

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-01-21

```
CUSTOMER INVOICE
================

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Date: 21/01/2026

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: Q4 FY 2026-27
Contract Ref: SOF-0001

Terms
-----
Due Date: 28/01/2026

Parties
-------
Customer: Riverfront Group
Contract Ref: SOF-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 28/01/2026
Subtotal: GBP 226,745.79
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 27,209.49
CGST Amount: GBP 13,604.75
SGST Amount: GBP 13,604.74
Total: GBP 253,955.28

Line Items
----------
Items:
  - Description Team Support Plan | Amount GBP 90,291.95
  - Description Service coverage under contract | Amount GBP 136,453.84

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D013 — Implementation Acceptance Memo

- **Type:** `implementation_acceptance_memo`
- **Role:** `support_doc`
- **Date:** 2026-01-21

```
IMPLEMENTATION ACCEPTANCE MEMO / REFERENCE COPY
===============================================

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Document Date: 21/01/2026

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D013
Document Type: implementation_acceptance_memo
Period: Q4 FY 2026-27

Acceptance
----------
Memo ID: ACCEPT-0001
Contract Reference: ASC606-0001
Customer: Blue Finch Holdings
Acceptance Date: 21/01/2026
Accepted Obligation: Implementation
Accepted Amount: GBP 291,335.27

Narrative
---------
Details: Customer accepted implementation. Only the implementation performance obligation is
 released on acceptance.

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D009 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2026-02-01

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: GBP 44,786.95
Draw Amount: GBP 312,551.87
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 357,338.82
Note: Scheduled lender activity for the selected period.
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2026-03-05

```
PAYROLL SUMMARY
===============

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Document Date: 05/03/2026

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q4 FY 2026-27
Headcount: 12
Gross Pay: GBP 68,364.90
Employer Tax: 9,562.21
Cash Outflow: GBP 77,927.11

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-03-09

```
PAYMENT ADVICE
==============

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Date: 09/03/2026

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: Q4 FY 2026-27
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: GBP 16,066.98
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D017 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `posting_doc`
- **Date:** 2026-03-10

```
CREDIT MEMO
===========

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Date: 10/03/2026

To
--
Riverfront Group

Reference Box
-------------
Document ID: D017
Document Type: credit_memo
Period: Q4 FY 2026-27
Reference: INV-0001

Approval / Context
------------------
Reason: Service issue

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Riverfront Group
Currency: GBP
Reference: INV-0001
Reason: Service issue
Tax Label: India GST
Tax Rate: 0.00%
Tax Amount: GBP 6,100.69
Amount: GBP 38,129.32

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-03-18

```
PAYMENT ADVICE
==============

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Date: 18/03/2026

To
--
Riverfront Group

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q4 FY 2026-27
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: GBP 220,952.94
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D015 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2026-03-21

```
TRANSFER ADVICE
===============

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Date: 21/03/2026

Reference Box
-------------
Document ID: D015
Document Type: transfer_advice
Period: Q4 FY 2026-27
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: GBP 198,287.61
Transfer Date: 21/03/2026
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
REVENUE RECOGNITION SCHEDULE / REFERENCE COPY
=============================================

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Document Date: 31/03/2026

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: Q4 FY 2026-27

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: Q4 FY 2026-27
Opening Deferred: GBP 226,745.79
Added Deferred: GBP 0.00
Released This Period: 56,686.45
Ending Deferred: GBP 170,059.34

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D014 — Performance Obligation Schedule

- **Type:** `performance_obligation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
PERFORMANCE OBLIGATION SCHEDULE
===============================

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Date: 31/03/2026

Reference Box
-------------
Document ID: D014
Document Type: performance_obligation_schedule
Period: Q4 FY 2026-27

Allocation Summary
------------------
Schedule ID: POB-0001
Contract Reference: ASC606-0001
Transaction Price: GBP 875,109.19
Total SSP: GBP 1,028,070.88
Allocation Total: GBP 875,109.19
Released This Period: 437,278.75
Ending Deferred: GBP 437,830.44

Performance Obligations
-----------------------
Obligations:
  - Obligation Implementation | Ssp Amount GBP 342,258.21 | Invoice Line Amount GBP 
131,266.38 | Allocated Transaction Price GBP 291,335.27 | Release Pattern On acceptance | 
Released This Period 291,335.27
  - Obligation Platform access | Ssp Amount GBP 685,812.67 | Invoice Line Amount GBP 
743,842.81 | Allocated Transaction Price GBP 583,773.92 | Release Pattern Ratable over 12 
months | Released This Period 145,943.48

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D016 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Date: 31/03/2026

Reference Box
-------------
Document ID: D016
Document Type: service_period_memo
Period: Q4 FY 2026-27
Reference: Q4 FY 2026-27

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: Q4 FY 2026-27
Recognized Amount: GBP 2,597.62

Explanation
-----------
Narrative: Accrue unpaid utilities expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D019 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Document Date: 31/03/2026

Reference Box
-------------
Document ID: D019
Document Type: bank_statement
Period: Q4 FY 2026-27

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0113
Statement Currency: GBP
Opening Balance: GBP 320,276.45
Closing Balance: GBP 561,499.56

Statement Rows
--------------
Rows:
  - Date 01/02/2026 | Description Loan draw LOAN-0001 | Amount GBP 312,551.87 | Running 
Balance GBP 632,828.32
  - Date 05/03/2026 | Description Payroll PAYRUN-0001 | Amount GBP -77,927.11 | Running 
Balance GBP 554,901.21
  - Date 09/03/2026 | Description Supplier settlement BILL-0001 | Amount GBP -16,066.98 | 
Running Balance GBP 538,834.23
  - Date 18/03/2026 | Description Customer settlement INV-0001 | Amount GBP 220,952.94 | 
Running Balance GBP 759,787.17
  - Date 21/03/2026 | Description Transfer out TRX-0001 | Amount GBP -198,287.61 | Running 
Balance GBP 561,499.56

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Silverline Clinic
220 Lake View Road, Bengaluru
Date: 31/03/2026

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: Q4 FY 2026-27

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-1399
Statement Currency: GBP
Opening Balance: GBP 0.00
Closing Balance: GBP 198,287.61

Statement Rows
--------------
Rows:
  - Date 21/03/2026 | Description Transfer in TRX-0001 | Amount GBP 198,287.61 | Running 
Balance GBP 198,287.61

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D020
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Unearned Revenue | 226,745.79 | D002, D003 | 2026-01-21 | subscription_invoice |
| 2 | Accounts Receivable | CGST Payable | 13,604.75 | D002, D003 | 2026-01-21 | subscription_invoice_tax_cgst |
| 3 | Accounts Receivable | SGST Payable | 13,604.74 | D002, D003 | 2026-01-21 | subscription_invoice_tax_sgst |
| 4 | Unearned Revenue | Service Revenue | 56,686.45 | D004, D003 | 2026-03-31 | revenue_release |
| 5 | Cash | Accounts Receivable | 220,952.94 | D005, D003 | 2026-03-18 | customer_payment |
| 6 | Utilities Expense | Accounts Payable | 22,295.30 | D006 | 2026-01-12 | hosting_bill |
| 7 | Input CGST Receivable | Accounts Payable | 1,337.72 | D006 | 2026-01-12 | hosting_bill_tax_cgst |
| 8 | Input SGST Receivable | Accounts Payable | 1,337.72 | D006 | 2026-01-12 | hosting_bill_tax_sgst |
| 9 | Accounts Payable | Cash | 16,066.98 | D007, D006 | 2026-03-09 | vendor_payment |
| 10 | Salaries Expense | Cash | 68,364.90 | D008 | 2026-03-05 | payroll_gross |
| 11 | Payroll Tax Expense | Cash | 9,562.21 | D008 | 2026-03-05 | payroll_tax |
| 12 | Cash | Loans Payable | 312,551.87 | D009 | 2026-02-01 | loan_draw |
| 13 | Accounts Receivable | Unearned Revenue | 875,109.19 | D010, D011, D012 | 2026-01-12 | bundled_contract_allocation_invoice |
| 14 | Unearned Revenue | Service Revenue | 291,335.27 | D011, D012, D013, D014 | 2026-01-21 | bundled_contract_allocation_implementation_release |
| 15 | Unearned Revenue | Service Revenue | 145,943.48 | D011, D012, D013, D014 | 2026-03-31 | bundled_contract_allocation_platform_release |
| 16 | Reserve Cash | Cash | 198,287.61 | D015 | 2026-03-21 | interbank_transfer |
| 17 | Utilities Expense | Accrued Expenses | 2,597.62 | D016 | 2026-03-31 | expense_accrual |
| 18 | Unearned Revenue | Accounts Receivable | 38,129.32 | D003, D017 | 2026-03-10 | credit_memo |
| 19 | CGST Payable | Accounts Receivable | 3,050.34 | D003, D017 | 2026-03-10 | credit_memo_tax_cgst |
| 20 | SGST Payable | Accounts Receivable | 3,050.35 | D003, D017 | 2026-03-10 | credit_memo_tax_sgst |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 561,499.56
- Accounts Receivable: 906,091.78
- Prepaid Insurance: 6,017.48
- Equipment: 26,791.98
- Office Supplies: 1,814.33
- Input CGST Receivable: 1,337.72
- Input SGST Receivable: 1,337.72
- Reserve Cash: 198,287.61

**Liabilities**
- Accounts Payable: 22,886.54
- Accrued Expenses: 10,040.96
- Unearned Revenue: 635,588.65
- Loans Payable: 327,350.83
- CGST Payable: 10,554.41
- SGST Payable: 10,554.39

**Equity**
- Retained Earnings: 430,715.38
- Share Capital: 255,487.02

**Totals:** Assets = 1,703,178.18; Liabilities = 1,016,975.78; Equity = 686,202.40
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
