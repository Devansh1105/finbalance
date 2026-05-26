# Verification Packet — COV_WHO_Q2_0051

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 2
- **Period type:** quarter
- **Period label:** Q1 FY 2025-26
- **Period start → end:** 2025-04-01 → 2025-06-30
- **Entity:** Harbor Property Services
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 10
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 54,698.59
- Inventory: 30,343.00
- Accounts Receivable: 6,557.50
- Office Supplies: 1,760.79

**Liabilities**
- Accounts Payable: 15,225.35
- Accrued Expenses: 3,478.37

**Equity**
- Retained Earnings: 24,110.39
- Owner's Equity: 50,545.77


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
Statement Date: 2025-04-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $54,698.59
  - Section assets | Account Inventory | Amount $30,343.00
  - Section assets | Account Accounts Receivable | Amount $6,557.50
  - Section assets | Account Office Supplies | Amount $1,760.79
  - Section liabilities | Account Accounts Payable | Amount $15,225.35
  - Section liabilities | Account Accrued Expenses | Amount $3,478.37
  - Section equity | Account Retained Earnings | Amount $24,110.39
  - Section equity | Account Owner's Equity | Amount $50,545.77

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
Supplier: Golden State Finance
Purchase Ref: PO-0001
Total Quantity: $77.00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Premium Kit | Quantity 77 | Unit Cost $81.16
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
Harbor Property Services
220 Lake View Road, Bengaluru
Date: 2025-04-12

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: Q1 FY 2025-26

Terms
-----
Due Date: 2025-04-25

Supplier Header
---------------
Supplier: Golden State Finance
Goods Receipt Ref: GRN-0001
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 2025-04-25
Subtotal: $6,249.32
Tax Label: GST
Tax Rate: 7.00%
Tax Amount: $437.45
Total: $6,686.77

Supplier Bill Lines
-------------------
Lines:
  - Description Premium Kit | Quantity 77 | Unit Cost $81.16 | Amount $6,249.32

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-05-03

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Blue Finch Holdings
Shipment Ref: SHP-0001
Billed Amount: $2,914.57
Cost Basis Amount: $1,981.39
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Widget A | Quantity 18 | Unit Price $154.21 | Unit Cost 
$110.08 | Extended Cost $1,981.39
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-03

```
CUSTOMER INVOICE
================

From
----
Harbor Property Services
220 Lake View Road, Bengaluru
Date: 2025-05-03

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: Q1 FY 2025-26
Shipment Ref: SHP-0001

Terms
-----
Due Date: 2025-05-17

Parties
-------
Customer: Blue Finch Holdings
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-05-17
Subtotal: $2,775.78
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $138.79
Total: $2,914.57

Line Items
----------
Items:
  - Description Widget A | Amount $2,775.78

Shipment Link
-------------
Shipment Ref: SHP-0001

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D008 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-05-23

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0002
Customer: Metro Edge Partners
Shipment Ref: SHP-0002
Billed Amount: $8,289.05
Cost Basis Amount: $5,367.23
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0003 | Description Filter Pack | Quantity 35 | Unit Price $215.30 | Unit Cost 
$153.35 | Extended Cost $5,367.23
```

### Document D009 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-23

```
CUSTOMER INVOICE
================

From
----
Harbor Property Services
220 Lake View Road, Bengaluru
Date: 2025-05-23

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D009
Document Type: customer_invoice
Period: Q1 FY 2025-26
Shipment Ref: SHP-0002

Terms
-----
Due Date: 2025-06-08

Parties
-------
Customer: Metro Edge Partners
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-06-08
Subtotal: $7,535.50
Tax Label: GST
Tax Rate: 10.00%
Tax Amount: $753.55
Total: $8,289.05

Line Items
----------
Items:
  - Description Filter Pack | Amount $7,535.50

Shipment Link
-------------
Shipment Ref: SHP-0002

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-01

```
PAYMENT ADVICE
==============

From
----
Harbor Property Services
220 Lake View Road, Bengaluru
Document Date: 2025-06-01

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q1 FY 2025-26
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: $2,914.57
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-19

```
PAYMENT ADVICE
==============

From
----
Harbor Property Services
220 Lake View Road, Bengaluru
Date: 2025-06-19

To
--
Golden State Finance

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: Q1 FY 2025-26
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Golden State Finance
Amount: $6,686.77
Reference: SUP-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D010 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-06-30

```
BANK STATEMENT
==============

From
----
Harbor Property Services
220 Lake View Road, Bengaluru
Document Date: 2025-06-30

Reference Box
-------------
Document ID: D010
Document Type: bank_statement
Period: Q1 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0051
Statement Currency: USD
Opening Balance: $54,698.59
Closing Balance: $50,926.39

Statement Rows
--------------
Rows:
  - Date 2025-06-01 | Description Customer settlement INV-0001 | Amount $2,914.57 | Running 
Balance $57,613.16
  - Date 2025-06-19 | Description Supplier settlement SUP-0001 | Amount $-6,686.77 | Running
 Balance $50,926.39

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 6,249.32 | D002, D003 | 2025-04-12 | goods_receipt_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 437.45 | D002, D003 | 2025-04-12 | goods_receipt_purchase_tax |
| 3 | Accounts Receivable | Sales Revenue | 2,775.78 | D004, D005 | 2025-05-03 | delivery_sale_sale |
| 4 | Cost of Goods Sold | Inventory | 1,981.39 | D004, D005 | 2025-05-03 | delivery_sale_cogs |
| 5 | Accounts Receivable | Sales Tax Payable | 138.79 | D004, D005 | 2025-05-03 | delivery_sale_tax |
| 6 | Cash | Accounts Receivable | 2,914.57 | D006, D005 | 2025-06-01 | customer_payment |
| 7 | Accounts Payable | Cash | 6,686.77 | D007, D003 | 2025-06-19 | supplier_payment |
| 8 | Accounts Receivable | Sales Revenue | 7,535.50 | D008, D009 | 2025-05-23 | delivery_sale_sale |
| 9 | Cost of Goods Sold | Inventory | 5,367.23 | D008, D009 | 2025-05-23 | delivery_sale_cogs |
| 10 | Accounts Receivable | Sales Tax Payable | 753.55 | D008, D009 | 2025-05-23 | delivery_sale_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 50,926.39
- Inventory: 29,243.70
- Accounts Receivable: 14,846.55
- Office Supplies: 1,760.79
- Input Tax Receivable: 437.45

**Liabilities**
- Accounts Payable: 15,225.35
- Accrued Expenses: 3,478.37
- Sales Tax Payable: 892.34

**Equity**
- Retained Earnings: 27,073.05
- Owner's Equity: 50,545.77

**Totals:** Assets = 97,214.88; Liabilities = 19,596.06; Equity = 77,618.82
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
