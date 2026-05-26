# Verification Packet — COV_WHO_Y1_0055

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 1
- **Period type:** year
- **Period label:** FY 2025
- **Period start → end:** 2025-01-01 → 2025-12-31
- **Entity:** Granite Advisors
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `none`
- **Document count:** 11
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 206,263.47
- Inventory: 135,269.22
- Accounts Receivable: 12,027.15

**Liabilities**
- Accounts Payable: 27,598.35

**Equity**
- Owner's Equity: 325,961.49


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
  - Section assets | Account Cash | Amount EUR 206.263,47
  - Section assets | Account Inventory | Amount EUR 135.269,22
  - Section assets | Account Accounts Receivable | Amount EUR 12.027,15
  - Section liabilities | Account Accounts Payable | Amount EUR 27.598,35
  - Section equity | Account Owner's Equity | Amount EUR 325.961,49

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2025-02-28

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Oakline Services
Purchase Ref: PO-0001
Total Quantity: EUR 155,00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Premium Kit | Quantity 155 | Unit Cost EUR 118,77
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-02

```
SUPPLIER INVOICE
================

From
----
Granite Advisors
90 Hill Park, Hyderabad
Date: 02/03/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: FY 2025

Terms
-----
Due Date: 18/03/2025

Supplier Header
---------------
Supplier: Oakline Services
Goods Receipt Ref: GRN-0001
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 18/03/2025
Total: EUR 18.409,35

Supplier Bill Lines
-------------------
Lines:
  - Description Premium Kit | Quantity 155 | Unit Cost EUR 118,77 | Amount EUR 18.409,35

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D008 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-05-12

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0003
Customer: Maple Ridge Trading
Shipment Ref: SHP-0003
Billed Amount: EUR 13.535,41
Cost Basis Amount: EUR 7.688,03
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0004 | Description Widget A | Quantity 19 | Unit Price EUR 712,39 | Unit Cost 
EUR 404,63 | Extended Cost EUR 7.688,03
```

### Document D009 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-12

```
CUSTOMER INVOICE
================

From
----
Granite Advisors
90 Hill Park, Hyderabad
Date: 12/05/2025

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D009
Document Type: customer_invoice
Period: FY 2025
Shipment Ref: SHP-0003

Terms
-----
Due Date: 31/05/2025

Parties
-------
Customer: Maple Ridge Trading
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 31/05/2025
Total: EUR 13.535,41

Line Items
----------
Items:
  - Description Widget A | Amount EUR 13.535,41

Shipment Link
-------------
Shipment Ref: SHP-0003

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D006 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-06-01

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0002
Customer: Blue Finch Holdings
Shipment Ref: SHP-0002
Billed Amount: EUR 9.597,28
Cost Basis Amount: EUR 5.524,12
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0003 | Description Service Bundle | Quantity 19 | Unit Price EUR 505,12 | Unit 
Cost EUR 290,74 | Extended Cost EUR 5.524,12
```

### Document D007 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-01

```
CUSTOMER INVOICE
================

From
----
Granite Advisors
90 Hill Park, Hyderabad
Document Date: 01/06/2025

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D007
Document Type: customer_invoice
Period: FY 2025
Shipment Ref: SHP-0002

Terms
-----
Due Date: 12/06/2025

Parties
-------
Customer: Blue Finch Holdings
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 12/06/2025
Total: EUR 9.597,28

Line Items
----------
Items:
  - Description Service Bundle | Amount EUR 9.597,28

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
- **Date:** 2025-06-14

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Metro Edge Partners
Shipment Ref: SHP-0001
Billed Amount: EUR 20.921,60
Cost Basis Amount: EUR 13.257,94
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Widget B | Quantity 70 | Unit Price EUR 298,88 | Unit Cost 
EUR 189,40 | Extended Cost EUR 13.257,94
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-14

```
CUSTOMER INVOICE
================

From
----
Granite Advisors
90 Hill Park, Hyderabad
Document Date: 14/06/2025

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: FY 2025
Shipment Ref: SHP-0001

Terms
-----
Due Date: 25/06/2025

Parties
-------
Customer: Metro Edge Partners
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 25/06/2025
Total: EUR 20.921,60

Line Items
----------
Items:
  - Description Widget B | Amount EUR 20.921,60

Shipment Link
-------------
Shipment Ref: SHP-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D010 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
VENDOR STATEMENT
================

From
----
Granite Advisors
90 Hill Park, Hyderabad
Date: 31/12/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: vendor_statement
Period: FY 2025

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Oakline Services
Closing Balance: EUR 18.409,35

Statement Lines
---------------
Lines:
  - Reference SUP-0001 | Document Type Open invoice | Amount EUR 18.409,35 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D011 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Granite Advisors
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D011
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0055
Statement Currency: EUR
Opening Balance: EUR 206.263,47
Closing Balance: EUR 206.263,47

Statement Rows
--------------
Rows: None

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 18,409.35 | D002, D003 | 2025-03-02 | goods_receipt_purchase |
| 2 | Accounts Receivable | Sales Revenue | 20,921.60 | D004, D005 | 2025-06-14 | delivery_sale_sale |
| 3 | Cost of Goods Sold | Inventory | 13,257.94 | D004, D005 | 2025-06-14 | delivery_sale_cogs |
| 4 | Accounts Receivable | Sales Revenue | 9,597.28 | D006, D007 | 2025-06-01 | delivery_sale_sale |
| 5 | Cost of Goods Sold | Inventory | 5,524.12 | D006, D007 | 2025-06-01 | delivery_sale_cogs |
| 6 | Accounts Receivable | Sales Revenue | 13,535.41 | D008, D009 | 2025-05-12 | delivery_sale_sale |
| 7 | Cost of Goods Sold | Inventory | 7,688.03 | D008, D009 | 2025-05-12 | delivery_sale_cogs |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 206,263.47
- Inventory: 127,208.48
- Accounts Receivable: 56,081.44

**Liabilities**
- Accounts Payable: 46,007.70

**Equity**
- Owner's Equity: 325,961.49
- Retained Earnings: 17,584.20

**Totals:** Assets = 389,553.39; Liabilities = 46,007.70; Equity = 343,545.69
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
