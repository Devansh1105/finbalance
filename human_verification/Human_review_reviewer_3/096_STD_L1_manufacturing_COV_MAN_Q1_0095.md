# Verification Packet — COV_MAN_Q1_0095

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 1
- **Period type:** quarter
- **Period label:** Q4 FY 2024
- **Period start → end:** 2024-10-01 → 2024-12-31
- **Entity:** Granite Distribution
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `none`
- **Document count:** 7
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-10-01_

**Assets**
- Cash: 72,999.30
- Raw Materials Inventory: 58,194.73

**Liabilities**
- Accounts Payable: 19,303.04

**Equity**
- Share Capital: 111,890.99


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
Statement Date: 01/10/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 72,999.30
  - Section assets | Account Raw Materials Inventory | Amount GBP 58,194.73
  - Section liabilities | Account Accounts Payable | Amount GBP 19,303.04
  - Section equity | Account Share Capital | Amount GBP 111,890.99

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-10-21

```
SUPPLIER INVOICE
================

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Date: 21/10/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: Q4 FY 2024

Terms
-----
Due Date: 07/11/2024

Supplier Header
---------------
Supplier: Pace Office Mart
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 07/11/2024
Total: GBP 20,040.02

Supplier Bill Lines
-------------------
Lines:
  - Description Resin pellets | Quantity 338 | Unit Cost GBP 59.29 | Amount GBP 20,040.02

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2024-10-31

```
MATERIAL REQUISITION SLIP
=========================

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Date: 31/10/2024

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: Q4 FY 2024

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Resin pellets
Quantity Issued: 152
Issue Value: GBP 9,032.60
Warehouse: Plant Floor Store

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2024-10-31

```
PRODUCTION BATCH SHEET
======================

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Document Date: 31/10/2024

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: Q4 FY 2024

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Assembly Unit
Planned Units: 50
Material Value: GBP 9,032.60
Labor Value: GBP 0.00
Overhead Value: GBP 0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D005 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2024-12-12

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Date: 12/12/2024

Reference Box
-------------
Document ID: D005
Document Type: finished_goods_transfer_note
Period: Q4 FY 2024

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Assembly Unit
Units Completed: 29
Transfer Value: GBP 9,032.60

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D006 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-12

```
CUSTOMER INVOICE
================

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Date: 12/12/2024

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D006
Document Type: customer_invoice
Period: Q4 FY 2024
Contract Ref: FGT-0001

Terms
-----
Due Date: 31/12/2024

Parties
-------
Customer: Crescent Labs
Contract Ref: FGT-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 31/12/2024
Total: GBP 11,949.59

Line Items
----------
Items:
  - Description Assembly Unit | Amount GBP 11,949.59

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D007 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Date: 31/12/2024

Reference Box
-------------
Document ID: D007
Document Type: bank_statement
Period: Q4 FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0095
Statement Currency: GBP
Opening Balance: GBP 72,999.30
Closing Balance: GBP 72,999.30

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
| 1 | Raw Materials Inventory | Accounts Payable | 20,040.02 | D002 | 2024-10-21 | raw_material_purchase |
| 2 | Work In Process | Raw Materials Inventory | 9,032.60 | D003, D004, D002 | 2024-10-31 | material_issue |
| 3 | Finished Goods Inventory | Work In Process | 9,032.60 | D005, D004 | 2024-12-12 | finished_goods_transfer |
| 4 | Accounts Receivable | Sales Revenue | 11,949.59 | D006, D005 | 2024-12-12 | finished_goods_sale_sale |
| 5 | Cost of Goods Sold | Finished Goods Inventory | 9,032.60 | D006, D005 | 2024-12-12 | finished_goods_sale_cogs |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 72,999.30
- Raw Materials Inventory: 69,202.15
- Accounts Receivable: 11,949.59

**Liabilities**
- Accounts Payable: 39,343.06

**Equity**
- Share Capital: 111,890.99
- Retained Earnings: 2,916.99

**Totals:** Assets = 154,151.04; Liabilities = 39,343.06; Equity = 114,807.98
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
- Notes: Overhead absorption lumped in one line. Fine for this purpose.

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
