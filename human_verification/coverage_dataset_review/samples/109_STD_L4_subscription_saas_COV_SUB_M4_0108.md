# Verification Packet — COV_SUB_M4_0108

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** April 2025
- **Period start → end:** 2025-04-01 → 2025-04-30
- **Entity:** Summit Clinic
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 17
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 87,539.98
- Accounts Receivable: 8,560.87
- Prepaid Insurance: 4,920.92
- Equipment: 23,364.87
- Office Supplies: 2,659.04

**Liabilities**
- Accounts Payable: 9,267.60
- Accrued Expenses: 2,435.95
- Unearned Revenue: 16,661.47
- Loans Payable: 4,607.48

**Equity**
- Retained Earnings: 9,868.00
- Share Capital: 84,205.18


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-04-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-04-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $87,539.98
  - Section assets | Account Accounts Receivable | Amount $8,560.87
  - Section assets | Account Prepaid Insurance | Amount $4,920.92
  - Section assets | Account Equipment | Amount $23,364.87
  - Section assets | Account Office Supplies | Amount $2,659.04
  - Section liabilities | Account Accounts Payable | Amount $9,267.60
  - Section liabilities | Account Accrued Expenses | Amount $2,435.95
  - Section liabilities | Account Unearned Revenue | Amount $16,661.47
  - Section liabilities | Account Loans Payable | Amount $4,607.48
  - Section equity | Account Retained Earnings | Amount $9,868.00
  - Section equity | Account Share Capital | Amount $84,205.18

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D010 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-04-04

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Summit Clinic
75 Market Road, Mumbai
Document Date: 2025-04-04

To
--
Riverfront Group
Customer account on file

Terms
-----
Contract Start: 2025-04-04

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: ASC606-0001
Customer: Riverfront Group
Plan Name: Enterprise License
Term Months: 12
Contract Start: 2025-04-04
Contract Value: $256,289.21

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-04

```
CUSTOMER INVOICE
================

From
----
Summit Clinic
75 Market Road, Mumbai
Date: 2025-04-04

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: April 2025
Contract Ref: ASC606-0001

Terms
-----
Due Date: 2025-04-13

Parties
-------
Customer: Riverfront Group
Contract Ref: ASC606-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-04-13
Total: $256,289.21

Line Items
----------
Items:
  - Description Implementation invoice line | Amount $38,443.38
  - Description Platform access invoice line | Amount $217,845.83

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D012 — SSP Rate Card

- **Type:** `ssp_rate_card`
- **Role:** `support_doc`
- **Date:** 2025-04-04

```
SSP RATE CARD
=============

From
----
Summit Clinic
75 Market Road, Mumbai
Date: 2025-04-04

Reference Box
-------------
Document ID: D012
Document Type: ssp_rate_card
Period: April 2025

Rate Card
---------
Rate Card ID: SSP-0001
Contract Reference: ASC606-0001
Effective Date: 2025-04-04
Total SSP: $299,610.90

Standalone Selling Prices
-------------------------
Obligations:
  - Obligation Implementation | Ssp Amount $100,656.37
  - Obligation Platform access | Ssp Amount $198,954.53

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-05

```
VENDOR INVOICE
==============

From
----
Summit Clinic
75 Market Road, Mumbai
Date: 2025-04-05

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: April 2025

Terms
-----
Due Date: 2025-04-23

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Utilities Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-04-23
Total: $17,259.80

Bill Lines
----------
Lines:
  - Description Review pack | Amount $4,309.87
  - Description Support fee | Amount $12,949.93

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-04-06

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Summit Clinic
75 Market Road, Mumbai
Date: 2025-04-06

To
--
Oak Harbor Foods
Customer account on file

Terms
-----
Contract Start: 2025-04-06

Approval / Context
------------------
Plan Name: Team Support Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Oak Harbor Foods
Plan Name: Team Support Plan
Term Months: 12
Contract Start: 2025-04-06
Contract Value: $84,594.83

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-06

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Summit Clinic
75 Market Road, Mumbai
Date: 2025-04-06

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: April 2025
Contract Ref: SOF-0001

Terms
-----
Due Date: 2025-04-21

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: SOF-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-04-21
Total: $84,594.83

Line Items
----------
Items:
  - Description Annual Growth Plan | Amount $30,718.80
  - Description Service coverage under contract | Amount $53,876.03

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D013 — Implementation Acceptance Memo

- **Type:** `implementation_acceptance_memo`
- **Role:** `support_doc`
- **Date:** 2025-04-07

```
IMPLEMENTATION ACCEPTANCE MEMO / REFERENCE COPY
===============================================

From
----
Summit Clinic
75 Market Road, Mumbai
Document Date: 2025-04-07

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D013
Document Type: implementation_acceptance_memo
Period: April 2025

Acceptance
----------
Memo ID: ACCEPT-0001
Contract Reference: ASC606-0001
Customer: Riverfront Group
Acceptance Date: 2025-04-07
Accepted Obligation: Implementation
Accepted Amount: $86,102.15

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
- **Date:** 2025-04-11

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: $15,242.32
Draw Amount: $154,022.49
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $169,264.81
Note: Scheduled lender activity for the selected period.
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-04-24

```
PAYMENT ADVICE
==============

From
----
Summit Clinic
75 Market Road, Mumbai
Date: 2025-04-24

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: April 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: $10,415.73
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-04-24

```
PAYROLL SUMMARY
===============

From
----
Summit Clinic
75 Market Road, Mumbai
Document Date: 2025-04-24

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: April 2025
Headcount: 5
Gross Pay: $41,132.76
Employer Tax: 4,937.97
Cash Outflow: $46,070.73

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D015 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-04-26

```
TRANSFER ADVICE
===============

From
----
Summit Clinic
75 Market Road, Mumbai
Document Date: 2025-04-26

Reference Box
-------------
Document ID: D015
Document Type: transfer_advice
Period: April 2025
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: $111,994.97
Transfer Date: 2025-04-26
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-04-27

```
PAYMENT ADVICE
==============

From
----
Summit Clinic
75 Market Road, Mumbai
Date: 2025-04-27

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: April 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Oak Harbor Foods
Amount: $71,078.11
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-04-30

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Summit Clinic
75 Market Road, Mumbai
Document Date: 2025-04-30

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: April 2025

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: April 2025
Opening Deferred: $84,594.83
Added Deferred: $0.00
Released This Period: 7,049.57
Ending Deferred: $77,545.26

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D014 — Performance Obligation Schedule

- **Type:** `performance_obligation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-04-30

```
PERFORMANCE OBLIGATION SCHEDULE
===============================

From
----
Summit Clinic
75 Market Road, Mumbai
Document Date: 2025-04-30

Reference Box
-------------
Document ID: D014
Document Type: performance_obligation_schedule
Period: April 2025

Allocation Summary
------------------
Schedule ID: POB-0001
Contract Reference: ASC606-0001
Transaction Price: $256,289.21
Total SSP: $299,610.90
Allocation Total: $256,289.21
Released This Period: 100,284.40
Ending Deferred: $156,004.81

Performance Obligations
-----------------------
Obligations:
  - Obligation Implementation | Ssp Amount $100,656.37 | Invoice Line Amount $38,443.38 | 
Allocated Transaction Price $86,102.15 | Release Pattern On acceptance | Released This 
Period 86,102.15
  - Obligation Platform access | Ssp Amount $198,954.53 | Invoice Line Amount $217,845.83 | 
Allocated Transaction Price $170,187.06 | Release Pattern Ratable over 12 months | Released 
This Period 14,182.25

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D016 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-04-30

```
BANK STATEMENT
==============

From
----
Summit Clinic
75 Market Road, Mumbai
Date: 2025-04-30

Reference Box
-------------
Document ID: D016
Document Type: bank_statement
Period: April 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0108
Statement Currency: USD
Opening Balance: $87,539.98
Closing Balance: $144,159.15

Statement Rows
--------------
Rows:
  - Date 2025-04-11 | Description Loan draw LOAN-0001 | Amount $154,022.49 | Running Balance
 $241,562.47
  - Date 2025-04-24 | Description Payroll PAYRUN-0001 | Amount $-46,070.73 | Running Balance
 $195,491.74
  - Date 2025-04-24 | Description Supplier settlement BILL-0001 | Amount $-10,415.73 | 
Running Balance $185,076.01
  - Date 2025-04-26 | Description Transfer out TRX-0001 | Amount $-111,994.97 | Running 
Balance $73,081.04
  - Date 2025-04-27 | Description Customer settlement INV-0001 | Amount $71,078.11 | Running
 Balance $144,159.15

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D017 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-04-30

```
BANK STATEMENT
==============

From
----
Summit Clinic
75 Market Road, Mumbai
Document Date: 2025-04-30

Reference Box
-------------
Document ID: D017
Document Type: bank_statement
Period: April 2025

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-0899
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $111,994.97

Statement Rows
--------------
Rows:
  - Date 2025-04-26 | Description Transfer in TRX-0001 | Amount $111,994.97 | Running 
Balance $111,994.97

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Unearned Revenue | 84,594.83 | D002, D003 | 2025-04-06 | subscription_invoice |
| 2 | Unearned Revenue | Service Revenue | 7,049.57 | D004, D003 | 2025-04-30 | revenue_release |
| 3 | Cash | Accounts Receivable | 71,078.11 | D005, D003 | 2025-04-27 | customer_payment |
| 4 | Utilities Expense | Accounts Payable | 17,259.80 | D006 | 2025-04-05 | hosting_bill |
| 5 | Accounts Payable | Cash | 10,415.73 | D007, D006 | 2025-04-24 | vendor_payment |
| 6 | Salaries Expense | Cash | 41,132.76 | D008 | 2025-04-24 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 4,937.97 | D008 | 2025-04-24 | payroll_tax |
| 8 | Cash | Loans Payable | 154,022.49 | D009 | 2025-04-11 | loan_draw |
| 9 | Accounts Receivable | Unearned Revenue | 256,289.21 | D010, D011, D012 | 2025-04-04 | bundled_contract_allocation_invoice |
| 10 | Unearned Revenue | Service Revenue | 86,102.15 | D011, D012, D013, D014 | 2025-04-07 | bundled_contract_allocation_implementation_release |
| 11 | Unearned Revenue | Service Revenue | 14,182.25 | D011, D012, D013, D014 | 2025-04-30 | bundled_contract_allocation_platform_release |
| 12 | Reserve Cash | Cash | 111,994.97 | D015 | 2025-04-26 | interbank_transfer |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 144,159.15
- Accounts Receivable: 278,366.80
- Prepaid Insurance: 4,920.92
- Equipment: 23,364.87
- Office Supplies: 2,659.04
- Reserve Cash: 111,994.97

**Liabilities**
- Accounts Payable: 16,111.67
- Accrued Expenses: 2,435.95
- Unearned Revenue: 250,211.54
- Loans Payable: 158,629.97

**Equity**
- Retained Earnings: 53,871.44
- Share Capital: 84,205.18

**Totals:** Assets = 565,465.75; Liabilities = 427,389.13; Equity = 138,076.62
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
