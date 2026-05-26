# Verification Packet — COV_PRO_M1_0000

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 1
- **Period type:** month
- **Period label:** December 2024
- **Period start → end:** 2024-12-01 → 2024-12-31
- **Entity:** Cedar Distribution
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 6
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-12-01_

**Assets**
- Cash: 20,459.88
- Accounts Receivable: 4,526.83

**Liabilities**
- Accounts Payable: 985.81

**Equity**
- Owner's Equity: 24,000.90


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-12-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-12-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $20,459.88
  - Section assets | Account Accounts Receivable | Amount $4,526.83
  - Section liabilities | Account Accounts Payable | Amount $985.81
  - Section equity | Account Owner's Equity | Amount $24,000.90

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-05

```
CUSTOMER INVOICE
================

From
----
Cedar Distribution
220 Lake View Road, Bengaluru
Date: 2024-12-05

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: December 2024
Contract Ref: CTR-0001

Terms
-----
Due Date: 2024-12-15

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-12-15
Total: $4,530.84

Line Items
----------
Items:
  - Description Support package | Amount $1,131.39
  - Description Follow-up support | Amount $3,399.45

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D005 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-12-05

```
CANCELLATION NOTE
=================

From
----
Cedar Distribution
220 Lake View Road, Bengaluru
Date: 2024-12-05

Reference Box
-------------
Document ID: D005
Document Type: cancellation_note
Period: December 2024

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
Page marker: D005
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-08

```
VENDOR INVOICE
==============

From
----
Cedar Distribution
220 Lake View Road, Bengaluru
Document Date: 2024-12-08

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: December 2024

Terms
-----
Due Date: 2024-12-18

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-12-18
Total: $2,391.35

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $962.18
  - Description Support fee | Amount $1,429.17

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-12-12

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Meridian Support LLP
Total: $74.90
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $19.01
  - Description Travel Incidentals | Amount $55.89
```

### Document D006 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Cedar Distribution
220 Lake View Road, Bengaluru
Date: 2024-12-31

Reference Box
-------------
Document ID: D006
Document Type: bank_statement
Period: December 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0000
Statement Currency: USD
Opening Balance: $20,459.88
Closing Balance: $20,384.98

Statement Rows
--------------
Rows:
  - Date 2024-12-12 | Description Meridian Support LLP receipt RCPT-0001 | Amount $-74.90 | 
Running Balance $20,384.98

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D006
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 4,530.84 | D002 | 2024-12-05 | service_invoice |
| 2 | Office Supplies Expense | Accounts Payable | 2,391.35 | D003 | 2024-12-08 | vendor_bill |
| 3 | Travel Expense | Cash | 74.90 | D004 | 2024-12-12 | expense_receipt |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 20,384.98
- Accounts Receivable: 9,057.67

**Liabilities**
- Accounts Payable: 3,377.16

**Equity**
- Owner's Equity: 24,000.90
- Retained Earnings: 2,064.59

**Totals:** Assets = 29,442.65; Liabilities = 3,377.16; Equity = 26,065.49
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
