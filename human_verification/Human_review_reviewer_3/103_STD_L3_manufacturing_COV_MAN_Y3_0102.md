# Verification Packet — COV_MAN_Y3_0102

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 3
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Willow Builders
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 21
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 237,347.09
- Raw Materials Inventory: 141,469.79
- Work In Process: 52,077.44
- Finished Goods Inventory: 102,356.95
- Accounts Receivable: 56,397.76

**Liabilities**
- Accounts Payable: 77,243.96
- Accrued Expenses: 14,258.00

**Equity**
- Retained Earnings: 67,171.42
- Share Capital: 430,975.65


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
  - Section assets | Account Cash | Amount $237,347.09
  - Section assets | Account Raw Materials Inventory | Amount $141,469.79
  - Section assets | Account Work In Process | Amount $52,077.44
  - Section assets | Account Finished Goods Inventory | Amount $102,356.95
  - Section assets | Account Accounts Receivable | Amount $56,397.76
  - Section liabilities | Account Accounts Payable | Amount $77,243.96
  - Section liabilities | Account Accrued Expenses | Amount $14,258.00
  - Section equity | Account Retained Earnings | Amount $67,171.42
  - Section equity | Account Share Capital | Amount $430,975.65

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D015 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-24

```
SUPPLIER INVOICE
================

From
----
Willow Builders
220 Lake View Road, Bengaluru
Document Date: 2024-04-24

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D015
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-05-14

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: MAT-0004
Due Date: 2024-05-14
Total: $46,860.45

Supplier Bill Lines
-------------------
Lines:
  - Description Control boards | Quantity 195 | Unit Cost $240.31 | Amount $46,860.45

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-13

```
SUPPLIER INVOICE
================

From
----
Willow Builders
220 Lake View Road, Bengaluru
Document Date: 2024-06-13

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-06-29

Supplier Header
---------------
Supplier: Meridian Support LLP
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 2024-06-29
Total: $40,337.00

Supplier Bill Lines
-------------------
Lines:
  - Description Resin pellets | Quantity 209 | Unit Cost $193.00 | Amount $40,337.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D013 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-23

```
SUPPLIER INVOICE
================

From
----
Willow Builders
220 Lake View Road, Bengaluru
Document Date: 2024-06-23

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D013
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-07-06

Supplier Header
---------------
Supplier: Golden State Finance
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: MAT-0002
Due Date: 2024-07-06
Total: $62,812.26

Supplier Bill Lines
-------------------
Lines:
  - Description Packing film | Quantity 382 | Unit Cost $164.43 | Amount $62,812.26

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D017 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-06-23

```
SECONDARY COPY
==============

From
----
Willow Builders
220 Lake View Road, Bengaluru
Date: 2024-06-23

To
--
Golden State Finance

Reference Box
-------------
Document ID: D017
Document Type: secondary_copy
Period: FY 2024-25

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: MAT-0002
Counterparty: Golden State Finance
Total: $62,812.26
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D014 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-06

```
SUPPLIER INVOICE
================

From
----
Willow Builders
220 Lake View Road, Bengaluru
Date: 2024-07-06

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D014
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-07-30

Supplier Header
---------------
Supplier: Vertex Supply Co.
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: MAT-0003
Due Date: 2024-07-30
Total: $60,403.20

Supplier Bill Lines
-------------------
Lines:
  - Description Control boards | Quantity 363 | Unit Cost $166.40 | Amount $60,403.20

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D016 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-11

```
SUPPLIER INVOICE
================

From
----
Willow Builders
220 Lake View Road, Bengaluru
Date: 2024-07-11

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-07-30

Supplier Header
---------------
Supplier: Prime Utility Desk
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: MAT-0005
Due Date: 2024-07-30
Total: $16,023.28

Supplier Bill Lines
-------------------
Lines:
  - Description Resin pellets | Quantity 142 | Unit Cost $112.84 | Amount $16,023.28

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2024-09-30

```
MATERIAL REQUISITION SLIP
=========================

From
----
Willow Builders
220 Lake View Road, Bengaluru
Document Date: 2024-09-30

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: FY 2024-25

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Resin pellets
Quantity Issued: 153
Issue Value: $29,628.51
Warehouse: Main Warehouse

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2024-09-30

```
PRODUCTION BATCH SHEET
======================

From
----
Willow Builders
220 Lake View Road, Bengaluru
Document Date: 2024-09-30

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: FY 2024-25

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Subscription Bundle
Planned Units: 45
Material Value: $29,628.51
Labor Value: $0.00
Overhead Value: $0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D005 — Direct Labor Record

- **Type:** `direct_labor_record`
- **Role:** `posting_doc`
- **Date:** 2024-10-16

```
DIRECT LABOR RECORD
===================

From
----
Willow Builders
220 Lake View Road, Bengaluru
Date: 2024-10-16

Reference Box
-------------
Document ID: D005
Document Type: direct_labor_record
Period: FY 2024-25

Labor Summary
-------------
Batch ID: BATCH-0001
Product: Subscription Bundle
Planned Units: 37
Labor Value: $62,079.74
Labor Cash Paid: $62,079.74

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D011 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-12-12

```
PAYROLL SUMMARY
===============

From
----
Willow Builders
220 Lake View Road, Bengaluru
Document Date: 2024-12-12

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024-25
Headcount: 4
Gross Pay: $56,421.57
Employer Tax: 6,495.34
Cash Outflow: $62,916.91

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D009 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-25

```
PAYMENT ADVICE
==============

From
----
Willow Builders
220 Lake View Road, Bengaluru
Document Date: 2024-12-25

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D009
Document Type: payment_advice
Period: FY 2024-25
Reference: FGINV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: $169,702.75
Reference: FGINV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D007 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2024-12-31

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Willow Builders
220 Lake View Road, Bengaluru
Date: 2024-12-31

Reference Box
-------------
Document ID: D007
Document Type: finished_goods_transfer_note
Period: FY 2024-25

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Subscription Bundle
Units Completed: 51
Transfer Value: $124,987.11

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D010 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-01-21

```
PAYMENT ADVICE
==============

From
----
Willow Builders
220 Lake View Road, Bengaluru
Date: 2025-01-21

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D010
Document Type: payment_advice
Period: FY 2024-25
Reference: MAT-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: $40,337.00
Reference: MAT-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D008 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-05

```
CUSTOMER INVOICE
================

From
----
Willow Builders
220 Lake View Road, Bengaluru
Date: 2025-02-05

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D008
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: FGT-0001

Terms
-----
Due Date: 2025-02-23

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: FGT-0001
Currency: USD

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 2025-02-23
Total: $169,702.75

Line Items
----------
Items:
  - Description Subscription Bundle | Amount $169,702.75

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D019 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-02-05

```
CANCELLATION NOTE
=================

From
----
Willow Builders
220 Lake View Road, Bengaluru
Document Date: 2025-02-05

Reference Box
-------------
Document ID: D019
Document Type: cancellation_note
Period: FY 2024-25

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: FGINV-0001-OLD
Replacement Reference: FGINV-0001

Background
----------
Narrative: FGINV-0001-OLD is withdrawn and must not be posted. Use FGINV-0001 as the only 
valid invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D006 — Overhead Accrual Memo

- **Type:** `overhead_accrual_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-16

```
OVERHEAD ACCRUAL MEMO
=====================

From
----
Willow Builders
220 Lake View Road, Bengaluru
Document Date: 2025-03-16

Reference Box
-------------
Document ID: D006
Document Type: overhead_accrual_memo
Period: FY 2024-25

Overhead Summary
----------------
Batch ID: BATCH-0001
Product: Subscription Bundle
Planned Units: 35
Overhead Value: $33,278.86
Accrued Overhead: $33,278.86

Explanation
-----------
Narrative: Factory overhead incurred this period has been accrued into work in process.

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D012 — Scrap Report

- **Type:** `scrap_report`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
SCRAP REPORT
============

From
----
Willow Builders
220 Lake View Road, Bengaluru
Date: 2025-03-31

Reference Box
-------------
Document ID: D012
Document Type: scrap_report
Period: FY 2024-25

Approval / Context
------------------
Reason: Obsolete units

Scrap Summary
-------------
Report Number: SCRAP-0001
Batch Or Lot: OPEN-FG
Reason: Obsolete units
Write Down: $14,939.60

Footer
------
Internal document packet copy.
Page marker: D012
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
Willow Builders
220 Lake View Road, Bengaluru
Date: 2025-03-31

Reference Box
-------------
Document ID: D018
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Scanning checklist for back-office staff

Memo Summary
------------
Memo ID: INFO-0001
Subject: Scanning checklist for back-office staff
Audience: Finance Team

Memo Body
---------
Narrative: Please route scanned paperwork to the shared archive after the period binder is 
complete.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D020 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Willow Builders
220 Lake View Road, Bengaluru
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D020
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0002
Subject: Document retention reminder
Audience: Finance Team

Memo Body
---------
Narrative: Please route scanned paperwork to the shared archive after the period binder is 
complete.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D021 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Willow Builders
220 Lake View Road, Bengaluru
Date: 2025-03-31

Reference Box
-------------
Document ID: D021
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0102
Statement Currency: USD
Opening Balance: $237,347.09
Closing Balance: $241,716.19

Statement Rows
--------------
Rows:
  - Date 2024-10-16 | Description Direct labor BATCH-0001 | Amount $-62,079.74 | Running 
Balance $175,267.35
  - Date 2024-12-12 | Description Payroll PAYRUN-0001 | Amount $-62,916.91 | Running Balance
 $112,350.44
  - Date 2024-12-25 | Description Customer settlement FGINV-0001 | Amount $169,702.75 | 
Running Balance $282,053.19
  - Date 2025-01-21 | Description Supplier settlement MAT-0001 | Amount $-40,337.00 | 
Running Balance $241,716.19

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D021
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Raw Materials Inventory | Accounts Payable | 40,337.00 | D002 | 2024-06-13 | raw_material_purchase |
| 2 | Work In Process | Raw Materials Inventory | 29,628.51 | D003, D004, D002 | 2024-09-30 | material_issue |
| 3 | Work In Process | Cash | 62,079.74 | D005, D004 | 2024-10-16 | direct_labor_labor |
| 4 | Work In Process | Accrued Expenses | 33,278.86 | D006, D004 | 2025-03-16 | overhead_accrual_overhead |
| 5 | Finished Goods Inventory | Work In Process | 124,987.11 | D007, D004 | 2024-12-31 | finished_goods_transfer |
| 6 | Accounts Receivable | Sales Revenue | 169,702.75 | D008, D007 | 2025-02-05 | finished_goods_sale_sale |
| 7 | Cost of Goods Sold | Finished Goods Inventory | 124,987.11 | D008, D007 | 2025-02-05 | finished_goods_sale_cogs |
| 8 | Cash | Accounts Receivable | 169,702.75 | D009, D008 | 2024-12-25 | customer_payment |
| 9 | Accounts Payable | Cash | 40,337.00 | D010, D002 | 2025-01-21 | supplier_payment |
| 10 | Salaries Expense | Cash | 56,421.57 | D011 | 2024-12-12 | payroll_gross |
| 11 | Payroll Tax Expense | Cash | 6,495.34 | D011 | 2024-12-12 | payroll_tax |
| 12 | Inventory Shrinkage Expense | Finished Goods Inventory | 14,939.60 | D012, D001 | 2025-03-31 | scrap_report |
| 13 | Raw Materials Inventory | Accounts Payable | 62,812.26 | D013 | 2024-06-23 | raw_material_purchase |
| 14 | Raw Materials Inventory | Accounts Payable | 60,403.20 | D014 | 2024-07-06 | raw_material_purchase |
| 15 | Raw Materials Inventory | Accounts Payable | 46,860.45 | D015 | 2024-04-24 | raw_material_purchase |
| 16 | Raw Materials Inventory | Accounts Payable | 16,023.28 | D016 | 2024-07-11 | raw_material_purchase |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 241,716.19
- Raw Materials Inventory: 338,277.47
- Work In Process: 52,077.44
- Finished Goods Inventory: 87,417.35
- Accounts Receivable: 56,397.76

**Liabilities**
- Accounts Payable: 263,343.15
- Accrued Expenses: 47,536.86

**Equity**
- Retained Earnings: 34,030.55
- Share Capital: 430,975.65

**Totals:** Assets = 775,886.21; Liabilities = 310,880.01; Equity = 465,006.20
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
- Notes: Fine as ground truth.
