# Verification Packet — COV_PRO_Q1_0005

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 1
- **Period type:** quarter
- **Period label:** Q4 FY 2025-26
- **Period start → end:** 2025-01-01 → 2025-03-31
- **Entity:** Pioneer Manufacturing
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `none`
- **Document count:** 7
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 30,298.66
- Accounts Receivable: 2,004.54

**Liabilities**
- Accounts Payable: 963.88

**Equity**
- Owner's Equity: 31,339.32


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/01/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 30,298.66
  - Section assets | Account Accounts Receivable | Amount GBP 2,004.54
  - Section liabilities | Account Accounts Payable | Amount GBP 963.88
  - Section equity | Account Owner's Equity | Amount GBP 31,339.32

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-05

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Date: 05/01/2025

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: Q4 FY 2025-26
Contract Ref: CTR-0001

Terms
-----
Due Date: 27/01/2025

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 27/01/2025
Total: GBP 15,509.26

Line Items
----------
Items:
  - Description Review pack | Amount GBP 5,908.48
  - Description Follow-up support | Amount GBP 9,600.78

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-15

```
VENDOR INVOICE
==============

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Date: 15/01/2025

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q4 FY 2025-26

Terms
-----
Due Date: 30/01/2025

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 30/01/2025
Total: GBP 5,048.88

Bill Lines
----------
Lines:
  - Description Implementation work | Amount GBP 1,670.26
  - Description Support fee | Amount GBP 3,378.62

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D006 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-15

```
CUSTOMER INVOICE
================

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Document Date: 15/01/2025

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D006
Document Type: customer_invoice
Period: Q4 FY 2025-26
Contract Ref: CTR-0002

Terms
-----
Due Date: 31/01/2025

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0002
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 31/01/2025
Total: GBP 8,161.90

Line Items
----------
Items:
  - Description Support package | Amount GBP 2,734.50
  - Description Follow-up support | Amount GBP 5,427.40

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-02-10

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Oakline Services
Total: GBP 370.65
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount GBP 160.82
  - Description Travel Incidentals | Amount GBP 209.83
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-02-13

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Vertex Supply Co.
Total: GBP 364.99
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount GBP 105.25
  - Description Travel Incidentals | Amount GBP 259.74
```

### Document D007 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Date: 31/03/2025

Reference Box
-------------
Document ID: D007
Document Type: bank_statement
Period: Q4 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0005
Statement Currency: GBP
Opening Balance: GBP 30,298.66
Closing Balance: GBP 29,563.02

Statement Rows
--------------
Rows:
  - Date 10/02/2025 | Description Oakline Services receipt RCPT-0002 | Amount GBP -370.65 | 
Running Balance GBP 29,928.01
  - Date 13/02/2025 | Description Vertex Supply Co. receipt RCPT-0001 | Amount GBP -364.99 |
 Running Balance GBP 29,563.02

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D007
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 15,509.26 | D002 | 2025-01-05 | service_invoice |
| 2 | Office Supplies Expense | Accounts Payable | 5,048.88 | D003 | 2025-01-15 | vendor_bill |
| 3 | Travel Expense | Cash | 364.99 | D004 | 2025-02-13 | expense_receipt |
| 4 | Travel Expense | Cash | 370.65 | D005 | 2025-02-10 | expense_receipt |
| 5 | Accounts Receivable | Service Revenue | 8,161.90 | D006 | 2025-01-15 | service_invoice |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 29,563.02
- Accounts Receivable: 25,675.70

**Liabilities**
- Accounts Payable: 6,012.76

**Equity**
- Owner's Equity: 31,339.32
- Retained Earnings: 17,886.64

**Totals:** Assets = 55,238.72; Liabilities = 6,012.76; Equity = 49,225.96
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
- [ ] Yes — entries match what I would book
- [x] Mostly — minor account / amount issues (please describe)
- [ ] No — significant errors (missing entries, wrong entries, wrong amounts)
- Notes: Minor classification on one expense line — could go either way.

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

### Q7 — Overall verdict
- [ ] Acceptable as ground truth for benchmark evaluation
- [x] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes: Minor classification on vendor bill — line items read as services but coded to Office Supplies Expense.
