# Verification Packet — COV_NEG_00_SSP_ALLOCATION_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** August 2024
- **Period start → end:** 2024-08-01 → 2024-08-31
- **Entity:** Northwind Builders
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `us_sales_tax`
- **Document count:** 17
- **Labeled as inconsistent:** True
- **Inconsistency codes:** ssp_allocation_mismatch
- **Inconsistency reasons:** ASC 606 allocation does not reconcile transaction price to standalone selling prices.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-08-01_

**Assets**
- Cash: 62,856.19
- Accounts Receivable: 14,253.72
- Prepaid Insurance: 2,833.29
- Equipment: 17,061.03
- Office Supplies: 2,643.39

**Liabilities**
- Accounts Payable: 7,657.67
- Accrued Expenses: 1,980.18
- Unearned Revenue: 34,488.06
- Loans Payable: 8,396.36

**Equity**
- Retained Earnings: 29,269.36
- Share Capital: 17,855.99


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-08-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/08/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 62,856.19
  - Section assets | Account Accounts Receivable | Amount GBP 14,253.72
  - Section assets | Account Prepaid Insurance | Amount GBP 2,833.29
  - Section assets | Account Equipment | Amount GBP 17,061.03
  - Section assets | Account Office Supplies | Amount GBP 2,643.39
  - Section liabilities | Account Accounts Payable | Amount GBP 7,657.67
  - Section liabilities | Account Accrued Expenses | Amount GBP 1,980.18
  - Section liabilities | Account Unearned Revenue | Amount GBP 34,488.06
  - Section liabilities | Account Loans Payable | Amount GBP 8,396.36
  - Section equity | Account Retained Earnings | Amount GBP 29,269.36
  - Section equity | Account Share Capital | Amount GBP 17,855.99

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-08-05

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Northwind Builders
75 Market Road, Mumbai
Document Date: 05/08/2024

To
--
Blue Finch Holdings
Customer account on file

Terms
-----
Contract Start: 05/08/2024

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: SOF-0001
Customer: Blue Finch Holdings
Plan Name: Enterprise License
Term Months: 3
Contract Start: 05/08/2024
Contract Value: GBP 86,194.25

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-05

```
CUSTOMER INVOICE
================

From
----
Northwind Builders
75 Market Road, Mumbai
Document Date: 05/08/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: August 2024
Contract Ref: SOF-0001

Terms
-----
Due Date: 23/08/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: SOF-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 23/08/2024
Subtotal: GBP 81,124.00
Tax Label: US Sales Tax
Tax Rate: 6.25%
Tax Amount: GBP 5,070.25
Total: GBP 86,194.25

Line Items
----------
Items:
  - Description Annual Growth Plan | Amount GBP 29,402.05
  - Description Service coverage under contract | Amount GBP 51,721.95

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D010 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-08-05

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Northwind Builders
75 Market Road, Mumbai
Document Date: 05/08/2024

To
--
Metro Edge Partners
Customer account on file

Terms
-----
Contract Start: 05/08/2024

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: ASC606-0001
Customer: Metro Edge Partners
Plan Name: Annual Growth Plan
Term Months: 12
Contract Start: 05/08/2024
Contract Value: GBP 404,255.31

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-05

```
CUSTOMER INVOICE
================

From
----
Northwind Builders
75 Market Road, Mumbai
Date: 05/08/2024

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: August 2024
Contract Ref: ASC606-0001

Terms
-----
Due Date: 23/08/2024

Parties
-------
Customer: Metro Edge Partners
Contract Ref: ASC606-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 23/08/2024
Total: GBP 404,255.31

Line Items
----------
Items:
  - Description Implementation invoice line | Amount GBP 60,638.30
  - Description Platform access invoice line | Amount GBP 343,617.01

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D012 — SSP Rate Card

- **Type:** `ssp_rate_card`
- **Role:** `support_doc`
- **Date:** 2024-08-05

```
SSP RATE CARD
=============

From
----
Northwind Builders
75 Market Road, Mumbai
Document Date: 05/08/2024

Reference Box
-------------
Document ID: D012
Document Type: ssp_rate_card
Period: August 2024

Rate Card
---------
Rate Card ID: SSP-0001
Contract Reference: ASC606-0001
Effective Date: 05/08/2024
Total SSP: GBP 477,782.01

Standalone Selling Prices
-------------------------
Obligations:
  - Obligation Implementation | Ssp Amount GBP 91,164.13
  - Obligation Platform access | Ssp Amount GBP 386,617.88

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-07

```
VENDOR INVOICE
==============

From
----
Northwind Builders
75 Market Road, Mumbai
Date: 07/08/2024

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: August 2024

Terms
-----
Due Date: 26/08/2024

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Utilities Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 26/08/2024
Subtotal: GBP 6,941.17
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: GBP 503.23
Total: GBP 7,444.40

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 2,163.92
  - Description Support fee | Amount GBP 4,777.25

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D013 — Implementation Acceptance Memo

- **Type:** `implementation_acceptance_memo`
- **Role:** `support_doc`
- **Date:** 2024-08-08

```
IMPLEMENTATION ACCEPTANCE MEMO
==============================

From
----
Northwind Builders
75 Market Road, Mumbai
Document Date: 08/08/2024

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D013
Document Type: implementation_acceptance_memo
Period: August 2024

Acceptance
----------
Memo ID: ACCEPT-0001
Contract Reference: ASC606-0001
Customer: Metro Edge Partners
Acceptance Date: 08/08/2024
Accepted Obligation: Implementation
Accepted Amount: GBP 77,134.72

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
- **Date:** 2024-08-10

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: GBP 24,750.34
Draw Amount: GBP 128,673.28
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 153,423.62
Note: Scheduled lender activity for the selected period.
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-08-22

```
PAYMENT ADVICE
==============

From
----
Northwind Builders
75 Market Road, Mumbai
Date: 22/08/2024

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: August 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: GBP 79,229.14
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
- **Date:** 2024-08-24

```
TRANSFER ADVICE
===============

From
----
Northwind Builders
75 Market Road, Mumbai
Date: 24/08/2024

Reference Box
-------------
Document ID: D015
Document Type: transfer_advice
Period: August 2024
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: GBP 147,536.01
Transfer Date: 24/08/2024
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
- **Date:** 2024-08-25

```
PAYMENT ADVICE
==============

From
----
Northwind Builders
75 Market Road, Mumbai
Date: 25/08/2024

To
--
Oakline Services

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: August 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: GBP 5,155.18
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-08-27

```
PAYROLL SUMMARY
===============

From
----
Northwind Builders
75 Market Road, Mumbai
Document Date: 27/08/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: August 2024
Headcount: 5
Gross Pay: GBP 21,278.91
Employer Tax: 2,071.67
Cash Outflow: GBP 23,350.58

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-08-31

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Northwind Builders
75 Market Road, Mumbai
Date: 31/08/2024

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: August 2024

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: August 2024
Opening Deferred: GBP 81,124.00
Added Deferred: GBP 0.00
Released This Period: 27,041.33
Ending Deferred: GBP 54,082.67

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D014 — Performance Obligation Schedule

- **Type:** `performance_obligation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-08-31

```
PERFORMANCE OBLIGATION SCHEDULE
===============================

From
----
Northwind Builders
75 Market Road, Mumbai
Document Date: 31/08/2024

Reference Box
-------------
Document ID: D014
Document Type: performance_obligation_schedule
Period: August 2024

Allocation Summary
------------------
Schedule ID: POB-0001
Contract Reference: ASC606-0001
Transaction Price: GBP 404,255.31
Total SSP: GBP 477,782.01
Allocation Total: GBP 401,586.26
Released This Period: 104,394.77
Ending Deferred: GBP 299,860.54

Performance Obligations
-----------------------
Obligations:
  - Obligation Implementation | Ssp Amount GBP 91,164.13 | Invoice Line Amount GBP 60,638.30
 | Allocated Transaction Price GBP 77,134.72 | Release Pattern On acceptance | Released This
 Period 77,134.72
  - Obligation Platform access | Ssp Amount GBP 386,617.88 | Invoice Line Amount GBP 
343,617.01 | Allocated Transaction Price GBP 327,120.59 | Release Pattern Ratable over 12 
months | Released This Period 27,260.05

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D016 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-08-31

```
BANK STATEMENT
==============

From
----
Northwind Builders
75 Market Road, Mumbai
Date: 31/08/2024

Reference Box
-------------
Document ID: D016
Document Type: bank_statement
Period: August 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: GBP
Opening Balance: GBP 62,856.19
Closing Balance: GBP 94,716.84

Statement Rows
--------------
Rows:
  - Date 10/08/2024 | Description Loan draw LOAN-0001 | Amount GBP 128,673.28 | Running 
Balance GBP 191,529.47
  - Date 22/08/2024 | Description Customer settlement INV-0001 | Amount GBP 79,229.14 | 
Running Balance GBP 270,758.61
  - Date 24/08/2024 | Description Transfer out TRX-0001 | Amount GBP -147,536.01 | Running 
Balance GBP 123,222.60
  - Date 25/08/2024 | Description Supplier settlement BILL-0001 | Amount GBP -5,155.18 | 
Running Balance GBP 118,067.42
  - Date 27/08/2024 | Description Payroll PAYRUN-0001 | Amount GBP -23,350.58 | Running 
Balance GBP 94,716.84

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
- **Date:** 2024-08-31

```
BANK STATEMENT
==============

From
----
Northwind Builders
75 Market Road, Mumbai
Date: 31/08/2024

Reference Box
-------------
Document ID: D017
Document Type: bank_statement
Period: August 2024

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-CH99
Statement Currency: GBP
Opening Balance: GBP 0.00
Closing Balance: GBP 147,536.01

Statement Rows
--------------
Rows:
  - Date 24/08/2024 | Description Transfer in TRX-0001 | Amount GBP 147,536.01 | Running 
Balance GBP 147,536.01

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
- Notes: Entries empty — SSP allocation issue confirmed.

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
- Notes: N/A.

### Q5 — Difficulty calibration
Is the difficulty level (section 1) appropriately calibrated for this packet? L1=trivial, L5=hardest.
- [x] Calibration feels right
- [ ] Too easy for this level
- [ ] Too hard for this level
- Notes:

### Q6 — Inconsistency validity (inconsistency packets only)
Is the labeled contradiction (codes: `ssp_allocation_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [x] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes: SSP split in entries doesn't tie to the allocation schedule. Contradiction present.

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes: Acceptable.
