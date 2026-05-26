# Verification Packet — COV_RET_M5_0034

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 5
- **Period type:** month
- **Period label:** July 2025
- **Period start → end:** 2025-07-01 → 2025-07-31
- **Entity:** Summit Clinic
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 18
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-07-01_

**Assets**
- Cash: 19,220.71
- Inventory: 21,611.46
- Card Settlement Clearing: 549.73
- Store Fixtures: 4,932.77
- Office Supplies: 360.41

**Liabilities**
- Accounts Payable: 4,760.61
- Accrued Expenses: 1,775.52
- Loans Payable: 3,459.09

**Equity**
- Retained Earnings: 3,058.98
- Owner's Equity: 33,620.88


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
  - Section assets | Account Cash | Amount EUR 19.220,71
  - Section assets | Account Inventory | Amount EUR 21.611,46
  - Section assets | Account Card Settlement Clearing | Amount EUR 549,73
  - Section assets | Account Store Fixtures | Amount EUR 4.932,77
  - Section assets | Account Office Supplies | Amount EUR 360,41
  - Section liabilities | Account Accounts Payable | Amount EUR 4.760,61
  - Section liabilities | Account Accrued Expenses | Amount EUR 1.775,52
  - Section liabilities | Account Loans Payable | Amount EUR 3.459,09
  - Section equity | Account Retained Earnings | Amount EUR 3.058,98
  - Section equity | Account Owner's Equity | Amount EUR 33.620,88

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-04

```
SUPPLIER INVOICE
================

From
----
Summit Clinic
14 King Street, Pune
Date: 04/07/2025

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: July 2025

Terms
-----
Due Date: 25/07/2025

Supplier Header
---------------
Supplier: Vertex Supply Co.
Expense Category: Inventory
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 25/07/2025
Subtotal: EUR 2.889,37
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 238,37
Total: EUR 3.127,74

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 22 | Unit Cost EUR 56,95 | Amount EUR 1.252,81
  - Description Widget B | Quantity 4 | Unit Cost EUR 409,14 | Amount EUR 1.636,56

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-07-11

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Summit Clinic
Gross Sales: EUR 26.335,11
Returns: 804,31
Net Sales: EUR 25.530,80
Tax Label: US Sales Tax
Tax Amount: EUR 1.595,67
COGS Amount: EUR 16.148,89
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: EUR 4.176,47
Card Sales: EUR 22.950,00
Units Sold: 187
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-07-11

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: HarborPay
Batch Total: EUR 22.950,00
Fee Amount: EUR 413,10
Expected Deposit: EUR 22.536,90
Terminal ID: TERM-0001
```

### Document D016 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-07-13

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0002
Store Name: Summit Clinic
Gross Sales: EUR 7.162,55
Returns: 275,40
Net Sales: EUR 6.887,15
Tax Label: US Sales Tax
Tax Amount: EUR 568,19
COGS Amount: EUR 4.071,41
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: EUR 1.784,05
Card Sales: EUR 5.671,29
Units Sold: 273
```

### Document D017 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-07-13

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0002
Processor: ClearRoute
Batch Total: EUR 5.671,29
Fee Amount: EUR 102,08
Expected Deposit: EUR 5.569,21
Terminal ID: TERM-0002
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-18

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Oakline Services
Asset Name: CNC router
Asset Tag: TAG-0001
Useful Life Months: 24
Total: EUR 21.053,75
Paid Cash: EUR 8.059,76
Financed Amount: EUR 12.993,99
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-07-19

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: EUR 12.248,45
Draw Amount: EUR 15.037,00
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 27.285,45
Note: Scheduled lender activity for the selected period.
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-07-21

```
PAYROLL SUMMARY
===============

From
----
Summit Clinic
14 King Street, Pune
Date: 21/07/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: July 2025
Headcount: 12
Gross Pay: EUR 12.347,94
Employer Tax: 1.123,78
Cash Outflow: EUR 13.471,72

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D015 — Return Note

- **Type:** `return_note`
- **Role:** `posting_doc`
- **Date:** 2025-07-21

```
RETURN NOTE
===========

Return Summary
--------------
Return ID: RTN-0001
Reason: Shelf defect
Amount: EUR 200,12
Reference: SALE-REF-0001
```

### Document D005 — Card Settlement Report

- **Type:** `card_settlement_report`
- **Role:** `posting_doc`
- **Date:** 2025-07-23

```
CARD SETTLEMENT REPORT
======================

Settlement Summary
------------------
Settlement ID: SETTLE-0001
Processor: ClearRoute
Gross Amount: EUR 22.950,00
Fees: EUR 413,10
Net Deposit: EUR 22.536,90
Deposit Date: 23/07/2025

Linked Batches
--------------
Batch References:
  - BATCH-0001
```

### Document D010 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-07-26

```
UTILITY INVOICE
===============

From
----
Summit Clinic
14 King Street, Pune
Date: 26/07/2025

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: utilities_statement
Period: July 2025

Terms
-----
Due Date: 10/08/2025

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: July 2025
Due Date: 10/08/2025
Total: EUR 1.850,69

Charges
-------
Charges:
  - Description Electricity | Amount EUR 649,17
  - Description Water | Amount EUR 1.201,52

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-07-27

```
PAYMENT ADVICE
==============

From
----
Summit Clinic
14 King Street, Pune
Date: 27/07/2025

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: July 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Vertex Supply Co.
Amount: EUR 2.563,48
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D014 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-07-27

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Stonebridge Finance
Opening Principal: EUR 43.358,52
Draw Amount: EUR 0,00
Principal Paid: EUR 10.112,16
Interest Paid: EUR 647,23
Ending Principal: EUR 33.246,36
Note: Scheduled lender activity for the selected period.
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-07-31

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
  - Sku SKU-0001 | Description Filter Pack | System Qty 100 | Counted Qty 92 | Unit Cost EUR
 16,21
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2025-07-31

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: EUR 129,68
Reference Sheet: COUNT-0001
```

### Document D013 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-07-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: CNC router
Asset Tag: TAG-0001
Cost: EUR 21.053,75
Useful Life Months: 24
Current Period Charge: EUR 877,24
Accumulated Depreciation: 877,24
```

### Document D018 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-07-31

```
BANK STATEMENT
==============

From
----
Summit Clinic
14 King Street, Pune
Date: 31/07/2025

Reference Box
-------------
Document ID: D018
Document Type: bank_statement
Period: July 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0034
Statement Currency: EUR
Opening Balance: EUR 19.220,71
Closing Balance: EUR 27.700,66

Statement Rows
--------------
Rows:
  - Date 11/07/2025 | Description Cash till SALES-0001 | Amount EUR 4.176,47 | Running 
Balance EUR 23.397,18
  - Date 13/07/2025 | Description Cash till SALES-0002 | Amount EUR 1.784,05 | Running 
Balance EUR 25.181,23
  - Date 18/07/2025 | Description Asset purchase ASSET-0001 | Amount EUR -8.059,76 | Running
 Balance EUR 17.121,47
  - Date 19/07/2025 | Description Loan draw LOAN-0001 | Amount EUR 15.037,00 | Running 
Balance EUR 32.158,47
  - Date 21/07/2025 | Description Payroll PAYRUN-0001 | Amount EUR -13.471,72 | Running 
Balance EUR 18.686,75
  - Date 21/07/2025 | Description Return RTN-0001 | Amount EUR -200,12 | Running Balance EUR
 18.486,63
  - Date 23/07/2025 | Description Card settlement SETTLE-0001 | Amount EUR 22.536,90 | 
Running Balance EUR 41.023,53
  - Date 27/07/2025 | Description Loan payment LOAN-0002 | Amount EUR -10.759,39 | Running 
Balance EUR 30.264,14
  - Date 27/07/2025 | Description Supplier settlement BILL-0001 | Amount EUR -2.563,48 | 
Running Balance EUR 27.700,66

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
| 1 | Inventory | Accounts Payable | 2,889.37 | D002 | 2025-07-04 | inventory_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 238.37 | D002 | 2025-07-04 | inventory_purchase_tax |
| 3 | Cash | Sales Revenue | 3,930.80 | D003, D004 | 2025-07-11 | retail_sale_cash |
| 4 | Card Settlement Clearing | Sales Revenue | 21,600.00 | D003, D004 | 2025-07-11 | retail_sale_card |
| 5 | Cost of Goods Sold | Inventory | 16,148.89 | D003, D004 | 2025-07-11 | retail_sale_cogs |
| 6 | Cash | Sales Tax Payable | 245.67 | D003, D004 | 2025-07-11 | retail_sale_cash_tax |
| 7 | Card Settlement Clearing | Sales Tax Payable | 1,350.00 | D003, D004 | 2025-07-11 | retail_sale_card_tax |
| 8 | Cash | Card Settlement Clearing | 22,536.90 | D005, D004 | 2025-07-23 | card_settlement_deposit |
| 9 | Maintenance Expense | Card Settlement Clearing | 413.10 | D005, D004 | 2025-07-23 | card_settlement_fees |
| 10 | Accounts Payable | Cash | 2,563.48 | D006, D002 | 2025-07-27 | supplier_payment |
| 11 | Salaries Expense | Cash | 12,347.94 | D007 | 2025-07-21 | payroll_gross |
| 12 | Payroll Tax Expense | Cash | 1,123.78 | D007 | 2025-07-21 | payroll_tax |
| 13 | Inventory Shrinkage Expense | Inventory | 129.68 | D008, D009 | 2025-07-31 | stock_adjustment |
| 14 | Utilities Expense | Accounts Payable | 1,850.69 | D010 | 2025-07-26 | utilities_bill |
| 15 | Cash | Loans Payable | 15,037.00 | D011 | 2025-07-19 | loan_draw |
| 16 | Store Fixtures | Cash | 8,059.76 | D012 | 2025-07-18 | equipment_purchase_cash |
| 17 | Store Fixtures | Notes Payable | 12,993.99 | D012 | 2025-07-18 | equipment_purchase_financed |
| 18 | Depreciation Expense | Accumulated Depreciation | 877.24 | D013 | 2025-07-31 | depreciation |
| 19 | Loans Payable | Cash | 10,112.16 | D014 | 2025-07-27 | loan_repayment_principal |
| 20 | Interest Expense | Cash | 647.23 | D014 | 2025-07-27 | loan_repayment_interest |
| 21 | Sales Revenue | Cash | 200.12 | D015 | 2025-07-21 | return |
| 22 | Cash | Sales Revenue | 1,648.08 | D016, D017 | 2025-07-13 | retail_sale_cash |
| 23 | Card Settlement Clearing | Sales Revenue | 5,239.07 | D016, D017 | 2025-07-13 | retail_sale_card |
| 24 | Cost of Goods Sold | Inventory | 4,071.41 | D016, D017 | 2025-07-13 | retail_sale_cogs |
| 25 | Cash | Sales Tax Payable | 135.97 | D016, D017 | 2025-07-13 | retail_sale_cash_tax |
| 26 | Card Settlement Clearing | Sales Tax Payable | 432.22 | D016, D017 | 2025-07-13 | retail_sale_card_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 27,700.66
- Inventory: 4,150.85
- Card Settlement Clearing: 6,221.02
- Store Fixtures: 25,986.52
- Office Supplies: 360.41
- Input Tax Receivable: 238.37
- Accumulated Depreciation: -877.24

**Liabilities**
- Accounts Payable: 7,175.56
- Accrued Expenses: 1,775.52
- Loans Payable: 8,383.93
- Sales Tax Payable: 2,163.86
- Notes Payable: 12,993.99

**Equity**
- Retained Earnings: -2,333.15
- Owner's Equity: 33,620.88

**Totals:** Assets = 63,780.59; Liabilities = 32,492.86; Equity = 31,287.73
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
