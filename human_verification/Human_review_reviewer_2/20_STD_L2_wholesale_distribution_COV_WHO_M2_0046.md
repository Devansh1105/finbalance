# Verification Packet — COV_WHO_M2_0046

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 2
- **Period type:** month
- **Period label:** June 2024
- **Period start → end:** 2024-06-01 → 2024-06-30
- **Entity:** Northwind Advisors
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 8
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-06-01_

**Assets**
- Cash: 26,281.31
- Inventory: 28,063.47
- Accounts Receivable: 8,141.12
- Office Supplies: 1,282.22

**Liabilities**
- Accounts Payable: 6,201.03
- Accrued Expenses: 1,280.45

**Equity**
- Retained Earnings: 12,179.92
- Owner's Equity: 44,106.72


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-06-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/06/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 26.281,31
  - Section assets | Account Inventory | Amount EUR 28.063,47
  - Section assets | Account Accounts Receivable | Amount EUR 8.141,12
  - Section assets | Account Office Supplies | Amount EUR 1.282,22
  - Section liabilities | Account Accounts Payable | Amount EUR 6.201,03
  - Section liabilities | Account Accrued Expenses | Amount EUR 1.280,45
  - Section equity | Account Retained Earnings | Amount EUR 12.179,92
  - Section equity | Account Owner's Equity | Amount EUR 44.106,72

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2024-06-02

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
  - Sku SKU-0001 | Description Filter Pack | Quantity 155 | Unit Cost EUR 49,79
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-04

```
SUPPLIER INVOICE
================

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Document Date: 04/06/2024

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: June 2024

Terms
-----
Due Date: 17/06/2024

Supplier Header
---------------
Supplier: Oakline Services
Goods Receipt Ref: GRN-0001
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 17/06/2024
Subtotal: EUR 7.717,45
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 559,52
Total: EUR 8.276,97

Supplier Bill Lines
-------------------
Lines:
  - Description Filter Pack | Quantity 155 | Unit Cost EUR 49,79 | Amount EUR 7.717,45

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2024-06-12

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Blue Finch Holdings
Shipment Ref: SHP-0001
Billed Amount: EUR 4.888,08
Cost Basis Amount: EUR 3.021,10
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Widget A | Quantity 30 | Unit Price EUR 148,80 | Unit Cost 
EUR 100,70 | Extended Cost EUR 3.021,10
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-12

```
CUSTOMER INVOICE
================

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Document Date: 12/06/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: June 2024
Shipment Ref: SHP-0001

Terms
-----
Due Date: 29/06/2024

Parties
-------
Customer: Blue Finch Holdings
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 29/06/2024
Subtotal: EUR 4.464,00
Tax Label: US Sales Tax
Tax Rate: 9.50%
Tax Amount: EUR 424,08
Total: EUR 4.888,08

Line Items
----------
Items:
  - Description Widget A | Amount EUR 4.464,00

Shipment Link
-------------
Shipment Ref: SHP-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-26

```
PAYMENT ADVICE
==============

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Document Date: 26/06/2024

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: June 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: EUR 4.888,08
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-26

```
PAYMENT ADVICE
==============

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Date: 26/06/2024

To
--
Oakline Services

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: June 2024
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: EUR 8.276,97
Reference: SUP-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
BANK STATEMENT
==============

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Date: 30/06/2024

Reference Box
-------------
Document ID: D008
Document Type: bank_statement
Period: June 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0046
Statement Currency: EUR
Opening Balance: EUR 26.281,31
Closing Balance: EUR 22.892,42

Statement Rows
--------------
Rows:
  - Date 26/06/2024 | Description Customer settlement INV-0001 | Amount EUR 4.888,08 | 
Running Balance EUR 31.169,39
  - Date 26/06/2024 | Description Supplier settlement SUP-0001 | Amount EUR -8.276,97 | 
Running Balance EUR 22.892,42

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D008
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 7,717.45 | D002, D003 | 2024-06-04 | goods_receipt_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 559.52 | D002, D003 | 2024-06-04 | goods_receipt_purchase_tax |
| 3 | Accounts Receivable | Sales Revenue | 4,464.00 | D004, D005 | 2024-06-12 | delivery_sale_sale |
| 4 | Cost of Goods Sold | Inventory | 3,021.10 | D004, D005 | 2024-06-12 | delivery_sale_cogs |
| 5 | Accounts Receivable | Sales Tax Payable | 424.08 | D004, D005 | 2024-06-12 | delivery_sale_tax |
| 6 | Cash | Accounts Receivable | 4,888.08 | D006, D005 | 2024-06-26 | customer_payment |
| 7 | Accounts Payable | Cash | 8,276.97 | D007, D003 | 2024-06-26 | supplier_payment |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 22,892.42
- Inventory: 32,759.82
- Accounts Receivable: 8,141.12
- Office Supplies: 1,282.22
- Input Tax Receivable: 559.52

**Liabilities**
- Accounts Payable: 6,201.03
- Accrued Expenses: 1,280.45
- Sales Tax Payable: 424.08

**Equity**
- Retained Earnings: 13,622.82
- Owner's Equity: 44,106.72

**Totals:** Assets = 65,635.10; Liabilities = 7,905.56; Equity = 57,729.54
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
