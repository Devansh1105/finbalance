# Verification Packet — COV_RET_Y3_0042

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 3
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Willow Advisors
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 20
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 57,980.43
- Inventory: 45,487.19
- Card Settlement Clearing: 4,776.72
- Office Supplies: 2,331.93

**Liabilities**
- Accounts Payable: 9,509.03
- Unearned Revenue: 9,123.74
- Accrued Expenses: 3,543.71

**Equity**
- Retained Earnings: 25,827.67
- Owner's Equity: 62,572.12


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-04-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-04-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $57,980.43
  - Section assets | Account Inventory | Amount $45,487.19
  - Section assets | Account Card Settlement Clearing | Amount $4,776.72
  - Section assets | Account Office Supplies | Amount $2,331.93
  - Section liabilities | Account Accounts Payable | Amount $9,509.03
  - Section liabilities | Account Unearned Revenue | Amount $9,123.74
  - Section liabilities | Account Accrued Expenses | Amount $3,543.71
  - Section equity | Account Retained Earnings | Amount $25,827.67
  - Section equity | Account Owner's Equity | Amount $62,572.12

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-08

```
SUPPLIER INVOICE
================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 2024-05-08

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-05-18

Supplier Header
---------------
Supplier: Vertex Supply Co.
Expense Category: Inventory
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 2024-05-18
Total: $16,054.70

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 19 | Unit Cost $314.14 | Amount $5,968.73
  - Description Widget B | Quantity 5 | Unit Cost $2,017.19 | Amount $10,085.97

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D013 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2024-08-14

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0002
Store Name: Willow Advisors
Gross Sales: $20,320.64
Returns: 895.84
Net Sales: $19,424.80
Tax Label: 
Tax Amount: $0.00
COGS Amount: $12,744.89
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: $5,223.19
Card Sales: $14,201.61
Units Sold: 222
```

### Document D014 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2024-08-14

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0002
Processor: Axis Payments
Batch Total: $14,201.61
Fee Amount: $255.63
Expected Deposit: $13,945.98
Terminal ID: TERM-0002
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2024-11-11

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Willow Advisors
Gross Sales: $29,285.39
Returns: 1,117.11
Net Sales: $28,168.28
Tax Label: 
Tax Amount: $0.00
COGS Amount: $18,372.61
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: $5,755.81
Card Sales: $22,412.47
Units Sold: 86
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2024-11-11

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: ClearRoute
Batch Total: $22,412.47
Fee Amount: $403.42
Expected Deposit: $22,009.05
Terminal ID: TERM-0001
```

### Document D005 — Card Settlement Report

- **Type:** `card_settlement_report`
- **Role:** `posting_doc`
- **Date:** 2024-12-13

```
CARD SETTLEMENT REPORT
======================

Settlement Summary
------------------
Settlement ID: SETTLE-0001
Processor: HarborPay
Gross Amount: $22,412.47
Fees: $403.42
Net Deposit: $22,009.05
Deposit Date: 2024-12-13

Linked Batches
--------------
Batch References:
  - BATCH-0001
```

### Document D010 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-12-24

```
UTILITY INVOICE
===============

From
----
Willow Advisors
90 Hill Park, Hyderabad
Document Date: 2024-12-24

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: utilities_statement
Period: FY 2024-25

Terms
-----
Due Date: 2025-01-05

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: FY 2024-25
Due Date: 2025-01-05
Total: $1,934.98

Charges
-------
Charges:
  - Description Electricity | Amount $647.17
  - Description Water | Amount $1,287.81

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-02-03

```
PAYROLL SUMMARY
===============

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 2025-02-03

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024-25
Headcount: 3
Gross Pay: $21,553.49
Employer Tax: 2,726.42
Cash Outflow: $24,279.91

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-02-12

```
PAYMENT ADVICE
==============

From
----
Willow Advisors
90 Hill Park, Hyderabad
Document Date: 2025-02-12

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2024-25
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Vertex Supply Co.
Amount: $16,054.70
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-03-31

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
  - Sku SKU-0001 | Description Widget B | System Qty 100 | Counted Qty 88 | Unit Cost $54.35
```

### Document D009 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D009
Document Type: inventory_rollforward
Period: FY 2024-25

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0001
Opening Balance: $12,118.63
Additions: 11,959.91
Usage Or Sales: $11,204.77
Write Down: 652.20
Ending Balance: $12,221.57

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D011 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0002
Location: Back room

Counted Items
-------------
Items:
  - Sku SKU-0002 | Description Widget B | System Qty 100 | Counted Qty 91 | Unit Cost $22.66
```

### Document D012 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 2025-03-31

Reference Box
-------------
Document ID: D012
Document Type: inventory_rollforward
Period: FY 2024-25

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0002
Opening Balance: $2,997.99
Additions: 3,886.47
Usage Or Sales: $2,840.34
Write Down: 203.94
Ending Balance: $3,840.18

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D015 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0003
Location: Back room

Counted Items
-------------
Items:
  - Sku SKU-0003 | Description Filter Pack | System Qty 100 | Counted Qty 88 | Unit Cost 
$38.77
```

### Document D016 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D016
Document Type: inventory_rollforward
Period: FY 2024-25

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0003
Opening Balance: $7,342.13
Additions: 6,410.64
Usage Or Sales: $8,373.29
Write Down: 465.24
Ending Balance: $4,914.24

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D017 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 2025-03-31

Reference Box
-------------
Document ID: D017
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Annual leave policy reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Annual leave policy reminder
Audience: Operations Team

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
Page marker: D017
```

### Document D018 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Willow Advisors
90 Hill Park, Hyderabad
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D018
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0002
Subject: Document retention reminder
Audience: Operations Team

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D019 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
VENDOR STATEMENT
================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 2025-03-31

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D019
Document Type: vendor_statement
Period: FY 2024-25

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Metro Water
Closing Balance: $1,934.98

Statement Lines
---------------
Lines:
  - Reference UTIL-0001 | Document Type Open invoice | Amount $1,934.98 | Status Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 2025-03-31

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0042
Statement Currency: USD
Opening Balance: $57,980.43
Closing Balance: $50,633.87

Statement Rows
--------------
Rows:
  - Date 2024-08-14 | Description Cash till SALES-0002 | Amount $5,223.19 | Running Balance 
$63,203.62
  - Date 2024-11-11 | Description Cash till SALES-0001 | Amount $5,755.81 | Running Balance 
$68,959.43
  - Date 2024-12-13 | Description Card settlement SETTLE-0001 | Amount $22,009.05 | Running 
Balance $90,968.48
  - Date 2025-02-03 | Description Payroll PAYRUN-0001 | Amount $-24,279.91 | Running Balance
 $66,688.57
  - Date 2025-02-12 | Description Supplier settlement BILL-0001 | Amount $-16,054.70 | 
Running Balance $50,633.87

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D020
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 16,054.70 | D002 | 2024-05-08 | inventory_purchase |
| 2 | Cash | Sales Revenue | 5,755.81 | D003, D004 | 2024-11-11 | retail_sale_cash |
| 3 | Card Settlement Clearing | Sales Revenue | 22,412.47 | D003, D004 | 2024-11-11 | retail_sale_card |
| 4 | Cost of Goods Sold | Inventory | 18,372.61 | D003, D004 | 2024-11-11 | retail_sale_cogs |
| 5 | Cash | Card Settlement Clearing | 22,009.05 | D005, D004 | 2024-12-13 | card_settlement_deposit |
| 6 | Maintenance Expense | Card Settlement Clearing | 403.42 | D005, D004 | 2024-12-13 | card_settlement_fees |
| 7 | Accounts Payable | Cash | 16,054.70 | D006, D002 | 2025-02-12 | supplier_payment |
| 8 | Salaries Expense | Cash | 21,553.49 | D007 | 2025-02-03 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 2,726.42 | D007 | 2025-02-03 | payroll_tax |
| 10 | Inventory Shrinkage Expense | Inventory | 652.20 | D008, D009 | 2025-03-31 | stock_adjustment |
| 11 | Utilities Expense | Accounts Payable | 1,934.98 | D010 | 2024-12-24 | utilities_bill |
| 12 | Inventory Shrinkage Expense | Inventory | 203.94 | D011, D012 | 2025-03-31 | stock_adjustment |
| 13 | Cash | Sales Revenue | 5,223.19 | D013, D014 | 2024-08-14 | retail_sale_cash |
| 14 | Card Settlement Clearing | Sales Revenue | 14,201.61 | D013, D014 | 2024-08-14 | retail_sale_card |
| 15 | Cost of Goods Sold | Inventory | 12,744.89 | D013, D014 | 2024-08-14 | retail_sale_cogs |
| 16 | Inventory Shrinkage Expense | Inventory | 465.24 | D015, D016 | 2025-03-31 | stock_adjustment |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 50,633.87
- Inventory: 29,103.01
- Card Settlement Clearing: 18,978.33
- Office Supplies: 2,331.93

**Liabilities**
- Accounts Payable: 11,444.01
- Unearned Revenue: 9,123.74
- Accrued Expenses: 3,543.71

**Equity**
- Retained Earnings: 14,363.56
- Owner's Equity: 62,572.12

**Totals:** Assets = 101,047.14; Liabilities = 24,111.46; Equity = 76,935.68
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
