# Verification Packet — COV_NEG_00_PERFORMANCE_OBLIGATION_RELEASE_M

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** June 2024
- **Period start → end:** 2024-06-01 → 2024-06-30
- **Entity:** Silverline Advisors
- **Currency (display / functional):** USD / USD
- **Tax regime:** `us_sales_tax`
- **Document count:** 17
- **Labeled as inconsistent:** True
- **Inconsistency codes:** performance_obligation_release_mismatch
- **Inconsistency reasons:** Performance obligation release evidence does not reconcile to the recognition schedule.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-06-01_

**Assets**
- Cash: 124,240.80
- Accounts Receivable: 14,512.25
- Prepaid Insurance: 3,395.43
- Equipment: 12,077.89
- Office Supplies: 805.86

**Liabilities**
- Accounts Payable: 7,795.92
- Accrued Expenses: 1,590.71
- Unearned Revenue: 33,774.19
- Loans Payable: 10,503.77

**Equity**
- Retained Earnings: 21,779.49
- Share Capital: 79,588.15


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-06-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-06-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $124,240.80
  - Section assets | Account Accounts Receivable | Amount $14,512.25
  - Section assets | Account Prepaid Insurance | Amount $3,395.43
  - Section assets | Account Equipment | Amount $12,077.89
  - Section assets | Account Office Supplies | Amount $805.86
  - Section liabilities | Account Accounts Payable | Amount $7,795.92
  - Section liabilities | Account Accrued Expenses | Amount $1,590.71
  - Section liabilities | Account Unearned Revenue | Amount $33,774.19
  - Section liabilities | Account Loans Payable | Amount $10,503.77
  - Section equity | Account Retained Earnings | Amount $21,779.49
  - Section equity | Account Share Capital | Amount $79,588.15

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-06-05

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Date: 2024-06-05

To
--
Crescent Labs
Customer account on file

Terms
-----
Contract Start: 2024-06-05

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Crescent Labs
Plan Name: Annual Growth Plan
Term Months: 12
Contract Start: 2024-06-05
Contract Value: $109,138.00

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-05

```
CUSTOMER INVOICE
================

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Date: 2024-06-05

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: June 2024
Contract Ref: SOF-0001

Terms
-----
Due Date: 2024-06-12

Parties
-------
Customer: Crescent Labs
Contract Ref: SOF-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-06-12
Subtotal: $101,760.37
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: $7,377.63
Total: $109,138.00

Line Items
----------
Items:
  - Description Annual Growth Plan | Amount $27,525.97
  - Description Service coverage under contract | Amount $74,234.40

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D010 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-06-05

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Date: 2024-06-05

To
--
Riverfront Group
Customer account on file

Terms
-----
Contract Start: 2024-06-05

Approval / Context
------------------
Plan Name: Business Suite

Order Summary
-------------
Form Number: ASC606-0001
Customer: Riverfront Group
Plan Name: Business Suite
Term Months: 12
Contract Start: 2024-06-05
Contract Value: $352,234.57

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-05

```
CUSTOMER INVOICE
================

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Document Date: 2024-06-05

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: June 2024
Contract Ref: ASC606-0001

Terms
-----
Due Date: 2024-06-14

Parties
-------
Customer: Riverfront Group
Contract Ref: ASC606-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2024-06-14
Total: $352,234.57

Line Items
----------
Items:
  - Description Implementation invoice line | Amount $52,835.19
  - Description Platform access invoice line | Amount $299,399.38

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D012 — SSP Rate Card

- **Type:** `ssp_rate_card`
- **Role:** `support_doc`
- **Date:** 2024-06-05

```
SSP RATE CARD
=============

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Document Date: 2024-06-05

Reference Box
-------------
Document ID: D012
Document Type: ssp_rate_card
Period: June 2024

Rate Card
---------
Rate Card ID: SSP-0001
Contract Reference: ASC606-0001
Effective Date: 2024-06-05
Total SSP: $417,391.88

Standalone Selling Prices
-------------------------
Obligations:
  - Obligation Implementation | Ssp Amount $77,234.87
  - Obligation Platform access | Ssp Amount $340,157.01

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D013 — Implementation Acceptance Memo

- **Type:** `implementation_acceptance_memo`
- **Role:** `support_doc`
- **Date:** 2024-06-08

```
IMPLEMENTATION ACCEPTANCE MEMO
==============================

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Document Date: 2024-06-08

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D013
Document Type: implementation_acceptance_memo
Period: June 2024

Acceptance
----------
Memo ID: ACCEPT-0001
Contract Reference: ASC606-0001
Customer: Riverfront Group
Acceptance Date: 2024-06-08
Accepted Obligation: Implementation
Accepted Amount: $65,178.06

Narrative
---------
Details: Customer accepted implementation. Only the implementation performance obligation is
 released on acceptance.

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-09

```
VENDOR INVOICE
==============

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Date: 2024-06-09

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: June 2024

Terms
-----
Due Date: 2024-06-23

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Utilities Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-06-23
Subtotal: $13,479.17
Tax Label: US Sales Tax
Tax Rate: 9.50%
Tax Amount: $1,280.52
Total: $14,759.69

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $5,604.21
  - Description Support fee | Amount $7,874.96

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D009 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-06-11

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: $4,005.74
Draw Amount: $64,664.31
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $68,670.05
Note: Scheduled lender activity for the selected period.
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-20

```
PAYMENT ADVICE
==============

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Date: 2024-06-20

To
--
Crescent Labs

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: June 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Crescent Labs
Amount: $79,497.98
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D015 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-21

```
TRANSFER ADVICE
===============

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Date: 2024-06-21

Reference Box
-------------
Document ID: D015
Document Type: transfer_advice
Period: June 2024
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: $31,957.82
Transfer Date: 2024-06-21
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-22

```
PAYMENT ADVICE
==============

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Date: 2024-06-22

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: June 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Pace Office Mart
Amount: $9,900.72
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
- **Date:** 2024-06-26

```
PAYROLL SUMMARY
===============

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Date: 2024-06-26

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: June 2024
Headcount: 7
Gross Pay: $30,503.50
Employer Tax: 3,576.38
Cash Outflow: $34,079.88

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-30

```
REVENUE RECOGNITION SCHEDULE / REFERENCE COPY
=============================================

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: June 2024

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: June 2024
Opening Deferred: $101,760.37
Added Deferred: $0.00
Released This Period: 8,480.03
Ending Deferred: $93,280.34

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D014 — Performance Obligation Schedule

- **Type:** `performance_obligation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-30

```
PERFORMANCE OBLIGATION SCHEDULE
===============================

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D014
Document Type: performance_obligation_schedule
Period: June 2024

Allocation Summary
------------------
Schedule ID: POB-0001
Contract Reference: ASC606-0001
Transaction Price: $352,234.57
Total SSP: $417,391.88
Allocation Total: $352,234.57
Released This Period: $87,055.92
Ending Deferred: $263,135.13

Performance Obligations
-----------------------
Obligations:
  - Obligation Implementation | Ssp Amount $77,234.87 | Invoice Line Amount $52,835.19 | 
Allocated Transaction Price $65,178.06 | Release Pattern On acceptance | Released This 
Period 65,178.06
  - Obligation Platform access | Ssp Amount $340,157.01 | Invoice Line Amount $299,399.38 | 
Allocated Transaction Price $287,056.51 | Release Pattern Ratable over 12 months | Released 
This Period 23,921.38

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D016 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
BANK STATEMENT
==============

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D016
Document Type: bank_statement
Period: June 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-SE_M
Statement Currency: USD
Opening Balance: $124,240.80
Closing Balance: $192,464.67

Statement Rows
--------------
Rows:
  - Date 2024-06-11 | Description Loan draw LOAN-0001 | Amount $64,664.31 | Running Balance 
$188,905.11
  - Date 2024-06-20 | Description Customer settlement INV-0001 | Amount $79,497.98 | Running
 Balance $268,403.09
  - Date 2024-06-21 | Description Transfer out TRX-0001 | Amount $-31,957.82 | Running 
Balance $236,445.27
  - Date 2024-06-22 | Description Supplier settlement BILL-0001 | Amount $-9,900.72 | 
Running Balance $226,544.55
  - Date 2024-06-26 | Description Payroll PAYRUN-0001 | Amount $-34,079.88 | Running Balance
 $192,464.67

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D017 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
BANK STATEMENT
==============

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Date: 2024-06-30

Reference Box
-------------
Document ID: D017
Document Type: bank_statement
Period: June 2024

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-_M99
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $31,957.82

Statement Rows
--------------
Rows:
  - Date 2024-06-21 | Description Transfer in TRX-0001 | Amount $31,957.82 | Running Balance
 $31,957.82

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D017
```

## 5. Expected Journal Entries (ground truth)

_(no expected entries — packet is labeled inconsistent)_

## 6. Expected Final Balance Sheet (ground truth)

_Packet is labeled inconsistent — the expected balance sheet should be empty._

**Totals:** Assets = 0.00; Liabilities = 0.00; Equity = 0.00
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

### Q6 — Inconsistency validity (inconsistency packets only)
Is the labeled contradiction (codes: `performance_obligation_release_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [x] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes: Release evidence doesn't match the recognition schedule.

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
