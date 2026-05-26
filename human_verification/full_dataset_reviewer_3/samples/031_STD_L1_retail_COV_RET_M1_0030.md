# Verification Packet — COV_RET_M1_0030

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 1
- **Period type:** month
- **Period label:** June 2024
- **Period start → end:** 2024-06-01 → 2024-06-30
- **Entity:** Pioneer Property Services
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 5
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-06-01_

**Assets**
- Cash: 29,080.20
- Inventory: 23,641.22

**Liabilities**
- Accounts Payable: 3,771.32

**Equity**
- Owner's Equity: 48,950.10


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-06-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-06-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $29,080.20
  - Section assets | Account Inventory | Amount $23,641.22
  - Section liabilities | Account Accounts Payable | Amount $3,771.32
  - Section equity | Account Owner's Equity | Amount $48,950.10

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-08

```
SUPPLIER INVOICE
================

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Date: 2024-06-08

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: June 2024

Terms
-----
Due Date: 2024-06-18

Supplier Header
---------------
Supplier: Oakline Services
Expense Category: Inventory
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 2024-06-18
Total: $3,539.76

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 9 | Unit Cost $146.70 | Amount $1,320.34
  - Description Widget B | Quantity 16 | Unit Cost $138.71 | Amount $2,219.42

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2024-06-14

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Pioneer Property Services
Gross Sales: $4,667.74
Returns: 105.98
Net Sales: $4,561.76
Tax Label: 
Tax Amount: $0.00
COGS Amount: $2,551.02
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: $700.49
Card Sales: $3,861.27
Units Sold: 125
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2024-06-14

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: HarborPay
Batch Total: $3,861.27
Fee Amount: $69.50
Expected Deposit: $3,791.77
Terminal ID: TERM-0001
```

### Document D005 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
BANK STATEMENT
==============

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Date: 2024-06-30

Reference Box
-------------
Document ID: D005
Document Type: bank_statement
Period: June 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0030
Statement Currency: USD
Opening Balance: $29,080.20
Closing Balance: $29,780.69

Statement Rows
--------------
Rows:
  - Date 2024-06-14 | Description Cash till SALES-0001 | Amount $700.49 | Running Balance 
$29,780.69

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D005
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 3,539.76 | D002 | 2024-06-08 | inventory_purchase |
| 2 | Cash | Sales Revenue | 700.49 | D003, D004 | 2024-06-14 | retail_sale_cash |
| 3 | Card Settlement Clearing | Sales Revenue | 3,861.27 | D003, D004 | 2024-06-14 | retail_sale_card |
| 4 | Cost of Goods Sold | Inventory | 2,551.02 | D003, D004 | 2024-06-14 | retail_sale_cogs |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 29,780.69
- Inventory: 24,629.96
- Card Settlement Clearing: 3,861.27

**Liabilities**
- Accounts Payable: 7,311.08

**Equity**
- Owner's Equity: 48,950.10
- Retained Earnings: 2,010.74

**Totals:** Assets = 58,271.92; Liabilities = 7,311.08; Equity = 50,960.84
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
