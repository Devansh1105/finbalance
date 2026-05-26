# Verification Packet — COV_RET_M4_0033

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** August 2025
- **Period start → end:** 2025-08-01 → 2025-08-31
- **Entity:** Atlas Software
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 14
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-08-01_

**Assets**
- Cash: 28,945.24
- Inventory: 21,323.70
- Card Settlement Clearing: 1,646.13
- Store Fixtures: 8,271.58
- Office Supplies: 1,019.99

**Liabilities**
- Accounts Payable: 4,826.65
- Accrued Expenses: 1,031.32
- Loans Payable: 4,632.13

**Equity**
- Retained Earnings: 9,264.14
- Owner's Equity: 41,452.40


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-08-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-08-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $28,945.24
  - Section assets | Account Inventory | Amount $21,323.70
  - Section assets | Account Card Settlement Clearing | Amount $1,646.13
  - Section assets | Account Store Fixtures | Amount $8,271.58
  - Section assets | Account Office Supplies | Amount $1,019.99
  - Section liabilities | Account Accounts Payable | Amount $4,826.65
  - Section liabilities | Account Accrued Expenses | Amount $1,031.32
  - Section liabilities | Account Loans Payable | Amount $4,632.13
  - Section equity | Account Retained Earnings | Amount $9,264.14
  - Section equity | Account Owner's Equity | Amount $41,452.40

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-05

```
SUPPLIER INVOICE
================

From
----
Atlas Software
75 Market Road, Mumbai
Date: 2025-08-05

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: August 2025

Terms
-----
Due Date: 2025-08-22

Supplier Header
---------------
Supplier: Oakline Services
Expense Category: Inventory
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 2025-08-22
Subtotal: $2,858.00
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $142.90
Total: $3,000.90

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 7 | Unit Cost $179.54 | Amount $1,256.76
  - Description Widget B | Quantity 28 | Unit Cost $57.19 | Amount $1,601.24

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-08-18

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $4,574.26
Draw Amount: $57,584.35
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $62,158.61
Note: Scheduled lender activity for the selected period.
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-18

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Beacon Industrial Supply
Asset Name: Ultrasound console
Asset Tag: TAG-0001
Useful Life Months: 60
Total: $43,828.32
Paid Cash: $11,229.03
Financed Amount: $32,599.29
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-08-19

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Atlas Software
Gross Sales: $19,216.25
Returns: 246.12
Net Sales: $18,970.13
Tax Label: GST
Tax Amount: $1,327.91
COGS Amount: $9,314.45
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: $4,359.56
Card Sales: $15,938.48
Units Sold: 268
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-08-19

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: HarborPay
Batch Total: $15,938.48
Fee Amount: $286.89
Expected Deposit: $15,651.59
Terminal ID: TERM-0001
```

### Document D005 — Card Settlement Report

- **Type:** `card_settlement_report`
- **Role:** `posting_doc`
- **Date:** 2025-08-22

```
CARD SETTLEMENT REPORT
======================

Settlement Summary
------------------
Settlement ID: SETTLE-0001
Processor: HarborPay
Gross Amount: $15,938.48
Fees: $286.89
Net Deposit: $15,651.59
Deposit Date: 2025-08-22

Linked Batches
--------------
Batch References:
  - BATCH-0001
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-08-22

```
PAYMENT ADVICE
==============

From
----
Atlas Software
75 Market Road, Mumbai
Date: 2025-08-22

To
--
Oakline Services

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: August 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Oakline Services
Amount: $2,140.22
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
- **Date:** 2025-08-24

```
PAYROLL SUMMARY
===============

From
----
Atlas Software
75 Market Road, Mumbai
Date: 2025-08-24

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: August 2025
Headcount: 6
Gross Pay: $15,161.40
Employer Tax: 1,478.46
Cash Outflow: $16,639.86

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D010 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-08-26

```
UTILITY INVOICE
===============

From
----
Atlas Software
75 Market Road, Mumbai
Date: 2025-08-26

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: utilities_statement
Period: August 2025

Terms
-----
Due Date: 2025-09-10

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: August 2025
Due Date: 2025-09-10
Total: $671.89

Charges
-------
Charges:
  - Description Electricity | Amount $160.76
  - Description Water | Amount $511.13

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-08-31

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
  - Sku SKU-0001 | Description Premium Kit | System Qty 100 | Counted Qty 98 | Unit Cost 
$9.52
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2025-08-31

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: $19.04
Reference Sheet: COUNT-0001
```

### Document D013 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-08-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Ultrasound console
Asset Tag: TAG-0001
Cost: $43,828.32
Useful Life Months: 60
Current Period Charge: $730.47
Accumulated Depreciation: 730.47
```

### Document D014 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-08-31

```
BANK STATEMENT
==============

From
----
Atlas Software
75 Market Road, Mumbai
Date: 2025-08-31

Reference Box
-------------
Document ID: D014
Document Type: bank_statement
Period: August 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0033
Statement Currency: USD
Opening Balance: $28,945.24
Closing Balance: $76,531.63

Statement Rows
--------------
Rows:
  - Date 2025-08-18 | Description Asset purchase ASSET-0001 | Amount $-11,229.03 | Running 
Balance $17,716.21
  - Date 2025-08-18 | Description Loan draw LOAN-0001 | Amount $57,584.35 | Running Balance 
$75,300.56
  - Date 2025-08-19 | Description Cash till SALES-0001 | Amount $4,359.56 | Running Balance 
$79,660.12
  - Date 2025-08-22 | Description Card settlement SETTLE-0001 | Amount $15,651.59 | Running 
Balance $95,311.71
  - Date 2025-08-22 | Description Supplier settlement BILL-0001 | Amount $-2,140.22 | 
Running Balance $93,171.49
  - Date 2025-08-24 | Description Payroll PAYRUN-0001 | Amount $-16,639.86 | Running Balance
 $76,531.63

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
| 1 | Inventory | Accounts Payable | 2,858.00 | D002 | 2025-08-05 | inventory_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 142.90 | D002 | 2025-08-05 | inventory_purchase_tax |
| 3 | Cash | Sales Revenue | 4,074.35 | D003, D004 | 2025-08-19 | retail_sale_cash |
| 4 | Card Settlement Clearing | Sales Revenue | 14,895.78 | D003, D004 | 2025-08-19 | retail_sale_card |
| 5 | Cost of Goods Sold | Inventory | 9,314.45 | D003, D004 | 2025-08-19 | retail_sale_cogs |
| 6 | Cash | Sales Tax Payable | 285.21 | D003, D004 | 2025-08-19 | retail_sale_cash_tax |
| 7 | Card Settlement Clearing | Sales Tax Payable | 1,042.70 | D003, D004 | 2025-08-19 | retail_sale_card_tax |
| 8 | Cash | Card Settlement Clearing | 15,651.59 | D005, D004 | 2025-08-22 | card_settlement_deposit |
| 9 | Maintenance Expense | Card Settlement Clearing | 286.89 | D005, D004 | 2025-08-22 | card_settlement_fees |
| 10 | Accounts Payable | Cash | 2,140.22 | D006, D002 | 2025-08-22 | supplier_payment |
| 11 | Salaries Expense | Cash | 15,161.40 | D007 | 2025-08-24 | payroll_gross |
| 12 | Payroll Tax Expense | Cash | 1,478.46 | D007 | 2025-08-24 | payroll_tax |
| 13 | Inventory Shrinkage Expense | Inventory | 19.04 | D008, D009 | 2025-08-31 | stock_adjustment |
| 14 | Utilities Expense | Accounts Payable | 671.89 | D010 | 2025-08-26 | utilities_bill |
| 15 | Cash | Loans Payable | 57,584.35 | D011 | 2025-08-18 | loan_draw |
| 16 | Store Fixtures | Cash | 11,229.03 | D012 | 2025-08-18 | equipment_purchase_cash |
| 17 | Store Fixtures | Notes Payable | 32,599.29 | D012 | 2025-08-18 | equipment_purchase_financed |
| 18 | Depreciation Expense | Accumulated Depreciation | 730.47 | D013 | 2025-08-31 | depreciation |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 76,531.63
- Inventory: 14,848.21
- Card Settlement Clearing: 1,646.13
- Store Fixtures: 52,099.90
- Office Supplies: 1,019.99
- Input Tax Receivable: 142.90
- Accumulated Depreciation: -730.47

**Liabilities**
- Accounts Payable: 6,359.22
- Accrued Expenses: 1,031.32
- Loans Payable: 62,216.48
- Sales Tax Payable: 1,327.91
- Notes Payable: 32,599.29

**Equity**
- Retained Earnings: 571.67
- Owner's Equity: 41,452.40

**Totals:** Assets = 145,558.29; Liabilities = 103,534.22; Equity = 42,024.07
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
