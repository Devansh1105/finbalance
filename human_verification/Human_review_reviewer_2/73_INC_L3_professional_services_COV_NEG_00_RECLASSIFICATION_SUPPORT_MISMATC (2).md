# Verification Packet — COV_NEG_00_RECLASSIFICATION_SUPPORT_MISMATC

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 3
- **Period type:** quarter
- **Period label:** Q2 FY 2025
- **Period start → end:** 2025-04-01 → 2025-06-30
- **Entity:** Northwind Software
- **Currency (display / functional):** USD / USD
- **Tax regime:** `sales_tax`
- **Document count:** 19
- **Labeled as inconsistent:** True
- **Inconsistency codes:** reclassification_support_mismatch
- **Inconsistency reasons:** Correction memo details do not reconcile with the linked original posting support.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 48,632.38
- Accounts Receivable: 7,764.08
- Prepaid Rent: 3,862.91
- Prepaid Insurance: 1,428.53
- Office Supplies: 470.46

**Liabilities**
- Accounts Payable: 3,421.55
- Accrued Expenses: 683.40
- Unearned Revenue: 4,903.48

**Equity**
- Retained Earnings: 4,151.93
- Owner's Equity: 48,998.00


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
  - Section assets | Account Cash | Amount $48,632.38
  - Section assets | Account Accounts Receivable | Amount $7,764.08
  - Section assets | Account Prepaid Rent | Amount $3,862.91
  - Section assets | Account Prepaid Insurance | Amount $1,428.53
  - Section assets | Account Office Supplies | Amount $470.46
  - Section liabilities | Account Accounts Payable | Amount $3,421.55
  - Section liabilities | Account Accrued Expenses | Amount $683.40
  - Section liabilities | Account Unearned Revenue | Amount $4,903.48
  - Section equity | Account Retained Earnings | Amount $4,151.93
  - Section equity | Account Owner's Equity | Amount $48,998.00

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2025-04-03

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Meridian Support LLP
Property: Cedar Plaza
Service Start: 2025-04-03
Service End: 2025-07-02
Total: $9,197.36
Monthly Amount: $3,065.79

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D013 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-06

```
CUSTOMER INVOICE
================

From
----
Northwind Software
90 Hill Park, Hyderabad
Document Date: 2025-04-06

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D013
Document Type: customer_invoice
Period: Q2 FY 2025
Contract Ref: CTR-0003

Terms
-----
Due Date: 2025-04-19

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 2025-04-19
Total: $3,250.90

Line Items
----------
Items:
  - Description Consulting sprint | Amount $1,022.93
  - Description Milestone 1 work | Amount $2,227.97

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-07

```
VENDOR INVOICE
==============

From
----
Northwind Software
90 Hill Park, Hyderabad
Date: 2025-04-07

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q2 FY 2025

Terms
-----
Due Date: 2025-04-24

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-04-24
Subtotal: $9,523.25
Tax Label: Sales Tax
Tax Rate: 5.00%
Tax Amount: $476.16
Total: $9,999.41

Bill Lines
----------
Lines:
  - Description Implementation work | Amount $3,753.40
  - Description Support fee | Amount $5,769.85

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D010 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2025-04-07

```
RETAINER AGREEMENT MEMO
=======================

From
----
Northwind Software
90 Hill Park, Hyderabad
Document Date: 2025-04-07

Reference Box
-------------
Document ID: D010
Document Type: retainer_agreement_memo
Period: Q2 FY 2025
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
Total Contract Value: $78,312.86

Explanation
-----------
Narrative: Customer Blue Finch Holdings agreed to a service package spanning 6 months.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-07

```
CUSTOMER INVOICE
================

From
----
Northwind Software
90 Hill Park, Hyderabad
Date: 2025-04-07

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: Q2 FY 2025
Contract Ref: CTR-0002

Terms
-----
Due Date: 2025-04-16

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-04-16
Subtotal: $72,344.44
Tax Label: Sales Tax
Tax Rate: 8.25%
Tax Amount: $5,968.42
Total: $78,312.86

Line Items
----------
Items:
  - Description Enterprise License | Amount $23,520.75
  - Description Service coverage under contract | Amount $48,823.69

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D014 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-18

```
CUSTOMER INVOICE
================

From
----
Northwind Software
90 Hill Park, Hyderabad
Date: 2025-04-18

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D014
Document Type: customer_invoice
Period: Q2 FY 2025
Contract Ref: CTR-0004

Terms
-----
Due Date: 2025-04-30

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0004

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 2025-04-30
Total: $3,229.90

Line Items
----------
Items:
  - Description Review pack | Amount $1,328.15
  - Description Milestone 2 work | Amount $1,901.75

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-26

```
CUSTOMER INVOICE
================

From
----
Northwind Software
90 Hill Park, Hyderabad
Document Date: 2025-04-26

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: Q2 FY 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-05-07

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-05-07
Subtotal: $8,942.61
Tax Label: Sales Tax
Tax Rate: 9.50%
Tax Amount: $849.55
Total: $9,792.16

Line Items
----------
Items:
  - Description Consulting sprint | Amount $3,359.17
  - Description Follow-up support | Amount $5,583.44

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-05-01

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Beacon Industrial Supply
Total: $301.92
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $99.38
  - Description Travel Incidentals | Amount $202.54
```

### Document D017 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-05-06

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Meridian Support LLP
Total: $343.08
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Office Supplies Expense | Amount $126.17
  - Description Office Supplies follow-up | Amount $216.91
```

### Document D015 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-22

```
CUSTOMER INVOICE
================

From
----
Northwind Software
90 Hill Park, Hyderabad
Date: 2025-05-22

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D015
Document Type: customer_invoice
Period: Q2 FY 2025
Contract Ref: CTR-0005

Terms
-----
Due Date: 2025-06-13

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0005

Invoice Details
---------------
Invoice Number: INV-0005
Due Date: 2025-06-13
Total: $9,969.52

Line Items
----------
Items:
  - Description Consulting sprint | Amount $3,152.98
  - Description Milestone 3 work | Amount $6,816.54

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-05

```
PAYMENT ADVICE
==============

From
----
Northwind Software
90 Hill Park, Hyderabad
Date: 2025-06-05

To
--
Crescent Labs

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q2 FY 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Crescent Labs
Amount: $9,792.16
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D016 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-07

```
PAYMENT ADVICE
==============

From
----
Northwind Software
90 Hill Park, Hyderabad
Document Date: 2025-06-07

To
--
Crescent Labs

Reference Box
-------------
Document ID: D016
Document Type: payment_advice
Period: Q2 FY 2025
Reference: Multiple invoice allocation

Payment Details
---------------
Advice Number: PAY-0003
Counterparty: Crescent Labs
Amount: $11,393.80
Reference: Multiple invoice allocation
Payment Method: Bank transfer
Payment For: Combined settlement against several invoices

Allocation Details
------------------
Allocations:
  - Reference INV-0003 | Allocated Amount $3,250.90 | Status Closed
  - Reference INV-0004 | Allocated Amount $3,229.90 | Status Closed
  - Reference INV-0005 | Allocated Amount $4,913.00 | Status Partially paid

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-14

```
PAYMENT ADVICE
==============

From
----
Northwind Software
90 Hill Park, Hyderabad
Date: 2025-06-14

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q2 FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: $9,999.41
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-06-15

```
PAYROLL SUMMARY
===============

From
----
Northwind Software
90 Hill Park, Hyderabad
Date: 2025-06-15

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q2 FY 2025
Headcount: 4
Gross Pay: $14,292.45
Employer Tax: 1,656.69
Cash Outflow: $15,949.14

Footer
------
Internal document packet copy.
Page marker: D007
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
Northwind Software
90 Hill Park, Hyderabad
Document Date: 2025-06-30

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: Q2 FY 2025
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: $3,065.79

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
- **Date:** 2025-06-30

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Northwind Software
90 Hill Park, Hyderabad
Date: 2025-06-30

Reference Box
-------------
Document ID: D012
Document Type: revenue_recognition_schedule
Period: Q2 FY 2025

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0002
Period: Q2 FY 2025
Opening Deferred: $72,344.44
Added Deferred: $0.00
Released This Period: 36,172.22
Ending Deferred: $36,172.22

Footer
------
Internal document packet copy.
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
Northwind Software
90 Hill Park, Hyderabad
Date: 2025-06-30

Reference Box
-------------
Document ID: D018
Document Type: reclassification_memo
Period: Q2 FY 2025

Correction Summary
------------------
Memo ID: RECLASS-0001
Original Reference: RCPT-0002
From Account: Office Supplies Expense
To Account: Travel Expense
Amount: $853.72

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

### Document D019 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-06-30

```
BANK STATEMENT
==============

From
----
Northwind Software
90 Hill Park, Hyderabad
Document Date: 2025-06-30

Reference Box
-------------
Document ID: D019
Document Type: bank_statement
Period: Q2 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-MATC
Statement Currency: USD
Opening Balance: $48,632.38
Closing Balance: $34,027.43

Statement Rows
--------------
Rows:
  - Date 2025-04-03 | Description Rent prepayment PRE-0001 | Amount $-9,197.36 | Running 
Balance $39,435.02
  - Date 2025-05-01 | Description Beacon Industrial Supply receipt RCPT-0001 | Amount 
$-301.92 | Running Balance $39,133.10
  - Date 2025-05-06 | Description Meridian Support LLP receipt RCPT-0002 | Amount $-343.08 |
 Running Balance $38,790.02
  - Date 2025-06-05 | Description Customer settlement INV-0001 | Amount $9,792.16 | Running 
Balance $48,582.18
  - Date 2025-06-07 | Description Combined customer settlement PAY-0003 | Amount $11,393.80 
| Running Balance $59,975.98
  - Date 2025-06-14 | Description Supplier settlement BILL-0001 | Amount $-9,999.41 | 
Running Balance $49,976.57
  - Date 2025-06-15 | Description Payroll PAYRUN-0001 | Amount $-15,949.14 | Running Balance
 $34,027.43

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
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
Is the labeled contradiction (codes: `reclassification_support_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [ ] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes:

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
