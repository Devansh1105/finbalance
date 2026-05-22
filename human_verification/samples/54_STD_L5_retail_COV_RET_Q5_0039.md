# Verification Packet — COV_RET_Q5_0039

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `retail`
- **Difficulty level (1–5):** 5
- **Period type:** quarter
- **Period label:** Q4 FY 2026-27
- **Period start → end:** 2026-01-01 → 2026-03-31
- **Entity:** Willow Advisors
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 23
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Inventory`, `Card Settlement Clearing`, `Store Fixtures`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Maintenance Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2026-01-01_

**Assets**
- Cash: 52,996.42
- Inventory: 16,599.55
- Card Settlement Clearing: 3,122.44
- Store Fixtures: 14,352.10
- Office Supplies: 941.54

**Liabilities**
- Accounts Payable: 10,857.63
- Unearned Revenue: 2,548.86
- Accrued Expenses: 2,638.04
- Loans Payable: 12,110.34

**Equity**
- Retained Earnings: 13,399.55
- Owner's Equity: 46,457.63


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2026-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2026-01-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $52,996.42
  - Section assets | Account Inventory | Amount $16,599.55
  - Section assets | Account Card Settlement Clearing | Amount $3,122.44
  - Section assets | Account Store Fixtures | Amount $14,352.10
  - Section assets | Account Office Supplies | Amount $941.54
  - Section liabilities | Account Accounts Payable | Amount $10,857.63
  - Section liabilities | Account Unearned Revenue | Amount $2,548.86
  - Section liabilities | Account Accrued Expenses | Amount $2,638.04
  - Section liabilities | Account Loans Payable | Amount $12,110.34
  - Section equity | Account Retained Earnings | Amount $13,399.55
  - Section equity | Account Owner's Equity | Amount $46,457.63

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-01-19

```
SUPPLIER INVOICE
================

From
----
Willow Advisors
220 Lake View Road, Bengaluru
Date: 2026-01-19

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: Q4 FY 2026-27

Terms
-----
Due Date: 2026-02-04

Supplier Header
---------------
Supplier: Vertex Supply Co.
Expense Category: Inventory
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 2026-02-04
Subtotal: $11,761.54
Tax Label: GST
Tax Rate: 7.00%
Tax Amount: $823.31
Total: $12,584.85

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 25 | Unit Cost $206.96 | Amount $5,174.02
  - Description Widget B | Quantity 28 | Unit Cost $235.27 | Amount $6,587.52

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-01-29

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Pace Office Mart
Asset Name: Display fixtures
Asset Tag: TAG-0001
Useful Life Months: 48
Total: $103,474.68
Paid Cash: $32,198.68
Financed Amount: $71,276.00
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D003 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2026-02-15

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0001
Store Name: Willow Advisors
Gross Sales: $41,406.64
Returns: 1,605.78
Net Sales: $39,800.86
Tax Label: GST
Tax Amount: $1,990.04
COGS Amount: $26,448.55
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: $7,632.51
Card Sales: $34,158.39
Units Sold: 229
```

### Document D004 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2026-02-15

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0001
Processor: HarborPay
Batch Total: $34,158.39
Fee Amount: $614.85
Expected Deposit: $33,543.54
Terminal ID: TERM-0001
```

### Document D017 — Sales Summary

- **Type:** `sales_summary`
- **Role:** `posting_doc`
- **Date:** 2026-02-16

```
SALES SUMMARY
=============

Sales Summary
-------------
Report ID: SALES-0002
Store Name: Willow Advisors
Gross Sales: $56,039.98
Returns: 1,833.37
Net Sales: $54,206.61
Tax Label: GST
Tax Amount: $2,710.33
COGS Amount: $31,325.37
COGS Source: POS inventory cost layer for items sold in this sales summary.
Cash Sales: $13,893.93
Card Sales: $43,023.01
Units Sold: 159
```

### Document D018 — POS Batch Report

- **Type:** `pos_batch_report`
- **Role:** `support_doc`
- **Date:** 2026-02-16

```
POS BATCH REPORT
================

Batch Summary
-------------
Batch ID: BATCH-0002
Processor: ClearRoute
Batch Total: $43,023.01
Fee Amount: $774.41
Expected Deposit: $42,248.60
Terminal ID: TERM-0002
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2026-02-22

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: $6,199.30
Draw Amount: $96,132.51
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $102,331.81
Note: Scheduled lender activity for the selected period.
```

### Document D015 — Return Note

- **Type:** `return_note`
- **Role:** `posting_doc`
- **Date:** 2026-03-02

```
RETURN NOTE
===========

Return Summary
--------------
Return ID: RTN-0001
Reason: Shelf defect
Amount: $441.54
Reference: SALE-REF-0001
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2026-03-07

```
PAYROLL SUMMARY
===============

From
----
Willow Advisors
220 Lake View Road, Bengaluru
Date: 2026-03-07

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q4 FY 2026-27
Headcount: 12
Gross Pay: $13,044.00
Employer Tax: 1,191.34
Cash Outflow: $14,235.34

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-03-09

```
PAYMENT ADVICE
==============

From
----
Willow Advisors
220 Lake View Road, Bengaluru
Date: 2026-03-09

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q4 FY 2026-27
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Vertex Supply Co.
Amount: $12,131.18
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D005 — Card Settlement Report

- **Type:** `card_settlement_report`
- **Role:** `posting_doc`
- **Date:** 2026-03-10

```
CARD SETTLEMENT REPORT
======================

Settlement Summary
------------------
Settlement ID: SETTLE-0001
Processor: Axis Payments
Gross Amount: $34,158.39
Fees: $614.85
Net Deposit: $33,543.54
Deposit Date: 2026-03-10

Linked Batches
--------------
Batch References:
  - BATCH-0001
```

### Document D010 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2026-03-14

```
UTILITY INVOICE
===============

From
----
Willow Advisors
220 Lake View Road, Bengaluru
Document Date: 2026-03-14

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: utilities_statement
Period: Q4 FY 2026-27

Terms
-----
Due Date: 2026-03-22

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: Q4 FY 2026-27
Due Date: 2026-03-22
Total: $1,247.81

Charges
-------
Charges:
  - Description Electricity | Amount $514.41
  - Description Water | Amount $733.40

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D014 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2026-03-15

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: $117,087.65
Draw Amount: $0.00
Principal Paid: $16,157.91
Interest Paid: $1,254.35
Ending Principal: $100,929.74
Note: Scheduled lender activity for the selected period.
```

### Document D016 — Return Note

- **Type:** `return_note`
- **Role:** `posting_doc`
- **Date:** 2026-03-17

```
RETURN NOTE
===========

Return Summary
--------------
Return ID: RTN-0002
Reason: Customer return
Amount: $550.06
Reference: SALE-REF-0002
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2026-03-31

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
  - Sku SKU-0001 | Description Widget A | System Qty 100 | Counted Qty 92 | Unit Cost $36.71
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: $293.68
Reference Sheet: COUNT-0001
```

### Document D013 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Store Fixtures
Asset Tag: OPEN-STO
Cost: $14,352.10
Useful Life Months: 60
Current Period Charge: $717.60
Accumulated Depreciation: 717.60
```

### Document D019 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2026-03-31

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
  - Sku SKU-0002 | Description Filter Pack | System Qty 100 | Counted Qty 95 | Unit Cost 
$40.42
```

### Document D020 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0002
Reason: Shrinkage found during physical count
Amount: $202.10
Reference Sheet: COUNT-0002
```

### Document D021 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0003
Location: Warehouse A

Counted Items
-------------
Items:
  - Sku SKU-0003 | Description Service Bundle | System Qty 100 | Counted Qty 92 | Unit Cost 
$44.55
```

### Document D022 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0003
Reason: Shrinkage found during physical count
Amount: $356.40
Reference Sheet: COUNT-0003
```

### Document D023 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Willow Advisors
220 Lake View Road, Bengaluru
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D023
Document Type: bank_statement
Period: Q4 FY 2026-27

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0039
Statement Currency: USD
Opening Balance: $52,996.42
Closing Balance: $127,229.85

Statement Rows
--------------
Rows:
  - Date 2026-01-29 | Description Asset purchase ASSET-0001 | Amount $-32,198.68 | Running 
Balance $20,797.74
  - Date 2026-02-15 | Description Cash till SALES-0001 | Amount $7,632.51 | Running Balance 
$28,430.25
  - Date 2026-02-16 | Description Cash till SALES-0002 | Amount $13,893.93 | Running Balance
 $42,324.18
  - Date 2026-02-22 | Description Loan draw LOAN-0001 | Amount $96,132.51 | Running Balance 
$138,456.69
  - Date 2026-03-02 | Description Return RTN-0001 | Amount $-441.54 | Running Balance 
$138,015.15
  - Date 2026-03-07 | Description Payroll PAYRUN-0001 | Amount $-14,235.34 | Running Balance
 $123,779.81
  - Date 2026-03-09 | Description Supplier settlement BILL-0001 | Amount $-12,131.18 | 
Running Balance $111,648.63
  - Date 2026-03-10 | Description Card settlement SETTLE-0001 | Amount $33,543.54 | Running 
Balance $145,192.17
  - Date 2026-03-15 | Description Loan payment LOAN-0002 | Amount $-17,412.26 | Running 
Balance $127,779.91
  - Date 2026-03-17 | Description Return RTN-0002 | Amount $-550.06 | Running Balance 
$127,229.85

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D023
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 11,761.54 | D002 | 2026-01-19 | inventory_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 823.31 | D002 | 2026-01-19 | inventory_purchase_tax |
| 3 | Cash | Sales Revenue | 7,269.06 | D003, D004 | 2026-02-15 | retail_sale_cash |
| 4 | Card Settlement Clearing | Sales Revenue | 32,531.80 | D003, D004 | 2026-02-15 | retail_sale_card |
| 5 | Cost of Goods Sold | Inventory | 26,448.55 | D003, D004 | 2026-02-15 | retail_sale_cogs |
| 6 | Cash | Sales Tax Payable | 363.45 | D003, D004 | 2026-02-15 | retail_sale_cash_tax |
| 7 | Card Settlement Clearing | Sales Tax Payable | 1,626.59 | D003, D004 | 2026-02-15 | retail_sale_card_tax |
| 8 | Cash | Card Settlement Clearing | 33,543.54 | D005, D004 | 2026-03-10 | card_settlement_deposit |
| 9 | Maintenance Expense | Card Settlement Clearing | 614.85 | D005, D004 | 2026-03-10 | card_settlement_fees |
| 10 | Accounts Payable | Cash | 12,131.18 | D006, D002 | 2026-03-09 | supplier_payment |
| 11 | Salaries Expense | Cash | 13,044.00 | D007 | 2026-03-07 | payroll_gross |
| 12 | Payroll Tax Expense | Cash | 1,191.34 | D007 | 2026-03-07 | payroll_tax |
| 13 | Inventory Shrinkage Expense | Inventory | 293.68 | D008, D009 | 2026-03-31 | stock_adjustment |
| 14 | Utilities Expense | Accounts Payable | 1,247.81 | D010 | 2026-03-14 | utilities_bill |
| 15 | Cash | Loans Payable | 96,132.51 | D011 | 2026-02-22 | loan_draw |
| 16 | Store Fixtures | Cash | 32,198.68 | D012 | 2026-01-29 | equipment_purchase_cash |
| 17 | Store Fixtures | Notes Payable | 71,276.00 | D012 | 2026-01-29 | equipment_purchase_financed |
| 18 | Depreciation Expense | Accumulated Depreciation | 717.60 | D013 | 2026-03-31 | depreciation |
| 19 | Loans Payable | Cash | 16,157.91 | D014 | 2026-03-15 | loan_repayment_principal |
| 20 | Interest Expense | Cash | 1,254.35 | D014 | 2026-03-15 | loan_repayment_interest |
| 21 | Sales Revenue | Cash | 441.54 | D015 | 2026-03-02 | return |
| 22 | Sales Revenue | Cash | 550.06 | D016 | 2026-03-17 | return |
| 23 | Cash | Sales Revenue | 13,232.31 | D017, D018 | 2026-02-16 | retail_sale_cash |
| 24 | Card Settlement Clearing | Sales Revenue | 40,974.30 | D017, D018 | 2026-02-16 | retail_sale_card |
| 25 | Cost of Goods Sold | Inventory | 31,325.37 | D017, D018 | 2026-02-16 | retail_sale_cogs |
| 26 | Cash | Sales Tax Payable | 661.62 | D017, D018 | 2026-02-16 | retail_sale_cash_tax |
| 27 | Card Settlement Clearing | Sales Tax Payable | 2,048.71 | D017, D018 | 2026-02-16 | retail_sale_card_tax |
| 28 | Inventory Shrinkage Expense | Inventory | 202.10 | D019, D020 | 2026-03-31 | stock_adjustment |
| 29 | Inventory Shrinkage Expense | Inventory | 356.40 | D021, D022 | 2026-03-31 | stock_adjustment |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 127,229.85
- Inventory: -30,265.01
- Card Settlement Clearing: 46,145.45
- Store Fixtures: 117,826.78
- Office Supplies: 941.54
- Input Tax Receivable: 823.31
- Accumulated Depreciation: -717.60

**Liabilities**
- Accounts Payable: 12,559.11
- Unearned Revenue: 2,548.86
- Accrued Expenses: 2,638.04
- Loans Payable: 92,084.94
- Sales Tax Payable: 4,700.37
- Notes Payable: 71,276.00

**Equity**
- Retained Earnings: 29,719.37
- Owner's Equity: 46,457.63

**Totals:** Assets = 261,984.32; Liabilities = 185,807.32; Equity = 76,177.00
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
