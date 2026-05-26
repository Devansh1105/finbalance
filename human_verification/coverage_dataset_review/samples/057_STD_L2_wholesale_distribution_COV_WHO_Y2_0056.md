# Verification Packet — COV_WHO_Y2_0056

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 2
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Granite Operations
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 16
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 153,630.83
- Inventory: 129,463.82
- Accounts Receivable: 33,637.55
- Office Supplies: 5,747.94

**Liabilities**
- Accounts Payable: 38,965.89
- Accrued Expenses: 9,273.51

**Equity**
- Retained Earnings: 48,576.32
- Owner's Equity: 225,664.42


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
  - Section assets | Account Cash | Amount GBP 153,630.83
  - Section assets | Account Inventory | Amount GBP 129,463.82
  - Section assets | Account Accounts Receivable | Amount GBP 33,637.55
  - Section assets | Account Office Supplies | Amount GBP 5,747.94
  - Section liabilities | Account Accounts Payable | Amount GBP 38,965.89
  - Section liabilities | Account Accrued Expenses | Amount GBP 9,273.51
  - Section equity | Account Retained Earnings | Amount GBP 48,576.32
  - Section equity | Account Owner's Equity | Amount GBP 225,664.42

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2024-04-24

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Meridian Support LLP
Purchase Ref: PO-0001
Total Quantity: GBP 135.00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Filter Pack | Quantity 135 | Unit Cost GBP 212.63
```

### Document D012 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2024-04-24

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0003
Supplier: Pace Office Mart
Purchase Ref: PO-0003
Total Quantity: GBP 131.00

Received Items
--------------
Items:
  - Sku SKU-0005 | Description Premium Kit | Quantity 131 | Unit Cost GBP 170.52
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-26

```
SUPPLIER INVOICE
================

From
----
Granite Operations
14 King Street, Pune
Date: 26/04/2024

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 09/05/2024

Supplier Header
---------------
Supplier: Meridian Support LLP
Goods Receipt Ref: GRN-0001
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 09/05/2024
Subtotal: GBP 28,705.05
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 5,741.01
Total: GBP 34,446.06

Supplier Bill Lines
-------------------
Lines:
  - Description Filter Pack | Quantity 135 | Unit Cost GBP 212.63 | Amount GBP 28,705.05

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D013 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-26

```
SUPPLIER INVOICE
================

From
----
Granite Operations
14 King Street, Pune
Date: 26/04/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D013
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 16/05/2024

Supplier Header
---------------
Supplier: Pace Office Mart
Goods Receipt Ref: GRN-0003
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: SUP-0003
Due Date: 16/05/2024
Subtotal: GBP 22,338.12
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 4,467.62
Total: GBP 26,805.74

Supplier Bill Lines
-------------------
Lines:
  - Description Premium Kit | Quantity 131 | Unit Cost GBP 170.52 | Amount GBP 22,338.12

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D014 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-04-26

```
SECONDARY COPY
==============

From
----
Granite Operations
14 King Street, Pune
Date: 26/04/2024

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D014
Document Type: secondary_copy
Period: FY 2024-25

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: SUP-0003
Counterparty: Pace Office Mart
Total: GBP 26,805.74
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D010 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2024-05-29

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0002
Supplier: Pace Office Mart
Purchase Ref: PO-0002
Total Quantity: GBP 62.00

Received Items
--------------
Items:
  - Sku SKU-0004 | Description Service Bundle | Quantity 62 | Unit Cost GBP 213.44
```

### Document D011 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-31

```
SUPPLIER INVOICE
================

From
----
Granite Operations
14 King Street, Pune
Date: 31/05/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 11/06/2024

Supplier Header
---------------
Supplier: Pace Office Mart
Goods Receipt Ref: GRN-0002
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: SUP-0002
Due Date: 11/06/2024
Subtotal: GBP 13,233.28
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: GBP 1,323.33
Total: GBP 14,556.61

Supplier Bill Lines
-------------------
Lines:
  - Description Service Bundle | Quantity 62 | Unit Cost GBP 213.44 | Amount GBP 13,233.28

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2024-09-07

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Maple Ridge Trading
Shipment Ref: SHP-0001
Billed Amount: GBP 16,475.03
Cost Basis Amount: GBP 8,592.64
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Service Bundle | Quantity 26 | Unit Price GBP 576.05 | Unit 
Cost GBP 330.49 | Extended Cost GBP 8,592.64
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-07

```
CUSTOMER INVOICE
================

From
----
Granite Operations
14 King Street, Pune
Date: 07/09/2024

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: FY 2024-25
Shipment Ref: SHP-0001

Terms
-----
Due Date: 19/09/2024

Parties
-------
Customer: Maple Ridge Trading
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 19/09/2024
Subtotal: GBP 14,977.30
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: GBP 1,497.73
Total: GBP 16,475.03

Line Items
----------
Items:
  - Description Service Bundle | Amount GBP 14,977.30

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
- **Date:** 2024-11-08

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0002
Customer: Aster Point Services
Shipment Ref: SHP-0002
Billed Amount: GBP 19,180.73
Cost Basis Amount: GBP 10,779.15
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0003 | Description Filter Pack | Quantity 21 | Unit Price GBP 761.14 | Unit Cost
 GBP 513.29 | Extended Cost GBP 10,779.15
```

### Document D009 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-08

```
CUSTOMER INVOICE
================

From
----
Granite Operations
14 King Street, Pune
Document Date: 08/11/2024

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D009
Document Type: customer_invoice
Period: FY 2024-25
Shipment Ref: SHP-0002

Terms
-----
Due Date: 20/11/2024

Parties
-------
Customer: Aster Point Services
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 20/11/2024
Subtotal: GBP 15,983.94
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 3,196.79
Total: GBP 19,180.73

Line Items
----------
Items:
  - Description Filter Pack | Amount GBP 15,983.94

Shipment Link
-------------
Shipment Ref: SHP-0002

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-29

```
PAYMENT ADVICE
==============

From
----
Granite Operations
14 King Street, Pune
Date: 29/12/2024

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2024-25
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: GBP 34,446.06
Reference: SUP-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
PAYMENT ADVICE
==============

From
----
Granite Operations
14 King Street, Pune
Date: 31/12/2024

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2024-25
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Maple Ridge Trading
Amount: GBP 16,475.03
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D015 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Granite Operations
14 King Street, Pune
Date: 31/03/2025

Reference Box
-------------
Document ID: D015
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Document retention reminder
Audience: Finance Team

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D016 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Granite Operations
14 King Street, Pune
Date: 31/03/2025

Reference Box
-------------
Document ID: D016
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0056
Statement Currency: GBP
Opening Balance: GBP 153,630.83
Closing Balance: GBP 135,659.80

Statement Rows
--------------
Rows:
  - Date 29/12/2024 | Description Supplier settlement SUP-0001 | Amount GBP -34,446.06 | 
Running Balance GBP 119,184.77
  - Date 31/12/2024 | Description Customer settlement INV-0001 | Amount GBP 16,475.03 | 
Running Balance GBP 135,659.80

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D016
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 28,705.05 | D002, D003 | 2024-04-26 | goods_receipt_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 5,741.01 | D002, D003 | 2024-04-26 | goods_receipt_purchase_tax |
| 3 | Accounts Receivable | Sales Revenue | 14,977.30 | D004, D005 | 2024-09-07 | delivery_sale_sale |
| 4 | Cost of Goods Sold | Inventory | 8,592.64 | D004, D005 | 2024-09-07 | delivery_sale_cogs |
| 5 | Accounts Receivable | Sales Tax Payable | 1,497.73 | D004, D005 | 2024-09-07 | delivery_sale_tax |
| 6 | Cash | Accounts Receivable | 16,475.03 | D006, D005 | 2024-12-31 | customer_payment |
| 7 | Accounts Payable | Cash | 34,446.06 | D007, D003 | 2024-12-29 | supplier_payment |
| 8 | Accounts Receivable | Sales Revenue | 15,983.94 | D008, D009 | 2024-11-08 | delivery_sale_sale |
| 9 | Cost of Goods Sold | Inventory | 10,779.15 | D008, D009 | 2024-11-08 | delivery_sale_cogs |
| 10 | Accounts Receivable | Sales Tax Payable | 3,196.79 | D008, D009 | 2024-11-08 | delivery_sale_tax |
| 11 | Inventory | Accounts Payable | 13,233.28 | D010, D011 | 2024-05-31 | goods_receipt_purchase |
| 12 | Input Tax Receivable | Accounts Payable | 1,323.33 | D010, D011 | 2024-05-31 | goods_receipt_purchase_tax |
| 13 | Inventory | Accounts Payable | 22,338.12 | D012, D013 | 2024-04-26 | goods_receipt_purchase |
| 14 | Input Tax Receivable | Accounts Payable | 4,467.62 | D012, D013 | 2024-04-26 | goods_receipt_purchase_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 135,659.80
- Inventory: 174,368.48
- Accounts Receivable: 52,818.28
- Office Supplies: 5,747.94
- Input Tax Receivable: 11,531.96

**Liabilities**
- Accounts Payable: 80,328.24
- Accrued Expenses: 9,273.51
- Sales Tax Payable: 4,694.52

**Equity**
- Retained Earnings: 60,165.77
- Owner's Equity: 225,664.42

**Totals:** Assets = 380,126.46; Liabilities = 94,296.27; Equity = 285,830.19
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
