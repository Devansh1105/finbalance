# Verification Packet — COV_NEG_00_SCHEDULE_ROLLFORWARD_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 3
- **Period type:** quarter
- **Period label:** Q3 FY 2025-26
- **Period start → end:** 2025-10-01 → 2025-12-31
- **Entity:** Atlas Operations
- **Currency (display / functional):** USD / USD
- **Tax regime:** `vat`
- **Document count:** 21
- **Labeled as inconsistent:** True
- **Inconsistency codes:** schedule_rollforward_mismatch
- **Inconsistency reasons:** Schedule opening, additions, and releases do not roll forward to the stated ending balance.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-10-01_

**Assets**
- Cash: 33,663.02
- Accounts Receivable: 7,847.96
- Prepaid Rent: 3,260.19
- Prepaid Insurance: 1,993.94
- Office Supplies: 1,802.78

**Liabilities**
- Accounts Payable: 2,301.74
- Accrued Expenses: 1,754.43
- Unearned Revenue: 1,170.02

**Equity**
- Retained Earnings: 8,330.04
- Owner's Equity: 35,011.66


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
  - Section assets | Account Cash | Amount $33,663.02
  - Section assets | Account Accounts Receivable | Amount $7,847.96
  - Section assets | Account Prepaid Rent | Amount $3,260.19
  - Section assets | Account Prepaid Insurance | Amount $1,993.94
  - Section assets | Account Office Supplies | Amount $1,802.78
  - Section liabilities | Account Accounts Payable | Amount $2,301.74
  - Section liabilities | Account Accrued Expenses | Amount $1,754.43
  - Section liabilities | Account Unearned Revenue | Amount $1,170.02
  - Section equity | Account Retained Earnings | Amount $8,330.04
  - Section equity | Account Owner's Equity | Amount $35,011.66

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D013 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-06

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 2025-10-06

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D013
Document Type: customer_invoice
Period: Q3 FY 2025-26
Contract Ref: CTR-0003

Terms
-----
Due Date: 2025-10-19

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 2025-10-19
Total: $10,366.45

Line Items
----------
Items:
  - Description Implementation work | Amount $3,000.86
  - Description Milestone 1 work | Amount $7,365.59

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2025-10-07

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Beacon Industrial Supply
Property: Park Lane Residences
Service Start: 2025-10-07
Service End: 2026-01-06
Total: $8,137.14
Monthly Amount: $2,712.38

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D014 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-08

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 2025-10-08

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D014
Document Type: customer_invoice
Period: Q3 FY 2025-26
Contract Ref: CTR-0004

Terms
-----
Due Date: 2025-10-26

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0004

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 2025-10-26
Total: $6,039.03

Line Items
----------
Items:
  - Description Support package | Amount $1,433.06
  - Description Milestone 2 work | Amount $4,605.97

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D010 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2025-10-14

```
RETAINER AGREEMENT MEMO
=======================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 2025-10-14

Reference Box
-------------
Document ID: D010
Document Type: retainer_agreement_memo
Period: Q3 FY 2025-26
Reference: RET-CTR-0001

Approval / Context
------------------
Subject: Retainer engagement

Memo Summary
------------
Memo ID: RET-0001
Subject: Retainer engagement
Reference: RET-CTR-0001
Contract Months: 3
Total Contract Value: $22,759.74

Explanation
-----------
Narrative: Customer Aster Point Services agreed to a service package spanning 3 months.

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-14

```
CUSTOMER INVOICE
================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 2025-10-14

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: Q3 FY 2025-26
Contract Ref: CTR-0002

Terms
-----
Due Date: 2025-10-23

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-10-23
Subtotal: $20,690.67
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: $2,069.07
Total: $22,759.74

Line Items
----------
Items:
  - Description Team Support Plan | Amount $6,503.94
  - Description Service coverage under contract | Amount $14,186.73

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-23

```
VENDOR INVOICE
==============

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 2025-10-23

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q3 FY 2025-26

Terms
-----
Due Date: 2025-11-03

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-11-03
Subtotal: $2,522.13
Tax Label: VAT
Tax Rate: 12.50%
Tax Amount: $315.27
Total: $2,837.40

Bill Lines
----------
Lines:
  - Description Support package | Amount $621.80
  - Description Support fee | Amount $1,900.33

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-24

```
CUSTOMER INVOICE
================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 2025-10-24

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: Q3 FY 2025-26
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-11-03

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-11-03
Subtotal: $6,927.44
Tax Label: VAT
Tax Rate: 12.50%
Tax Amount: $865.93
Total: $7,793.37

Line Items
----------
Items:
  - Description Implementation work | Amount $2,631.95
  - Description Follow-up support | Amount $4,295.49

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D020 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-10-24

```
CANCELLATION NOTE
=================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 2025-10-24

Reference Box
-------------
Document ID: D020
Document Type: cancellation_note
Period: Q3 FY 2025-26

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
Page marker: D020
```

### Document D017 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-11-07

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Pace Office Mart
Total: $285.88
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Office Supplies Expense | Amount $128.05
  - Description Office Supplies follow-up | Amount $157.83
```

### Document D015 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-18

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 2025-11-18

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D015
Document Type: customer_invoice
Period: Q3 FY 2025-26
Contract Ref: CTR-0005

Terms
-----
Due Date: 2025-12-05

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0005

Invoice Details
---------------
Invoice Number: INV-0005
Due Date: 2025-12-05
Total: $10,049.79

Line Items
----------
Items:
  - Description Monthly retainer | Amount $3,301.73
  - Description Milestone 3 work | Amount $6,748.06

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-11-30

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Oakline Services
Total: $5.52
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $2.11
  - Description Travel Incidentals | Amount $3.41
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-12-01

```
PAYROLL SUMMARY
===============

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 2025-12-01

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q3 FY 2025-26
Headcount: 10
Gross Pay: $19,633.19
Employer Tax: 1,914.65
Cash Outflow: $21,547.84

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-10

```
PAYMENT ADVICE
==============

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 2025-12-10

To
--
Aster Point Services

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q3 FY 2025-26
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Aster Point Services
Amount: $7,793.37
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-14

```
PAYMENT ADVICE
==============

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 2025-12-14

To
--
Oakline Services

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q3 FY 2025-26
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: $2,837.40
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D016 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-19

```
PAYMENT ADVICE
==============

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 2025-12-19

To
--
Riverfront Group

Reference Box
-------------
Document ID: D016
Document Type: payment_advice
Period: Q3 FY 2025-26
Reference: Multiple invoice allocation

Payment Details
---------------
Advice Number: PAY-0003
Counterparty: Riverfront Group
Amount: $20,858.63
Reference: Multiple invoice allocation
Payment Method: Wire
Payment For: Combined settlement against several invoices

Allocation Details
------------------
Allocations:
  - Reference INV-0003 | Allocated Amount $10,366.45 | Status Closed
  - Reference INV-0004 | Allocated Amount $6,039.03 | Status Closed
  - Reference INV-0005 | Allocated Amount $4,453.15 | Status Partially paid

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
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
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 2025-12-31

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: Q3 FY 2025-26
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: $2,712.38

Explanation
-----------
Narrative: One month of rent has expired and should be expensed this period.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D012 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 2025-12-31

Reference Box
-------------
Document ID: D012
Document Type: revenue_recognition_schedule
Period: Q3 FY 2025-26

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0002
Period: Q3 FY 2025-26
Opening Deferred: $20,690.67
Added Deferred: $0.00
Released This Period: 20,690.67
Ending Deferred: $1,569.96

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D018 — Reclassification Memo

- **Type:** `reclassification_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
RECLASSIFICATION MEMO
=====================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 2025-12-31

Reference Box
-------------
Document ID: D018
Document Type: reclassification_memo
Period: Q3 FY 2025-26

Correction Summary
------------------
Memo ID: RECLASS-0001
Original Reference: RCPT-0002
From Account: Office Supplies Expense
To Account: Travel Expense
Amount: $285.88

Explanation
-----------
Narrative: Review of the card packet showed the spend belonged in a different expense 
category.

Notes
-----
Approved during the period-end account review.

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D019 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 2025-12-31

Reference Box
-------------
Document ID: D019
Document Type: memo
Period: Q3 FY 2025-26

Approval / Context
------------------
Subject: Annual leave policy reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Annual leave policy reminder
Audience: Finance Team

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
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
Atlas Operations
90 Hill Park, Hyderabad
Date: 2025-12-31

Reference Box
-------------
Document ID: D021
Document Type: bank_statement
Period: Q3 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $33,663.02
Closing Balance: $29,501.24

Statement Rows
--------------
Rows:
  - Date 2025-10-07 | Description Rent prepayment PRE-0001 | Amount $-8,137.14 | Running 
Balance $25,525.88
  - Date 2025-11-07 | Description Pace Office Mart receipt RCPT-0002 | Amount $-285.88 | 
Running Balance $25,240.00
  - Date 2025-11-30 | Description Oakline Services receipt RCPT-0001 | Amount $-5.52 | 
Running Balance $25,234.48
  - Date 2025-12-01 | Description Payroll PAYRUN-0001 | Amount $-21,547.84 | Running Balance
 $3,686.64
  - Date 2025-12-10 | Description Customer settlement INV-0001 | Amount $7,793.37 | Running 
Balance $11,480.01
  - Date 2025-12-14 | Description Supplier settlement BILL-0001 | Amount $-2,837.40 | 
Running Balance $8,642.61
  - Date 2025-12-19 | Description Combined customer settlement PAY-0003 | Amount $20,858.63 
| Running Balance $29,501.24

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
- Notes: No entries expected on a flagged packet — correct.

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
Is the labeled contradiction (codes: `schedule_rollforward_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [x] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes: Schedule doesn't roll opening+adds-releases to the ending.

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
