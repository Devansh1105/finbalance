# Verification Packet — COV_NEG_00_BANK_CLOSING_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 1
- **Period type:** month
- **Period label:** March 2025
- **Period start → end:** 2025-03-01 → 2025-03-31
- **Entity:** Silverline Builders
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 5
- **Labeled as inconsistent:** True
- **Inconsistency codes:** bank_closing_mismatch
- **Inconsistency reasons:** Bank statement closing balance does not reconcile with the listed movements.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-03-01_

**Assets**
- Cash: 20,952.95
- Accounts Receivable: 5,530.52

**Liabilities**
- Accounts Payable: 2,631.55

**Equity**
- Owner's Equity: 23,851.92


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-03-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-03-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $20,952.95
  - Section assets | Account Accounts Receivable | Amount $5,530.52
  - Section liabilities | Account Accounts Payable | Amount $2,631.55
  - Section equity | Account Owner's Equity | Amount $23,851.92

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-06

```
CUSTOMER INVOICE
================

From
----
Silverline Builders
220 Lake View Road, Bengaluru
Document Date: 2025-03-06

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: March 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-03-21

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-03-21
Total: $1,771.50

Line Items
----------
Items:
  - Description Review pack | Amount $487.22
  - Description Follow-up support | Amount $1,284.28

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-08

```
VENDOR INVOICE
==============

From
----
Silverline Builders
220 Lake View Road, Bengaluru
Document Date: 2025-03-08

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: March 2025

Terms
-----
Due Date: 2025-03-21

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-03-21
Total: $3,660.08

Bill Lines
----------
Lines:
  - Description Support package | Amount $949.82
  - Description Support fee | Amount $2,710.26

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-03-15

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Golden State Finance
Total: $39.78
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $7.97
  - Description Travel Incidentals | Amount $31.81
```

### Document D005 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Silverline Builders
220 Lake View Road, Bengaluru
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D005
Document Type: bank_statement
Period: March 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $20,952.95
Closing Balance: $18,409.53

Statement Rows
--------------
Rows:
  - Date 2025-03-15 | Description Golden State Finance receipt RCPT-0001 | Amount $-39.78 | 
Running Balance $20,913.17

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
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
Is the labeled contradiction (codes: `bank_closing_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [ ] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes:

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
