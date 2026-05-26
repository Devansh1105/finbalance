# Verification Packet — COV_MAN_Y4_0103

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 4
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Willow Advisors
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 28
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 470,459.35
- Raw Materials Inventory: 182,658.13
- Work In Process: 108,320.90
- Finished Goods Inventory: 94,925.50
- Accounts Receivable: 52,512.74
- Equipment: 101,626.39

**Liabilities**
- Accounts Payable: 56,643.63
- Accrued Expenses: 23,198.82
- Notes Payable: 61,530.92
- Loans Payable: 116,281.04

**Equity**
- Retained Earnings: 51,321.59
- Share Capital: 701,527.01


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
Statement Date: 01/04/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 470.459,35
  - Section assets | Account Raw Materials Inventory | Amount EUR 182.658,13
  - Section assets | Account Work In Process | Amount EUR 108.320,90
  - Section assets | Account Finished Goods Inventory | Amount EUR 94.925,50
  - Section assets | Account Accounts Receivable | Amount EUR 52.512,74
  - Section assets | Account Equipment | Amount EUR 101.626,39
  - Section liabilities | Account Accounts Payable | Amount EUR 56.643,63
  - Section liabilities | Account Accrued Expenses | Amount EUR 23.198,82
  - Section liabilities | Account Notes Payable | Amount EUR 61.530,92
  - Section liabilities | Account Loans Payable | Amount EUR 116.281,04
  - Section equity | Account Retained Earnings | Amount EUR 51.321,59
  - Section equity | Account Share Capital | Amount EUR 701.527,01

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D016 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-01

```
CUSTOMER INVOICE
================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Document Date: 01/04/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D016
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0001

Terms
-----
Due Date: 25/04/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0001

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 25/04/2024
Total: EUR 43.248,15

Line Items
----------
Items:
  - Description Monthly retainer | Amount EUR 15.217,12
  - Description Milestone 1 work | Amount EUR 28.031,03

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D024 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-04-01

```
SECONDARY COPY
==============

From
----
Willow Advisors
18 Marina Avenue, Chennai
Date: 01/04/2024

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D024
Document Type: secondary_copy
Period: FY 2024-25

Copy Summary
------------
Copy ID: COPY-0002
Source Reference: INV-0001
Counterparty: Blue Finch Holdings
Total: EUR 43.248,15
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D020 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-27

```
SUPPLIER INVOICE
================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Document Date: 27/04/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D020
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 13/05/2024

Supplier Header
---------------
Supplier: Pace Office Mart
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: MAT-0002
Due Date: 13/05/2024
Subtotal: EUR 34.588,46
Tax Label: Sales Tax
Tax Rate: 5.00%
Tax Amount: EUR 1.729,42
Total: EUR 36.317,88

Supplier Bill Lines
-------------------
Lines:
  - Description Resin pellets | Quantity 202 | Unit Cost EUR 171,23 | Amount EUR 34.588,46

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D017 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-04

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Date: 04/06/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D017
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0002

Terms
-----
Due Date: 15/06/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0002

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 15/06/2024
Total: EUR 50.414,18

Line Items
----------
Items:
  - Description Support package | Amount EUR 12.995,07
  - Description Milestone 2 work | Amount EUR 37.419,11

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D025 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-06-04

```
CANCELLATION NOTE
=================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Document Date: 04/06/2024

Reference Box
-------------
Document ID: D025
Document Type: cancellation_note
Period: FY 2024-25

Cancellation Summary
--------------------
Note Number: CNCL-0002
Withdrawn Reference: INV-0002-OLD
Replacement Reference: INV-0002

Background
----------
Narrative: INV-0002-OLD is withdrawn and must not be posted. Use INV-0002 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D025
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-16

```
SUPPLIER INVOICE
================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Document Date: 16/06/2024

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
Due Date: 08/07/2024

Supplier Header
---------------
Supplier: Meridian Support LLP
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 08/07/2024
Subtotal: EUR 53.772,11
Tax Label: Sales Tax
Tax Rate: 5.00%
Tax Amount: EUR 2.688,61
Total: EUR 56.460,72

Supplier Bill Lines
-------------------
Lines:
  - Description Control boards | Quantity 343 | Unit Cost EUR 156,77 | Amount EUR 53.772,11

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D021 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-27

```
SUPPLIER INVOICE
================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Document Date: 27/06/2024

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D021
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 11/07/2024

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: MAT-0003
Due Date: 11/07/2024
Subtotal: EUR 98.592,90
Tax Label: Sales Tax
Tax Rate: 5.00%
Tax Amount: EUR 4.929,65
Total: EUR 103.522,55

Supplier Bill Lines
-------------------
Lines:
  - Description Control boards | Quantity 399 | Unit Cost EUR 247,10 | Amount EUR 98.592,90

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D018 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-15

```
CUSTOMER INVOICE
================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Date: 15/09/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D018
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0003

Terms
-----
Due Date: 08/10/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 08/10/2024
Total: EUR 77.901,66

Line Items
----------
Items:
  - Description Consulting sprint | Amount EUR 32.872,42
  - Description Milestone 3 work | Amount EUR 45.029,24

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D023 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-09-15

```
SECONDARY COPY
==============

From
----
Willow Advisors
18 Marina Avenue, Chennai
Document Date: 15/09/2024

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D023
Document Type: secondary_copy
Period: FY 2024-25

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: INV-0003
Counterparty: Blue Finch Holdings
Total: EUR 77.901,66
Copy Context: Forwarded copy attached to the customer correspondence bundle.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D023
```

### Document D012 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-18

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: EUR 36.597,39
Draw Amount: EUR 244.776,09
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 281.373,48
Note: Scheduled lender activity for the selected period.
```

### Document D005 — Direct Labor Record

- **Type:** `direct_labor_record`
- **Role:** `posting_doc`
- **Date:** 2024-09-29

```
DIRECT LABOR RECORD
===================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Date: 29/09/2024

Reference Box
-------------
Document ID: D005
Document Type: direct_labor_record
Period: FY 2024-25

Labor Summary
-------------
Batch ID: BATCH-0001
Product: Assembly Unit
Planned Units: 57
Labor Value: EUR 36.815,05
Labor Cash Paid: EUR 36.815,05

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2024-10-09

```
MATERIAL REQUISITION SLIP
=========================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Document Date: 09/10/2024

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: FY 2024-25

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Control boards
Quantity Issued: 171
Issue Value: EUR 26.898,73
Warehouse: Overflow Storage

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2024-10-09

```
PRODUCTION BATCH SHEET
======================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Date: 09/10/2024

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: FY 2024-25

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Assembly Unit
Planned Units: 39
Material Value: EUR 26.898,73
Labor Value: EUR 0,00
Overhead Value: EUR 0,00

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D010 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-06

```
PAYMENT ADVICE
==============

From
----
Willow Advisors
18 Marina Avenue, Chennai
Document Date: 06/12/2024

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
Amount: EUR 51.463,37
Reference: MAT-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D019 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-14

```
PAYMENT ADVICE
==============

From
----
Willow Advisors
18 Marina Avenue, Chennai
Date: 14/12/2024

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D019
Document Type: payment_advice
Period: FY 2024-25
Reference: Multiple invoice allocation

Payment Details
---------------
Advice Number: PAY-0003
Counterparty: Blue Finch Holdings
Amount: EUR 127.739,39
Reference: Multiple invoice allocation
Payment Method: Wire
Payment For: Combined settlement against several invoices

Allocation Details
------------------
Allocations:
  - Reference INV-0001 | Allocated Amount EUR 43.248,15 | Status Closed
  - Reference INV-0002 | Allocated Amount EUR 50.414,18 | Status Closed
  - Reference INV-0003 | Allocated Amount EUR 34.077,06 | Status Partially paid

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D011 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-12-27

```
PAYROLL SUMMARY
===============

From
----
Willow Advisors
18 Marina Avenue, Chennai
Date: 27/12/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024-25
Headcount: 10
Gross Pay: EUR 161.897,09
Employer Tax: 21.230,79
Cash Outflow: EUR 183.127,88

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D008 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-02

```
CUSTOMER INVOICE
================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Document Date: 02/01/2025

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
Due Date: 21/01/2025

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: FGT-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 21/01/2025
Subtotal: EUR 168.572,53
Tax Label: Sales Tax
Tax Rate: 9.50%
Tax Amount: EUR 16.014,39
Total: EUR 184.586,92

Line Items
----------
Items:
  - Description Assembly Unit | Amount EUR 168.572,53

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D022 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-01-02

```
CANCELLATION NOTE
=================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Document Date: 02/01/2025

Reference Box
-------------
Document ID: D022
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
Page marker: D022
```

### Document D007 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2025-01-21

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Date: 21/01/2025

Reference Box
-------------
Document ID: D007
Document Type: finished_goods_transfer_note
Period: FY 2024-25

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Assembly Unit
Units Completed: 43
Transfer Value: EUR 128.406,14

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D009 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-01-25

```
PAYMENT ADVICE
==============

From
----
Willow Advisors
18 Marina Avenue, Chennai
Date: 25/01/2025

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
Amount: EUR 151.014,10
Reference: FGINV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D014 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-01-26

```
TRANSFER ADVICE
===============

From
----
Willow Advisors
18 Marina Avenue, Chennai
Date: 26/01/2025

Reference Box
-------------
Document ID: D014
Document Type: transfer_advice
Period: FY 2024-25
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: EUR 205.560,07
Transfer Date: 26/01/2025
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D006 — Overhead Accrual Memo

- **Type:** `overhead_accrual_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-02-24

```
OVERHEAD ACCRUAL MEMO
=====================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Date: 24/02/2025

Reference Box
-------------
Document ID: D006
Document Type: overhead_accrual_memo
Period: FY 2024-25

Overhead Summary
----------------
Batch ID: BATCH-0001
Product: Assembly Unit
Planned Units: 68
Overhead Value: EUR 64.692,36
Accrued Overhead: EUR 64.692,36

Explanation
-----------
Narrative: Factory overhead incurred this period has been accrued into work in process.

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D013 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Date: 31/03/2025

Reference Box
-------------
Document ID: D013
Document Type: fixed_asset_rollforward
Period: FY 2024-25

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: EUR 101.626,39
Useful Life: 48
Current Charge: EUR 25.406,64
Accumulated Depreciation: 25.406,64
Opening Balance: EUR 101.626,39
Additions: 0,00
Disposals: 0,00
Ending Balance: EUR 101.626,39

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D015 — Scrap Report

- **Type:** `scrap_report`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
SCRAP REPORT
============

From
----
Willow Advisors
18 Marina Avenue, Chennai
Date: 31/03/2025

Reference Box
-------------
Document ID: D015
Document Type: scrap_report
Period: FY 2024-25

Approval / Context
------------------
Reason: Damage in production

Scrap Summary
-------------
Report Number: SCRAP-0001
Batch Or Lot: OPEN-FG
Reason: Damage in production
Write Down: EUR 14.436,16

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D026 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
VENDOR STATEMENT
================

From
----
Willow Advisors
18 Marina Avenue, Chennai
Document Date: 31/03/2025

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D026
Document Type: vendor_statement
Period: FY 2024-25

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Meridian Support LLP
Closing Balance: EUR 4.997,35

Statement Lines
---------------
Lines:
  - Reference MAT-0001 | Document Type Open invoice | Amount EUR 4.997,35 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D026
```

### Document D027 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Willow Advisors
18 Marina Avenue, Chennai
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D027
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0103
Statement Currency: EUR
Opening Balance: EUR 470.459,35
Closing Balance: EUR 517.022,56

Statement Rows
--------------
Rows:
  - Date 18/09/2024 | Description Loan draw LOAN-0001 | Amount EUR 244.776,09 | Running 
Balance EUR 715.235,44
  - Date 29/09/2024 | Description Direct labor BATCH-0001 | Amount EUR -36.815,05 | Running 
Balance EUR 678.420,39
  - Date 06/12/2024 | Description Supplier settlement MAT-0001 | Amount EUR -51.463,37 | 
Running Balance EUR 626.957,02
  - Date 14/12/2024 | Description Combined customer settlement PAY-0003 | Amount EUR 
127.739,39 | Running Balance EUR 754.696,41
  - Date 27/12/2024 | Description Payroll PAYRUN-0001 | Amount EUR -183.127,88 | Running 
Balance EUR 571.568,53
  - Date 25/01/2025 | Description Customer settlement FGINV-0001 | Amount EUR 151.014,10 | 
Running Balance EUR 722.582,63
  - Date 26/01/2025 | Description Transfer out TRX-0001 | Amount EUR -205.560,07 | Running 
Balance EUR 517.022,56

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D027
```

### Document D028 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Willow Advisors
18 Marina Avenue, Chennai
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D028
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-0399
Statement Currency: EUR
Opening Balance: EUR 0,00
Closing Balance: EUR 205.560,07

Statement Rows
--------------
Rows:
  - Date 26/01/2025 | Description Transfer in TRX-0001 | Amount EUR 205.560,07 | Running 
Balance EUR 205.560,07

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D028
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Raw Materials Inventory | Accounts Payable | 53,772.11 | D002 | 2024-06-16 | raw_material_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 2,688.61 | D002 | 2024-06-16 | raw_material_purchase_tax |
| 3 | Work In Process | Raw Materials Inventory | 26,898.73 | D003, D004, D002 | 2024-10-09 | material_issue |
| 4 | Work In Process | Cash | 36,815.05 | D005, D004 | 2024-09-29 | direct_labor_labor |
| 5 | Work In Process | Accrued Expenses | 64,692.36 | D006, D004 | 2025-02-24 | overhead_accrual_overhead |
| 6 | Finished Goods Inventory | Work In Process | 128,406.14 | D007, D004 | 2025-01-21 | finished_goods_transfer |
| 7 | Accounts Receivable | Sales Revenue | 168,572.53 | D008, D007 | 2025-01-02 | finished_goods_sale_sale |
| 8 | Cost of Goods Sold | Finished Goods Inventory | 128,406.14 | D008, D007 | 2025-01-02 | finished_goods_sale_cogs |
| 9 | Accounts Receivable | Sales Tax Payable | 16,014.39 | D008, D007 | 2025-01-02 | finished_goods_sale_tax |
| 10 | Cash | Accounts Receivable | 151,014.10 | D009, D008 | 2025-01-25 | customer_payment |
| 11 | Accounts Payable | Cash | 51,463.37 | D010, D002 | 2024-12-06 | supplier_payment |
| 12 | Salaries Expense | Cash | 161,897.09 | D011 | 2024-12-27 | payroll_gross |
| 13 | Payroll Tax Expense | Cash | 21,230.79 | D011 | 2024-12-27 | payroll_tax |
| 14 | Cash | Loans Payable | 244,776.09 | D012 | 2024-09-18 | loan_draw |
| 15 | Depreciation Expense | Accumulated Depreciation | 25,406.64 | D013 | 2025-03-31 | depreciation |
| 16 | Reserve Cash | Cash | 205,560.07 | D014 | 2025-01-26 | interbank_transfer |
| 17 | Inventory Shrinkage Expense | Finished Goods Inventory | 14,436.16 | D015, D001 | 2025-03-31 | scrap_report |
| 18 | Accounts Receivable | Sales Revenue | 43,248.15 | D016 | 2024-04-01 | multi_invoice_payment_invoice_1 |
| 19 | Accounts Receivable | Sales Revenue | 50,414.18 | D017 | 2024-06-04 | multi_invoice_payment_invoice_2 |
| 20 | Accounts Receivable | Sales Revenue | 77,901.66 | D018 | 2024-09-15 | multi_invoice_payment_invoice_3 |
| 21 | Cash | Accounts Receivable | 43,248.15 | D019, D016 | 2024-12-14 | multi_invoice_payment_INV-0001 |
| 22 | Cash | Accounts Receivable | 50,414.18 | D019, D017 | 2024-12-14 | multi_invoice_payment_INV-0002 |
| 23 | Cash | Accounts Receivable | 34,077.06 | D019, D018 | 2024-12-14 | multi_invoice_payment_INV-0003 |
| 24 | Raw Materials Inventory | Accounts Payable | 34,588.46 | D020 | 2024-04-27 | raw_material_purchase |
| 25 | Input Tax Receivable | Accounts Payable | 1,729.42 | D020 | 2024-04-27 | raw_material_purchase_tax |
| 26 | Raw Materials Inventory | Accounts Payable | 98,592.90 | D021 | 2024-06-27 | raw_material_purchase |
| 27 | Input Tax Receivable | Accounts Payable | 4,929.65 | D021 | 2024-06-27 | raw_material_purchase_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 517,022.56
- Raw Materials Inventory: 342,712.87
- Work In Process: 108,320.90
- Finished Goods Inventory: 80,489.34
- Accounts Receivable: 129,910.16
- Equipment: 101,626.39
- Input Tax Receivable: 9,347.68
- Accumulated Depreciation: -25,406.64
- Reserve Cash: 205,560.07

**Liabilities**
- Accounts Payable: 201,481.41
- Accrued Expenses: 87,891.18
- Notes Payable: 61,530.92
- Loans Payable: 361,057.13
- Sales Tax Payable: 16,014.39

**Equity**
- Retained Earnings: 40,081.29
- Share Capital: 701,527.01

**Totals:** Assets = 1,469,583.33; Liabilities = 727,975.03; Equity = 741,608.30
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
