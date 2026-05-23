# Verification Packet — COV_WHO_Q1_0050

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 1
- **Period type:** quarter
- **Period label:** Q1 FY 2025-26
- **Period start → end:** 2025-04-01 → 2025-06-30
- **Entity:** Silverline Software
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `none`
- **Document count:** 8
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 90,536.60
- Inventory: 54,053.05
- Accounts Receivable: 5,240.61

**Liabilities**
- Accounts Payable: 16,235.98

**Equity**
- Owner's Equity: 133,594.28


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
Statement Date: 01/04/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 90,536.60
  - Section assets | Account Inventory | Amount GBP 54,053.05
  - Section assets | Account Accounts Receivable | Amount GBP 5,240.61
  - Section liabilities | Account Accounts Payable | Amount GBP 16,235.98
  - Section equity | Account Owner's Equity | Amount GBP 133,594.28

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2025-04-10

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Beacon Industrial Supply
Purchase Ref: PO-0001
Total Quantity: GBP 114.00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Service Bundle | Quantity 114 | Unit Cost GBP 38.80
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-12

```
SUPPLIER INVOICE
================

From
----
Silverline Software
75 Market Road, Mumbai
Date: 12/04/2025

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: Q1 FY 2025-26

Terms
-----
Due Date: 24/04/2025

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Goods Receipt Ref: GRN-0001
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 24/04/2025
Total: GBP 4,423.20

Supplier Bill Lines
-------------------
Lines:
  - Description Service Bundle | Quantity 114 | Unit Cost GBP 38.80 | Amount GBP 4,423.20

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D006 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-05-08

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0002
Customer: Crescent Labs
Shipment Ref: SHP-0002
Billed Amount: GBP 5,223.24
Cost Basis Amount: GBP 3,094.63
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0003 | Description Widget A | Quantity 44 | Unit Price GBP 118.71 | Unit Cost 
GBP 70.33 | Extended Cost GBP 3,094.63
```

### Document D007 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-08

```
CUSTOMER INVOICE
================

From
----
Silverline Software
75 Market Road, Mumbai
Document Date: 08/05/2025

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D007
Document Type: customer_invoice
Period: Q1 FY 2025-26
Shipment Ref: SHP-0002

Terms
-----
Due Date: 22/05/2025

Parties
-------
Customer: Crescent Labs
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 22/05/2025
Total: GBP 5,223.24

Line Items
----------
Items:
  - Description Widget A | Amount GBP 5,223.24

Shipment Link
-------------
Shipment Ref: SHP-0002

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-05-25

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Maple Ridge Trading
Shipment Ref: SHP-0001
Billed Amount: GBP 14,928.98
Cost Basis Amount: GBP 8,257.82
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Widget A | Quantity 62 | Unit Price GBP 240.79 | Unit Cost 
GBP 133.19 | Extended Cost GBP 8,257.82
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-25

```
CUSTOMER INVOICE
================

From
----
Silverline Software
75 Market Road, Mumbai
Date: 25/05/2025

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: Q1 FY 2025-26
Shipment Ref: SHP-0001

Terms
-----
Due Date: 14/06/2025

Parties
-------
Customer: Maple Ridge Trading
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 14/06/2025
Total: GBP 14,928.98

Line Items
----------
Items:
  - Description Widget A | Amount GBP 14,928.98

Shipment Link
-------------
Shipment Ref: SHP-0001

Footer
------
Internal document packet copy.
Page marker: D005
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
Silverline Software
75 Market Road, Mumbai
Document Date: 30/06/2025

Reference Box
-------------
Document ID: D008
Document Type: bank_statement
Period: Q1 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0050
Statement Currency: GBP
Opening Balance: GBP 90,536.60
Closing Balance: GBP 90,536.60

Statement Rows
--------------
Rows: None

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 4,423.20 | D002, D003 | 2025-04-12 | goods_receipt_purchase |
| 2 | Accounts Receivable | Sales Revenue | 14,928.98 | D004, D005 | 2025-05-25 | delivery_sale_sale |
| 3 | Cost of Goods Sold | Inventory | 8,257.82 | D004, D005 | 2025-05-25 | delivery_sale_cogs |
| 4 | Accounts Receivable | Sales Revenue | 5,223.24 | D006, D007 | 2025-05-08 | delivery_sale_sale |
| 5 | Cost of Goods Sold | Inventory | 3,094.63 | D006, D007 | 2025-05-08 | delivery_sale_cogs |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 90,536.60
- Inventory: 47,123.80
- Accounts Receivable: 25,392.83

**Liabilities**
- Accounts Payable: 20,659.18

**Equity**
- Owner's Equity: 133,594.28
- Retained Earnings: 8,799.77

**Totals:** Assets = 163,053.23; Liabilities = 20,659.18; Equity = 142,394.05
**Balanced (A = L + E):** True

---

## 7. Verification Form

_Fill in your judgement below. For each question, mark one box and add notes where applicable._

### Q1 — Document analogy to real paperwork
We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?
- [ ] Yes — analogous to what an accountant would receive
- [x] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes: Line item descriptions are a bit generic but still readable.

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
- Notes: Support ties to postings well enough.
