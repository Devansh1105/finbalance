# Verification Packet — COV_NEG_00_PAYMENT_ALLOCATION_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 3
- **Period type:** quarter
- **Period label:** Q1 FY 2025-26
- **Period start → end:** 2025-04-01 → 2025-06-30
- **Entity:** Cedar Software
- **Currency (display / functional):** USD / USD
- **Tax regime:** `vat`
- **Document count:** 21
- **Labeled as inconsistent:** True
- **Inconsistency codes:** payment_allocation_mismatch
- **Inconsistency reasons:** Payment advice amount does not reconcile with the listed invoice allocations.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 50,804.14
- Accounts Receivable: 4,636.34
- Prepaid Rent: 1,966.95
- Prepaid Insurance: 1,681.97
- Office Supplies: 495.58

**Liabilities**
- Accounts Payable: 2,613.05
- Accrued Expenses: 669.10
- Unearned Revenue: 1,189.91

**Equity**
- Retained Earnings: 3,034.44
- Owner's Equity: 52,078.48


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
  - Section assets | Account Cash | Amount $50,804.14
  - Section assets | Account Accounts Receivable | Amount $4,636.34
  - Section assets | Account Prepaid Rent | Amount $1,966.95
  - Section assets | Account Prepaid Insurance | Amount $1,681.97
  - Section assets | Account Office Supplies | Amount $495.58
  - Section liabilities | Account Accounts Payable | Amount $2,613.05
  - Section liabilities | Account Accrued Expenses | Amount $669.10
  - Section liabilities | Account Unearned Revenue | Amount $1,189.91
  - Section equity | Account Retained Earnings | Amount $3,034.44
  - Section equity | Account Owner's Equity | Amount $52,078.48

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-05

```
VENDOR INVOICE
==============

From
----
Cedar Software
14 King Street, Pune
Date: 2025-04-05

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q1 FY 2025-26

Terms
-----
Due Date: 2025-04-24

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-04-24
Subtotal: $11,153.61
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: $1,115.36
Total: $12,268.97

Bill Lines
----------
Lines:
  - Description Review pack | Amount $3,379.38
  - Description Support fee | Amount $7,774.23

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2025-04-05

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Beacon Industrial Supply
Property: Park Lane Residences
Service Start: 2025-04-05
Service End: 2025-07-04
Total: $8,219.84
Monthly Amount: $2,739.95

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D013 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-05

```
CUSTOMER INVOICE
================

From
----
Cedar Software
14 King Street, Pune
Date: 2025-04-05

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D013
Document Type: customer_invoice
Period: Q1 FY 2025-26
Contract Ref: CTR-0003

Terms
-----
Due Date: 2025-04-29

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 2025-04-29
Total: $7,912.65

Line Items
----------
Items:
  - Description Review pack | Amount $3,170.83
  - Description Milestone 1 work | Amount $4,741.82

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D019 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-04-05

```
CANCELLATION NOTE
=================

From
----
Cedar Software
14 King Street, Pune
Date: 2025-04-05

Reference Box
-------------
Document ID: D019
Document Type: cancellation_note
Period: Q1 FY 2025-26

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0003-OLD
Replacement Reference: INV-0003

Background
----------
Narrative: INV-0003-OLD is withdrawn and must not be posted. Use INV-0003 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-13

```
CUSTOMER INVOICE
================

From
----
Cedar Software
14 King Street, Pune
Date: 2025-04-13

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: Q1 FY 2025-26
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-05-06

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-05-06
Subtotal: $9,008.12
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: $1,801.62
Total: $10,809.74

Line Items
----------
Items:
  - Description Support package | Amount $3,438.68
  - Description Follow-up support | Amount $5,569.44

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D010 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2025-04-16

```
RETAINER AGREEMENT MEMO
=======================

From
----
Cedar Software
14 King Street, Pune
Document Date: 2025-04-16

Reference Box
-------------
Document ID: D010
Document Type: retainer_agreement_memo
Period: Q1 FY 2025-26
Reference: RET-CTR-0001

Approval / Context
------------------
Subject: Retainer engagement

Memo Summary
------------
Memo ID: RET-0001
Subject: Retainer engagement
Reference: RET-CTR-0001
Contract Months: 6
Total Contract Value: $20,001.24

Explanation
-----------
Narrative: Customer Oak Harbor Foods agreed to a service package spanning 6 months.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-16

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Cedar Software
14 King Street, Pune
Date: 2025-04-16

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: Q1 FY 2025-26
Contract Ref: CTR-0002

Terms
-----
Due Date: 2025-04-27

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-04-27
Subtotal: $17,778.88
Tax Label: VAT
Tax Rate: 12.50%
Tax Amount: $2,222.36
Total: $20,001.24

Line Items
----------
Items:
  - Description Annual Growth Plan | Amount $6,512.87
  - Description Service coverage under contract | Amount $11,266.01

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D014 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-16

```
CUSTOMER INVOICE
================

From
----
Cedar Software
14 King Street, Pune
Document Date: 2025-04-16

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D014
Document Type: customer_invoice
Period: Q1 FY 2025-26
Contract Ref: CTR-0004

Terms
-----
Due Date: 2025-05-09

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0004

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 2025-05-09
Total: $11,011.42

Line Items
----------
Items:
  - Description Implementation work | Amount $3,418.23
  - Description Milestone 2 work | Amount $7,593.19

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D020 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-04-16

```
CANCELLATION NOTE
=================

From
----
Cedar Software
14 King Street, Pune
Date: 2025-04-16

Reference Box
-------------
Document ID: D020
Document Type: cancellation_note
Period: Q1 FY 2025-26

Cancellation Summary
--------------------
Note Number: CNCL-0002
Withdrawn Reference: INV-0004-OLD
Replacement Reference: INV-0004

Background
----------
Narrative: INV-0004-OLD is withdrawn and must not be posted. Use INV-0004 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D015 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-04

```
CUSTOMER INVOICE
================

From
----
Cedar Software
14 King Street, Pune
Date: 2025-05-04

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D015
Document Type: customer_invoice
Period: Q1 FY 2025-26
Contract Ref: CTR-0005

Terms
-----
Due Date: 2025-05-15

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0005

Invoice Details
---------------
Invoice Number: INV-0005
Due Date: 2025-05-15
Total: $9,419.82

Line Items
----------
Items:
  - Description Review pack | Amount $2,296.31
  - Description Milestone 3 work | Amount $7,123.51

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-05-13

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Oakline Services
Total: $344.57
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $138.86
  - Description Travel Incidentals | Amount $205.71
```

### Document D017 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-05-28

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Pace Office Mart
Total: $249.62
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Office Supplies Expense | Amount $51.03
  - Description Office Supplies follow-up | Amount $198.59
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-09

```
PAYMENT ADVICE
==============

From
----
Cedar Software
14 King Street, Pune
Document Date: 2025-06-09

To
--
Riverfront Group

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q1 FY 2025-26
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: $10,809.74
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D016 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-13

```
PAYMENT ADVICE
==============

From
----
Cedar Software
14 King Street, Pune
Document Date: 2025-06-13

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D016
Document Type: payment_advice
Period: Q1 FY 2025-26
Reference: Multiple invoice allocation

Payment Details
---------------
Advice Number: PAY-0003
Counterparty: Metro Edge Partners
Amount: $23,986.29
Reference: Multiple invoice allocation
Payment Method: Wire
Payment For: Combined settlement against several invoices

Allocation Details
------------------
Allocations:
  - Reference INV-0003 | Allocated Amount $7,912.65 | Status Closed
  - Reference INV-0004 | Allocated Amount $11,011.42 | Status Closed
  - Reference INV-0005 | Allocated Amount $5,684.19 | Status Partially paid

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-06-19

```
PAYROLL SUMMARY
===============

From
----
Cedar Software
14 King Street, Pune
Date: 2025-06-19

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q1 FY 2025-26
Headcount: 4
Gross Pay: $13,695.39
Employer Tax: 1,888.28
Cash Outflow: $15,583.67

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-20

```
PAYMENT ADVICE
==============

From
----
Cedar Software
14 King Street, Pune
Date: 2025-06-20

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q1 FY 2025-26
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: $12,268.97
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-06-30

```
SERVICE PERIOD MEMO
===================

From
----
Cedar Software
14 King Street, Pune
Date: 2025-06-30

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: Q1 FY 2025-26
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: $2,739.95

Explanation
-----------
Narrative: One month of rent has expired and should be expensed this period.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D012 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-06-30

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Cedar Software
14 King Street, Pune
Document Date: 2025-06-30

Reference Box
-------------
Document ID: D012
Document Type: revenue_recognition_schedule
Period: Q1 FY 2025-26

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0002
Period: Q1 FY 2025-26
Opening Deferred: $17,778.88
Added Deferred: $0.00
Released This Period: 8,889.44
Ending Deferred: $8,889.44

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D018 — Reclassification Memo

- **Type:** `reclassification_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-06-30

```
RECLASSIFICATION MEMO
=====================

From
----
Cedar Software
14 King Street, Pune
Date: 2025-06-30

Reference Box
-------------
Document ID: D018
Document Type: reclassification_memo
Period: Q1 FY 2025-26

Correction Summary
------------------
Memo ID: RECLASS-0001
Original Reference: RCPT-0002
From Account: Office Supplies Expense
To Account: Travel Expense
Amount: $249.62

Explanation
-----------
Narrative: Review of the card packet showed the spend belonged in a different expense 
category.

Notes
-----
Approved during the period-end account review.

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D021 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-06-30

```
BANK STATEMENT
==============

From
----
Cedar Software
14 King Street, Pune
Date: 2025-06-30

Reference Box
-------------
Document ID: D021
Document Type: bank_statement
Period: Q1 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $50,804.14
Closing Balance: $49,555.47

Statement Rows
--------------
Rows:
  - Date 2025-04-05 | Description Rent prepayment PRE-0001 | Amount $-8,219.84 | Running 
Balance $42,584.30
  - Date 2025-05-13 | Description Oakline Services receipt RCPT-0001 | Amount $-344.57 | 
Running Balance $42,239.73
  - Date 2025-05-28 | Description Pace Office Mart receipt RCPT-0002 | Amount $-249.62 | 
Running Balance $41,990.11
  - Date 2025-06-09 | Description Customer settlement INV-0001 | Amount $10,809.74 | Running
 Balance $52,799.85
  - Date 2025-06-13 | Description Combined customer settlement PAY-0003 | Amount $24,608.26 
| Running Balance $77,408.11
  - Date 2025-06-19 | Description Payroll PAYRUN-0001 | Amount $-15,583.67 | Running Balance
 $61,824.44
  - Date 2025-06-20 | Description Supplier settlement BILL-0001 | Amount $-12,268.97 | 
Running Balance $49,555.47

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
Is the labeled contradiction (codes: `payment_allocation_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [x] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes: Advice amount doesn't match the allocations. Good catch.

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
