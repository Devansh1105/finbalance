# Verification Packet — COV_MAN_Y2_0101

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 2
- **Period type:** year
- **Period label:** FY 2024
- **Period start → end:** 2024-01-01 → 2024-12-31
- **Entity:** Atlas Distribution
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 16
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-01-01_

**Assets**
- Cash: 369,472.27
- Raw Materials Inventory: 121,627.28
- Work In Process: 81,712.21
- Finished Goods Inventory: 55,192.42

**Liabilities**
- Accounts Payable: 78,367.73
- Accrued Expenses: 8,465.23

**Equity**
- Retained Earnings: 101,373.33
- Share Capital: 439,797.89


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/01/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 369,472.27
  - Section assets | Account Raw Materials Inventory | Amount GBP 121,627.28
  - Section assets | Account Work In Process | Amount GBP 81,712.21
  - Section assets | Account Finished Goods Inventory | Amount GBP 55,192.42
  - Section liabilities | Account Accounts Payable | Amount GBP 78,367.73
  - Section liabilities | Account Accrued Expenses | Amount GBP 8,465.23
  - Section equity | Account Retained Earnings | Amount GBP 101,373.33
  - Section equity | Account Share Capital | Amount GBP 439,797.89

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D012 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-01-23

```
SUPPLIER INVOICE
================

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Document Date: 23/01/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 11/02/2024

Supplier Header
---------------
Supplier: Vertex Supply Co.
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: MAT-0004
Due Date: 11/02/2024
Subtotal: GBP 18,655.80
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 3,358.04
CGST Amount: GBP 1,679.02
SGST Amount: GBP 1,679.02
Total: GBP 22,013.84

Supplier Bill Lines
-------------------
Lines:
  - Description Packing film | Quantity 372 | Unit Cost GBP 50.15 | Amount GBP 18,655.80

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-08

```
SUPPLIER INVOICE
================

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Date: 08/02/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 25/02/2024

Supplier Header
---------------
Supplier: Pace Office Mart
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 25/02/2024
Subtotal: GBP 16,075.42
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 2,893.58
CGST Amount: GBP 1,446.79
SGST Amount: GBP 1,446.79
Total: GBP 18,969.00

Supplier Bill Lines
-------------------
Lines:
  - Description Control boards | Quantity 167 | Unit Cost GBP 96.26 | Amount GBP 16,075.42

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D011 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-16

```
SUPPLIER INVOICE
================

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Date: 16/03/2024

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 01/04/2024

Supplier Header
---------------
Supplier: Oakline Services
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: MAT-0003
Due Date: 01/04/2024
Subtotal: GBP 48,545.96
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 8,738.27
CGST Amount: GBP 4,369.14
SGST Amount: GBP 4,369.13
Total: GBP 57,284.23

Supplier Bill Lines
-------------------
Lines:
  - Description Control boards | Quantity 412 | Unit Cost GBP 117.83 | Amount GBP 48,545.96

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D010 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-28

```
SUPPLIER INVOICE
================

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Document Date: 28/03/2024

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 09/04/2024

Supplier Header
---------------
Supplier: Golden State Finance
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: MAT-0002
Due Date: 09/04/2024
Subtotal: GBP 13,134.16
Tax Label: India GST
Tax Rate: 5.00%
Tax Amount: GBP 656.71
CGST Amount: GBP 328.36
SGST Amount: GBP 328.35
Total: GBP 13,790.87

Supplier Bill Lines
-------------------
Lines:
  - Description Steel sheets | Quantity 173 | Unit Cost GBP 75.92 | Amount GBP 13,134.16

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2024-08-27

```
MATERIAL REQUISITION SLIP
=========================

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Date: 27/08/2024

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: FY 2024

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Control boards
Quantity Issued: 86
Issue Value: GBP 8,333.52
Warehouse: Main Warehouse

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2024-08-27

```
PRODUCTION BATCH SHEET
======================

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Document Date: 27/08/2024

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: FY 2024

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Assembly Unit
Planned Units: 64
Material Value: GBP 8,333.52
Labor Value: GBP 0.00
Overhead Value: GBP 0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D005 — Direct Labor Record

- **Type:** `direct_labor_record`
- **Role:** `posting_doc`
- **Date:** 2024-08-27

```
DIRECT LABOR RECORD
===================

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Date: 27/08/2024

Reference Box
-------------
Document ID: D005
Document Type: direct_labor_record
Period: FY 2024

Labor Summary
-------------
Batch ID: BATCH-0001
Product: Assembly Unit
Planned Units: 80
Labor Value: GBP 15,957.17
Labor Cash Paid: GBP 15,957.17

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D006 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2024-09-29

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Document Date: 29/09/2024

Reference Box
-------------
Document ID: D006
Document Type: finished_goods_transfer_note
Period: FY 2024

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Assembly Unit
Units Completed: 54
Transfer Value: GBP 24,290.69

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D007 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-10-20

```
CUSTOMER INVOICE
================

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Document Date: 20/10/2024

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D007
Document Type: customer_invoice
Period: FY 2024
Contract Ref: FGT-0001

Terms
-----
Due Date: 12/11/2024

Parties
-------
Customer: Riverfront Group
Contract Ref: FGT-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 12/11/2024
Subtotal: GBP 32,356.50
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 5,824.17
CGST Amount: GBP 2,912.09
SGST Amount: GBP 2,912.08
Total: GBP 38,180.67

Line Items
----------
Items:
  - Description Assembly Unit | Amount GBP 32,356.50

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D014 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-10-20

```
CANCELLATION NOTE
=================

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Date: 20/10/2024

Reference Box
-------------
Document ID: D014
Document Type: cancellation_note
Period: FY 2024

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
Internal document packet copy.
Page marker: D014
```

### Document D008 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-10-23

```
PAYMENT ADVICE
==============

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Document Date: 23/10/2024

To
--
Riverfront Group

Reference Box
-------------
Document ID: D008
Document Type: payment_advice
Period: FY 2024
Reference: FGINV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: GBP 38,180.67
Reference: FGINV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D009 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-23

```
PAYMENT ADVICE
==============

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Date: 23/11/2024

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D009
Document Type: payment_advice
Period: FY 2024
Reference: MAT-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Pace Office Mart
Amount: GBP 18,969.00
Reference: MAT-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D013 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
VENDOR STATEMENT
================

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Document Date: 31/12/2024

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D013
Document Type: vendor_statement
Period: FY 2024

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Golden State Finance
Closing Balance: GBP 13,790.87

Statement Lines
---------------
Lines:
  - Reference MAT-0002 | Document Type Open invoice | Amount GBP 13,790.87 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D015 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
VENDOR STATEMENT
================

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Document Date: 31/12/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D015
Document Type: vendor_statement
Period: FY 2024

Statement Header
----------------
Statement Number: VSTMT-0002
Vendor: Vertex Supply Co.
Closing Balance: GBP 22,013.84

Statement Lines
---------------
Lines:
  - Reference MAT-0004 | Document Type Open invoice | Amount GBP 22,013.84 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D016 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Atlas Distribution
220 Lake View Road, Bengaluru
Date: 31/12/2024

Reference Box
-------------
Document ID: D016
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0101
Statement Currency: GBP
Opening Balance: GBP 369,472.27
Closing Balance: GBP 372,726.77

Statement Rows
--------------
Rows:
  - Date 27/08/2024 | Description Direct labor BATCH-0001 | Amount GBP -15,957.17 | Running 
Balance GBP 353,515.10
  - Date 23/10/2024 | Description Customer settlement FGINV-0001 | Amount GBP 38,180.67 | 
Running Balance GBP 391,695.77
  - Date 23/11/2024 | Description Supplier settlement MAT-0001 | Amount GBP -18,969.00 | 
Running Balance GBP 372,726.77

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D016
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Raw Materials Inventory | Accounts Payable | 16,075.42 | D002 | 2024-02-08 | raw_material_purchase |
| 2 | Input CGST Receivable | Accounts Payable | 1,446.79 | D002 | 2024-02-08 | raw_material_purchase_tax_cgst |
| 3 | Input SGST Receivable | Accounts Payable | 1,446.79 | D002 | 2024-02-08 | raw_material_purchase_tax_sgst |
| 4 | Work In Process | Raw Materials Inventory | 8,333.52 | D003, D004, D002 | 2024-08-27 | material_issue |
| 5 | Work In Process | Cash | 15,957.17 | D005, D004 | 2024-08-27 | direct_labor_labor |
| 6 | Finished Goods Inventory | Work In Process | 24,290.69 | D006, D004 | 2024-09-29 | finished_goods_transfer |
| 7 | Accounts Receivable | Sales Revenue | 32,356.50 | D007, D006 | 2024-10-20 | finished_goods_sale_sale |
| 8 | Cost of Goods Sold | Finished Goods Inventory | 24,290.69 | D007, D006 | 2024-10-20 | finished_goods_sale_cogs |
| 9 | Accounts Receivable | CGST Payable | 2,912.09 | D007, D006 | 2024-10-20 | finished_goods_sale_tax_cgst |
| 10 | Accounts Receivable | SGST Payable | 2,912.08 | D007, D006 | 2024-10-20 | finished_goods_sale_tax_sgst |
| 11 | Cash | Accounts Receivable | 38,180.67 | D008, D007 | 2024-10-23 | customer_payment |
| 12 | Accounts Payable | Cash | 18,969.00 | D009, D002 | 2024-11-23 | supplier_payment |
| 13 | Raw Materials Inventory | Accounts Payable | 13,134.16 | D010 | 2024-03-28 | raw_material_purchase |
| 14 | Input CGST Receivable | Accounts Payable | 328.36 | D010 | 2024-03-28 | raw_material_purchase_tax_cgst |
| 15 | Input SGST Receivable | Accounts Payable | 328.35 | D010 | 2024-03-28 | raw_material_purchase_tax_sgst |
| 16 | Raw Materials Inventory | Accounts Payable | 48,545.96 | D011 | 2024-03-16 | raw_material_purchase |
| 17 | Input CGST Receivable | Accounts Payable | 4,369.14 | D011 | 2024-03-16 | raw_material_purchase_tax_cgst |
| 18 | Input SGST Receivable | Accounts Payable | 4,369.13 | D011 | 2024-03-16 | raw_material_purchase_tax_sgst |
| 19 | Raw Materials Inventory | Accounts Payable | 18,655.80 | D012 | 2024-01-23 | raw_material_purchase |
| 20 | Input CGST Receivable | Accounts Payable | 1,679.02 | D012 | 2024-01-23 | raw_material_purchase_tax_cgst |
| 21 | Input SGST Receivable | Accounts Payable | 1,679.02 | D012 | 2024-01-23 | raw_material_purchase_tax_sgst |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 372,726.77
- Raw Materials Inventory: 209,705.10
- Work In Process: 81,712.21
- Finished Goods Inventory: 55,192.42
- Input CGST Receivable: 7,823.31
- Input SGST Receivable: 7,823.29

**Liabilities**
- Accounts Payable: 171,456.67
- Accrued Expenses: 8,465.23
- CGST Payable: 2,912.09
- SGST Payable: 2,912.08

**Equity**
- Retained Earnings: 109,439.14
- Share Capital: 439,797.89

**Totals:** Assets = 734,983.10; Liabilities = 185,746.07; Equity = 549,237.03
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
