# Verification Packet — COV_WHO_M1_0045

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 1
- **Period type:** month
- **Period label:** September 2024
- **Period start → end:** 2024-09-01 → 2024-09-30
- **Entity:** Harbor Clinic
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 6
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-09-01_

**Assets**
- Cash: 51,389.22
- Inventory: 39,612.97
- Accounts Receivable: 3,082.50

**Liabilities**
- Accounts Payable: 4,608.79

**Equity**
- Owner's Equity: 89,475.90


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-09-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-09-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $51,389.22
  - Section assets | Account Inventory | Amount $39,612.97
  - Section assets | Account Accounts Receivable | Amount $3,082.50
  - Section liabilities | Account Accounts Payable | Amount $4,608.79
  - Section equity | Account Owner's Equity | Amount $89,475.90

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2024-09-09

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Golden State Finance
Purchase Ref: PO-0001
Total Quantity: $118.00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Widget A | Quantity 118 | Unit Cost $42.88
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-11

```
SUPPLIER INVOICE
================

From
----
Harbor Clinic
18 Marina Avenue, Chennai
Document Date: 2024-09-11

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: September 2024

Terms
-----
Due Date: 2024-10-01

Supplier Header
---------------
Supplier: Golden State Finance
Goods Receipt Ref: GRN-0001
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 2024-10-01
Total: $5,059.84

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 118 | Unit Cost $42.88 | Amount $5,059.84

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2024-09-13

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Riverfront Group
Shipment Ref: SHP-0001
Billed Amount: $2,839.98
Cost Basis Amount: $2,017.58
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Premium Kit | Quantity 26 | Unit Price $109.23 | Unit Cost 
$77.60 | Extended Cost $2,017.58
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-13

```
CUSTOMER INVOICE
================

From
----
Harbor Clinic
18 Marina Avenue, Chennai
Document Date: 2024-09-13

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: September 2024
Shipment Ref: SHP-0001

Terms
-----
Due Date: 2024-09-23

Parties
-------
Customer: Riverfront Group
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-09-23
Total: $2,839.98

Line Items
----------
Items:
  - Description Premium Kit | Amount $2,839.98

Shipment Link
-------------
Shipment Ref: SHP-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D006 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-09-30

```
BANK STATEMENT
==============

From
----
Harbor Clinic
18 Marina Avenue, Chennai
Date: 2024-09-30

Reference Box
-------------
Document ID: D006
Document Type: bank_statement
Period: September 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0045
Statement Currency: USD
Opening Balance: $51,389.22
Closing Balance: $51,389.22

Statement Rows
--------------
Rows: None

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
| 1 | Inventory | Accounts Payable | 5,059.84 | D002, D003 | 2024-09-11 | goods_receipt_purchase |
| 2 | Accounts Receivable | Sales Revenue | 2,839.98 | D004, D005 | 2024-09-13 | delivery_sale_sale |
| 3 | Cost of Goods Sold | Inventory | 2,017.58 | D004, D005 | 2024-09-13 | delivery_sale_cogs |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 51,389.22
- Inventory: 42,655.23
- Accounts Receivable: 5,922.48

**Liabilities**
- Accounts Payable: 9,668.63

**Equity**
- Owner's Equity: 89,475.90
- Retained Earnings: 822.40

**Totals:** Assets = 99,966.93; Liabilities = 9,668.63; Equity = 90,298.30
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
