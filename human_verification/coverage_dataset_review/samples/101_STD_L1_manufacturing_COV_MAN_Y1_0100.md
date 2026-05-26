# Verification Packet — COV_MAN_Y1_0100

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 1
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Willow Clinic
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `none`
- **Document count:** 10
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 345,830.79
- Raw Materials Inventory: 86,254.67

**Liabilities**
- Accounts Payable: 35,478.89

**Equity**
- Share Capital: 396,606.57


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-04-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/04/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 345.830,79
  - Section assets | Account Raw Materials Inventory | Amount EUR 86.254,67
  - Section liabilities | Account Accounts Payable | Amount EUR 35.478,89
  - Section equity | Account Share Capital | Amount EUR 396.606,57

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D007 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-19

```
SUPPLIER INVOICE
================

From
----
Willow Clinic
18 Marina Avenue, Chennai
Date: 19/05/2024

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D007
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 04/06/2024

Supplier Header
---------------
Supplier: Meridian Support LLP
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: MAT-0002
Due Date: 04/06/2024
Total: EUR 63.108,72

Supplier Bill Lines
-------------------
Lines:
  - Description Control boards | Quantity 324 | Unit Cost EUR 194,78 | Amount EUR 63.108,72

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-23

```
SUPPLIER INVOICE
================

From
----
Willow Clinic
18 Marina Avenue, Chennai
Document Date: 23/05/2024

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 15/06/2024

Supplier Header
---------------
Supplier: Meridian Support LLP
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: MAT-0003
Due Date: 15/06/2024
Total: EUR 30.029,40

Supplier Bill Lines
-------------------
Lines:
  - Description Control boards | Quantity 135 | Unit Cost EUR 222,44 | Amount EUR 30.029,40

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-18

```
SUPPLIER INVOICE
================

From
----
Willow Clinic
18 Marina Avenue, Chennai
Document Date: 18/06/2024

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 01/07/2024

Supplier Header
---------------
Supplier: Oakline Services
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 01/07/2024
Total: EUR 38.359,31

Supplier Bill Lines
-------------------
Lines:
  - Description Steel sheets | Quantity 281 | Unit Cost EUR 136,51 | Amount EUR 38.359,31

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2024-11-26

```
MATERIAL REQUISITION SLIP
=========================

From
----
Willow Clinic
18 Marina Avenue, Chennai
Date: 26/11/2024

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: FY 2024-25

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Steel sheets
Quantity Issued: 215
Issue Value: EUR 29.428,33
Warehouse: Plant Floor Store

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2024-11-26

```
PRODUCTION BATCH SHEET
======================

From
----
Willow Clinic
18 Marina Avenue, Chennai
Date: 26/11/2024

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: FY 2024-25

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Panel Kit
Planned Units: 37
Material Value: EUR 29.428,33
Labor Value: EUR 0,00
Overhead Value: EUR 0,00

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D006 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-04

```
CUSTOMER INVOICE
================

From
----
Willow Clinic
18 Marina Avenue, Chennai
Document Date: 04/12/2024

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D006
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: FGT-0001

Terms
-----
Due Date: 28/12/2024

Parties
-------
Customer: Crescent Labs
Contract Ref: FGT-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 28/12/2024
Total: EUR 41.805,38

Line Items
----------
Items:
  - Description Panel Kit | Amount EUR 41.805,38

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D005 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2024-12-21

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Willow Clinic
18 Marina Avenue, Chennai
Document Date: 21/12/2024

Reference Box
-------------
Document ID: D005
Document Type: finished_goods_transfer_note
Period: FY 2024-25

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Panel Kit
Units Completed: 63
Transfer Value: EUR 29.428,33

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D009 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
VENDOR STATEMENT
================

From
----
Willow Clinic
18 Marina Avenue, Chennai
Document Date: 31/03/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: vendor_statement
Period: FY 2024-25

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Oakline Services
Closing Balance: EUR 38.359,31

Statement Lines
---------------
Lines:
  - Reference MAT-0001 | Document Type Open invoice | Amount EUR 38.359,31 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D010 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Willow Clinic
18 Marina Avenue, Chennai
Date: 31/03/2025

Reference Box
-------------
Document ID: D010
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0100
Statement Currency: EUR
Opening Balance: EUR 345.830,79
Closing Balance: EUR 345.830,79

Statement Rows
--------------
Rows: None

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D010
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Raw Materials Inventory | Accounts Payable | 38,359.31 | D002 | 2024-06-18 | raw_material_purchase |
| 2 | Work In Process | Raw Materials Inventory | 29,428.33 | D003, D004, D002 | 2024-11-26 | material_issue |
| 3 | Finished Goods Inventory | Work In Process | 29,428.33 | D005, D004 | 2024-12-21 | finished_goods_transfer |
| 4 | Accounts Receivable | Sales Revenue | 41,805.38 | D006, D005 | 2024-12-04 | finished_goods_sale_sale |
| 5 | Cost of Goods Sold | Finished Goods Inventory | 29,428.33 | D006, D005 | 2024-12-04 | finished_goods_sale_cogs |
| 6 | Raw Materials Inventory | Accounts Payable | 63,108.72 | D007 | 2024-05-19 | raw_material_purchase |
| 7 | Raw Materials Inventory | Accounts Payable | 30,029.40 | D008 | 2024-05-23 | raw_material_purchase |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 345,830.79
- Raw Materials Inventory: 188,323.77
- Accounts Receivable: 41,805.38

**Liabilities**
- Accounts Payable: 166,976.32

**Equity**
- Share Capital: 396,606.57
- Retained Earnings: 12,377.05

**Totals:** Assets = 575,959.94; Liabilities = 166,976.32; Equity = 408,983.62
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
