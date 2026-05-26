# Verification Packet — COV_NEG_00_TRANSFER_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 4
- **Period type:** quarter
- **Period label:** Q4 FY 2025
- **Period start → end:** 2025-10-01 → 2025-12-31
- **Entity:** Summit Property Services
- **Currency (display / functional):** USD / USD
- **Tax regime:** `vat`
- **Document count:** 21
- **Labeled as inconsistent:** True
- **Inconsistency codes:** transfer_mismatch
- **Inconsistency reasons:** Inter-bank transfer support does not reconcile between the advice and bank evidence.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-10-01_

**Assets**
- Cash: 168,252.34
- Accounts Receivable: 42,023.73
- Prepaid Insurance: 12,109.84
- Equipment: 59,951.39
- Office Supplies: 5,116.50

**Liabilities**
- Accounts Payable: 20,794.75
- Accrued Expenses: 11,780.72
- Unearned Revenue: 79,062.95
- Loans Payable: 14,890.37

**Equity**
- Retained Earnings: 60,673.50
- Share Capital: 100,251.51


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
Statement Date: 2025-10-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $168,252.34
  - Section assets | Account Accounts Receivable | Amount $42,023.73
  - Section assets | Account Prepaid Insurance | Amount $12,109.84
  - Section assets | Account Equipment | Amount $59,951.39
  - Section assets | Account Office Supplies | Amount $5,116.50
  - Section liabilities | Account Accounts Payable | Amount $20,794.75
  - Section liabilities | Account Accrued Expenses | Amount $11,780.72
  - Section liabilities | Account Unearned Revenue | Amount $79,062.95
  - Section liabilities | Account Loans Payable | Amount $14,890.37
  - Section equity | Account Retained Earnings | Amount $60,673.50
  - Section equity | Account Share Capital | Amount $100,251.51

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-10-05

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Summit Property Services
14 King Street, Pune
Date: 2025-10-05

To
--
Oak Harbor Foods
Customer account on file

Terms
-----
Contract Start: 2025-10-05

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Oak Harbor Foods
Plan Name: Annual Growth Plan
Term Months: 3
Contract Start: 2025-10-05
Contract Value: $292,542.15

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-05

```
CUSTOMER INVOICE
================

From
----
Summit Property Services
14 King Street, Pune
Document Date: 2025-10-05

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: Q4 FY 2025
Contract Ref: SOF-0001

Terms
-----
Due Date: 2025-10-17

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: SOF-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-10-17
Subtotal: $265,947.41
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: $26,594.74
Total: $292,542.15

Line Items
----------
Items:
  - Description Business Suite | Amount $117,521.47
  - Description Service coverage under contract | Amount $148,425.94

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D018 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-10-05

```
CANCELLATION NOTE
=================

From
----
Summit Property Services
14 King Street, Pune
Date: 2025-10-05

Reference Box
-------------
Document ID: D018
Document Type: cancellation_note
Period: Q4 FY 2025

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0001-OLD
Replacement Reference: INV-0001

Background
----------
Narrative: INV-0001-OLD is withdrawn and must not be posted. Use INV-0001 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-09

```
VENDOR INVOICE
==============

From
----
Summit Property Services
14 King Street, Pune
Document Date: 2025-10-09

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-10-20

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Utilities Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-10-20
Subtotal: $38,585.59
Tax Label: VAT
Tax Rate: 12.50%
Tax Amount: $4,823.20
Total: $43,408.79

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount $9,726.50
  - Description Support fee | Amount $28,859.09

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D010 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-10-17

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Summit Property Services
14 King Street, Pune
Document Date: 2025-10-17

To
--
Riverfront Group
Customer account on file

Terms
-----
Contract Start: 2025-10-17

Approval / Context
------------------
Plan Name: Business Suite

Order Summary
-------------
Form Number: ASC606-0001
Customer: Riverfront Group
Plan Name: Business Suite
Term Months: 12
Contract Start: 2025-10-17
Contract Value: $988,891.18

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-17

```
CUSTOMER INVOICE
================

From
----
Summit Property Services
14 King Street, Pune
Date: 2025-10-17

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: Q4 FY 2025
Contract Ref: ASC606-0001

Terms
-----
Due Date: 2025-10-28

Parties
-------
Customer: Riverfront Group
Contract Ref: ASC606-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-10-28
Total: $988,891.18

Line Items
----------
Items:
  - Description Implementation invoice line | Amount $148,333.68
  - Description Platform access invoice line | Amount $840,557.50

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D012 — SSP Rate Card

- **Type:** `ssp_rate_card`
- **Role:** `support_doc`
- **Date:** 2025-10-17

```
SSP RATE CARD
=============

From
----
Summit Property Services
14 King Street, Pune
Document Date: 2025-10-17

Reference Box
-------------
Document ID: D012
Document Type: ssp_rate_card
Period: Q4 FY 2025

Rate Card
---------
Rate Card ID: SSP-0001
Contract Reference: ASC606-0001
Effective Date: 2025-10-17
Total SSP: $1,112,864.24

Standalone Selling Prices
-------------------------
Obligations:
  - Obligation Implementation | Ssp Amount $300,995.16
  - Obligation Platform access | Ssp Amount $811,869.08

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D013 — Implementation Acceptance Memo

- **Type:** `implementation_acceptance_memo`
- **Role:** `support_doc`
- **Date:** 2025-10-26

```
IMPLEMENTATION ACCEPTANCE MEMO
==============================

From
----
Summit Property Services
14 King Street, Pune
Document Date: 2025-10-26

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D013
Document Type: implementation_acceptance_memo
Period: Q4 FY 2025

Acceptance
----------
Memo ID: ACCEPT-0001
Contract Reference: ASC606-0001
Customer: Riverfront Group
Acceptance Date: 2025-10-26
Accepted Obligation: Implementation
Accepted Amount: $267,464.30

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
- **Date:** 2025-12-01

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: $69,685.66
Draw Amount: $402,922.30
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $472,607.96
Note: Scheduled lender activity for the selected period.
```

### Document D015 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-08

```
TRANSFER ADVICE
===============

From
----
Summit Property Services
14 King Street, Pune
Date: 2025-12-08

Reference Box
-------------
Document ID: D015
Document Type: transfer_advice
Period: Q4 FY 2025
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: $264,070.31
Transfer Date: 2025-12-08
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-12

```
PAYMENT ADVICE
==============

From
----
Summit Property Services
14 King Street, Pune
Date: 2025-12-12

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q4 FY 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Oak Harbor Foods
Amount: $192,445.09
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
- **Date:** 2025-12-14

```
PAYMENT ADVICE
==============

From
----
Summit Property Services
14 King Street, Pune
Date: 2025-12-14

To
--
Golden State Finance

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: Q4 FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Golden State Finance
Amount: $38,123.46
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-12-15

```
PAYROLL SUMMARY
===============

From
----
Summit Property Services
14 King Street, Pune
Date: 2025-12-15

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q4 FY 2025
Headcount: 5
Gross Pay: $108,455.29
Employer Tax: 11,287.17
Cash Outflow: $119,742.46

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D017 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `posting_doc`
- **Date:** 2025-12-19

```
CREDIT MEMO
===========

From
----
Summit Property Services
14 King Street, Pune
Date: 2025-12-19

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D017
Document Type: credit_memo
Period: Q4 FY 2025
Reference: INV-0001

Approval / Context
------------------
Reason: Pricing adjustment

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Oak Harbor Foods
Currency: USD
Reference: INV-0001
Reason: Pricing adjustment
Amount: $20,412.84

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Summit Property Services
14 King Street, Pune
Date: 2025-12-31

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
Opening Deferred: $265,947.41
Added Deferred: $0.00
Released This Period: 265,947.41
Ending Deferred: $0.00

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D014 — Performance Obligation Schedule

- **Type:** `performance_obligation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
PERFORMANCE OBLIGATION SCHEDULE
===============================

From
----
Summit Property Services
14 King Street, Pune
Document Date: 2025-12-31

Reference Box
-------------
Document ID: D014
Document Type: performance_obligation_schedule
Period: Q4 FY 2025

Allocation Summary
------------------
Schedule ID: POB-0001
Contract Reference: ASC606-0001
Transaction Price: $988,891.18
Total SSP: $1,112,864.24
Allocation Total: $988,891.18
Released This Period: 447,821.02
Ending Deferred: $541,070.16

Performance Obligations
-----------------------
Obligations:
  - Obligation Implementation | Ssp Amount $300,995.16 | Invoice Line Amount $148,333.68 | 
Allocated Transaction Price $267,464.30 | Release Pattern On acceptance | Released This 
Period 267,464.30
  - Obligation Platform access | Ssp Amount $811,869.08 | Invoice Line Amount $840,557.50 | 
Allocated Transaction Price $721,426.88 | Release Pattern Ratable over 12 months | Released 
This Period 180,356.72

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D016 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Summit Property Services
14 King Street, Pune
Date: 2025-12-31

Reference Box
-------------
Document ID: D016
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
Recognized Amount: $4,789.48

Explanation
-----------
Narrative: Accrue unpaid utilities expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D019 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
VENDOR STATEMENT
================

From
----
Summit Property Services
14 King Street, Pune
Document Date: 2025-12-31

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D019
Document Type: vendor_statement
Period: Q4 FY 2025

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Golden State Finance
Closing Balance: $5,285.33

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount $5,285.33 | Status Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Summit Property Services
14 King Street, Pune
Date: 2025-12-31

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: Q4 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $168,252.34
Closing Balance: $341,082.75

Statement Rows
--------------
Rows:
  - Date 2025-12-01 | Description Loan draw LOAN-0001 | Amount $402,922.30 | Running Balance
 $571,174.64
  - Date 2025-12-08 | Description Transfer out TRX-0001 | Amount $-264,671.06 | Running 
Balance $306,503.58
  - Date 2025-12-12 | Description Customer settlement INV-0001 | Amount $192,445.09 | 
Running Balance $498,948.67
  - Date 2025-12-14 | Description Supplier settlement BILL-0001 | Amount $-38,123.46 | 
Running Balance $460,825.21
  - Date 2025-12-15 | Description Payroll PAYRUN-0001 | Amount $-119,742.46 | Running 
Balance $341,082.75

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D021 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Summit Property Services
14 King Street, Pune
Date: 2025-12-31

Reference Box
-------------
Document ID: D021
Document Type: bank_statement
Period: Q4 FY 2025

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-CH99
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $264,671.06

Statement Rows
--------------
Rows:
  - Date 2025-12-08 | Description Transfer in TRX-0001 | Amount $264,671.06 | Running 
Balance $264,671.06

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D021
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
Is the labeled contradiction (codes: `transfer_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [x] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes: Transfer advice and bank evidence disagree.

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
