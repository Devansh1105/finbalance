# Verification Packet — COV_WHO_Q3_0052

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 3
- **Period type:** quarter
- **Period label:** Q3 FY 2024
- **Period start → end:** 2024-07-01 → 2024-09-30
- **Entity:** Cedar Operations
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 14
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-07-01_

**Assets**
- Cash: 81,459.81
- Inventory: 65,149.10
- Accounts Receivable: 12,217.67
- Office Supplies: 3,037.43

**Liabilities**
- Accounts Payable: 21,243.55
- Accrued Expenses: 2,289.71

**Equity**
- Retained Earnings: 16,312.60
- Owner's Equity: 122,018.15


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
Statement Date: 01/07/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 81.459,81
  - Section assets | Account Inventory | Amount EUR 65.149,10
  - Section assets | Account Accounts Receivable | Amount EUR 12.217,67
  - Section assets | Account Office Supplies | Amount EUR 3.037,43
  - Section liabilities | Account Accounts Payable | Amount EUR 21.243,55
  - Section liabilities | Account Accrued Expenses | Amount EUR 2.289,71
  - Section equity | Account Retained Earnings | Amount EUR 16.312,60
  - Section equity | Account Owner's Equity | Amount EUR 122.018,15

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2024-07-13

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Oakline Services
Purchase Ref: PO-0001
Total Quantity: EUR 51,00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Premium Kit | Quantity 51 | Unit Cost EUR 100,66
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-15

```
SUPPLIER INVOICE
================

From
----
Cedar Operations
14 King Street, Pune
Date: 15/07/2024

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: Q3 FY 2024

Terms
-----
Due Date: 01/08/2024

Supplier Header
---------------
Supplier: Oakline Services
Goods Receipt Ref: GRN-0001
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 01/08/2024
Subtotal: EUR 5.133,66
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 423,53
Total: EUR 5.557,19

Supplier Bill Lines
-------------------
Lines:
  - Description Premium Kit | Quantity 51 | Unit Cost EUR 100,66 | Amount EUR 5.133,66

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2024-08-03

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Crescent Labs
Shipment Ref: SHP-0001
Billed Amount: EUR 10.074,37
Cost Basis Amount: EUR 4.913,96
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Widget A | Quantity 38 | Unit Price EUR 244,91 | Unit Cost 
EUR 129,31 | Extended Cost EUR 4.913,96
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-03

```
CUSTOMER INVOICE
================

From
----
Cedar Operations
14 King Street, Pune
Document Date: 03/08/2024

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: Q3 FY 2024
Shipment Ref: SHP-0001

Terms
-----
Due Date: 17/08/2024

Parties
-------
Customer: Crescent Labs
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 17/08/2024
Subtotal: EUR 9.306,58
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 767,79
Total: EUR 10.074,37

Line Items
----------
Items:
  - Description Widget A | Amount EUR 9.306,58

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
- **Date:** 2024-09-07

```
PAYMENT ADVICE
==============

From
----
Cedar Operations
14 King Street, Pune
Document Date: 07/09/2024

To
--
Crescent Labs

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q3 FY 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Crescent Labs
Amount: EUR 10.074,37
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
- **Date:** 2024-09-14

```
PAYMENT ADVICE
==============

From
----
Cedar Operations
14 King Street, Pune
Document Date: 14/09/2024

To
--
Oakline Services

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: Q3 FY 2024
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: EUR 5.557,19
Reference: SUP-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D011 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-15

```
UTILITY INVOICE
===============

From
----
Cedar Operations
14 King Street, Pune
Date: 15/09/2024

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: utilities_statement
Period: Q3 FY 2024

Terms
-----
Due Date: 25/09/2024

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: Q3 FY 2024
Due Date: 25/09/2024
Total: EUR 3.466,50

Charges
-------
Charges:
  - Description Electricity | Amount EUR 1.177,73
  - Description Water | Amount EUR 2.288,77

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D010 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-09-18

```
PAYROLL SUMMARY
===============

From
----
Cedar Operations
14 King Street, Pune
Date: 18/09/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q3 FY 2024
Headcount: 6
Gross Pay: EUR 33.615,71
Employer Tax: 4.191,96
Cash Outflow: EUR 37.807,67

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2024-09-30

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0001
Location: Front store

Counted Items
-------------
Items:
  - Sku SKU-0003 | Description Widget B | System Qty 100 | Counted Qty 96 | Unit Cost EUR 
20,84
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2024-09-30

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: EUR 83,36
Reference Sheet: COUNT-0001
```

### Document D012 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2024-09-30

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0002
Location: Warehouse A

Counted Items
-------------
Items:
  - Sku SKU-0004 | Description Refill Pack | System Qty 100 | Counted Qty 97 | Unit Cost EUR
 41,41
```

### Document D013 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2024-09-30

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0002
Reason: Shrinkage found during physical count
Amount: EUR 124,23
Reference Sheet: COUNT-0002
```

### Document D014 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-09-30

```
BANK STATEMENT
==============

From
----
Cedar Operations
14 King Street, Pune
Date: 30/09/2024

Reference Box
-------------
Document ID: D014
Document Type: bank_statement
Period: Q3 FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0052
Statement Currency: EUR
Opening Balance: EUR 81.459,81
Closing Balance: EUR 48.169,32

Statement Rows
--------------
Rows:
  - Date 07/09/2024 | Description Customer settlement INV-0001 | Amount EUR 10.074,37 | 
Running Balance EUR 91.534,18
  - Date 14/09/2024 | Description Supplier settlement SUP-0001 | Amount EUR -5.557,19 | 
Running Balance EUR 85.976,99
  - Date 18/09/2024 | Description Payroll PAYRUN-0001 | Amount EUR -37.807,67 | Running 
Balance EUR 48.169,32

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D014
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 5,133.66 | D002, D003 | 2024-07-15 | goods_receipt_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 423.53 | D002, D003 | 2024-07-15 | goods_receipt_purchase_tax |
| 3 | Accounts Receivable | Sales Revenue | 9,306.58 | D004, D005 | 2024-08-03 | delivery_sale_sale |
| 4 | Cost of Goods Sold | Inventory | 4,913.96 | D004, D005 | 2024-08-03 | delivery_sale_cogs |
| 5 | Accounts Receivable | Sales Tax Payable | 767.79 | D004, D005 | 2024-08-03 | delivery_sale_tax |
| 6 | Cash | Accounts Receivable | 10,074.37 | D006, D005 | 2024-09-07 | customer_payment |
| 7 | Accounts Payable | Cash | 5,557.19 | D007, D003 | 2024-09-14 | supplier_payment |
| 8 | Inventory Shrinkage Expense | Inventory | 83.36 | D008, D009 | 2024-09-30 | inventory_adjustment |
| 9 | Salaries Expense | Cash | 33,615.71 | D010 | 2024-09-18 | payroll_gross |
| 10 | Payroll Tax Expense | Cash | 4,191.96 | D010 | 2024-09-18 | payroll_tax |
| 11 | Utilities Expense | Accounts Payable | 3,466.50 | D011 | 2024-09-15 | utilities_bill |
| 12 | Inventory Shrinkage Expense | Inventory | 124.23 | D012, D013 | 2024-09-30 | inventory_adjustment |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 48,169.32
- Inventory: 65,161.21
- Accounts Receivable: 12,217.67
- Office Supplies: 3,037.43
- Input Tax Receivable: 423.53

**Liabilities**
- Accounts Payable: 24,710.05
- Accrued Expenses: 2,289.71
- Sales Tax Payable: 767.79

**Equity**
- Retained Earnings: -20,776.54
- Owner's Equity: 122,018.15

**Totals:** Assets = 129,009.16; Liabilities = 27,767.55; Equity = 101,241.61
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
