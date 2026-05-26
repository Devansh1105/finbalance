# Verification Packet — COV_RET_M2_0031

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 2
- **Period type:** month
- **Period label:** September 2024
- **Period start → end:** 2024-09-01 → 2024-09-30
- **Entity:** Willow Retail Group
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 9
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-09-01_

**Assets**
- Cash: 15,619.95
- Inventory: 16,507.59
- Card Settlement Clearing: 439.78
- Office Supplies: 1,154.23

**Liabilities**
- Accounts Payable: 4,630.72
- Accrued Expenses: 1,788.35

**Equity**
- Retained Earnings: 3,003.08
- Owner's Equity: 24,299.40


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-09-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/09/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 15.619,95
  - Section assets | Account Inventory | Amount EUR 16.507,59
  - Section assets | Account Card Settlement Clearing | Amount EUR 439,78
  - Section assets | Account Office Supplies | Amount EUR 1.154,23
  - Section liabilities | Account Accounts Payable | Amount EUR 4.630,72
  - Section liabilities | Account Accrued Expenses | Amount EUR 1.788,35
  - Section equity | Account Retained Earnings | Amount EUR 3.003,08
  - Section equity | Account Owner's Equity | Amount EUR 24.299,40

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-05

```
SUPPLIER INVOICE
================

From
----
Willow Retail Group
75 Market Road, Mumbai
Date: 05/09/2024

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: September 2024

Terms
-----
Due Date: 20/09/2024

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Expense Category: Inventory
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 20/09/2024
Subtotal: EUR 5.255,53
Tax Label: Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 433,58
Total: EUR 5.689,11

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 16 | Unit Cost EUR 135,96 | Amount EUR 2.175,34
  - Description Widget B | Quantity 24 | Unit Cost EUR 128,34 | Amount EUR 3.080,19

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D007 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2024-09-11

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0002
Store Name: Willow Retail Group
Gross Sales: EUR 15.276,46
Returns: 202,82
Net Sales: EUR 15.073,64
Tax Label: Sales Tax
Tax Amount: EUR 1.092,84
COGS Amount: EUR 7.643,64
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: EUR 2.851,47
Card Sales: EUR 13.315,01
Units Sold: 178
```

### Document D008 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2024-09-11

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0002
Processor: HarborPay
Batch Total: EUR 13.315,01
Fee Amount: EUR 239,67
Expected Deposit: EUR 13.075,34
Terminal ID: TERM-0002
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2024-09-13

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Willow Retail Group
Gross Sales: EUR 4.209,87
Returns: 188,25
Net Sales: EUR 4.021,62
Tax Label: Sales Tax
Tax Amount: EUR 331,78
COGS Amount: EUR 2.471,42
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: EUR 1.462,37
Card Sales: EUR 2.891,03
Units Sold: 255
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2024-09-13

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: Axis Payments
Batch Total: EUR 2.891,03
Fee Amount: EUR 52,04
Expected Deposit: EUR 2.838,99
Terminal ID: TERM-0001
```

### Document D005 — Card Settlement Report

- **Type:** `card_settlement_report`
- **Role:** `posting_doc`
- **Date:** 2024-09-22

```
CARD SETTLEMENT REPORT
======================

Settlement Summary
------------------
Settlement ID: SETTLE-0001
Processor: ClearRoute
Gross Amount: EUR 2.891,03
Fees: EUR 52,04
Net Deposit: EUR 2.838,99
Deposit Date: 22/09/2024

Linked Batches
--------------
Batch References:
  - BATCH-0001
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
Willow Retail Group
75 Market Road, Mumbai
Date: 26/09/2024

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: September 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Beacon Industrial Supply
Amount: EUR 5.689,11
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D009 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-09-30

```
BANK STATEMENT
==============

From
----
Willow Retail Group
75 Market Road, Mumbai
Date: 30/09/2024

Reference Box
-------------
Document ID: D009
Document Type: bank_statement
Period: September 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0031
Statement Currency: EUR
Opening Balance: EUR 15.619,95
Closing Balance: EUR 17.083,67

Statement Rows
--------------
Rows:
  - Date 11/09/2024 | Description Cash till SALES-0002 | Amount EUR 2.851,47 | Running 
Balance EUR 18.471,42
  - Date 13/09/2024 | Description Cash till SALES-0001 | Amount EUR 1.462,37 | Running 
Balance EUR 19.933,79
  - Date 22/09/2024 | Description Card settlement SETTLE-0001 | Amount EUR 2.838,99 | 
Running Balance EUR 22.772,78
  - Date 26/09/2024 | Description Supplier settlement BILL-0001 | Amount EUR -5.689,11 | 
Running Balance EUR 17.083,67

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D009
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 5,255.53 | D002 | 2024-09-05 | inventory_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 433.58 | D002 | 2024-09-05 | inventory_purchase_tax |
| 3 | Cash | Sales Revenue | 1,350.92 | D003, D004 | 2024-09-13 | retail_sale_cash |
| 4 | Card Settlement Clearing | Sales Revenue | 2,670.70 | D003, D004 | 2024-09-13 | retail_sale_card |
| 5 | Cost of Goods Sold | Inventory | 2,471.42 | D003, D004 | 2024-09-13 | retail_sale_cogs |
| 6 | Cash | Sales Tax Payable | 111.45 | D003, D004 | 2024-09-13 | retail_sale_cash_tax |
| 7 | Card Settlement Clearing | Sales Tax Payable | 220.33 | D003, D004 | 2024-09-13 | retail_sale_card_tax |
| 8 | Cash | Card Settlement Clearing | 2,838.99 | D005, D004 | 2024-09-22 | card_settlement_deposit |
| 9 | Maintenance Expense | Card Settlement Clearing | 52.04 | D005, D004 | 2024-09-22 | card_settlement_fees |
| 10 | Accounts Payable | Cash | 5,689.11 | D006, D002 | 2024-09-26 | supplier_payment |
| 11 | Cash | Sales Revenue | 2,658.71 | D007, D008 | 2024-09-11 | retail_sale_cash |
| 12 | Card Settlement Clearing | Sales Revenue | 12,414.93 | D007, D008 | 2024-09-11 | retail_sale_card |
| 13 | Cost of Goods Sold | Inventory | 7,643.64 | D007, D008 | 2024-09-11 | retail_sale_cogs |
| 14 | Cash | Sales Tax Payable | 192.76 | D007, D008 | 2024-09-11 | retail_sale_cash_tax |
| 15 | Card Settlement Clearing | Sales Tax Payable | 900.08 | D007, D008 | 2024-09-11 | retail_sale_card_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 17,083.67
- Inventory: 11,648.06
- Card Settlement Clearing: 13,754.79
- Office Supplies: 1,154.23
- Input Tax Receivable: 433.58

**Liabilities**
- Accounts Payable: 4,630.72
- Accrued Expenses: 1,788.35
- Sales Tax Payable: 1,424.62

**Equity**
- Retained Earnings: 11,931.24
- Owner's Equity: 24,299.40

**Totals:** Assets = 44,074.33; Liabilities = 7,843.69; Equity = 36,230.64
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
