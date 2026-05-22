# Verification Packet — COV_NEG_00_TAX_RATE_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 2
- **Period type:** month
- **Period label:** June 2025
- **Period start → end:** 2025-06-01 → 2025-06-30
- **Entity:** Silverline Advisors
- **Currency (display / functional):** USD / USD
- **Tax regime:** `sales_tax`
- **Document count:** 8
- **Labeled as inconsistent:** True
- **Inconsistency codes:** tax_rate_mismatch
- **Inconsistency reasons:** Shown indirect tax amount does not reconcile with the shown tax rate and basis.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-06-01_

**Assets**
- Cash: 32,976.65
- Accounts Receivable: 3,434.50
- Prepaid Rent: 3,159.68
- Office Supplies: 1,514.83

**Liabilities**
- Accounts Payable: 1,345.17
- Accrued Expenses: 1,402.23

**Equity**
- Retained Earnings: 4,877.94
- Owner's Equity: 33,460.32


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-06-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-06-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $32,976.65
  - Section assets | Account Accounts Receivable | Amount $3,434.50
  - Section assets | Account Prepaid Rent | Amount $3,159.68
  - Section assets | Account Office Supplies | Amount $1,514.83
  - Section liabilities | Account Accounts Payable | Amount $1,345.17
  - Section liabilities | Account Accrued Expenses | Amount $1,402.23
  - Section equity | Account Retained Earnings | Amount $4,877.94
  - Section equity | Account Owner's Equity | Amount $33,460.32

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-06

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Silverline Advisors
90 Hill Park, Hyderabad
Date: 2025-06-06

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: June 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-06-29

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-06-29
Subtotal: $5,797.06
Tax Label: Sales Tax
Tax Rate: 11.46%
Tax Amount: $550.72
Total: $6,347.78

Line Items
----------
Items:
  - Description Implementation work | Amount $2,278.19
  - Description Follow-up support | Amount $3,518.87

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-08

```
VENDOR INVOICE
==============

From
----
Silverline Advisors
90 Hill Park, Hyderabad
Document Date: 2025-06-08

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: June 2025

Terms
-----
Due Date: 2025-06-24

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-06-24
Subtotal: $2,219.39
Tax Label: Sales Tax
Tax Rate: 9.50%
Tax Amount: $210.84
Total: $2,430.23

Bill Lines
----------
Lines:
  - Description Implementation work | Amount $640.42
  - Description Support fee | Amount $1,578.97

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D007 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-08

```
CUSTOMER INVOICE
================

From
----
Silverline Advisors
90 Hill Park, Hyderabad
Document Date: 2025-06-08

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D007
Document Type: customer_invoice
Period: June 2025
Contract Ref: CTR-0002

Terms
-----
Due Date: 2025-06-30

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-06-30
Subtotal: $7,182.77
Tax Label: Sales Tax
Tax Rate: 9.50%
Tax Amount: $682.36
Total: $7,865.13

Line Items
----------
Items:
  - Description Monthly retainer | Amount $2,252.74
  - Description Follow-up support | Amount $4,930.03

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-06-19

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Prime Utility Desk
Total: $247.81
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $75.92
  - Description Travel Incidentals | Amount $171.89
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-25

```
PAYMENT ADVICE
==============

From
----
Silverline Advisors
90 Hill Park, Hyderabad
Document Date: 2025-06-25

To
--
Crescent Labs

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: June 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Crescent Labs
Amount: $6,347.78
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-27

```
PAYMENT ADVICE
==============

From
----
Silverline Advisors
90 Hill Park, Hyderabad
Document Date: 2025-06-27

To
--
Oakline Services

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: June 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: $2,430.23
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D008 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-06-30

```
BANK STATEMENT
==============

From
----
Silverline Advisors
90 Hill Park, Hyderabad
Date: 2025-06-30

Reference Box
-------------
Document ID: D008
Document Type: bank_statement
Period: June 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $32,976.65
Closing Balance: $36,646.39

Statement Rows
--------------
Rows:
  - Date 2025-06-19 | Description Prime Utility Desk receipt RCPT-0001 | Amount $-247.81 | 
Running Balance $32,728.84
  - Date 2025-06-25 | Description Customer settlement INV-0001 | Amount $6,347.78 | Running 
Balance $39,076.62
  - Date 2025-06-27 | Description Supplier settlement BILL-0001 | Amount $-2,430.23 | 
Running Balance $36,646.39

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D008
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

### Q6 — Inconsistency validity (inconsistency packets only)
Is the labeled contradiction (codes: `tax_rate_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [ ] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes:

### Q7 — Overall verdict
- [ ] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
