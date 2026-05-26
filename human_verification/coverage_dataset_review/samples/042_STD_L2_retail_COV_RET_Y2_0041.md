# Verification Packet — COV_RET_Y2_0041

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 2
- **Period type:** year
- **Period label:** FY 2025-26
- **Period start → end:** 2025-04-01 → 2026-03-31
- **Entity:** Harbor Retail Group
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 15
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 83,873.94
- Inventory: 27,858.16
- Card Settlement Clearing: 5,181.06
- Office Supplies: 1,566.86

**Liabilities**
- Accounts Payable: 7,700.87
- Accrued Expenses: 3,406.44

**Equity**
- Retained Earnings: 20,432.21
- Owner's Equity: 86,940.50


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-04-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/04/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 83,873.94
  - Section assets | Account Inventory | Amount GBP 27,858.16
  - Section assets | Account Card Settlement Clearing | Amount GBP 5,181.06
  - Section assets | Account Office Supplies | Amount GBP 1,566.86
  - Section liabilities | Account Accounts Payable | Amount GBP 7,700.87
  - Section liabilities | Account Accrued Expenses | Amount GBP 3,406.44
  - Section equity | Account Retained Earnings | Amount GBP 20,432.21
  - Section equity | Account Owner's Equity | Amount GBP 86,940.50

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D007 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-13

```
SUPPLIER INVOICE
================

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 13/05/2025

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D007
Document Type: supplier_invoice
Period: FY 2025-26

Terms
-----
Due Date: 01/06/2025

Supplier Header
---------------
Supplier: Meridian Support LLP
Expense Category: Inventory
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 01/06/2025
Subtotal: GBP 12,700.99
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 2,286.18
CGST Amount: GBP 1,143.09
SGST Amount: GBP 1,143.09
Total: GBP 14,987.17

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 5 | Unit Cost GBP 530.30 | Amount GBP 2,651.51
  - Description Widget B | Quantity 17 | Unit Cost GBP 591.15 | Amount GBP 10,049.48

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D011 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-23

```
SUPPLIER INVOICE
================

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 23/05/2025

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: supplier_invoice
Period: FY 2025-26

Terms
-----
Due Date: 07/06/2025

Supplier Header
---------------
Supplier: Prime Utility Desk
Expense Category: Inventory
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0003
Due Date: 07/06/2025
Subtotal: GBP 18,035.81
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 3,246.45
CGST Amount: GBP 1,623.22
SGST Amount: GBP 1,623.23
Total: GBP 21,282.26

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 7 | Unit Cost GBP 781.37 | Amount GBP 5,469.58
  - Description Widget B | Quantity 20 | Unit Cost GBP 628.31 | Amount GBP 12,566.23

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-17

```
SUPPLIER INVOICE
================

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 17/06/2025

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: FY 2025-26

Terms
-----
Due Date: 02/07/2025

Supplier Header
---------------
Supplier: Prime Utility Desk
Expense Category: Inventory
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 02/07/2025
Subtotal: GBP 11,255.90
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 1,350.71
CGST Amount: GBP 675.36
SGST Amount: GBP 675.35
Total: GBP 12,606.61

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 19 | Unit Cost GBP 225.65 | Amount GBP 4,287.28
  - Description Widget B | Quantity 29 | Unit Cost GBP 240.30 | Amount GBP 6,968.62

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D013 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-06-17

```
SECONDARY COPY
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 17/06/2025

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D013
Document Type: secondary_copy
Period: FY 2025-26

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0001
Counterparty: Prime Utility Desk
Total: GBP 12,606.61
Copy Context: Forwarded copy attached to the customer correspondence bundle.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D012 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-28

```
SUPPLIER INVOICE
================

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 28/06/2025

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: supplier_invoice
Period: FY 2025-26

Terms
-----
Due Date: 16/07/2025

Supplier Header
---------------
Supplier: Golden State Finance
Expense Category: Inventory
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0004
Due Date: 16/07/2025
Subtotal: GBP 17,369.14
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 2,084.30
CGST Amount: GBP 1,042.15
SGST Amount: GBP 1,042.15
Total: GBP 19,453.44

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 29 | Unit Cost GBP 209.55 | Amount GBP 6,077.04
  - Description Widget B | Quantity 2 | Unit Cost GBP 5,646.05 | Amount GBP 11,292.10

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D014 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-06-28

```
SECONDARY COPY
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 28/06/2025

To
--
Golden State Finance

Reference Box
-------------
Document ID: D014
Document Type: secondary_copy
Period: FY 2025-26

Copy Summary
------------
Copy ID: COPY-0002
Source Reference: BILL-0004
Counterparty: Golden State Finance
Total: GBP 19,453.44
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D009 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-08-14

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0002
Store Name: Harbor Retail Group
Gross Sales: GBP 26,899.39
Returns: 931.14
Net Sales: GBP 25,968.25
Tax Label: India GST
Tax Amount: GBP 4,674.28
CGST Amount: GBP 2,337.14
SGST Amount: GBP 2,337.14
COGS Amount: GBP 13,361.82
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: GBP 8,275.30
Card Sales: GBP 22,367.23
Units Sold: 266
```

### Document D010 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-08-14

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0002
Processor: HarborPay
Batch Total: GBP 22,367.23
Fee Amount: GBP 402.61
Expected Deposit: GBP 21,964.62
Terminal ID: TERM-0002
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2025-10-16

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Harbor Retail Group
Gross Sales: GBP 44,833.31
Returns: 692.21
Net Sales: GBP 44,141.10
Tax Label: India GST
Tax Amount: GBP 7,945.40
CGST Amount: GBP 3,972.70
SGST Amount: GBP 3,972.70
COGS Amount: GBP 25,468.48
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: GBP 12,057.06
Card Sales: GBP 40,029.44
Units Sold: 107
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2025-10-16

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: ClearRoute
Batch Total: GBP 40,029.44
Fee Amount: GBP 720.53
Expected Deposit: GBP 39,308.91
Terminal ID: TERM-0001
```

### Document D005 — Card Settlement Report

- **Type:** `card_settlement_report`
- **Role:** `posting_doc`
- **Date:** 2025-12-20

```
CARD SETTLEMENT REPORT
======================

Settlement Summary
------------------
Settlement ID: SETTLE-0001
Processor: Axis Payments
Gross Amount: GBP 40,029.44
Fees: GBP 720.53
Net Deposit: GBP 39,308.91
Deposit Date: 20/12/2025

Linked Batches
--------------
Batch References:
  - BATCH-0001
```

### Document D008 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-22

```
UTILITY INVOICE
===============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 22/12/2025

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: utilities_statement
Period: FY 2025-26

Terms
-----
Due Date: 02/01/2026

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: FY 2025-26
Due Date: 02/01/2026
Total: GBP 2,066.88

Charges
-------
Charges:
  - Description Electricity | Amount GBP 463.88
  - Description Water | Amount GBP 1,603.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-01-20

```
PAYMENT ADVICE
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 20/01/2026

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2025-26
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Prime Utility Desk
Amount: GBP 12,606.61
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D015 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 31/03/2026

Reference Box
-------------
Document ID: D015
Document Type: bank_statement
Period: FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0041
Statement Currency: GBP
Opening Balance: GBP 83,873.94
Closing Balance: GBP 130,908.60

Statement Rows
--------------
Rows:
  - Date 14/08/2025 | Description Cash till SALES-0002 | Amount GBP 8,275.30 | Running 
Balance GBP 92,149.24
  - Date 16/10/2025 | Description Cash till SALES-0001 | Amount GBP 12,057.06 | Running 
Balance GBP 104,206.30
  - Date 20/12/2025 | Description Card settlement SETTLE-0001 | Amount GBP 39,308.91 | 
Running Balance GBP 143,515.21
  - Date 20/01/2026 | Description Supplier settlement BILL-0001 | Amount GBP -12,606.61 | 
Running Balance GBP 130,908.60

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D015
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 11,255.90 | D002 | 2025-06-17 | inventory_purchase |
| 2 | Input CGST Receivable | Accounts Payable | 675.36 | D002 | 2025-06-17 | inventory_purchase_tax_cgst |
| 3 | Input SGST Receivable | Accounts Payable | 675.35 | D002 | 2025-06-17 | inventory_purchase_tax_sgst |
| 4 | Cash | Sales Revenue | 10,217.85 | D003, D004 | 2025-10-16 | retail_sale_cash |
| 5 | Card Settlement Clearing | Sales Revenue | 33,923.25 | D003, D004 | 2025-10-16 | retail_sale_card |
| 6 | Cost of Goods Sold | Inventory | 25,468.48 | D003, D004 | 2025-10-16 | retail_sale_cogs |
| 7 | Cash | CGST Payable | 919.61 | D003, D004 | 2025-10-16 | retail_sale_cash_tax_cgst |
| 8 | Cash | SGST Payable | 919.60 | D003, D004 | 2025-10-16 | retail_sale_cash_tax_sgst |
| 9 | Card Settlement Clearing | CGST Payable | 3,053.09 | D003, D004 | 2025-10-16 | retail_sale_card_tax_cgst |
| 10 | Card Settlement Clearing | SGST Payable | 3,053.10 | D003, D004 | 2025-10-16 | retail_sale_card_tax_sgst |
| 11 | Cash | Card Settlement Clearing | 39,308.91 | D005, D004 | 2025-12-20 | card_settlement_deposit |
| 12 | Maintenance Expense | Card Settlement Clearing | 720.53 | D005, D004 | 2025-12-20 | card_settlement_fees |
| 13 | Accounts Payable | Cash | 12,606.61 | D006, D002 | 2026-01-20 | supplier_payment |
| 14 | Inventory | Accounts Payable | 12,700.99 | D007 | 2025-05-13 | inventory_purchase |
| 15 | Input CGST Receivable | Accounts Payable | 1,143.09 | D007 | 2025-05-13 | inventory_purchase_tax_cgst |
| 16 | Input SGST Receivable | Accounts Payable | 1,143.09 | D007 | 2025-05-13 | inventory_purchase_tax_sgst |
| 17 | Utilities Expense | Accounts Payable | 2,066.88 | D008 | 2025-12-22 | utilities_bill |
| 18 | Cash | Sales Revenue | 7,012.97 | D009, D010 | 2025-08-14 | retail_sale_cash |
| 19 | Card Settlement Clearing | Sales Revenue | 18,955.28 | D009, D010 | 2025-08-14 | retail_sale_card |
| 20 | Cost of Goods Sold | Inventory | 13,361.82 | D009, D010 | 2025-08-14 | retail_sale_cogs |
| 21 | Cash | CGST Payable | 631.16 | D009, D010 | 2025-08-14 | retail_sale_cash_tax_cgst |
| 22 | Cash | SGST Payable | 631.17 | D009, D010 | 2025-08-14 | retail_sale_cash_tax_sgst |
| 23 | Card Settlement Clearing | CGST Payable | 1,705.97 | D009, D010 | 2025-08-14 | retail_sale_card_tax_cgst |
| 24 | Card Settlement Clearing | SGST Payable | 1,705.98 | D009, D010 | 2025-08-14 | retail_sale_card_tax_sgst |
| 25 | Inventory | Accounts Payable | 18,035.81 | D011 | 2025-05-23 | inventory_purchase |
| 26 | Input CGST Receivable | Accounts Payable | 1,623.22 | D011 | 2025-05-23 | inventory_purchase_tax_cgst |
| 27 | Input SGST Receivable | Accounts Payable | 1,623.23 | D011 | 2025-05-23 | inventory_purchase_tax_sgst |
| 28 | Inventory | Accounts Payable | 17,369.14 | D012 | 2025-06-28 | inventory_purchase |
| 29 | Input CGST Receivable | Accounts Payable | 1,042.15 | D012 | 2025-06-28 | inventory_purchase_tax_cgst |
| 30 | Input SGST Receivable | Accounts Payable | 1,042.15 | D012 | 2025-06-28 | inventory_purchase_tax_sgst |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 130,908.60
- Inventory: 48,389.70
- Card Settlement Clearing: 27,548.29
- Office Supplies: 1,566.86
- Input CGST Receivable: 4,483.82
- Input SGST Receivable: 4,483.82

**Liabilities**
- Accounts Payable: 65,490.62
- Accrued Expenses: 3,406.44
- CGST Payable: 6,309.83
- SGST Payable: 6,309.85

**Equity**
- Retained Earnings: 48,923.85
- Owner's Equity: 86,940.50

**Totals:** Assets = 217,381.09; Liabilities = 81,516.74; Equity = 135,864.35
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
