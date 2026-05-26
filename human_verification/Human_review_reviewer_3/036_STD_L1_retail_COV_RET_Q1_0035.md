# Verification Packet — COV_RET_Q1_0035

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 1
- **Period type:** quarter
- **Period label:** Q2 FY 2025-26
- **Period start → end:** 2025-07-01 → 2025-09-30
- **Entity:** Summit Distribution
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `none`
- **Document count:** 7
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-07-01_

**Assets**
- Cash: 36,015.97
- Inventory: 12,944.17

**Liabilities**
- Accounts Payable: 5,195.82

**Equity**
- Owner's Equity: 43,764.32


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
  - Section assets | Account Cash | Amount GBP 36,015.97
  - Section assets | Account Inventory | Amount GBP 12,944.17
  - Section liabilities | Account Accounts Payable | Amount GBP 5,195.82
  - Section equity | Account Owner's Equity | Amount GBP 43,764.32

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-05

```
SUPPLIER INVOICE
================

From
----
Summit Distribution
14 King Street, Pune
Document Date: 05/07/2025

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: Q2 FY 2025-26

Terms
-----
Due Date: 18/07/2025

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Expense Category: Inventory
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 18/07/2025
Total: GBP 3,755.19

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 17 | Unit Cost GBP 90.31 | Amount GBP 1,535.33
  - Description Widget B | Quantity 7 | Unit Cost GBP 317.12 | Amount GBP 2,219.86

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D005 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-08-12

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0002
Store Name: Summit Distribution
Gross Sales: GBP 13,443.95
Returns: 173.10
Net Sales: GBP 13,270.85
Tax Label: 
Tax Amount: GBP 0.00
COGS Amount: GBP 8,128.05
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: GBP 4,234.45
Card Sales: GBP 9,036.40
Units Sold: 172
```

### Document D006 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-08-12

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0002
Processor: ClearRoute
Batch Total: GBP 9,036.40
Fee Amount: GBP 162.66
Expected Deposit: GBP 8,873.74
Terminal ID: TERM-0002
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-08-23

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Summit Distribution
Gross Sales: GBP 12,273.92
Returns: 280.57
Net Sales: GBP 11,993.35
Tax Label: 
Tax Amount: GBP 0.00
COGS Amount: GBP 7,531.30
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: GBP 2,008.12
Card Sales: GBP 9,985.23
Units Sold: 196
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-08-23

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: HarborPay
Batch Total: GBP 9,985.23
Fee Amount: GBP 179.73
Expected Deposit: GBP 9,805.50
Terminal ID: TERM-0001
```

### Document D007 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-09-30

```
BANK STATEMENT
==============

From
----
Summit Distribution
14 King Street, Pune
Date: 30/09/2025

Reference Box
-------------
Document ID: D007
Document Type: bank_statement
Period: Q2 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0035
Statement Currency: GBP
Opening Balance: GBP 36,015.97
Closing Balance: GBP 42,258.54

Statement Rows
--------------
Rows:
  - Date 12/08/2025 | Description Cash till SALES-0002 | Amount GBP 4,234.45 | Running 
Balance GBP 40,250.42
  - Date 23/08/2025 | Description Cash till SALES-0001 | Amount GBP 2,008.12 | Running 
Balance GBP 42,258.54

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D007
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 3,755.19 | D002 | 2025-07-05 | inventory_purchase |
| 2 | Cash | Sales Revenue | 2,008.12 | D003, D004 | 2025-08-23 | retail_sale_cash |
| 3 | Card Settlement Clearing | Sales Revenue | 9,985.23 | D003, D004 | 2025-08-23 | retail_sale_card |
| 4 | Cost of Goods Sold | Inventory | 7,531.30 | D003, D004 | 2025-08-23 | retail_sale_cogs |
| 5 | Cash | Sales Revenue | 4,234.45 | D005, D006 | 2025-08-12 | retail_sale_cash |
| 6 | Card Settlement Clearing | Sales Revenue | 9,036.40 | D005, D006 | 2025-08-12 | retail_sale_card |
| 7 | Cost of Goods Sold | Inventory | 8,128.05 | D005, D006 | 2025-08-12 | retail_sale_cogs |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 42,258.54
- Inventory: 1,040.01
- Card Settlement Clearing: 19,021.63

**Liabilities**
- Accounts Payable: 8,951.01

**Equity**
- Owner's Equity: 43,764.32
- Retained Earnings: 9,604.85

**Totals:** Assets = 62,320.18; Liabilities = 8,951.01; Equity = 53,369.17
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
