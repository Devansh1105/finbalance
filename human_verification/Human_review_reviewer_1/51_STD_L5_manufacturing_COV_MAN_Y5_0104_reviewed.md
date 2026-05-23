# Verification Packet — COV_MAN_Y5_0104

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 5
- **Period type:** year
- **Period label:** FY 2024
- **Period start → end:** 2024-01-01 → 2024-12-31
- **Entity:** Silverline Property Services
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 31
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-01-01_

**Assets**
- Cash: 408,615.77
- Raw Materials Inventory: 229,452.14
- Work In Process: 140,169.92
- Finished Goods Inventory: 152,462.47
- Accounts Receivable: 36,414.71
- Equipment: 184,102.41

**Liabilities**
- Accounts Payable: 46,773.04
- Accrued Expenses: 32,806.43
- Notes Payable: 46,473.08
- Loans Payable: 117,663.19

**Equity**
- Retained Earnings: 149,574.96
- Share Capital: 757,926.72


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
  - Section assets | Account Cash | Amount GBP 408,615.77
  - Section assets | Account Raw Materials Inventory | Amount GBP 229,452.14
  - Section assets | Account Work In Process | Amount GBP 140,169.92
  - Section assets | Account Finished Goods Inventory | Amount GBP 152,462.47
  - Section assets | Account Accounts Receivable | Amount GBP 36,414.71
  - Section assets | Account Equipment | Amount GBP 184,102.41
  - Section liabilities | Account Accounts Payable | Amount GBP 46,773.04
  - Section liabilities | Account Accrued Expenses | Amount GBP 32,806.43
  - Section liabilities | Account Notes Payable | Amount GBP 46,473.08
  - Section liabilities | Account Loans Payable | Amount GBP 117,663.19
  - Section equity | Account Retained Earnings | Amount GBP 149,574.96
  - Section equity | Account Share Capital | Amount GBP 757,926.72

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D023 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-01-05

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Silverline Property Services
14 King Street, Pune
Date: 05/01/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D023
Document Type: customer_invoice
Period: FY 2024
Contract Ref: CTR-0002

Terms
-----
Due Date: 26/01/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0002

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 26/01/2024
Total: GBP 75,646.45

Line Items
----------
Items:
  - Description Monthly retainer | Amount GBP 15,325.19
  - Description Milestone 1 work | Amount GBP 60,321.26

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D029 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-01-05

```
CANCELLATION NOTE
=================

From
----
Silverline Property Services
14 King Street, Pune
Date: 05/01/2024

Reference Box
-------------
Document ID: D029
Document Type: cancellation_note
Period: FY 2024

Cancellation Summary
--------------------
Note Number: CNCL-0002
Withdrawn Reference: INV-0003-OLD
Replacement Reference: INV-0003

Background
----------
Narrative: INV-0003-OLD is withdrawn and must not be posted. Use INV-0003 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D029
```

### Document D017 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-05

```
SUPPLIER INVOICE
================

From
----
Silverline Property Services
14 King Street, Pune
Date: 05/02/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D017
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 25/02/2024

Supplier Header
---------------
Supplier: Pace Office Mart
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: FXBILL-0001
Due Date: 25/02/2024
Total: $50,167.78

Supplier Bill Lines
-------------------
Lines:
  - Description Support package | Amount $17,104.78
  - Description Foreign-currency support | Amount $33,063.00

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D018 — Exchange Rate Notice

- **Type:** `exchange_rate_notice`
- **Role:** `support_doc`
- **Date:** 2024-02-05

```
EXCHANGE RATE NOTICE
====================

From
----
Silverline Property Services
14 King Street, Pune
Date: 05/02/2024

Reference Box
-------------
Document ID: D018
Document Type: exchange_rate_notice
Period: FY 2024
Reference: FXBILL-0001

Rate Summary
------------
Notice Number: RATE-0001
Reference: FXBILL-0001
Rate Date: 05/02/2024
Rate Type: Spot rate at bill date

Conversion Details
------------------
Source Currency: USD
Source Amount: $50,167.78
Functional Currency: GBP
Exchange Rate: 0.8104
Functional Amount: GBP 40,655.97

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D024 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-05

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Silverline Property Services
14 King Street, Pune
Date: 05/02/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D024
Document Type: customer_invoice
Period: FY 2024
Contract Ref: CTR-0003

Terms
-----
Due Date: 22/02/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 22/02/2024
Total: GBP 94,299.08

Line Items
----------
Items:
  - Description Review pack | Amount GBP 19,553.20
  - Description Milestone 2 work | Amount GBP 74,745.88

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D027 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-02-05

```
SECONDARY COPY
==============

From
----
Silverline Property Services
14 King Street, Pune
Date: 05/02/2024

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D027
Document Type: secondary_copy
Period: FY 2024

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: FXBILL-0001
Counterparty: Pace Office Mart
Total: GBP 50,167.78
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D027
```

### Document D020 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `distractor_doc`
- **Date:** 2024-03-16

```
CUSTOMER INVOICE
================

From
----
Silverline Property Services
14 King Street, Pune
Document Date: 16/03/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D020
Document Type: customer_invoice
Period: FY 2024
Contract Ref: CTR-0001

Terms
-----
Due Date: 04/04/2024

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0001

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 04/04/2024
Total: GBP 84,109.71

Line Items
----------
Items:
  - Description Consulting sprint | Amount GBP 17,651.46
  - Description Draft billing copy | Amount GBP 66,458.25

Notes
-----
Billing office archive copy retained with the packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D021 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `support_doc`
- **Date:** 2024-03-23

```
CANCELLATION NOTE
=================

From
----
Silverline Property Services
14 King Street, Pune
Document Date: 23/03/2024

Reference Box
-------------
Document ID: D021
Document Type: cancellation_note
Period: FY 2024

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0001
Replacement Reference: INV-0002

Background
----------
Narrative: INV-0001 is withdrawn and must not be posted. Use INV-0002 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D022 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-23

```
CUSTOMER INVOICE
================

From
----
Silverline Property Services
14 King Street, Pune
Date: 23/03/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D022
Document Type: customer_invoice
Period: FY 2024
Contract Ref: CTR-0001

Terms
-----
Due Date: 09/04/2024

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0001

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 09/04/2024
Total: GBP 83,943.10

Line Items
----------
Items:
  - Description Review pack | Amount GBP 25,695.44
  - Description Reissued billing | Amount GBP 58,247.66

Footer
------
Internal document packet copy.
Page marker: D022
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-11

```
SUPPLIER INVOICE
================

From
----
Silverline Property Services
14 King Street, Pune
Document Date: 11/04/2024

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 28/04/2024

Supplier Header
---------------
Supplier: Prime Utility Desk
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 28/04/2024
Subtotal: GBP 138,135.12
Tax Label: VAT
Tax Rate: 12.50%
Tax Amount: GBP 17,266.89
Total: GBP 155,402.01

Supplier Bill Lines
-------------------
Lines:
  - Description Packing film | Quantity 348 | Unit Cost GBP 396.94 | Amount GBP 138,135.12

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D025 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-09

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Silverline Property Services
14 King Street, Pune
Date: 09/05/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D025
Document Type: customer_invoice
Period: FY 2024
Contract Ref: CTR-0004

Terms
-----
Due Date: 21/05/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0004

Invoice Details
---------------
Invoice Number: INV-0005
Due Date: 21/05/2024
Total: GBP 31,785.63

Line Items
----------
Items:
  - Description Monthly retainer | Amount GBP 8,011.21
  - Description Milestone 3 work | Amount GBP 23,774.42

Footer
------
Internal document packet copy.
Page marker: D025
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2024-06-02

```
MATERIAL REQUISITION SLIP
=========================

From
----
Silverline Property Services
14 King Street, Pune
Date: 02/06/2024

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: FY 2024

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Packing film
Quantity Issued: 227
Issue Value: GBP 90,256.33
Warehouse: Overflow Storage

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2024-06-02

```
PRODUCTION BATCH SHEET
======================

From
----
Silverline Property Services
14 King Street, Pune
Document Date: 02/06/2024

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: FY 2024

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Panel Kit
Planned Units: 35
Material Value: GBP 90,256.33
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
- **Date:** 2024-06-09

```
DIRECT LABOR RECORD
===================

From
----
Silverline Property Services
14 King Street, Pune
Date: 09/06/2024

Reference Box
-------------
Document ID: D005
Document Type: direct_labor_record
Period: FY 2024

Labor Summary
-------------
Batch ID: BATCH-0001
Product: Panel Kit
Planned Units: 41
Labor Value: GBP 38,310.27
Labor Cash Paid: GBP 38,310.27

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D012 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-08-30

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: GBP 15,265.38
Draw Amount: GBP 615,783.53
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 631,048.91
Note: Scheduled lender activity for the selected period.
```

### Document D026 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-11

```
PAYMENT ADVICE
==============

From
----
Silverline Property Services
14 King Street, Pune
Date: 11/09/2024

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D026
Document Type: payment_advice
Period: FY 2024
Reference: Multiple invoice allocation

Payment Details
---------------
Advice Number: PAY-0003
Counterparty: Blue Finch Holdings
Amount: GBP 182,937.67
Reference: Multiple invoice allocation
Payment Method: Bank transfer
Payment For: Combined settlement against several invoices

Allocation Details
------------------
Allocations:
  - Reference INV-0003 | Allocated Amount GBP 75,646.45 | Status Closed
  - Reference INV-0004 | Allocated Amount GBP 94,299.08 | Status Closed
  - Reference INV-0005 | Allocated Amount GBP 12,992.14 | Status Partially paid

Footer
------
Internal document packet copy.
Page marker: D026
```

### Document D009 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-13

```
PAYMENT ADVICE
==============

From
----
Silverline Property Services
14 King Street, Pune
Date: 13/09/2024

To
--
Riverfront Group

Reference Box
-------------
Document ID: D009
Document Type: payment_advice
Period: FY 2024
Reference: FGINV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: GBP 182,094.66
Reference: FGINV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D007 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2024-09-21

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Silverline Property Services
14 King Street, Pune
Document Date: 21/09/2024

Reference Box
-------------
Document ID: D007
Document Type: finished_goods_transfer_note
Period: FY 2024

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Panel Kit
Units Completed: 55
Transfer Value: GBP 193,506.82

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D010 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-10-09

```
PAYMENT ADVICE
==============

From
----
Silverline Property Services
14 King Street, Pune
Date: 09/10/2024

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D010
Document Type: payment_advice
Period: FY 2024
Reference: MAT-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: GBP 141,011.84
Reference: MAT-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D011 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-10-18

```
PAYROLL SUMMARY
===============

From
----
Silverline Property Services
14 King Street, Pune
Document Date: 18/10/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024
Headcount: 12
Gross Pay: GBP 152,703.47
Employer Tax: 19,211.33
Cash Outflow: GBP 171,914.80

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D008 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-10-28

```
CUSTOMER INVOICE
================

From
----
Silverline Property Services
14 King Street, Pune
Date: 28/10/2024

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D008
Document Type: customer_invoice
Period: FY 2024
Contract Ref: FGT-0001

Terms
-----
Due Date: 15/11/2024

Parties
-------
Customer: Riverfront Group
Contract Ref: FGT-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 15/11/2024
Subtotal: GBP 234,561.58
Tax Label: VAT
Tax Rate: 12.50%
Tax Amount: GBP 29,320.20
Total: GBP 263,881.78

Line Items
----------
Items:
  - Description Panel Kit | Amount GBP 234,561.58

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D014 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-10-28

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Stonebridge Finance
Opening Principal: GBP 96,926.12
Draw Amount: GBP 0.00
Principal Paid: GBP 86,790.08
Interest Paid: GBP 12,635.69
Ending Principal: GBP 10,136.04
Note: Scheduled lender activity for the selected period.
```

### Document D028 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-10-28

```
SECONDARY COPY
==============

From
----
Silverline Property Services
14 King Street, Pune
Date: 28/10/2024

To
--
Riverfront Group

Reference Box
-------------
Document ID: D028
Document Type: secondary_copy
Period: FY 2024

Copy Summary
------------
Copy ID: COPY-0002
Source Reference: FGINV-0001
Counterparty: Riverfront Group
Total: GBP 263,881.78
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D028
```

### Document D015 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-02

```
TRANSFER ADVICE
===============

From
----
Silverline Property Services
14 King Street, Pune
Document Date: 02/11/2024

Reference Box
-------------
Document ID: D015
Document Type: transfer_advice
Period: FY 2024
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: GBP 675,575.58
Transfer Date: 02/11/2024
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D006 — Overhead Accrual Memo

- **Type:** `overhead_accrual_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-17

```
OVERHEAD ACCRUAL MEMO
=====================

From
----
Silverline Property Services
14 King Street, Pune
Date: 17/12/2024

Reference Box
-------------
Document ID: D006
Document Type: overhead_accrual_memo
Period: FY 2024

Overhead Summary
----------------
Batch ID: BATCH-0001
Product: Panel Kit
Planned Units: 51
Overhead Value: GBP 64,940.22
Accrued Overhead: GBP 64,940.22

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
- **Date:** 2024-12-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Silverline Property Services
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D013
Document Type: fixed_asset_rollforward
Period: FY 2024

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: GBP 184,102.41
Useful Life: 48
Current Charge: GBP 46,025.64
Accumulated Depreciation: 46,025.64
Opening Balance: GBP 184,102.41
Additions: 0.00
Disposals: 0.00
Ending Balance: GBP 184,102.41

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D016 — Scrap Report

- **Type:** `scrap_report`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
SCRAP REPORT
============

From
----
Silverline Property Services
14 King Street, Pune
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D016
Document Type: scrap_report
Period: FY 2024

Approval / Context
------------------
Reason: Damage in production

Scrap Summary
-------------
Report Number: SCRAP-0001
Batch Or Lot: OPEN-FG
Reason: Damage in production
Write Down: GBP 27,695.55

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D019 — FX Remeasurement Memo

- **Type:** `fx_remeasurement_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
FX REMEASUREMENT MEMO
=====================

From
----
Silverline Property Services
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D019
Document Type: fx_remeasurement_memo
Period: FY 2024
Reference: FXBILL-0001

Remeasurement Details
---------------------
Memo ID: FXREM-0001
Reference: FXBILL-0001
Source Currency: USD
Functional Currency: GBP
Source Amount: $50,167.78
Booked Amount: GBP 40,655.97
Closing Rate: 0.8340
Remeasured Amount: GBP 41,839.93
Difference Amount: GBP 1,183.96
Narrative: Open foreign-currency balance remeasured at the closing rate.

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D030 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Silverline Property Services
14 King Street, Pune
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D030
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0104
Statement Currency: GBP
Opening Balance: GBP 408,615.77
Closing Balance: GBP 263,193.37

Statement Rows
--------------
Rows:
  - Date 09/06/2024 | Description Direct labor BATCH-0001 | Amount GBP -38,310.27 | Running 
Balance GBP 370,305.50
  - Date 30/08/2024 | Description Loan draw LOAN-0001 | Amount GBP 615,783.53 | Running 
Balance GBP 986,089.03
  - Date 11/09/2024 | Description Combined customer settlement PAY-0003 | Amount GBP 
182,937.67 | Running Balance GBP 1,169,026.70
  - Date 13/09/2024 | Description Customer settlement FGINV-0001 | Amount GBP 182,094.66 | 
Running Balance GBP 1,351,121.36
  - Date 09/10/2024 | Description Supplier settlement MAT-0001 | Amount GBP -141,011.84 | 
Running Balance GBP 1,210,109.52
  - Date 18/10/2024 | Description Payroll PAYRUN-0001 | Amount GBP -171,914.80 | Running 
Balance GBP 1,038,194.72
  - Date 28/10/2024 | Description Loan payment LOAN-0002 | Amount GBP -99,425.77 | Running 
Balance GBP 938,768.95
  - Date 02/11/2024 | Description Transfer out TRX-0001 | Amount GBP -675,575.58 | Running 
Balance GBP 263,193.37

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D030
```

### Document D031 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Silverline Property Services
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D031
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-0499
Statement Currency: GBP
Opening Balance: GBP 0.00
Closing Balance: GBP 675,575.58

Statement Rows
--------------
Rows:
  - Date 02/11/2024 | Description Transfer in TRX-0001 | Amount GBP 675,575.58 | Running 
Balance GBP 675,575.58

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D031
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Raw Materials Inventory | Accounts Payable | 138,135.12 | D002 | 2024-04-11 | raw_material_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 17,266.89 | D002 | 2024-04-11 | raw_material_purchase_tax |
| 3 | Work In Process | Raw Materials Inventory | 90,256.33 | D003, D004, D002 | 2024-06-02 | material_issue |
| 4 | Work In Process | Cash | 38,310.27 | D005, D004 | 2024-06-09 | direct_labor_labor |
| 5 | Work In Process | Accrued Expenses | 64,940.22 | D006, D004 | 2024-12-17 | overhead_accrual_overhead |
| 6 | Finished Goods Inventory | Work In Process | 193,506.82 | D007, D004 | 2024-09-21 | finished_goods_transfer |
| 7 | Accounts Receivable | Sales Revenue | 234,561.58 | D008, D007 | 2024-10-28 | finished_goods_sale_sale |
| 8 | Cost of Goods Sold | Finished Goods Inventory | 193,506.82 | D008, D007 | 2024-10-28 | finished_goods_sale_cogs |
| 9 | Accounts Receivable | Sales Tax Payable | 29,320.20 | D008, D007 | 2024-10-28 | finished_goods_sale_tax |
| 10 | Cash | Accounts Receivable | 182,094.66 | D009, D008 | 2024-09-13 | customer_payment |
| 11 | Accounts Payable | Cash | 141,011.84 | D010, D002 | 2024-10-09 | supplier_payment |
| 12 | Salaries Expense | Cash | 152,703.47 | D011 | 2024-10-18 | payroll_gross |
| 13 | Payroll Tax Expense | Cash | 19,211.33 | D011 | 2024-10-18 | payroll_tax |
| 14 | Cash | Loans Payable | 615,783.53 | D012 | 2024-08-30 | loan_draw |
| 15 | Depreciation Expense | Accumulated Depreciation | 46,025.64 | D013 | 2024-12-31 | depreciation |
| 16 | Loans Payable | Cash | 86,790.08 | D014 | 2024-10-28 | loan_repayment_principal |
| 17 | Interest Expense | Cash | 12,635.69 | D014 | 2024-10-28 | loan_repayment_interest |
| 18 | Reserve Cash | Cash | 675,575.58 | D015 | 2024-11-02 | interbank_transfer |
| 19 | Inventory Shrinkage Expense | Finished Goods Inventory | 27,695.55 | D016, D001 | 2024-12-31 | scrap_report |
| 20 | Raw Materials Inventory | Accounts Payable | 40,655.97 | D017, D018 | 2024-02-05 | fx_material_purchase |
| 21 | Foreign Exchange Loss | Accounts Payable | 1,183.96 | D019, D017 | 2024-12-31 | fx_remeasurement |
| 22 | Accounts Receivable | Sales Revenue | 83,943.10 | D020, D021, D022 | 2024-03-23 | reissued_invoice |
| 23 | Accounts Receivable | Sales Revenue | 75,646.45 | D023 | 2024-01-05 | multi_invoice_payment_invoice_1 |
| 24 | Accounts Receivable | Sales Revenue | 94,299.08 | D024 | 2024-02-05 | multi_invoice_payment_invoice_2 |
| 25 | Accounts Receivable | Sales Revenue | 31,785.63 | D025 | 2024-05-09 | multi_invoice_payment_invoice_3 |
| 26 | Cash | Accounts Receivable | 75,646.45 | D026, D023 | 2024-09-11 | multi_invoice_payment_INV-0003 |
| 27 | Cash | Accounts Receivable | 94,299.08 | D026, D024 | 2024-09-11 | multi_invoice_payment_INV-0004 |
| 28 | Cash | Accounts Receivable | 12,992.14 | D026, D025 | 2024-09-11 | multi_invoice_payment_INV-0005 |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 263,193.37
- Raw Materials Inventory: 317,986.90
- Work In Process: 140,169.92
- Finished Goods Inventory: 124,766.92
- Accounts Receivable: 220,938.42
- Equipment: 184,102.41
- Input Tax Receivable: 17,266.89
- Accumulated Depreciation: -46,025.64
- Reserve Cash: 675,575.58

**Liabilities**
- Accounts Payable: 103,003.14
- Accrued Expenses: 97,746.65
- Notes Payable: 46,473.08
- Loans Payable: 646,656.64
- Sales Tax Payable: 29,320.20

**Equity**
- Retained Earnings: 216,848.34
- Share Capital: 757,926.72

**Totals:** Assets = 1,897,974.77; Liabilities = 923,199.71; Equity = 974,775.06
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
- Notes: Complex packet — entries hold up on review.
