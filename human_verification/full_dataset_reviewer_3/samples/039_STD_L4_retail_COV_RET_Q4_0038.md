# Verification Packet — COV_RET_Q4_0038

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 4
- **Period type:** quarter
- **Period label:** Q4 FY 2026-27
- **Period start → end:** 2026-01-01 → 2026-03-31
- **Entity:** Granite Property Services
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 18
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2026-01-01_

**Assets**
- Cash: 22,548.07
- Inventory: 36,075.78
- Card Settlement Clearing: 1,233.87
- Store Fixtures: 9,225.25
- Office Supplies: 1,285.64

**Liabilities**
- Accounts Payable: 6,519.10
- Unearned Revenue: 2,060.43
- Accrued Expenses: 1,969.12
- Loans Payable: 10,891.03

**Equity**
- Retained Earnings: 15,164.32
- Owner's Equity: 33,764.61


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2026-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/01/2026
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 22,548.07
  - Section assets | Account Inventory | Amount GBP 36,075.78
  - Section assets | Account Card Settlement Clearing | Amount GBP 1,233.87
  - Section assets | Account Store Fixtures | Amount GBP 9,225.25
  - Section assets | Account Office Supplies | Amount GBP 1,285.64
  - Section liabilities | Account Accounts Payable | Amount GBP 6,519.10
  - Section liabilities | Account Unearned Revenue | Amount GBP 2,060.43
  - Section liabilities | Account Accrued Expenses | Amount GBP 1,969.12
  - Section liabilities | Account Loans Payable | Amount GBP 10,891.03
  - Section equity | Account Retained Earnings | Amount GBP 15,164.32
  - Section equity | Account Owner's Equity | Amount GBP 33,764.61

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-01-05

```
SUPPLIER INVOICE
================

From
----
Granite Property Services
90 Hill Park, Hyderabad
Document Date: 05/01/2026

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: Q4 FY 2026-27

Terms
-----
Due Date: 24/01/2026

Supplier Header
---------------
Supplier: Meridian Support LLP
Expense Category: Inventory
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 24/01/2026
Subtotal: GBP 1,365.61
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 273.12
Total: GBP 1,638.73

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 11 | Unit Cost GBP 41.20 | Amount GBP 453.18
  - Description Widget B | Quantity 13 | Unit Cost GBP 70.19 | Amount GBP 912.43

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2026-01-29

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: GBP 21,269.87
Draw Amount: GBP 120,661.85
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 141,931.72
Note: Scheduled lender activity for the selected period.
```

### Document D016 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2026-02-04

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0002
Store Name: Granite Property Services
Gross Sales: GBP 13,896.70
Returns: 222.79
Net Sales: GBP 13,673.91
Tax Label: VAT
Tax Amount: GBP 1,709.24
COGS Amount: GBP 7,881.06
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: GBP 4,640.88
Card Sales: GBP 10,742.27
Units Sold: 136
```

### Document D017 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2026-02-04

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0002
Processor: ClearRoute
Batch Total: GBP 10,742.27
Fee Amount: GBP 193.36
Expected Deposit: GBP 10,548.91
Terminal ID: TERM-0002
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-02-27

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Pace Office Mart
Asset Name: Display fixtures
Asset Tag: TAG-0001
Useful Life Months: 36
Total: GBP 101,997.95
Paid Cash: GBP 48,278.22
Financed Amount: GBP 53,719.73
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2026-03-01

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Granite Property Services
Gross Sales: GBP 41,358.87
Returns: 816.37
Net Sales: GBP 40,542.50
Tax Label: VAT
Tax Amount: GBP 5,067.81
COGS Amount: GBP 23,374.10
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: GBP 11,808.80
Card Sales: GBP 33,801.51
Units Sold: 73
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2026-03-01

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: HarborPay
Batch Total: GBP 33,801.51
Fee Amount: GBP 608.43
Expected Deposit: GBP 33,193.08
Terminal ID: TERM-0001
```

### Document D010 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2026-03-02

```
UTILITY INVOICE
===============

From
----
Granite Property Services
90 Hill Park, Hyderabad
Date: 02/03/2026

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: utilities_statement
Period: Q4 FY 2026-27

Terms
-----
Due Date: 13/03/2026

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: Q4 FY 2026-27
Due Date: 13/03/2026
Total: GBP 669.90

Charges
-------
Charges:
  - Description Electricity | Amount GBP 193.14
  - Description Water | Amount GBP 476.76

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D005 — Card Settlement Report

- **Type:** `card_settlement_report`
- **Role:** `posting_doc`
- **Date:** 2026-03-08

```
CARD SETTLEMENT REPORT
======================

Settlement Summary
------------------
Settlement ID: SETTLE-0001
Processor: HarborPay
Gross Amount: GBP 33,801.51
Fees: GBP 608.43
Net Deposit: GBP 33,193.08
Deposit Date: 08/03/2026

Linked Batches
--------------
Batch References:
  - BATCH-0001
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-03-17

```
PAYMENT ADVICE
==============

From
----
Granite Property Services
90 Hill Park, Hyderabad
Date: 17/03/2026

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q4 FY 2026-27
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Meridian Support LLP
Amount: GBP 1,132.25
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2026-03-18

```
PAYROLL SUMMARY
===============

From
----
Granite Property Services
90 Hill Park, Hyderabad
Date: 18/03/2026

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q4 FY 2026-27
Headcount: 3
Gross Pay: GBP 16,983.24
Employer Tax: 2,046.15
Cash Outflow: GBP 19,029.39

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2026-03-31

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
  - Sku SKU-0001 | Description Widget A | System Qty 100 | Counted Qty 97 | Unit Cost GBP 
20.23
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: GBP 60.69
Reference Sheet: COUNT-0001
```

### Document D013 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Store Fixtures
Asset Tag: OPEN-STO
Cost: GBP 9,225.25
Useful Life Months: 60
Current Period Charge: GBP 461.25
Accumulated Depreciation: 461.25
```

### Document D014 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2026-03-31

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
  - Sku SKU-0002 | Description Widget B | System Qty 100 | Counted Qty 92 | Unit Cost GBP 
14.89
```

### Document D015 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0002
Reason: Shrinkage found during physical count
Amount: GBP 119.12
Reference Sheet: COUNT-0002
```

### Document D018 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Granite Property Services
90 Hill Park, Hyderabad
Date: 31/03/2026

Reference Box
-------------
Document ID: D018
Document Type: bank_statement
Period: Q4 FY 2026-27

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0038
Statement Currency: GBP
Opening Balance: GBP 22,548.07
Closing Balance: GBP 124,412.82

Statement Rows
--------------
Rows:
  - Date 29/01/2026 | Description Loan draw LOAN-0001 | Amount GBP 120,661.85 | Running 
Balance GBP 143,209.92
  - Date 04/02/2026 | Description Cash till SALES-0002 | Amount GBP 4,640.88 | Running 
Balance GBP 147,850.80
  - Date 27/02/2026 | Description Asset purchase ASSET-0001 | Amount GBP -48,278.22 | 
Running Balance GBP 99,572.58
  - Date 01/03/2026 | Description Cash till SALES-0001 | Amount GBP 11,808.80 | Running 
Balance GBP 111,381.38
  - Date 08/03/2026 | Description Card settlement SETTLE-0001 | Amount GBP 33,193.08 | 
Running Balance GBP 144,574.46
  - Date 17/03/2026 | Description Supplier settlement BILL-0001 | Amount GBP -1,132.25 | 
Running Balance GBP 143,442.21
  - Date 18/03/2026 | Description Payroll PAYRUN-0001 | Amount GBP -19,029.39 | Running 
Balance GBP 124,412.82

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D018
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 1,365.61 | D002 | 2026-01-05 | inventory_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 273.12 | D002 | 2026-01-05 | inventory_purchase_tax |
| 3 | Cash | Sales Revenue | 10,496.71 | D003, D004 | 2026-03-01 | retail_sale_cash |
| 4 | Card Settlement Clearing | Sales Revenue | 30,045.79 | D003, D004 | 2026-03-01 | retail_sale_card |
| 5 | Cost of Goods Sold | Inventory | 23,374.10 | D003, D004 | 2026-03-01 | retail_sale_cogs |
| 6 | Cash | Sales Tax Payable | 1,312.09 | D003, D004 | 2026-03-01 | retail_sale_cash_tax |
| 7 | Card Settlement Clearing | Sales Tax Payable | 3,755.72 | D003, D004 | 2026-03-01 | retail_sale_card_tax |
| 8 | Cash | Card Settlement Clearing | 33,193.08 | D005, D004 | 2026-03-08 | card_settlement_deposit |
| 9 | Maintenance Expense | Card Settlement Clearing | 608.43 | D005, D004 | 2026-03-08 | card_settlement_fees |
| 10 | Accounts Payable | Cash | 1,132.25 | D006, D002 | 2026-03-17 | supplier_payment |
| 11 | Salaries Expense | Cash | 16,983.24 | D007 | 2026-03-18 | payroll_gross |
| 12 | Payroll Tax Expense | Cash | 2,046.15 | D007 | 2026-03-18 | payroll_tax |
| 13 | Inventory Shrinkage Expense | Inventory | 60.69 | D008, D009 | 2026-03-31 | stock_adjustment |
| 14 | Utilities Expense | Accounts Payable | 669.90 | D010 | 2026-03-02 | utilities_bill |
| 15 | Cash | Loans Payable | 120,661.85 | D011 | 2026-01-29 | loan_draw |
| 16 | Store Fixtures | Cash | 48,278.22 | D012 | 2026-02-27 | equipment_purchase_cash |
| 17 | Store Fixtures | Notes Payable | 53,719.73 | D012 | 2026-02-27 | equipment_purchase_financed |
| 18 | Depreciation Expense | Accumulated Depreciation | 461.25 | D013 | 2026-03-31 | depreciation |
| 19 | Inventory Shrinkage Expense | Inventory | 119.12 | D014, D015 | 2026-03-31 | stock_adjustment |
| 20 | Cash | Sales Revenue | 4,125.23 | D016, D017 | 2026-02-04 | retail_sale_cash |
| 21 | Card Settlement Clearing | Sales Revenue | 9,548.68 | D016, D017 | 2026-02-04 | retail_sale_card |
| 22 | Cost of Goods Sold | Inventory | 7,881.06 | D016, D017 | 2026-02-04 | retail_sale_cogs |
| 23 | Cash | Sales Tax Payable | 515.65 | D016, D017 | 2026-02-04 | retail_sale_cash_tax |
| 24 | Card Settlement Clearing | Sales Tax Payable | 1,193.59 | D016, D017 | 2026-02-04 | retail_sale_card_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 124,412.82
- Inventory: 6,006.42
- Card Settlement Clearing: 11,976.14
- Store Fixtures: 111,223.20
- Office Supplies: 1,285.64
- Input Tax Receivable: 273.12
- Accumulated Depreciation: -461.25

**Liabilities**
- Accounts Payable: 7,695.48
- Unearned Revenue: 2,060.43
- Accrued Expenses: 1,969.12
- Loans Payable: 131,552.88
- Sales Tax Payable: 6,777.05
- Notes Payable: 53,719.73

**Equity**
- Retained Earnings: 17,176.79
- Owner's Equity: 33,764.61

**Totals:** Assets = 254,716.09; Liabilities = 203,774.69; Equity = 50,941.40
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
