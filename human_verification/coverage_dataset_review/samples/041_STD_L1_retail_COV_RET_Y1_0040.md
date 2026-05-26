# Verification Packet — COV_RET_Y1_0040

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 1
- **Period type:** year
- **Period label:** FY 2025
- **Period start → end:** 2025-01-01 → 2025-12-31
- **Entity:** Pioneer Clinic
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `none`
- **Document count:** 11
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 62,555.73
- Inventory: 49,025.24

**Liabilities**
- Accounts Payable: 10,219.01

**Equity**
- Owner's Equity: 101,361.96


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/01/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 62.555,73
  - Section assets | Account Inventory | Amount EUR 49.025,24
  - Section liabilities | Account Accounts Payable | Amount EUR 10.219,01
  - Section equity | Account Owner's Equity | Amount EUR 101.361,96

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-13

```
SUPPLIER INVOICE
================

From
----
Pioneer Clinic
220 Lake View Road, Bengaluru
Document Date: 13/02/2025

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: FY 2025

Terms
-----
Due Date: 05/03/2025

Supplier Header
---------------
Supplier: Prime Utility Desk
Expense Category: Inventory
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 05/03/2025
Total: EUR 13.870,35

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 17 | Unit Cost EUR 190,73 | Amount EUR 3.242,41
  - Description Widget B | Quantity 4 | Unit Cost EUR 2.656,99 | Amount EUR 10.627,94

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D010 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-02-13

```
SECONDARY COPY
==============

From
----
Pioneer Clinic
220 Lake View Road, Bengaluru
Document Date: 13/02/2025

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D010
Document Type: secondary_copy
Period: FY 2025

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0001
Counterparty: Prime Utility Desk
Total: EUR 13.870,35
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D007 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-07-10

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0003
Store Name: Pioneer Clinic
Gross Sales: EUR 52.106,41
Returns: 2.410,71
Net Sales: EUR 49.695,70
Tax Label: 
Tax Amount: EUR 0,00
COGS Amount: EUR 24.105,22
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: EUR 14.033,91
Card Sales: EUR 35.661,79
Units Sold: 136
```

### Document D008 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-07-10

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0003
Processor: Axis Payments
Batch Total: EUR 35.661,79
Fee Amount: EUR 641,91
Expected Deposit: EUR 35.019,88
Terminal ID: TERM-0003
```

### Document D005 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-07-13

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0002
Store Name: Pioneer Clinic
Gross Sales: EUR 16.701,45
Returns: 413,51
Net Sales: EUR 16.287,94
Tax Label: 
Tax Amount: EUR 0,00
COGS Amount: EUR 10.340,67
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: EUR 5.037,40
Card Sales: EUR 11.250,54
Units Sold: 166
```

### Document D006 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-07-13

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0002
Processor: HarborPay
Batch Total: EUR 11.250,54
Fee Amount: EUR 202,51
Expected Deposit: EUR 11.048,03
Terminal ID: TERM-0002
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-07-25

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Pioneer Clinic
Gross Sales: EUR 59.286,89
Returns: 799,53
Net Sales: EUR 58.487,36
Tax Label: 
Tax Amount: EUR 0,00
COGS Amount: EUR 37.380,05
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: EUR 20.114,64
Card Sales: EUR 38.372,72
Units Sold: 121
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-07-25

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: HarborPay
Batch Total: EUR 38.372,72
Fee Amount: EUR 690,71
Expected Deposit: EUR 37.682,01
Terminal ID: TERM-0001
```

### Document D009 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
VENDOR STATEMENT
================

From
----
Pioneer Clinic
220 Lake View Road, Bengaluru
Date: 31/12/2025

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: vendor_statement
Period: FY 2025

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Prime Utility Desk
Closing Balance: EUR 13.870,35

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount EUR 13.870,35 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D011 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Pioneer Clinic
220 Lake View Road, Bengaluru
Date: 31/12/2025

Reference Box
-------------
Document ID: D011
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0040
Statement Currency: EUR
Opening Balance: EUR 62.555,73
Closing Balance: EUR 101.741,68

Statement Rows
--------------
Rows:
  - Date 10/07/2025 | Description Cash till SALES-0003 | Amount EUR 14.033,91 | Running 
Balance EUR 76.589,64
  - Date 13/07/2025 | Description Cash till SALES-0002 | Amount EUR 5.037,40 | Running 
Balance EUR 81.627,04
  - Date 25/07/2025 | Description Cash till SALES-0001 | Amount EUR 20.114,64 | Running 
Balance EUR 101.741,68

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D011
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 13,870.35 | D002 | 2025-02-13 | inventory_purchase |
| 2 | Cash | Sales Revenue | 20,114.64 | D003, D004 | 2025-07-25 | retail_sale_cash |
| 3 | Card Settlement Clearing | Sales Revenue | 38,372.72 | D003, D004 | 2025-07-25 | retail_sale_card |
| 4 | Cost of Goods Sold | Inventory | 37,380.05 | D003, D004 | 2025-07-25 | retail_sale_cogs |
| 5 | Cash | Sales Revenue | 5,037.40 | D005, D006 | 2025-07-13 | retail_sale_cash |
| 6 | Card Settlement Clearing | Sales Revenue | 11,250.54 | D005, D006 | 2025-07-13 | retail_sale_card |
| 7 | Cost of Goods Sold | Inventory | 10,340.67 | D005, D006 | 2025-07-13 | retail_sale_cogs |
| 8 | Cash | Sales Revenue | 14,033.91 | D007, D008 | 2025-07-10 | retail_sale_cash |
| 9 | Card Settlement Clearing | Sales Revenue | 35,661.79 | D007, D008 | 2025-07-10 | retail_sale_card |
| 10 | Cost of Goods Sold | Inventory | 24,105.22 | D007, D008 | 2025-07-10 | retail_sale_cogs |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 101,741.68
- Inventory: -8,930.35
- Card Settlement Clearing: 85,285.05

**Liabilities**
- Accounts Payable: 24,089.36

**Equity**
- Owner's Equity: 101,361.96
- Retained Earnings: 52,645.06

**Totals:** Assets = 178,096.38; Liabilities = 24,089.36; Equity = 154,007.02
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
