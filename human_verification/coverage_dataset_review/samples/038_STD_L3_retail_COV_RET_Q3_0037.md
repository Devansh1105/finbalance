# Verification Packet — COV_RET_Q3_0037

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 3
- **Period type:** quarter
- **Period label:** Q3 FY 2025
- **Period start → end:** 2025-07-01 → 2025-09-30
- **Entity:** Silverline Retail Group
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 14
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-07-01_

**Assets**
- Cash: 38,586.74
- Inventory: 18,828.19
- Card Settlement Clearing: 2,843.20
- Office Supplies: 803.95

**Liabilities**
- Accounts Payable: 7,540.14
- Unearned Revenue: 4,102.24
- Accrued Expenses: 1,105.67

**Equity**
- Retained Earnings: 3,822.07
- Owner's Equity: 44,491.96


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-07-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/07/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 38.586,74
  - Section assets | Account Inventory | Amount EUR 18.828,19
  - Section assets | Account Card Settlement Clearing | Amount EUR 2.843,20
  - Section assets | Account Office Supplies | Amount EUR 803,95
  - Section liabilities | Account Accounts Payable | Amount EUR 7.540,14
  - Section liabilities | Account Unearned Revenue | Amount EUR 4.102,24
  - Section liabilities | Account Accrued Expenses | Amount EUR 1.105,67
  - Section equity | Account Retained Earnings | Amount EUR 3.822,07
  - Section equity | Account Owner's Equity | Amount EUR 44.491,96

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-19

```
SUPPLIER INVOICE
================

From
----
Silverline Retail Group
220 Lake View Road, Bengaluru
Date: 19/07/2025

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: Q3 FY 2025

Terms
-----
Due Date: 30/07/2025

Supplier Header
---------------
Supplier: Meridian Support LLP
Expense Category: Inventory
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 30/07/2025
Subtotal: EUR 2.148,80
Tax Label: Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 155,79
Total: EUR 2.304,59

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 5 | Unit Cost EUR 92,53 | Amount EUR 462,65
  - Description Widget B | Quantity 22 | Unit Cost EUR 76,64 | Amount EUR 1.686,15

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D013 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-07-19

```
SECONDARY COPY
==============

From
----
Silverline Retail Group
220 Lake View Road, Bengaluru
Date: 19/07/2025

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D013
Document Type: secondary_copy
Period: Q3 FY 2025

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0001
Counterparty: Meridian Support LLP
Total: EUR 2.304,59
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D011 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-07-31

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0002
Store Name: Silverline Retail Group
Gross Sales: EUR 30.660,49
Returns: 1.272,40
Net Sales: EUR 29.388,09
Tax Label: Sales Tax
Tax Amount: EUR 2.424,52
COGS Amount: EUR 18.665,08
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: EUR 4.878,14
Card Sales: EUR 26.934,47
Units Sold: 252
```

### Document D012 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-07-31

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0002
Processor: HarborPay
Batch Total: EUR 26.934,47
Fee Amount: EUR 484,82
Expected Deposit: EUR 26.449,65
Terminal ID: TERM-0002
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-08-16

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Silverline Retail Group
Gross Sales: EUR 21.384,36
Returns: 1.064,67
Net Sales: EUR 20.319,69
Tax Label: Sales Tax
Tax Amount: EUR 1.676,37
COGS Amount: EUR 10.432,38
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: EUR 5.351,36
Card Sales: EUR 16.644,70
Units Sold: 68
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-08-16

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: ClearRoute
Batch Total: EUR 16.644,70
Fee Amount: EUR 299,60
Expected Deposit: EUR 16.345,10
Terminal ID: TERM-0001
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-09-01

```
PAYMENT ADVICE
==============

From
----
Silverline Retail Group
220 Lake View Road, Bengaluru
Document Date: 01/09/2025

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q3 FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Meridian Support LLP
Amount: EUR 2.304,59
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
- **Date:** 2025-09-08

```
PAYROLL SUMMARY
===============

From
----
Silverline Retail Group
220 Lake View Road, Bengaluru
Date: 08/09/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q3 FY 2025
Headcount: 8
Gross Pay: EUR 13.816,81
Employer Tax: 1.843,07
Cash Outflow: EUR 15.659,88

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D005 — Card Settlement Report

- **Type:** `card_settlement_report`
- **Role:** `posting_doc`
- **Date:** 2025-09-17

```
CARD SETTLEMENT REPORT
======================

Settlement Summary
------------------
Settlement ID: SETTLE-0001
Processor: HarborPay
Gross Amount: EUR 16.644,70
Fees: EUR 299,60
Net Deposit: EUR 16.345,10
Deposit Date: 17/09/2025

Linked Batches
--------------
Batch References:
  - BATCH-0001
```

### Document D010 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-09-20

```
UTILITY INVOICE
===============

From
----
Silverline Retail Group
220 Lake View Road, Bengaluru
Date: 20/09/2025

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: utilities_statement
Period: Q3 FY 2025

Terms
-----
Due Date: 05/10/2025

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: Q3 FY 2025
Due Date: 05/10/2025
Total: EUR 2.844,09

Charges
-------
Charges:
  - Description Electricity | Amount EUR 1.008,10
  - Description Water | Amount EUR 1.835,99

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-09-30

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0001
Location: Warehouse A

Counted Items
-------------
Items:
  - Sku SKU-0001 | Description Refill Pack | System Qty 100 | Counted Qty 98 | Unit Cost EUR
 31,85
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2025-09-30

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: EUR 63,70
Reference Sheet: COUNT-0001
```

### Document D014 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-09-30

```
BANK STATEMENT
==============

From
----
Silverline Retail Group
220 Lake View Road, Bengaluru
Document Date: 30/09/2025

Reference Box
-------------
Document ID: D014
Document Type: bank_statement
Period: Q3 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0037
Statement Currency: EUR
Opening Balance: EUR 38.586,74
Closing Balance: EUR 47.196,87

Statement Rows
--------------
Rows:
  - Date 31/07/2025 | Description Cash till SALES-0002 | Amount EUR 4.878,14 | Running 
Balance EUR 43.464,88
  - Date 16/08/2025 | Description Cash till SALES-0001 | Amount EUR 5.351,36 | Running 
Balance EUR 48.816,24
  - Date 01/09/2025 | Description Supplier settlement BILL-0001 | Amount EUR -2.304,59 | 
Running Balance EUR 46.511,65
  - Date 08/09/2025 | Description Payroll PAYRUN-0001 | Amount EUR -15.659,88 | Running 
Balance EUR 30.851,77
  - Date 17/09/2025 | Description Card settlement SETTLE-0001 | Amount EUR 16.345,10 | 
Running Balance EUR 47.196,87

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 2,148.80 | D002 | 2025-07-19 | inventory_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 155.79 | D002 | 2025-07-19 | inventory_purchase_tax |
| 3 | Cash | Sales Revenue | 4,943.52 | D003, D004 | 2025-08-16 | retail_sale_cash |
| 4 | Card Settlement Clearing | Sales Revenue | 15,376.17 | D003, D004 | 2025-08-16 | retail_sale_card |
| 5 | Cost of Goods Sold | Inventory | 10,432.38 | D003, D004 | 2025-08-16 | retail_sale_cogs |
| 6 | Cash | Sales Tax Payable | 407.84 | D003, D004 | 2025-08-16 | retail_sale_cash_tax |
| 7 | Card Settlement Clearing | Sales Tax Payable | 1,268.53 | D003, D004 | 2025-08-16 | retail_sale_card_tax |
| 8 | Cash | Card Settlement Clearing | 16,345.10 | D005, D004 | 2025-09-17 | card_settlement_deposit |
| 9 | Maintenance Expense | Card Settlement Clearing | 299.60 | D005, D004 | 2025-09-17 | card_settlement_fees |
| 10 | Accounts Payable | Cash | 2,304.59 | D006, D002 | 2025-09-01 | supplier_payment |
| 11 | Salaries Expense | Cash | 13,816.81 | D007 | 2025-09-08 | payroll_gross |
| 12 | Payroll Tax Expense | Cash | 1,843.07 | D007 | 2025-09-08 | payroll_tax |
| 13 | Inventory Shrinkage Expense | Inventory | 63.70 | D008, D009 | 2025-09-30 | stock_adjustment |
| 14 | Utilities Expense | Accounts Payable | 2,844.09 | D010 | 2025-09-20 | utilities_bill |
| 15 | Cash | Sales Revenue | 4,506.36 | D011, D012 | 2025-07-31 | retail_sale_cash |
| 16 | Card Settlement Clearing | Sales Revenue | 24,881.73 | D011, D012 | 2025-07-31 | retail_sale_card |
| 17 | Cost of Goods Sold | Inventory | 18,665.08 | D011, D012 | 2025-07-31 | retail_sale_cogs |
| 18 | Cash | Sales Tax Payable | 371.78 | D011, D012 | 2025-07-31 | retail_sale_cash_tax |
| 19 | Card Settlement Clearing | Sales Tax Payable | 2,052.74 | D011, D012 | 2025-07-31 | retail_sale_card_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 47,196.87
- Inventory: -8,184.17
- Card Settlement Clearing: 29,777.67
- Office Supplies: 803.95
- Input Tax Receivable: 155.79

**Liabilities**
- Accounts Payable: 10,384.23
- Unearned Revenue: 4,102.24
- Accrued Expenses: 1,105.67
- Sales Tax Payable: 4,100.89

**Equity**
- Retained Earnings: 5,565.12
- Owner's Equity: 44,491.96

**Totals:** Assets = 69,750.11; Liabilities = 19,693.03; Equity = 50,057.08
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
