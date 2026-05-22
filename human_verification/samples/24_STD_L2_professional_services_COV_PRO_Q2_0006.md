# Verification Packet — COV_PRO_Q2_0006

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 2
- **Period type:** quarter
- **Period label:** Q3 FY 2024-25
- **Period start → end:** 2024-10-01 → 2024-12-31
- **Entity:** Pioneer Distribution
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 11
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-10-01_

**Assets**
- Cash: 45,304.70
- Accounts Receivable: 2,571.36
- Prepaid Rent: 1,541.66
- Prepaid Insurance: 2,327.15
- Office Supplies: 640.46

**Liabilities**
- Accounts Payable: 1,178.61
- Accrued Expenses: 744.87

**Equity**
- Retained Earnings: 9,178.04
- Owner's Equity: 41,283.81


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-10-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-10-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $45,304.70
  - Section assets | Account Accounts Receivable | Amount $2,571.36
  - Section assets | Account Prepaid Rent | Amount $1,541.66
  - Section assets | Account Prepaid Insurance | Amount $2,327.15
  - Section assets | Account Office Supplies | Amount $640.46
  - Section liabilities | Account Accounts Payable | Amount $1,178.61
  - Section liabilities | Account Accrued Expenses | Amount $744.87
  - Section equity | Account Retained Earnings | Amount $9,178.04
  - Section equity | Account Owner's Equity | Amount $41,283.81

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-10-15

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Pioneer Distribution
75 Market Road, Mumbai
Date: 2024-10-15

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: Q3 FY 2024-25
Contract Ref: CTR-0001

Terms
-----
Due Date: 2024-11-07

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-11-07
Total: $8,715.54

Line Items
----------
Items:
  - Description Implementation work | Amount $2,335.58
  - Description Follow-up support | Amount $6,379.96

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D007 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2024-10-15

```
RETAINER AGREEMENT MEMO
=======================

From
----
Pioneer Distribution
75 Market Road, Mumbai
Document Date: 2024-10-15

Reference Box
-------------
Document ID: D007
Document Type: retainer_agreement_memo
Period: Q3 FY 2024-25
Reference: RET-CTR-0001

Approval / Context
------------------
Subject: Retainer engagement

Memo Summary
------------
Memo ID: RET-0001
Subject: Retainer engagement
Reference: RET-CTR-0001
Contract Months: 12
Total Contract Value: $47,731.17

Explanation
-----------
Narrative: Customer Maple Ridge Trading agreed to a service package spanning 12 months.

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D008 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-10-15

```
CUSTOMER INVOICE
================

From
----
Pioneer Distribution
75 Market Road, Mumbai
Document Date: 2024-10-15

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D008
Document Type: customer_invoice
Period: Q3 FY 2024-25
Contract Ref: CTR-0002

Terms
-----
Due Date: 2024-10-28

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2024-10-28
Total: $47,731.17

Line Items
----------
Items:
  - Description Annual Growth Plan | Amount $18,779.88
  - Description Service coverage under contract | Amount $28,951.29

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D009 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-10-18

```
CUSTOMER INVOICE
================

From
----
Pioneer Distribution
75 Market Road, Mumbai
Document Date: 2024-10-18

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D009
Document Type: customer_invoice
Period: Q3 FY 2024-25
Contract Ref: CTR-0003

Terms
-----
Due Date: 2024-10-28

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0003
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 2024-10-28
Total: $16,441.00

Line Items
----------
Items:
  - Description Support package | Amount $7,044.95
  - Description Follow-up support | Amount $9,396.05

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-10-23

```
VENDOR INVOICE
==============

From
----
Pioneer Distribution
75 Market Road, Mumbai
Document Date: 2024-10-23

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q3 FY 2024-25

Terms
-----
Due Date: 2024-11-04

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-11-04
Total: $7,840.93

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $2,847.81
  - Description Support fee | Amount $4,993.12

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-11-16

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Vertex Supply Co.
Total: $188.74
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $51.50
  - Description Travel Incidentals | Amount $137.24
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-04

```
PAYMENT ADVICE
==============

From
----
Pioneer Distribution
75 Market Road, Mumbai
Date: 2024-12-04

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q3 FY 2024-25
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Oak Harbor Foods
Amount: $8,715.54
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-08

```
PAYMENT ADVICE
==============

From
----
Pioneer Distribution
75 Market Road, Mumbai
Date: 2024-12-08

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q3 FY 2024-25
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: $7,840.93
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D010 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
MEMO
====

From
----
Pioneer Distribution
75 Market Road, Mumbai
Date: 2024-12-31

Reference Box
-------------
Document ID: D010
Document Type: memo
Period: Q3 FY 2024-25

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0001
Subject: Quarter-end packet routing note
Audience: Back Office

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D011 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Pioneer Distribution
75 Market Road, Mumbai
Date: 2024-12-31

Reference Box
-------------
Document ID: D011
Document Type: bank_statement
Period: Q3 FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0006
Statement Currency: USD
Opening Balance: $45,304.70
Closing Balance: $45,990.57

Statement Rows
--------------
Rows:
  - Date 2024-11-16 | Description Vertex Supply Co. receipt RCPT-0001 | Amount $-188.74 | 
Running Balance $45,115.96
  - Date 2024-12-04 | Description Customer settlement INV-0001 | Amount $8,715.54 | Running 
Balance $53,831.50
  - Date 2024-12-08 | Description Supplier settlement BILL-0001 | Amount $-7,840.93 | 
Running Balance $45,990.57

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D011
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 8,715.54 | D002 | 2024-10-15 | service_invoice |
| 2 | Office Supplies Expense | Accounts Payable | 7,840.93 | D003 | 2024-10-23 | vendor_bill |
| 3 | Travel Expense | Cash | 188.74 | D004 | 2024-11-16 | expense_receipt |
| 4 | Cash | Accounts Receivable | 8,715.54 | D005, D002 | 2024-12-04 | customer_payment |
| 5 | Accounts Payable | Cash | 7,840.93 | D006, D003 | 2024-12-08 | supplier_payment |
| 6 | Accounts Receivable | Unearned Revenue | 47,731.17 | D007, D008 | 2024-10-15 | retainer_invoice |
| 7 | Accounts Receivable | Service Revenue | 16,441.00 | D009 | 2024-10-18 | service_invoice |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 45,990.57
- Accounts Receivable: 66,743.53
- Prepaid Rent: 1,541.66
- Prepaid Insurance: 2,327.15
- Office Supplies: 640.46

**Liabilities**
- Accounts Payable: 1,178.61
- Accrued Expenses: 744.87
- Unearned Revenue: 47,731.17

**Equity**
- Retained Earnings: 26,304.91
- Owner's Equity: 41,283.81

**Totals:** Assets = 117,243.37; Liabilities = 49,654.65; Equity = 67,588.72
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
