# Verification Packet — COV_RET_Y4_0043

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 4
- **Period type:** year
- **Period label:** FY 2024
- **Period start → end:** 2024-01-01 → 2024-12-31
- **Entity:** Granite Distribution
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 27
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-01-01_

**Assets**
- Cash: 100,333.77
- Inventory: 57,455.81
- Card Settlement Clearing: 4,424.17
- Store Fixtures: 15,924.19
- Office Supplies: 2,920.20

**Liabilities**
- Accounts Payable: 13,357.83
- Unearned Revenue: 7,835.89
- Accrued Expenses: 4,228.72
- Loans Payable: 21,936.51

**Equity**
- Retained Earnings: 23,498.40
- Owner's Equity: 110,200.79


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/01/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 100.333,77
  - Section assets | Account Inventory | Amount EUR 57.455,81
  - Section assets | Account Card Settlement Clearing | Amount EUR 4.424,17
  - Section assets | Account Store Fixtures | Amount EUR 15.924,19
  - Section assets | Account Office Supplies | Amount EUR 2.920,20
  - Section liabilities | Account Accounts Payable | Amount EUR 13.357,83
  - Section liabilities | Account Unearned Revenue | Amount EUR 7.835,89
  - Section liabilities | Account Accrued Expenses | Amount EUR 4.228,72
  - Section liabilities | Account Loans Payable | Amount EUR 21.936,51
  - Section equity | Account Retained Earnings | Amount EUR 23.498,40
  - Section equity | Account Owner's Equity | Amount EUR 110.200,79

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-02

```
SUPPLIER INVOICE
================

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Document Date: 02/02/2024

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 20/02/2024

Supplier Header
---------------
Supplier: Prime Utility Desk
Expense Category: Inventory
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 20/02/2024
Subtotal: EUR 33.260,93
Tax Label: Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 2.411,42
Total: EUR 35.672,35

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 20 | Unit Cost EUR 337,32 | Amount EUR 6.746,31
  - Description Widget B | Quantity 6 | Unit Cost EUR 4.419,10 | Amount EUR 26.514,62

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D023 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-02-02

```
SECONDARY COPY
==============

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Document Date: 02/02/2024

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D023
Document Type: secondary_copy
Period: FY 2024

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0001
Counterparty: Prime Utility Desk
Total: EUR 35.672,35
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D023
```

### Document D024 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-02-02

```
SECONDARY COPY
==============

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Document Date: 02/02/2024

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D024
Document Type: secondary_copy
Period: FY 2024

Copy Summary
------------
Copy ID: COPY-0002
Source Reference: BILL-0001
Counterparty: Prime Utility Desk
Total: EUR 35.672,35
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D024
```

### Document D014 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-02

```
SUPPLIER INVOICE
================

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Date: 02/04/2024

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D014
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 23/04/2024

Supplier Header
---------------
Supplier: Golden State Finance
Expense Category: Inventory
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 23/04/2024
Subtotal: EUR 7.686,32
Tax Label: Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 634,12
Total: EUR 8.320,44

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 18 | Unit Cost EUR 140,14 | Amount EUR 2.522,56
  - Description Widget B | Quantity 25 | Unit Cost EUR 206,55 | Amount EUR 5.163,76

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-05-31

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: EUR 43.835,90
Draw Amount: EUR 76.992,98
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 120.828,88
Note: Scheduled lender activity for the selected period.
```

### Document D017 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2024-06-21

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0002
Store Name: Granite Distribution
Gross Sales: EUR 93.165,50
Returns: 2.497,46
Net Sales: EUR 90.668,04
Tax Label: Sales Tax
Tax Amount: EUR 8.613,46
COGS Amount: EUR 48.893,40
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: EUR 20.717,89
Card Sales: EUR 78.563,61
Units Sold: 234
```

### Document D018 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2024-06-21

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0002
Processor: HarborPay
Batch Total: EUR 78.563,61
Fee Amount: EUR 1.414,14
Expected Deposit: EUR 77.149,47
Terminal ID: TERM-0002
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-10

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Vertex Supply Co.
Asset Name: Ultrasound console
Asset Tag: TAG-0001
Useful Life Months: 60
Total: EUR 122.849,65
Paid Cash: EUR 31.199,85
Financed Amount: EUR 91.649,80
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2024-08-21

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Granite Distribution
Gross Sales: EUR 83.888,60
Returns: 4.042,96
Net Sales: EUR 79.845,64
Tax Label: Sales Tax
Tax Amount: EUR 5.788,81
COGS Amount: EUR 39.901,29
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: EUR 13.831,35
Card Sales: EUR 71.803,10
Units Sold: 100
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2024-08-21

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: Axis Payments
Batch Total: EUR 71.803,10
Fee Amount: EUR 1.292,46
Expected Deposit: EUR 70.510,64
Terminal ID: TERM-0001
```

### Document D021 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2024-08-31

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0003
Store Name: Granite Distribution
Gross Sales: EUR 50.874,52
Returns: 1.200,52
Net Sales: EUR 49.674,00
Tax Label: Sales Tax
Tax Amount: EUR 3.601,36
COGS Amount: EUR 29.429,81
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: EUR 14.415,65
Card Sales: EUR 38.859,71
Units Sold: 91
```

### Document D022 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2024-08-31

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0003
Processor: Axis Payments
Batch Total: EUR 38.859,71
Fee Amount: EUR 699,47
Expected Deposit: EUR 38.160,24
Terminal ID: TERM-0003
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-26

```
PAYMENT ADVICE
==============

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Document Date: 26/09/2024

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Prime Utility Desk
Amount: EUR 28.549,80
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-09-27

```
PAYROLL SUMMARY
===============

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Date: 27/09/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024
Headcount: 7
Gross Pay: EUR 30.447,83
Employer Tax: 3.641,23
Cash Outflow: EUR 34.089,06

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D010 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-28

```
UTILITY INVOICE
===============

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Document Date: 28/09/2024

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: utilities_statement
Period: FY 2024

Terms
-----
Due Date: 10/10/2024

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: FY 2024
Due Date: 10/10/2024
Total: EUR 6.429,00

Charges
-------
Charges:
  - Description Electricity | Amount EUR 1.901,13
  - Description Water | Amount EUR 4.527,87

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D005 — Card Settlement Report

- **Type:** `card_settlement_report`
- **Role:** `posting_doc`
- **Date:** 2024-10-21

```
CARD SETTLEMENT REPORT
======================

Settlement Summary
------------------
Settlement ID: SETTLE-0001
Processor: HarborPay
Gross Amount: EUR 71.803,10
Fees: EUR 1.292,46
Net Deposit: EUR 70.510,64
Deposit Date: 21/10/2024

Linked Batches
--------------
Batch References:
  - BATCH-0001
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2024-12-31

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
  - Sku SKU-0001 | Description Widget B | System Qty 100 | Counted Qty 91 | Unit Cost EUR 
26,33
```

### Document D009 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Date: 31/12/2024

Reference Box
-------------
Document ID: D009
Document Type: inventory_rollforward
Period: FY 2024

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0001
Opening Balance: EUR 2.057,74
Additions: 3.261,98
Usage Or Sales: EUR 2.183,49
Write Down: 236,97
Ending Balance: EUR 2.899,26

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D013 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D013
Document Type: fixed_asset_rollforward
Period: FY 2024

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Store Fixtures
Asset Tag: OPEN-STO
Cost: EUR 15.924,19
Useful Life: 60
Current Charge: EUR 3.184,80
Accumulated Depreciation: 3.184,80
Opening Balance: EUR 15.924,19
Additions: 0,00
Disposals: 0,00
Ending Balance: EUR 15.924,19

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D015 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2024-12-31

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
  - Sku SKU-0002 | Description Filter Pack | System Qty 100 | Counted Qty 92 | Unit Cost EUR
 64,61
```

### Document D016 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D016
Document Type: inventory_rollforward
Period: FY 2024

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0002
Opening Balance: EUR 9.922,43
Additions: 9.613,75
Usage Or Sales: EUR 7.332,40
Write Down: 516,88
Ending Balance: EUR 11.686,90

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D019 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0003
Location: Front store

Counted Items
-------------
Items:
  - Sku SKU-0003 | Description Filter Pack | System Qty 100 | Counted Qty 91 | Unit Cost EUR
 76,20
```

### Document D020 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D020
Document Type: inventory_rollforward
Period: FY 2024

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0003
Opening Balance: EUR 11.043,23
Additions: 11.293,96
Usage Or Sales: EUR 6.023,92
Write Down: 685,80
Ending Balance: EUR 15.627,47

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D025 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
VENDOR STATEMENT
================

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Document Date: 31/12/2024

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D025
Document Type: vendor_statement
Period: FY 2024

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Harbor Utilities
Closing Balance: EUR 6.429,00

Statement Lines
---------------
Lines:
  - Reference UTIL-0001 | Document Type Open invoice | Amount EUR 6.429,00 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D025
```

### Document D026 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
MEMO
====

From
----
Granite Distribution
220 Lake View Road, Bengaluru
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D026
Document Type: memo
Period: FY 2024

Approval / Context
------------------
Subject: Scanning checklist for back-office staff

Memo Summary
------------
Memo ID: INFO-0001
Subject: Scanning checklist for back-office staff
Audience: Operations Team

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D026
```

### Document D027 — Bank Statement

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
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D027
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0043
Statement Currency: EUR
Opening Balance: EUR 100.333,77
Closing Balance: EUR 202.963,57

Statement Rows
--------------
Rows:
  - Date 31/05/2024 | Description Loan draw LOAN-0001 | Amount EUR 76.992,98 | Running 
Balance EUR 177.326,75
  - Date 21/06/2024 | Description Cash till SALES-0002 | Amount EUR 20.717,89 | Running 
Balance EUR 198.044,64
  - Date 10/07/2024 | Description Asset purchase ASSET-0001 | Amount EUR -31.199,85 | 
Running Balance EUR 166.844,79
  - Date 21/08/2024 | Description Cash till SALES-0001 | Amount EUR 13.831,35 | Running 
Balance EUR 180.676,14
  - Date 31/08/2024 | Description Cash till SALES-0003 | Amount EUR 14.415,65 | Running 
Balance EUR 195.091,79
  - Date 26/09/2024 | Description Supplier settlement BILL-0001 | Amount EUR -28.549,80 | 
Running Balance EUR 166.541,99
  - Date 27/09/2024 | Description Payroll PAYRUN-0001 | Amount EUR -34.089,06 | Running 
Balance EUR 132.452,93
  - Date 21/10/2024 | Description Card settlement SETTLE-0001 | Amount EUR 70.510,64 | 
Running Balance EUR 202.963,57

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D027
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 33,260.93 | D002 | 2024-02-02 | inventory_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 2,411.42 | D002 | 2024-02-02 | inventory_purchase_tax |
| 3 | Cash | Sales Revenue | 12,896.36 | D003, D004 | 2024-08-21 | retail_sale_cash |
| 4 | Card Settlement Clearing | Sales Revenue | 66,949.28 | D003, D004 | 2024-08-21 | retail_sale_card |
| 5 | Cost of Goods Sold | Inventory | 39,901.29 | D003, D004 | 2024-08-21 | retail_sale_cogs |
| 6 | Cash | Sales Tax Payable | 934.99 | D003, D004 | 2024-08-21 | retail_sale_cash_tax |
| 7 | Card Settlement Clearing | Sales Tax Payable | 4,853.82 | D003, D004 | 2024-08-21 | retail_sale_card_tax |
| 8 | Cash | Card Settlement Clearing | 70,510.64 | D005, D004 | 2024-10-21 | card_settlement_deposit |
| 9 | Maintenance Expense | Card Settlement Clearing | 1,292.46 | D005, D004 | 2024-10-21 | card_settlement_fees |
| 10 | Accounts Payable | Cash | 28,549.80 | D006, D002 | 2024-09-26 | supplier_payment |
| 11 | Salaries Expense | Cash | 30,447.83 | D007 | 2024-09-27 | payroll_gross |
| 12 | Payroll Tax Expense | Cash | 3,641.23 | D007 | 2024-09-27 | payroll_tax |
| 13 | Inventory Shrinkage Expense | Inventory | 236.97 | D008, D009 | 2024-12-31 | stock_adjustment |
| 14 | Utilities Expense | Accounts Payable | 6,429.00 | D010 | 2024-09-28 | utilities_bill |
| 15 | Cash | Loans Payable | 76,992.98 | D011 | 2024-05-31 | loan_draw |
| 16 | Store Fixtures | Cash | 31,199.85 | D012 | 2024-07-10 | equipment_purchase_cash |
| 17 | Store Fixtures | Notes Payable | 91,649.80 | D012 | 2024-07-10 | equipment_purchase_financed |
| 18 | Depreciation Expense | Accumulated Depreciation | 3,184.80 | D013 | 2024-12-31 | depreciation |
| 19 | Inventory | Accounts Payable | 7,686.32 | D014 | 2024-04-02 | inventory_purchase |
| 20 | Input Tax Receivable | Accounts Payable | 634.12 | D014 | 2024-04-02 | inventory_purchase_tax |
| 21 | Inventory Shrinkage Expense | Inventory | 516.88 | D015, D016 | 2024-12-31 | stock_adjustment |
| 22 | Cash | Sales Revenue | 18,920.45 | D017, D018 | 2024-06-21 | retail_sale_cash |
| 23 | Card Settlement Clearing | Sales Revenue | 71,747.59 | D017, D018 | 2024-06-21 | retail_sale_card |
| 24 | Cost of Goods Sold | Inventory | 48,893.40 | D017, D018 | 2024-06-21 | retail_sale_cogs |
| 25 | Cash | Sales Tax Payable | 1,797.44 | D017, D018 | 2024-06-21 | retail_sale_cash_tax |
| 26 | Card Settlement Clearing | Sales Tax Payable | 6,816.02 | D017, D018 | 2024-06-21 | retail_sale_card_tax |
| 27 | Inventory Shrinkage Expense | Inventory | 685.80 | D019, D020 | 2024-12-31 | stock_adjustment |
| 28 | Cash | Sales Revenue | 13,441.17 | D021, D022 | 2024-08-31 | retail_sale_cash |
| 29 | Card Settlement Clearing | Sales Revenue | 36,232.83 | D021, D022 | 2024-08-31 | retail_sale_card |
| 30 | Cost of Goods Sold | Inventory | 29,429.81 | D021, D022 | 2024-08-31 | retail_sale_cogs |
| 31 | Cash | Sales Tax Payable | 974.48 | D021, D022 | 2024-08-31 | retail_sale_cash_tax |
| 32 | Card Settlement Clearing | Sales Tax Payable | 2,626.88 | D021, D022 | 2024-08-31 | retail_sale_card_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 202,963.57
- Inventory: -21,261.09
- Card Settlement Clearing: 121,847.49
- Store Fixtures: 138,773.84
- Office Supplies: 2,920.20
- Input Tax Receivable: 3,045.54
- Accumulated Depreciation: -3,184.80

**Liabilities**
- Accounts Payable: 35,229.82
- Unearned Revenue: 7,835.89
- Accrued Expenses: 4,228.72
- Loans Payable: 98,929.49
- Sales Tax Payable: 18,003.63
- Notes Payable: 91,649.80

**Equity**
- Retained Earnings: 79,026.61
- Owner's Equity: 110,200.79

**Totals:** Assets = 445,104.75; Liabilities = 255,877.35; Equity = 189,227.40
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
- [ ] Calibration feels right
- [x] Too easy for this level
- [ ] Too hard for this level
- Notes: Feels a hair light for the level.

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
