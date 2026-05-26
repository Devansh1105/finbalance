# Verification Packet — COV_NEG_00_INPUT_TAX_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 2
- **Period type:** month
- **Period label:** June 2025
- **Period start → end:** 2025-06-01 → 2025-06-30
- **Entity:** Granite Manufacturing
- **Currency (display / functional):** USD / USD
- **Tax regime:** `sales_tax`
- **Document count:** 9
- **Labeled as inconsistent:** True
- **Inconsistency codes:** input_tax_mismatch
- **Inconsistency reasons:** Recoverable input tax fields do not reconcile with the underlying bill amounts.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-06-01_

**Assets**
- Cash: 36,357.20
- Accounts Receivable: 6,249.01
- Prepaid Rent: 2,808.63
- Office Supplies: 1,007.39

**Liabilities**
- Accounts Payable: 2,460.32
- Accrued Expenses: 2,036.26

**Equity**
- Retained Earnings: 6,847.61
- Owner's Equity: 35,078.04


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
  - Section assets | Account Cash | Amount $36,357.20
  - Section assets | Account Accounts Receivable | Amount $6,249.01
  - Section assets | Account Prepaid Rent | Amount $2,808.63
  - Section assets | Account Office Supplies | Amount $1,007.39
  - Section liabilities | Account Accounts Payable | Amount $2,460.32
  - Section liabilities | Account Accrued Expenses | Amount $2,036.26
  - Section equity | Account Retained Earnings | Amount $6,847.61
  - Section equity | Account Owner's Equity | Amount $35,078.04

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-06-01

```
MEMO
====

From
----
Granite Manufacturing
14 King Street, Pune
Date: 2025-06-01

Reference Box
-------------
Document ID: D008
Document Type: memo
Period: June 2025

Approval / Context
------------------
Subject: Annual leave policy reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Annual leave policy reminder
Audience: Operations Team

Memo Body
---------
Narrative: Please route scanned paperwork to the shared archive after the period binder is 
complete.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D007 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-02

```
CUSTOMER INVOICE
================

From
----
Granite Manufacturing
14 King Street, Pune
Date: 2025-06-02

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D007
Document Type: customer_invoice
Period: June 2025
Contract Ref: CTR-0002

Terms
-----
Due Date: 2025-06-20

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-06-20
Subtotal: $3,630.34
Tax Label: Sales Tax
Tax Rate: 8.25%
Tax Amount: $299.50
Total: $3,929.84

Line Items
----------
Items:
  - Description Support package | Amount $1,203.40
  - Description Follow-up support | Amount $2,426.94

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-03

```
CUSTOMER INVOICE
================

From
----
Granite Manufacturing
14 King Street, Pune
Date: 2025-06-03

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: June 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-06-13

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-06-13
Subtotal: $2,442.94
Tax Label: Sales Tax
Tax Rate: 8.25%
Tax Amount: $201.54
Total: $2,644.48

Line Items
----------
Items:
  - Description Support package | Amount $784.19
  - Description Follow-up support | Amount $1,658.75

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-04

```
VENDOR INVOICE
==============

From
----
Granite Manufacturing
14 King Street, Pune
Date: 2025-06-04

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: June 2025

Terms
-----
Due Date: 2025-06-16

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-06-16
Subtotal: $2,036.10
Tax Label: Sales Tax
Tax Rate: 7.25%
Tax Amount: $0.01
Total: $2,183.72

Bill Lines
----------
Lines:
  - Description Support package | Amount $811.92
  - Description Support fee | Amount $1,224.18

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-06-14

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Meridian Support LLP
Total: $60.44
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $26.21
  - Description Travel Incidentals | Amount $34.23
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-24

```
PAYMENT ADVICE
==============

From
----
Granite Manufacturing
14 King Street, Pune
Date: 2025-06-24

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: June 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: $2,183.72
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
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
Granite Manufacturing
14 King Street, Pune
Document Date: 2025-06-25

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: June 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: $2,644.48
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D009 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-06-30

```
BANK STATEMENT
==============

From
----
Granite Manufacturing
14 King Street, Pune
Date: 2025-06-30

Reference Box
-------------
Document ID: D009
Document Type: bank_statement
Period: June 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $36,357.20
Closing Balance: $36,757.52

Statement Rows
--------------
Rows:
  - Date 2025-06-14 | Description Meridian Support LLP receipt RCPT-0001 | Amount $-60.44 | 
Running Balance $36,296.76
  - Date 2025-06-24 | Description Supplier settlement BILL-0001 | Amount $-2,183.72 | 
Running Balance $34,113.04
  - Date 2025-06-25 | Description Customer settlement INV-0001 | Amount $2,644.48 | Running 
Balance $36,757.52

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D009
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
Is the labeled contradiction (codes: `input_tax_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [x] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes: Recoverable input tax doesn't tie to the bill.

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
