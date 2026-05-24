# Verification Packet — COV_FIE_Y5_0029

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 5
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Cedar Retail Group
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 31
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 161,182.64
- Accounts Receivable: 18,831.76
- Office Supplies: 7,663.23
- Vehicles: 79,271.45
- Equipment: 36,822.27
- Prepaid Insurance: 7,984.56

**Liabilities**
- Accounts Payable: 22,424.12
- Accrued Expenses: 4,859.23
- Notes Payable: 30,712.93
- Loans Payable: 47,475.03

**Equity**
- Retained Earnings: 27,705.56
- Owner's Equity: 178,579.04


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
  - Section assets | Account Cash | Amount GBP 161,182.64
  - Section assets | Account Accounts Receivable | Amount GBP 18,831.76
  - Section assets | Account Office Supplies | Amount GBP 7,663.23
  - Section assets | Account Vehicles | Amount GBP 79,271.45
  - Section assets | Account Equipment | Amount GBP 36,822.27
  - Section assets | Account Prepaid Insurance | Amount GBP 7,984.56
  - Section liabilities | Account Accounts Payable | Amount GBP 22,424.12
  - Section liabilities | Account Accrued Expenses | Amount GBP 4,859.23
  - Section liabilities | Account Notes Payable | Amount GBP 30,712.93
  - Section liabilities | Account Loans Payable | Amount GBP 47,475.03
  - Section equity | Account Retained Earnings | Amount GBP 27,705.56
  - Section equity | Account Owner's Equity | Amount GBP 178,579.04

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-04-26

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Blue Finch Holdings
Job Site: Riverbank Plaza
Scope: Implementation work
Approved Amount: GBP 38,043.49

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D026 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-26

```
SUPPLIER INVOICE
================

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Document Date: 26/04/2024

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D026
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 08/05/2024

Supplier Header
---------------
Supplier: Golden State Finance
Expense Category: Repairs Expense
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0003
Due Date: 08/05/2024
Subtotal: GBP 9,012.75
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 1,622.29
CGST Amount: GBP 811.14
SGST Amount: GBP 811.15
Total: GBP 10,635.04

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 16 | Unit Cost GBP 240.86 | 
Amount GBP 3,853.83
  - Description Preventive maintenance service parts | Quantity 9 | Unit Cost GBP 573.21 | 
Amount GBP 5,158.92

Footer
------
Generated for synthetic accounting research use.
Page marker: D026
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-27

```
CUSTOMER INVOICE
================

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 27/04/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 13/05/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 13/05/2024
Subtotal: GBP 38,043.49
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 6,847.83
CGST Amount: GBP 3,423.91
SGST Amount: GBP 3,423.92
Total: GBP 44,891.32

Line Items
----------
Items:
  - Description Review pack | Amount GBP 12,306.17
  - Description Follow-up support | Amount GBP 25,737.32

Field Job
---------
Job Code: JOB-0001

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D030 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-04-27

```
SECONDARY COPY
==============

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 27/04/2024

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D030
Document Type: secondary_copy
Period: FY 2024-25

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: INV-0001
Counterparty: Blue Finch Holdings
Total: GBP 44,891.32
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D030
```

### Document D016 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-05-25

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0002
Customer: Oak Harbor Foods
Job Site: Marina Site
Scope: Review pack
Approved Amount: GBP 21,132.83

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D017 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-26

```
CUSTOMER INVOICE
================

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 26/05/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D017
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0002
Job Code: JOB-0002

Terms
-----
Due Date: 06/06/2024

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0002
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 06/06/2024
Subtotal: GBP 21,132.83
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 3,803.91
CGST Amount: GBP 1,901.95
SGST Amount: GBP 1,901.96
Total: GBP 24,936.74

Line Items
----------
Items:
  - Description Consulting sprint | Amount GBP 5,537.55
  - Description Follow-up support | Amount GBP 15,595.28

Field Job
---------
Job Code: JOB-0002

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D004 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-03

```
SUPPLIER INVOICE
================

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 03/06/2024

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 15/06/2024

Supplier Header
---------------
Supplier: Prime Utility Desk
Expense Category: Repairs Expense
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 15/06/2024
Subtotal: GBP 58,002.56
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 10,440.46
CGST Amount: GBP 5,220.23
SGST Amount: GBP 5,220.23
Total: GBP 68,443.02

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 21 | Unit Cost GBP 693.69 | 
Amount GBP 14,567.49
  - Description Preventive maintenance service parts | Quantity 8 | Unit Cost GBP 5,429.38 |
 Amount GBP 43,435.07

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D024 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0003
Customer: Crescent Labs
Job Site: Marina Site
Scope: Implementation work
Approved Amount: GBP 84,890.29

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D025 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-01

```
CUSTOMER INVOICE
================

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 01/07/2024

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D025
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0003
Job Code: JOB-0003

Terms
-----
Due Date: 18/07/2024

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0003
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 18/07/2024
Subtotal: GBP 84,890.29
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 15,280.25
CGST Amount: GBP 7,640.12
SGST Amount: GBP 7,640.13
Total: GBP 100,170.54

Line Items
----------
Items:
  - Description Review pack | Amount GBP 26,549.90
  - Description Follow-up support | Amount GBP 58,340.39

Field Job
---------
Job Code: JOB-0003

Footer
------
Internal document packet copy.
Page marker: D025
```

### Document D029 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-07-01

```
CANCELLATION NOTE
=================

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 01/07/2024

Reference Box
-------------
Document ID: D029
Document Type: cancellation_note
Period: FY 2024-25

Cancellation Summary
--------------------
Note Number: CNCL-0001
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

### Document D019 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-03

```
SUPPLIER INVOICE
================

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 03/07/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D019
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 24/07/2024

Supplier Header
---------------
Supplier: Pace Office Mart
Expense Category: Repairs Expense
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 24/07/2024
Subtotal: GBP 7,468.72
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 1,344.37
CGST Amount: GBP 672.18
SGST Amount: GBP 672.19
Total: GBP 8,813.09

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 20 | Unit Cost GBP 110.26 | 
Amount GBP 2,205.20
  - Description Preventive maintenance service parts | Quantity 19 | Unit Cost GBP 277.03 | 
Amount GBP 5,263.52

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D015 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-07-27

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Beacon Industrial Supply
Total: GBP 1,386.76
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount GBP 500.96
  - Description Fuel Incidentals | Amount GBP 885.80
```

### Document D021 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-07-31

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0003
Merchant: Beacon Industrial Supply
Total: GBP 1,043.34
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount GBP 384.15
  - Description Fuel Incidentals | Amount GBP 659.19
```

### Document D027 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-09-12

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0004
Merchant: Pace Office Mart
Total: GBP 1,148.24
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount GBP 232.80
  - Description Fuel Incidentals | Amount GBP 915.44
```

### Document D011 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-18

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
Total: GBP 412,496.67
Paid Cash: GBP 137,017.25
Financed Amount: GBP 275,479.42
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-10-16

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Prime Utility Desk
Total: GBP 82.43
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount GBP 29.34
  - Description Fuel Incidentals | Amount GBP 53.09
```

### Document D010 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-11-22

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: GBP 10,068.44
Draw Amount: GBP 298,974.01
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 309,042.45
Note: Scheduled lender activity for the selected period.
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-07

```
PAYMENT ADVICE
==============

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 07/12/2024

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2024-25
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: GBP 29,899.63
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D023 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-12-13

```
UTILITY INVOICE
===============

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 13/12/2024

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D023
Document Type: utilities_statement
Period: FY 2024-25

Terms
-----
Due Date: 27/12/2024

Invoice Summary
---------------
Statement Number: UTIL-0005
Invoice Number: UTILINV-0005
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: FY 2024-25
Due Date: 27/12/2024
Total: GBP 11,193.73

Charges
-------
Charges:
  - Description Electricity | Amount GBP 2,692.83
  - Description Water | Amount GBP 8,500.90

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D018 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-12-23

```
UTILITY INVOICE
===============

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 23/12/2024

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D018
Document Type: utilities_statement
Period: FY 2024-25

Terms
-----
Due Date: 07/01/2025

Invoice Summary
---------------
Statement Number: UTIL-0002
Invoice Number: UTILINV-0002
Provider: Metro Water
Pay To: Metro Water
Service Period: FY 2024-25
Due Date: 07/01/2025
Total: GBP 9,006.82

Charges
-------
Charges:
  - Description Electricity | Amount GBP 3,672.39
  - Description Water | Amount GBP 5,334.43

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-01-01

```
PAYMENT ADVICE
==============

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 01/01/2025

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2024-25
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: GBP 63,686.14
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D009 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-01-04

```
UTILITY INVOICE
===============

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 04/01/2025

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: utilities_statement
Period: FY 2024-25

Terms
-----
Due Date: 11/01/2025

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: FY 2024-25
Due Date: 11/01/2025
Total: GBP 11,021.36

Charges
-------
Charges:
  - Description Electricity | Amount GBP 3,581.16
  - Description Water | Amount GBP 7,440.20

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D022 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-01-19

```
UTILITY INVOICE
===============

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 19/01/2025

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D022
Document Type: utilities_statement
Period: FY 2024-25

Terms
-----
Due Date: 02/02/2025

Invoice Summary
---------------
Statement Number: UTIL-0004
Invoice Number: UTILINV-0004
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: FY 2024-25
Due Date: 02/02/2025
Total: GBP 3,099.38

Charges
-------
Charges:
  - Description Electricity | Amount GBP 1,089.65
  - Description Water | Amount GBP 2,009.73

Footer
------
Internal document packet copy.
Page marker: D022
```

### Document D013 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-01-21

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: GBP 270,860.71
Draw Amount: GBP 0.00
Principal Paid: GBP 60,275.17
Interest Paid: GBP 6,602.50
Ending Principal: GBP 210,585.54
Note: Scheduled lender activity for the selected period.
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-02-06

```
PAYROLL SUMMARY
===============

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 06/02/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024-25
Headcount: 7
Gross Pay: GBP 59,466.32
Employer Tax: 7,756.58
Cash Outflow: GBP 67,222.90

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D020 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-02-12

```
UTILITY INVOICE
===============

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Document Date: 12/02/2025

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D020
Document Type: utilities_statement
Period: FY 2024-25

Terms
-----
Due Date: 02/03/2025

Invoice Summary
---------------
Statement Number: UTIL-0003
Invoice Number: UTILINV-0003
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: FY 2024-25
Due Date: 02/03/2025
Total: GBP 9,917.26

Charges
-------
Charges:
  - Description Electricity | Amount GBP 4,094.17
  - Description Water | Amount GBP 5,823.09

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D012 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 31/03/2025

Reference Box
-------------
Document ID: D012
Document Type: fixed_asset_rollforward
Period: FY 2024-25

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Vehicles
Asset Tag: OPEN-VEH
Cost: GBP 79,271.45
Useful Life: 48
Current Charge: GBP 19,817.88
Accumulated Depreciation: 19,817.88
Opening Balance: GBP 79,271.45
Additions: 0.00
Disposals: 0.00
Ending Balance: GBP 79,271.45

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D014 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 31/03/2025

Reference Box
-------------
Document ID: D014
Document Type: service_period_memo
Period: FY 2024-25
Reference: FY 2024-25

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: FY 2024-25
Recognized Amount: GBP 18,330.70

Explanation
-----------
Narrative: Accrue unpaid repairs expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D028 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
VENDOR STATEMENT
================

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Document Date: 31/03/2025

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D028
Document Type: vendor_statement
Period: FY 2024-25

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Golden State Finance
Closing Balance: GBP 10,635.04

Statement Lines
---------------
Lines:
  - Reference BILL-0003 | Document Type Open invoice | Amount GBP 10,635.04 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D028
```

### Document D031 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Cedar Retail Group
220 Lake View Road, Bengaluru
Date: 31/03/2025

Reference Box
-------------
Document ID: D031
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0029
Statement Currency: GBP
Opening Balance: GBP 161,182.64
Closing Balance: GBP 151,591.55

Statement Rows
--------------
Rows:
  - Date 27/07/2024 | Description Beacon Industrial Supply receipt RCPT-0002 | Amount GBP 
-1,386.76 | Running Balance GBP 159,795.88
  - Date 31/07/2024 | Description Beacon Industrial Supply receipt RCPT-0003 | Amount GBP 
-1,043.34 | Running Balance GBP 158,752.54
  - Date 12/09/2024 | Description Pace Office Mart receipt RCPT-0004 | Amount GBP -1,148.24 
| Running Balance GBP 157,604.30
  - Date 18/09/2024 | Description Asset purchase ASSET-0001 | Amount GBP -137,017.25 | 
Running Balance GBP 20,587.05
  - Date 16/10/2024 | Description Prime Utility Desk receipt RCPT-0001 | Amount GBP -82.43 |
 Running Balance GBP 20,504.62
  - Date 22/11/2024 | Description Loan draw LOAN-0001 | Amount GBP 298,974.01 | Running 
Balance GBP 319,478.63
  - Date 07/12/2024 | Description Customer settlement INV-0001 | Amount GBP 29,899.63 | 
Running Balance GBP 349,378.26
  - Date 01/01/2025 | Description Supplier settlement BILL-0001 | Amount GBP -63,686.14 | 
Running Balance GBP 285,692.12
  - Date 21/01/2025 | Description Loan payment LOAN-0002 | Amount GBP -66,877.67 | Running 
Balance GBP 218,814.45
  - Date 06/02/2025 | Description Payroll PAYRUN-0001 | Amount GBP -67,222.90 | Running 
Balance GBP 151,591.55

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
| 1 | Accounts Receivable | Service Revenue | 38,043.49 | D002, D003 | 2024-04-27 | job_invoice |
| 2 | Accounts Receivable | CGST Payable | 3,423.91 | D002, D003 | 2024-04-27 | job_invoice_tax_cgst |
| 3 | Accounts Receivable | SGST Payable | 3,423.92 | D002, D003 | 2024-04-27 | job_invoice_tax_sgst |
| 4 | Repairs Expense | Accounts Payable | 58,002.56 | D004 | 2024-06-03 | supplier_bill |
| 5 | Input CGST Receivable | Accounts Payable | 5,220.23 | D004 | 2024-06-03 | supplier_bill_tax_cgst |
| 6 | Input SGST Receivable | Accounts Payable | 5,220.23 | D004 | 2024-06-03 | supplier_bill_tax_sgst |
| 7 | Fuel Expense | Cash | 82.43 | D005 | 2024-10-16 | fuel_receipt |
| 8 | Cash | Accounts Receivable | 29,899.63 | D006, D003 | 2024-12-07 | customer_payment |
| 9 | Accounts Payable | Cash | 63,686.14 | D007, D004 | 2025-01-01 | supplier_payment |
| 10 | Salaries Expense | Cash | 59,466.32 | D008 | 2025-02-06 | payroll_gross |
| 11 | Payroll Tax Expense | Cash | 7,756.58 | D008 | 2025-02-06 | payroll_tax |
| 12 | Utilities Expense | Accounts Payable | 11,021.36 | D009 | 2025-01-04 | utilities_bill |
| 13 | Cash | Loans Payable | 298,974.01 | D010 | 2024-11-22 | loan_draw |
| 14 | Equipment | Cash | 137,017.25 | D011 | 2024-09-18 | equipment_purchase_cash |
| 15 | Equipment | Notes Payable | 275,479.42 | D011 | 2024-09-18 | equipment_purchase_financed |
| 16 | Depreciation Expense | Accumulated Depreciation | 19,817.88 | D012 | 2025-03-31 | depreciation |
| 17 | Loans Payable | Cash | 60,275.17 | D013 | 2025-01-21 | loan_repayment_principal |
| 18 | Interest Expense | Cash | 6,602.50 | D013 | 2025-01-21 | loan_repayment_interest |
| 19 | Repairs Expense | Accrued Expenses | 18,330.70 | D014 | 2025-03-31 | expense_accrual |
| 20 | Fuel Expense | Cash | 1,386.76 | D015 | 2024-07-27 | fuel_receipt |
| 21 | Accounts Receivable | Service Revenue | 21,132.83 | D016, D017 | 2024-05-26 | job_invoice |
| 22 | Accounts Receivable | CGST Payable | 1,901.95 | D016, D017 | 2024-05-26 | job_invoice_tax_cgst |
| 23 | Accounts Receivable | SGST Payable | 1,901.96 | D016, D017 | 2024-05-26 | job_invoice_tax_sgst |
| 24 | Utilities Expense | Accounts Payable | 9,006.82 | D018 | 2024-12-23 | utilities_bill |
| 25 | Repairs Expense | Accounts Payable | 7,468.72 | D019 | 2024-07-03 | supplier_bill |
| 26 | Input CGST Receivable | Accounts Payable | 672.18 | D019 | 2024-07-03 | supplier_bill_tax_cgst |
| 27 | Input SGST Receivable | Accounts Payable | 672.19 | D019 | 2024-07-03 | supplier_bill_tax_sgst |
| 28 | Utilities Expense | Accounts Payable | 9,917.26 | D020 | 2025-02-12 | utilities_bill |
| 29 | Fuel Expense | Cash | 1,043.34 | D021 | 2024-07-31 | fuel_receipt |
| 30 | Utilities Expense | Accounts Payable | 3,099.38 | D022 | 2025-01-19 | utilities_bill |
| 31 | Utilities Expense | Accounts Payable | 11,193.73 | D023 | 2024-12-13 | utilities_bill |
| 32 | Accounts Receivable | Service Revenue | 84,890.29 | D024, D025 | 2024-07-01 | job_invoice |
| 33 | Accounts Receivable | CGST Payable | 7,640.12 | D024, D025 | 2024-07-01 | job_invoice_tax_cgst |
| 34 | Accounts Receivable | SGST Payable | 7,640.13 | D024, D025 | 2024-07-01 | job_invoice_tax_sgst |
| 35 | Repairs Expense | Accounts Payable | 9,012.75 | D026 | 2024-04-26 | supplier_bill |
| 36 | Input CGST Receivable | Accounts Payable | 811.14 | D026 | 2024-04-26 | supplier_bill_tax_cgst |
| 37 | Input SGST Receivable | Accounts Payable | 811.15 | D026 | 2024-04-26 | supplier_bill_tax_sgst |
| 38 | Fuel Expense | Cash | 1,148.24 | D027 | 2024-09-12 | fuel_receipt |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 151,591.55
- Accounts Receivable: 158,930.73
- Office Supplies: 7,663.23
- Vehicles: 79,271.45
- Equipment: 449,318.94
- Prepaid Insurance: 7,984.56
- Input CGST Receivable: 6,703.55
- Input SGST Receivable: 6,703.57
- Accumulated Depreciation: -19,817.88

**Liabilities**
- Accounts Payable: 90,867.68
- Accrued Expenses: 23,189.93
- Notes Payable: 306,192.35
- Loans Payable: 286,173.87
- CGST Payable: 12,965.98
- SGST Payable: 12,966.01

**Equity**
- Retained Earnings: -62,585.16
- Owner's Equity: 178,579.04

**Totals:** Assets = 848,349.70; Liabilities = 732,355.82; Equity = 115,993.88
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
- Notes: Reviewed, no material concerns.
