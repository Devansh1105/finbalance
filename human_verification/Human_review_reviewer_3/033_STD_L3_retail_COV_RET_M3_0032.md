# Verification Packet — COV_RET_M3_0032

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 3
- **Period type:** month
- **Period label:** February 2025
- **Period start → end:** 2025-02-01 → 2025-02-28
- **Entity:** Cedar Retail Group
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 10
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-02-01_

**Assets**
- Cash: 23,716.62
- Inventory: 22,862.05
- Card Settlement Clearing: 964.03
- Office Supplies: 303.01

**Liabilities**
- Accounts Payable: 2,908.78
- Accrued Expenses: 1,069.94

**Equity**
- Retained Earnings: 5,624.21
- Owner's Equity: 38,242.78


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-02-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/02/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 23,716.62
  - Section assets | Account Inventory | Amount GBP 22,862.05
  - Section assets | Account Card Settlement Clearing | Amount GBP 964.03
  - Section assets | Account Office Supplies | Amount GBP 303.01
  - Section liabilities | Account Accounts Payable | Amount GBP 2,908.78
  - Section liabilities | Account Accrued Expenses | Amount GBP 1,069.94
  - Section equity | Account Retained Earnings | Amount GBP 5,624.21
  - Section equity | Account Owner's Equity | Amount GBP 38,242.78

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-04

```
SUPPLIER INVOICE
================

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Document Date: 04/02/2025

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: February 2025

Terms
-----
Due Date: 24/02/2025

Supplier Header
---------------
Supplier: Meridian Support LLP
Expense Category: Inventory
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 24/02/2025
Subtotal: GBP 6,030.84
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: GBP 603.08
Total: GBP 6,633.92

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 8 | Unit Cost GBP 150.78 | Amount GBP 1,206.24
  - Description Widget B | Quantity 29 | Unit Cost GBP 166.37 | Amount GBP 4,824.60

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-02-12

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Cedar Retail Group
Gross Sales: GBP 16,421.30
Returns: 383.30
Net Sales: GBP 16,038.00
Tax Label: VAT
Tax Amount: GBP 1,603.80
COGS Amount: GBP 10,272.68
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: GBP 2,711.40
Card Sales: GBP 14,930.40
Units Sold: 87
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-02-12

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: HarborPay
Batch Total: GBP 14,930.40
Fee Amount: GBP 268.75
Expected Deposit: GBP 14,661.65
Terminal ID: TERM-0001
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-02-22

```
PAYMENT ADVICE
==============

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 22/02/2025

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: February 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Meridian Support LLP
Amount: GBP 6,633.92
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
- **Date:** 2025-02-23

```
PAYROLL SUMMARY
===============

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 23/02/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: February 2025
Headcount: 5
Gross Pay: GBP 7,407.63
Employer Tax: 902.56
Cash Outflow: GBP 8,310.19

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D005 — Card Settlement Report

- **Type:** `card_settlement_report`
- **Role:** `posting_doc`
- **Date:** 2025-02-24

```
CARD SETTLEMENT REPORT
======================

Settlement Summary
------------------
Settlement ID: SETTLE-0001
Processor: ClearRoute
Gross Amount: GBP 14,930.40
Fees: GBP 268.75
Net Deposit: GBP 14,661.65
Deposit Date: 24/02/2025

Linked Batches
--------------
Batch References:
  - BATCH-0001
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-02-28

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
  - Sku SKU-0001 | Description Filter Pack | System Qty 100 | Counted Qty 92 | Unit Cost GBP
 13.34
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2025-02-28

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: GBP 106.72
Reference Sheet: COUNT-0001
```

### Document D010 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-02-28

```
BANK STATEMENT
==============

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Document Date: 28/02/2025

Reference Box
-------------
Document ID: D010
Document Type: bank_statement
Period: February 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0032
Statement Currency: GBP
Opening Balance: GBP 23,716.62
Closing Balance: GBP 26,145.56

Statement Rows
--------------
Rows:
  - Date 12/02/2025 | Description Cash till SALES-0001 | Amount GBP 2,711.40 | Running 
Balance GBP 26,428.02
  - Date 22/02/2025 | Description Supplier settlement BILL-0001 | Amount GBP -6,633.92 | 
Running Balance GBP 19,794.10
  - Date 23/02/2025 | Description Payroll PAYRUN-0001 | Amount GBP -8,310.19 | Running 
Balance GBP 11,483.91
  - Date 24/02/2025 | Description Card settlement SETTLE-0001 | Amount GBP 14,661.65 | 
Running Balance GBP 26,145.56

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 6,030.84 | D002 | 2025-02-04 | inventory_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 603.08 | D002 | 2025-02-04 | inventory_purchase_tax |
| 3 | Cash | Sales Revenue | 2,464.91 | D003, D004 | 2025-02-12 | retail_sale_cash |
| 4 | Card Settlement Clearing | Sales Revenue | 13,573.09 | D003, D004 | 2025-02-12 | retail_sale_card |
| 5 | Cost of Goods Sold | Inventory | 10,272.68 | D003, D004 | 2025-02-12 | retail_sale_cogs |
| 6 | Cash | Sales Tax Payable | 246.49 | D003, D004 | 2025-02-12 | retail_sale_cash_tax |
| 7 | Card Settlement Clearing | Sales Tax Payable | 1,357.31 | D003, D004 | 2025-02-12 | retail_sale_card_tax |
| 8 | Cash | Card Settlement Clearing | 14,661.65 | D005, D004 | 2025-02-24 | card_settlement_deposit |
| 9 | Maintenance Expense | Card Settlement Clearing | 268.75 | D005, D004 | 2025-02-24 | card_settlement_fees |
| 10 | Accounts Payable | Cash | 6,633.92 | D006, D002 | 2025-02-22 | supplier_payment |
| 11 | Salaries Expense | Cash | 7,407.63 | D007 | 2025-02-23 | payroll_gross |
| 12 | Payroll Tax Expense | Cash | 902.56 | D007 | 2025-02-23 | payroll_tax |
| 13 | Inventory Shrinkage Expense | Inventory | 106.72 | D008, D009 | 2025-02-28 | stock_adjustment |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 26,145.56
- Inventory: 18,513.49
- Card Settlement Clearing: 964.03
- Office Supplies: 303.01
- Input Tax Receivable: 603.08

**Liabilities**
- Accounts Payable: 2,908.78
- Accrued Expenses: 1,069.94
- Sales Tax Payable: 1,603.80

**Equity**
- Retained Earnings: 2,703.87
- Owner's Equity: 38,242.78

**Totals:** Assets = 46,529.17; Liabilities = 5,582.52; Equity = 40,946.65
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
- [ ] Yes, doc_refs are correct
- [x] Mostly correct with minor mismatches
- [ ] Doc_refs are systematically wrong
- Notes: Small ref overlap on the customer payment line. Not material.

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
