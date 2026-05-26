# Verification Packet — COV_MAN_M1_0090

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 1
- **Period type:** month
- **Period label:** July 2024
- **Period start → end:** 2024-07-01 → 2024-07-31
- **Entity:** Atlas Retail Group
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 7
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-07-01_

**Assets**
- Cash: 69,337.72
- Raw Materials Inventory: 25,374.83

**Liabilities**
- Accounts Payable: 13,821.53

**Equity**
- Share Capital: 80,891.02


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-07-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-07-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $69,337.72
  - Section assets | Account Raw Materials Inventory | Amount $25,374.83
  - Section liabilities | Account Accounts Payable | Amount $13,821.53
  - Section equity | Account Share Capital | Amount $80,891.02

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-06

```
SUPPLIER INVOICE
================

From
----
Atlas Retail Group
14 King Street, Pune
Date: 2024-07-06

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: July 2024

Terms
-----
Due Date: 2024-07-24

Supplier Header
---------------
Supplier: Oakline Services
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 2024-07-24
Total: $5,814.63

Supplier Bill Lines
-------------------
Lines:
  - Description Packing film | Quantity 207 | Unit Cost $28.09 | Amount $5,814.63

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2024-07-20

```
MATERIAL REQUISITION SLIP
=========================

From
----
Atlas Retail Group
14 King Street, Pune
Document Date: 2024-07-20

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: July 2024

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Packing film
Quantity Issued: 111
Issue Value: $3,119.81
Warehouse: Overflow Storage

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2024-07-20

```
PRODUCTION BATCH SHEET
======================

From
----
Atlas Retail Group
14 King Street, Pune
Date: 2024-07-20

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: July 2024

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 44
Material Value: $3,119.81
Labor Value: $0.00
Overhead Value: $0.00

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D006 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-22

```
CUSTOMER INVOICE
================

From
----
Atlas Retail Group
14 King Street, Pune
Document Date: 2024-07-22

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D006
Document Type: customer_invoice
Period: July 2024
Contract Ref: FGT-0001

Terms
-----
Due Date: 2024-08-15

Parties
-------
Customer: Aster Point Services
Contract Ref: FGT-0001
Currency: USD

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 2024-08-15
Total: $3,807.50

Line Items
----------
Items:
  - Description Retail Display | Amount $3,807.50

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D005 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2024-07-26

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Atlas Retail Group
14 King Street, Pune
Date: 2024-07-26

Reference Box
-------------
Document ID: D005
Document Type: finished_goods_transfer_note
Period: July 2024

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Retail Display
Units Completed: 30
Transfer Value: $3,119.81

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D007 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-07-31

```
BANK STATEMENT
==============

From
----
Atlas Retail Group
14 King Street, Pune
Date: 2024-07-31

Reference Box
-------------
Document ID: D007
Document Type: bank_statement
Period: July 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0090
Statement Currency: USD
Opening Balance: $69,337.72
Closing Balance: $69,337.72

Statement Rows
--------------
Rows: None

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
| 1 | Raw Materials Inventory | Accounts Payable | 5,814.63 | D002 | 2024-07-06 | raw_material_purchase |
| 2 | Work In Process | Raw Materials Inventory | 3,119.81 | D003, D004, D002 | 2024-07-20 | material_issue |
| 3 | Finished Goods Inventory | Work In Process | 3,119.81 | D005, D004 | 2024-07-26 | finished_goods_transfer |
| 4 | Accounts Receivable | Sales Revenue | 3,807.50 | D006, D005 | 2024-07-22 | finished_goods_sale_sale |
| 5 | Cost of Goods Sold | Finished Goods Inventory | 3,119.81 | D006, D005 | 2024-07-22 | finished_goods_sale_cogs |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 69,337.72
- Raw Materials Inventory: 28,069.65
- Accounts Receivable: 3,807.50

**Liabilities**
- Accounts Payable: 19,636.16

**Equity**
- Share Capital: 80,891.02
- Retained Earnings: 687.69

**Totals:** Assets = 101,214.87; Liabilities = 19,636.16; Equity = 81,578.71
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

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
