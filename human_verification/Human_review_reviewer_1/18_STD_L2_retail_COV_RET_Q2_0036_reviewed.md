# Verification Packet — COV_RET_Q2_0036

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 2
- **Period type:** quarter
- **Period label:** Q3 FY 2024
- **Period start → end:** 2024-07-01 → 2024-09-30
- **Entity:** Cedar Operations
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 12
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-07-01_

**Assets**
- Cash: 38,495.40
- Inventory: 21,791.73
- Card Settlement Clearing: 1,435.30
- Office Supplies: 355.81

**Liabilities**
- Accounts Payable: 6,086.35
- Accrued Expenses: 1,079.54

**Equity**
- Retained Earnings: 8,807.46
- Owner's Equity: 46,104.89


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-07-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-07-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $38,495.40
  - Section assets | Account Inventory | Amount $21,791.73
  - Section assets | Account Card Settlement Clearing | Amount $1,435.30
  - Section assets | Account Office Supplies | Amount $355.81
  - Section liabilities | Account Accounts Payable | Amount $6,086.35
  - Section liabilities | Account Accrued Expenses | Amount $1,079.54
  - Section equity | Account Retained Earnings | Amount $8,807.46
  - Section equity | Account Owner's Equity | Amount $46,104.89

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D007 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-08

```
SUPPLIER INVOICE
================

From
----
Cedar Operations
14 King Street, Pune
Document Date: 2024-07-08

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D007
Document Type: supplier_invoice
Period: Q3 FY 2024

Terms
-----
Due Date: 2024-07-24

Supplier Header
---------------
Supplier: Pace Office Mart
Expense Category: Inventory
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 2024-07-24
Total: $8,705.25

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 27 | Unit Cost $82.83 | Amount $2,236.28
  - Description Widget B | Quantity 4 | Unit Cost $1,617.24 | Amount $6,468.97

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D011 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-07-08

```
SECONDARY COPY
==============

From
----
Cedar Operations
14 King Street, Pune
Document Date: 2024-07-08

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D011
Document Type: secondary_copy
Period: Q3 FY 2024

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0002
Counterparty: Pace Office Mart
Total: $8,705.25
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-16

```
SUPPLIER INVOICE
================

From
----
Cedar Operations
14 King Street, Pune
Date: 2024-07-16

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: Q3 FY 2024

Terms
-----
Due Date: 2024-08-02

Supplier Header
---------------
Supplier: Prime Utility Desk
Expense Category: Inventory
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 2024-08-02
Total: $1,583.00

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 8 | Unit Cost $77.81 | Amount $622.52
  - Description Widget B | Quantity 6 | Unit Cost $160.08 | Amount $960.48

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2024-08-15

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Cedar Operations
Gross Sales: $29,774.75
Returns: 1,301.54
Net Sales: $28,473.21
Tax Label: 
Tax Amount: $0.00
COGS Amount: $17,286.03
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: $7,831.66
Card Sales: $20,641.55
Units Sold: 238
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2024-08-15

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: HarborPay
Batch Total: $20,641.55
Fee Amount: $371.55
Expected Deposit: $20,270.00
Terminal ID: TERM-0001
```

### Document D009 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2024-08-18

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0002
Store Name: Cedar Operations
Gross Sales: $11,770.99
Returns: 377.66
Net Sales: $11,393.33
Tax Label: 
Tax Amount: $0.00
COGS Amount: $6,854.60
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: $3,545.89
Card Sales: $7,847.44
Units Sold: 112
```

### Document D010 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2024-08-18

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0002
Processor: HarborPay
Batch Total: $7,847.44
Fee Amount: $141.25
Expected Deposit: $7,706.19
Terminal ID: TERM-0002
```

### Document D005 — Card Settlement Report

- **Type:** `card_settlement_report`
- **Role:** `posting_doc`
- **Date:** 2024-09-02

```
CARD SETTLEMENT REPORT
======================

Settlement Summary
------------------
Settlement ID: SETTLE-0001
Processor: ClearRoute
Gross Amount: $20,641.55
Fees: $371.55
Net Deposit: $20,270.00
Deposit Date: 2024-09-02

Linked Batches
--------------
Batch References:
  - BATCH-0001
```

### Document D008 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-04

```
UTILITY INVOICE
===============

From
----
Cedar Operations
14 King Street, Pune
Document Date: 2024-09-04

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: utilities_statement
Period: Q3 FY 2024

Terms
-----
Due Date: 2024-09-16

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: Q3 FY 2024
Due Date: 2024-09-16
Total: $1,634.40

Charges
-------
Charges:
  - Description Electricity | Amount $455.16
  - Description Water | Amount $1,179.24

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-16

```
PAYMENT ADVICE
==============

From
----
Cedar Operations
14 King Street, Pune
Document Date: 2024-09-16

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q3 FY 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Prime Utility Desk
Amount: $1,583.00
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D012 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-09-30

```
BANK STATEMENT
==============

From
----
Cedar Operations
14 King Street, Pune
Document Date: 2024-09-30

Reference Box
-------------
Document ID: D012
Document Type: bank_statement
Period: Q3 FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0036
Statement Currency: USD
Opening Balance: $38,495.40
Closing Balance: $68,559.95

Statement Rows
--------------
Rows:
  - Date 2024-08-15 | Description Cash till SALES-0001 | Amount $7,831.66 | Running Balance 
$46,327.06
  - Date 2024-08-18 | Description Cash till SALES-0002 | Amount $3,545.89 | Running Balance 
$49,872.95
  - Date 2024-09-02 | Description Card settlement SETTLE-0001 | Amount $20,270.00 | Running 
Balance $70,142.95
  - Date 2024-09-16 | Description Supplier settlement BILL-0001 | Amount $-1,583.00 | 
Running Balance $68,559.95

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 1,583.00 | D002 | 2024-07-16 | inventory_purchase |
| 2 | Cash | Sales Revenue | 7,831.66 | D003, D004 | 2024-08-15 | retail_sale_cash |
| 3 | Card Settlement Clearing | Sales Revenue | 20,641.55 | D003, D004 | 2024-08-15 | retail_sale_card |
| 4 | Cost of Goods Sold | Inventory | 17,286.03 | D003, D004 | 2024-08-15 | retail_sale_cogs |
| 5 | Cash | Card Settlement Clearing | 20,270.00 | D005, D004 | 2024-09-02 | card_settlement_deposit |
| 6 | Maintenance Expense | Card Settlement Clearing | 371.55 | D005, D004 | 2024-09-02 | card_settlement_fees |
| 7 | Accounts Payable | Cash | 1,583.00 | D006, D002 | 2024-09-16 | supplier_payment |
| 8 | Inventory | Accounts Payable | 8,705.25 | D007 | 2024-07-08 | inventory_purchase |
| 9 | Utilities Expense | Accounts Payable | 1,634.40 | D008 | 2024-09-04 | utilities_bill |
| 10 | Cash | Sales Revenue | 3,545.89 | D009, D010 | 2024-08-18 | retail_sale_cash |
| 11 | Card Settlement Clearing | Sales Revenue | 7,847.44 | D009, D010 | 2024-08-18 | retail_sale_card |
| 12 | Cost of Goods Sold | Inventory | 6,854.60 | D009, D010 | 2024-08-18 | retail_sale_cogs |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 68,559.95
- Inventory: 7,939.35
- Card Settlement Clearing: 9,282.74
- Office Supplies: 355.81

**Liabilities**
- Accounts Payable: 16,426.00
- Accrued Expenses: 1,079.54

**Equity**
- Retained Earnings: 22,527.42
- Owner's Equity: 46,104.89

**Totals:** Assets = 86,137.85; Liabilities = 17,505.54; Equity = 68,632.31
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
- Notes: Acceptable as ground truth.
