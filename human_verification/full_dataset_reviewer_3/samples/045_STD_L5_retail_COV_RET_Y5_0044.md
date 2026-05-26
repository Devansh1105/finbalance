# Verification Packet — COV_RET_Y5_0044

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 5
- **Period type:** year
- **Period label:** FY 2025
- **Period start → end:** 2025-01-01 → 2025-12-31
- **Entity:** Atlas Builders
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 31
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 79,416.34
- Inventory: 56,356.88
- Card Settlement Clearing: 5,029.79
- Store Fixtures: 23,335.19
- Office Supplies: 4,099.37

**Liabilities**
- Accounts Payable: 14,841.76
- Unearned Revenue: 12,493.97
- Accrued Expenses: 6,384.12
- Loans Payable: 8,016.07

**Equity**
- Retained Earnings: 13,808.75
- Owner's Equity: 112,692.90


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
  - Section assets | Account Cash | Amount GBP 79,416.34
  - Section assets | Account Inventory | Amount GBP 56,356.88
  - Section assets | Account Card Settlement Clearing | Amount GBP 5,029.79
  - Section assets | Account Store Fixtures | Amount GBP 23,335.19
  - Section assets | Account Office Supplies | Amount GBP 4,099.37
  - Section liabilities | Account Accounts Payable | Amount GBP 14,841.76
  - Section liabilities | Account Unearned Revenue | Amount GBP 12,493.97
  - Section liabilities | Account Accrued Expenses | Amount GBP 6,384.12
  - Section liabilities | Account Loans Payable | Amount GBP 8,016.07
  - Section equity | Account Retained Earnings | Amount GBP 13,808.75
  - Section equity | Account Owner's Equity | Amount GBP 112,692.90

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-14

```
SUPPLIER INVOICE
================

From
----
Atlas Builders
90 Hill Park, Hyderabad
Document Date: 14/02/2025

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: FY 2025

Terms
-----
Due Date: 04/03/2025

Supplier Header
---------------
Supplier: Meridian Support LLP
Expense Category: Inventory
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 04/03/2025
Subtotal: GBP 35,515.16
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 7,103.03
Total: GBP 42,618.19

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 10 | Unit Cost GBP 1,414.51 | Amount GBP 14,145.14
  - Description Widget B | Quantity 12 | Unit Cost GBP 1,780.84 | Amount GBP 21,370.02

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D028 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-02-14

```
SECONDARY COPY
==============

From
----
Atlas Builders
90 Hill Park, Hyderabad
Date: 14/02/2025

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D028
Document Type: secondary_copy
Period: FY 2025

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0001
Counterparty: Meridian Support LLP
Total: GBP 42,618.19
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D028
```

### Document D029 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-02-14

```
SECONDARY COPY
==============

From
----
Atlas Builders
90 Hill Park, Hyderabad
Document Date: 14/02/2025

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D029
Document Type: secondary_copy
Period: FY 2025

Copy Summary
------------
Copy ID: COPY-0002
Source Reference: BILL-0001
Counterparty: Meridian Support LLP
Total: GBP 42,618.19
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D029
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-13

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Meridian Support LLP
Asset Name: Server rack
Asset Tag: TAG-0001
Useful Life Months: 36
Total: GBP 136,827.49
Paid Cash: GBP 42,904.65
Financed Amount: GBP 93,922.84
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-06-27

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: GBP 43,311.21
Draw Amount: GBP 183,810.60
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 227,121.81
Note: Scheduled lender activity for the selected period.
```

### Document D026 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-07-08

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0003
Store Name: Atlas Builders
Gross Sales: GBP 67,386.92
Returns: 1,248.95
Net Sales: GBP 66,137.97
Tax Label: VAT
Tax Amount: GBP 13,227.59
COGS Amount: GBP 33,801.17
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: GBP 17,773.70
Card Sales: GBP 61,591.86
Units Sold: 262
```

### Document D027 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-07-08

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0003
Processor: HarborPay
Batch Total: GBP 61,591.86
Fee Amount: GBP 1,108.65
Expected Deposit: GBP 60,483.21
Terminal ID: TERM-0003
```

### Document D016 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-07-18

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0002
Store Name: Atlas Builders
Gross Sales: GBP 53,587.01
Returns: 563.89
Net Sales: GBP 53,023.12
Tax Label: VAT
Tax Amount: GBP 6,627.89
COGS Amount: GBP 27,675.81
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: GBP 13,290.02
Card Sales: GBP 46,360.99
Units Sold: 134
```

### Document D017 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-07-18

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0002
Processor: ClearRoute
Batch Total: GBP 46,360.99
Fee Amount: GBP 834.50
Expected Deposit: GBP 45,526.49
Terminal ID: TERM-0002
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-07-29

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Atlas Builders
Gross Sales: GBP 103,427.12
Returns: 2,639.32
Net Sales: GBP 100,787.80
Tax Label: VAT
Tax Amount: GBP 12,598.48
COGS Amount: GBP 63,266.24
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: GBP 26,879.44
Card Sales: GBP 86,506.84
Units Sold: 102
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-07-29

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: ClearRoute
Batch Total: GBP 86,506.84
Fee Amount: GBP 1,557.12
Expected Deposit: GBP 84,949.72
Terminal ID: TERM-0001
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-09-06

```
PAYROLL SUMMARY
===============

From
----
Atlas Builders
90 Hill Park, Hyderabad
Date: 06/09/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2025
Headcount: 5
Gross Pay: GBP 24,515.07
Employer Tax: 2,110.90
Cash Outflow: GBP 26,625.97

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D021 — Return Note

- **Type:** `return_note`
- **Role:** `posting_doc`
- **Date:** 2025-09-08

```
RETURN NOTE
===========

Return Summary
--------------
Return ID: RTN-0003
Reason: Shelf defect
Amount: GBP 1,322.26
Reference: SALE-REF-0003
```

### Document D022 — Return Note

- **Type:** `return_note`
- **Role:** `posting_doc`
- **Date:** 2025-09-11

```
RETURN NOTE
===========

Return Summary
--------------
Return ID: RTN-0004
Reason: Shelf defect
Amount: GBP 761.27
Reference: SALE-REF-0004
```

### Document D015 — Return Note

- **Type:** `return_note`
- **Role:** `posting_doc`
- **Date:** 2025-10-13

```
RETURN NOTE
===========

Return Summary
--------------
Return ID: RTN-0001
Reason: Damaged item
Amount: GBP 999.19
Reference: SALE-REF-0001
```

### Document D018 — Return Note

- **Type:** `return_note`
- **Role:** `posting_doc`
- **Date:** 2025-10-14

```
RETURN NOTE
===========

Return Summary
--------------
Return ID: RTN-0002
Reason: Customer return
Amount: GBP 953.48
Reference: SALE-REF-0002
```

### Document D023 — Return Note

- **Type:** `return_note`
- **Role:** `posting_doc`
- **Date:** 2025-10-28

```
RETURN NOTE
===========

Return Summary
--------------
Return ID: RTN-0005
Reason: Customer return
Amount: GBP 771.37
Reference: SALE-REF-0005
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-11-01

```
PAYMENT ADVICE
==============

From
----
Atlas Builders
90 Hill Park, Hyderabad
Document Date: 01/11/2025

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Meridian Support LLP
Amount: GBP 33,594.79
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D005 — Card Settlement Report

- **Type:** `card_settlement_report`
- **Role:** `posting_doc`
- **Date:** 2025-11-07

```
CARD SETTLEMENT REPORT
======================

Settlement Summary
------------------
Settlement ID: SETTLE-0001
Processor: ClearRoute
Gross Amount: GBP 86,506.84
Fees: GBP 1,557.12
Net Deposit: GBP 84,949.72
Deposit Date: 07/11/2025

Linked Batches
--------------
Batch References:
  - BATCH-0001
```

### Document D014 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-11

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: GBP 46,874.42
Draw Amount: GBP 0.00
Principal Paid: GBP 30,440.42
Interest Paid: GBP 3,793.34
Ending Principal: GBP 16,434.00
Note: Scheduled lender activity for the selected period.
```

### Document D010 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-13

```
UTILITY INVOICE
===============

From
----
Atlas Builders
90 Hill Park, Hyderabad
Date: 13/11/2025

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: utilities_statement
Period: FY 2025

Terms
-----
Due Date: 20/11/2025

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: FY 2025
Due Date: 20/11/2025
Total: GBP 6,814.92

Charges
-------
Charges:
  - Description Electricity | Amount GBP 1,926.52
  - Description Water | Amount GBP 4,888.40

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0001
Location: Back room

Counted Items
-------------
Items:
  - Sku SKU-0001 | Description Widget B | System Qty 100 | Counted Qty 92 | Unit Cost GBP 
27.25
```

### Document D009 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Atlas Builders
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D009
Document Type: inventory_rollforward
Period: FY 2025

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0001
Opening Balance: GBP 3,152.80
Additions: 4,669.96
Usage Or Sales: GBP 3,077.26
Write Down: 218.00
Ending Balance: GBP 4,527.50

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D013 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Atlas Builders
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D013
Document Type: fixed_asset_rollforward
Period: FY 2025

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Server rack
Asset Tag: TAG-0001
Cost: GBP 136,827.49
Useful Life: 36
Current Charge: GBP 45,609.12
Accumulated Depreciation: 45,609.12
Opening Balance: GBP 136,827.49
Additions: 0.00
Disposals: 0.00
Ending Balance: GBP 136,827.49

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D019 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0002
Location: Front store

Counted Items
-------------
Items:
  - Sku SKU-0002 | Description Widget A | System Qty 100 | Counted Qty 92 | Unit Cost GBP 
46.03
```

### Document D020 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Atlas Builders
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D020
Document Type: inventory_rollforward
Period: FY 2025

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0002
Opening Balance: GBP 3,791.54
Additions: 4,064.31
Usage Or Sales: GBP 6,495.78
Write Down: 368.24
Ending Balance: GBP 991.83

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D024 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-12-31

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
  - Sku SKU-0003 | Description Service Bundle | System Qty 100 | Counted Qty 88 | Unit Cost 
GBP 91.50
```

### Document D025 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Atlas Builders
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D025
Document Type: inventory_rollforward
Period: FY 2025

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0003
Opening Balance: GBP 12,369.32
Additions: 22,820.53
Usage Or Sales: GBP 13,610.48
Write Down: 1,098.00
Ending Balance: GBP 20,481.37

Footer
------
Internal document packet copy.
Page marker: D025
```

### Document D030 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Atlas Builders
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D030
Document Type: memo
Period: FY 2025

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
Narrative: The packet may include supporting correspondence gathered during the close 
review.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D030
```

### Document D031 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Atlas Builders
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D031
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0044
Statement Currency: GBP
Opening Balance: GBP 79,416.34
Closing Balance: GBP 263,953.08

Statement Rows
--------------
Rows:
  - Date 13/06/2025 | Description Asset purchase ASSET-0001 | Amount GBP -42,904.65 | 
Running Balance GBP 36,511.69
  - Date 27/06/2025 | Description Loan draw LOAN-0001 | Amount GBP 183,810.60 | Running 
Balance GBP 220,322.29
  - Date 08/07/2025 | Description Cash till SALES-0003 | Amount GBP 17,773.70 | Running 
Balance GBP 238,095.99
  - Date 18/07/2025 | Description Cash till SALES-0002 | Amount GBP 13,290.02 | Running 
Balance GBP 251,386.01
  - Date 29/07/2025 | Description Cash till SALES-0001 | Amount GBP 26,879.44 | Running 
Balance GBP 278,265.45
  - Date 06/09/2025 | Description Payroll PAYRUN-0001 | Amount GBP -26,625.97 | Running 
Balance GBP 251,639.48
  - Date 08/09/2025 | Description Return RTN-0003 | Amount GBP -1,322.26 | Running Balance 
GBP 250,317.22
  - Date 11/09/2025 | Description Return RTN-0004 | Amount GBP -761.27 | Running Balance GBP
 249,555.95
  - Date 13/10/2025 | Description Return RTN-0001 | Amount GBP -999.19 | Running Balance GBP
 248,556.76
  - Date 14/10/2025 | Description Return RTN-0002 | Amount GBP -953.48 | Running Balance GBP
 247,603.28
  - Date 28/10/2025 | Description Return RTN-0005 | Amount GBP -771.37 | Running Balance GBP
 246,831.91
  - Date 01/11/2025 | Description Supplier settlement BILL-0001 | Amount GBP -33,594.79 | 
Running Balance GBP 213,237.12
  - Date 07/11/2025 | Description Card settlement SETTLE-0001 | Amount GBP 84,949.72 | 
Running Balance GBP 298,186.84
  - Date 11/11/2025 | Description Loan payment LOAN-0002 | Amount GBP -34,233.76 | Running 
Balance GBP 263,953.08

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D031
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 35,515.16 | D002 | 2025-02-14 | inventory_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 7,103.03 | D002 | 2025-02-14 | inventory_purchase_tax |
| 3 | Cash | Sales Revenue | 23,892.83 | D003, D004 | 2025-07-29 | retail_sale_cash |
| 4 | Card Settlement Clearing | Sales Revenue | 76,894.97 | D003, D004 | 2025-07-29 | retail_sale_card |
| 5 | Cost of Goods Sold | Inventory | 63,266.24 | D003, D004 | 2025-07-29 | retail_sale_cogs |
| 6 | Cash | Sales Tax Payable | 2,986.61 | D003, D004 | 2025-07-29 | retail_sale_cash_tax |
| 7 | Card Settlement Clearing | Sales Tax Payable | 9,611.87 | D003, D004 | 2025-07-29 | retail_sale_card_tax |
| 8 | Cash | Card Settlement Clearing | 84,949.72 | D005, D004 | 2025-11-07 | card_settlement_deposit |
| 9 | Maintenance Expense | Card Settlement Clearing | 1,557.12 | D005, D004 | 2025-11-07 | card_settlement_fees |
| 10 | Accounts Payable | Cash | 33,594.79 | D006, D002 | 2025-11-01 | supplier_payment |
| 11 | Salaries Expense | Cash | 24,515.07 | D007 | 2025-09-06 | payroll_gross |
| 12 | Payroll Tax Expense | Cash | 2,110.90 | D007 | 2025-09-06 | payroll_tax |
| 13 | Inventory Shrinkage Expense | Inventory | 218.00 | D008, D009 | 2025-12-31 | stock_adjustment |
| 14 | Utilities Expense | Accounts Payable | 6,814.92 | D010 | 2025-11-13 | utilities_bill |
| 15 | Cash | Loans Payable | 183,810.60 | D011 | 2025-06-27 | loan_draw |
| 16 | Store Fixtures | Cash | 42,904.65 | D012 | 2025-06-13 | equipment_purchase_cash |
| 17 | Store Fixtures | Notes Payable | 93,922.84 | D012 | 2025-06-13 | equipment_purchase_financed |
| 18 | Depreciation Expense | Accumulated Depreciation | 45,609.12 | D013 | 2025-12-31 | depreciation |
| 19 | Loans Payable | Cash | 30,440.42 | D014 | 2025-11-11 | loan_repayment_principal |
| 20 | Interest Expense | Cash | 3,793.34 | D014 | 2025-11-11 | loan_repayment_interest |
| 21 | Sales Revenue | Cash | 999.19 | D015 | 2025-10-13 | return |
| 22 | Cash | Sales Revenue | 11,813.35 | D016, D017 | 2025-07-18 | retail_sale_cash |
| 23 | Card Settlement Clearing | Sales Revenue | 41,209.77 | D016, D017 | 2025-07-18 | retail_sale_card |
| 24 | Cost of Goods Sold | Inventory | 27,675.81 | D016, D017 | 2025-07-18 | retail_sale_cogs |
| 25 | Cash | Sales Tax Payable | 1,476.67 | D016, D017 | 2025-07-18 | retail_sale_cash_tax |
| 26 | Card Settlement Clearing | Sales Tax Payable | 5,151.22 | D016, D017 | 2025-07-18 | retail_sale_card_tax |
| 27 | Sales Revenue | Cash | 953.48 | D018 | 2025-10-14 | return |
| 28 | Inventory Shrinkage Expense | Inventory | 368.24 | D019, D020 | 2025-12-31 | stock_adjustment |
| 29 | Sales Revenue | Cash | 1,322.26 | D021 | 2025-09-08 | return |
| 30 | Sales Revenue | Cash | 761.27 | D022 | 2025-09-11 | return |
| 31 | Sales Revenue | Cash | 771.37 | D023 | 2025-10-28 | return |
| 32 | Inventory Shrinkage Expense | Inventory | 1,098.00 | D024, D025 | 2025-12-31 | stock_adjustment |
| 33 | Cash | Sales Revenue | 14,811.42 | D026, D027 | 2025-07-08 | retail_sale_cash |
| 34 | Card Settlement Clearing | Sales Revenue | 51,326.55 | D026, D027 | 2025-07-08 | retail_sale_card |
| 35 | Cost of Goods Sold | Inventory | 33,801.17 | D026, D027 | 2025-07-08 | retail_sale_cogs |
| 36 | Cash | Sales Tax Payable | 2,962.28 | D026, D027 | 2025-07-08 | retail_sale_cash_tax |
| 37 | Card Settlement Clearing | Sales Tax Payable | 10,265.31 | D026, D027 | 2025-07-08 | retail_sale_card_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 263,953.08
- Inventory: -34,555.42
- Card Settlement Clearing: 112,982.64
- Store Fixtures: 160,162.68
- Office Supplies: 4,099.37
- Input Tax Receivable: 7,103.03
- Accumulated Depreciation: -45,609.12

**Liabilities**
- Accounts Payable: 30,680.08
- Unearned Revenue: 12,493.97
- Accrued Expenses: 6,384.12
- Loans Payable: 161,386.25
- Sales Tax Payable: 32,453.96
- Notes Payable: 93,922.84

**Equity**
- Retained Earnings: 18,122.14
- Owner's Equity: 112,692.90

**Totals:** Assets = 468,136.26; Liabilities = 337,321.22; Equity = 130,815.04
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
