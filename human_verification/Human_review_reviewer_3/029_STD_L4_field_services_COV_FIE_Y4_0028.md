# Verification Packet — COV_FIE_Y4_0028

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 4
- **Period type:** year
- **Period label:** FY 2025
- **Period start → end:** 2025-01-01 → 2025-12-31
- **Entity:** Willow Manufacturing
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 27
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 121,254.82
- Accounts Receivable: 29,570.48
- Office Supplies: 6,323.23
- Vehicles: 39,478.04
- Equipment: 36,099.76
- Prepaid Insurance: 6,988.32

**Liabilities**
- Accounts Payable: 22,294.36
- Accrued Expenses: 7,017.72
- Notes Payable: 16,497.41
- Loans Payable: 33,412.46

**Equity**
- Retained Earnings: 34,478.98
- Owner's Equity: 126,013.72


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
  - Section assets | Account Cash | Amount EUR 121.254,82
  - Section assets | Account Accounts Receivable | Amount EUR 29.570,48
  - Section assets | Account Office Supplies | Amount EUR 6.323,23
  - Section assets | Account Vehicles | Amount EUR 39.478,04
  - Section assets | Account Equipment | Amount EUR 36.099,76
  - Section assets | Account Prepaid Insurance | Amount EUR 6.988,32
  - Section liabilities | Account Accounts Payable | Amount EUR 22.294,36
  - Section liabilities | Account Accrued Expenses | Amount EUR 7.017,72
  - Section liabilities | Account Notes Payable | Amount EUR 16.497,41
  - Section liabilities | Account Loans Payable | Amount EUR 33.412,46
  - Section equity | Account Retained Earnings | Amount EUR 34.478,98
  - Section equity | Account Owner's Equity | Amount EUR 126.013,72

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D016 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2025-01-22

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0002
Customer: Blue Finch Holdings
Job Site: Riverbank Plaza
Scope: Review pack
Approved Amount: EUR 42.327,59

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D017 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-23

```
CUSTOMER INVOICE
================

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Date: 23/01/2025

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D017
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0002
Job Code: JOB-0002

Terms
-----
Due Date: 14/02/2025

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0002
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 14/02/2025
Subtotal: EUR 42.327,59
Tax Label: US Sales Tax
Tax Rate: 6.25%
Tax Amount: EUR 2.645,47
Total: EUR 44.973,06

Line Items
----------
Items:
  - Description Implementation work | Amount EUR 13.448,62
  - Description Follow-up support | Amount EUR 28.878,97

Field Job
---------
Job Code: JOB-0002

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D014 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-28

```
SUPPLIER INVOICE
================

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Document Date: 28/01/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D014
Document Type: supplier_invoice
Period: FY 2025

Terms
-----
Due Date: 17/02/2025

Supplier Header
---------------
Supplier: Oakline Services
Expense Category: Repairs Expense
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 17/02/2025
Subtotal: EUR 22.939,21
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 1.892,48
Total: EUR 24.831,69

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 6 | Unit Cost EUR 1.256,57 | 
Amount EUR 7.539,42
  - Description Preventive maintenance service parts | Quantity 18 | Unit Cost EUR 855,54 | 
Amount EUR 15.399,79

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D024 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-01-28

```
SECONDARY COPY
==============

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Document Date: 28/01/2025

To
--
Oakline Services

Reference Box
-------------
Document ID: D024
Document Type: secondary_copy
Period: FY 2025

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0002
Counterparty: Oakline Services
Total: EUR 24.831,69
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D024
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2025-02-16

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Aster Point Services
Job Site: North Yard
Scope: Support package
Approved Amount: EUR 65.377,75

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-17

```
CUSTOMER INVOICE
================

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Date: 17/02/2025

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 05/03/2025

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 05/03/2025
Subtotal: EUR 65.377,75
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 5.393,66
Total: EUR 70.771,41

Line Items
----------
Items:
  - Description Monthly retainer | Amount EUR 25.701,97
  - Description Follow-up support | Amount EUR 39.675,78

Field Job
---------
Job Code: JOB-0001

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D020 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2025-03-16

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0003
Customer: Blue Finch Holdings
Job Site: Marina Site
Scope: Review pack
Approved Amount: EUR 48.157,39

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D021 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-17

```
CUSTOMER INVOICE
================

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Date: 17/03/2025

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D021
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0003
Job Code: JOB-0003

Terms
-----
Due Date: 05/04/2025

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0003
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 05/04/2025
Subtotal: EUR 48.157,39
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 3.972,98
Total: EUR 52.130,37

Line Items
----------
Items:
  - Description Review pack | Amount EUR 13.932,49
  - Description Follow-up support | Amount EUR 34.224,90

Field Job
---------
Job Code: JOB-0003

Footer
------
Internal document packet copy.
Page marker: D021
```

### Document D025 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-03-17

```
CANCELLATION NOTE
=================

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Date: 17/03/2025

Reference Box
-------------
Document ID: D025
Document Type: cancellation_note
Period: FY 2025

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
Page marker: D025
```

### Document D018 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-06

```
SUPPLIER INVOICE
================

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Date: 06/04/2025

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D018
Document Type: supplier_invoice
Period: FY 2025

Terms
-----
Due Date: 25/04/2025

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Expense Category: Repairs Expense
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0003
Due Date: 25/04/2025
Subtotal: EUR 35.643,32
Tax Label: US Sales Tax
Tax Rate: 6.25%
Tax Amount: EUR 2.227,71
Total: EUR 37.871,03

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 10 | Unit Cost EUR 1.057,21 | 
Amount EUR 10.572,11
  - Description Preventive maintenance service parts | Quantity 25 | Unit Cost EUR 1.002,85 
| Amount EUR 25.071,21

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D004 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-08

```
SUPPLIER INVOICE
================

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Document Date: 08/04/2025

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: FY 2025

Terms
-----
Due Date: 26/04/2025

Supplier Header
---------------
Supplier: Prime Utility Desk
Expense Category: Repairs Expense
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 26/04/2025
Subtotal: EUR 48.136,79
Tax Label: US Sales Tax
Tax Rate: 6.25%
Tax Amount: EUR 3.008,55
Total: EUR 51.145,34

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 6 | Unit Cost EUR 1.998,99 | 
Amount EUR 11.993,92
  - Description Preventive maintenance service parts | Quantity 20 | Unit Cost EUR 1.807,14 
| Amount EUR 36.142,87

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D011 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-10

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Oakline Services
Asset Name: Server rack
Asset Tag: TAG-0001
Useful Life Months: 24
Total: EUR 332.222,69
Paid Cash: EUR 149.429,06
Financed Amount: EUR 182.793,63
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D010 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-06-21

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: EUR 56.455,06
Draw Amount: EUR 150.922,02
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 207.377,08
Note: Scheduled lender activity for the selected period.
```

### Document D015 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-07-24

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Vertex Supply Co.
Total: EUR 2.154,24
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount EUR 456,73
  - Description Fuel Incidentals | Amount EUR 1.697,51
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-08-05

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Vertex Supply Co.
Total: EUR 84,54
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount EUR 33,25
  - Description Fuel Incidentals | Amount EUR 51,29
```

### Document D019 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-09-03

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0003
Merchant: Oakline Services
Total: EUR 464,37
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount EUR 147,60
  - Description Fuel Incidentals | Amount EUR 316,77
```

### Document D009 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-09-19

```
UTILITY INVOICE
===============

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Document Date: 19/09/2025

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: utilities_statement
Period: FY 2025

Terms
-----
Due Date: 26/09/2025

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: FY 2025
Due Date: 26/09/2025
Total: EUR 9.502,35

Charges
-------
Charges:
  - Description Electricity | Amount EUR 2.046,24
  - Description Water | Amount EUR 7.456,11

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-09-28

```
PAYROLL SUMMARY
===============

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Document Date: 28/09/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2025
Headcount: 12
Gross Pay: EUR 52.488,07
Employer Tax: 4.487,11
Cash Outflow: EUR 56.975,18

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-10-09

```
PAYMENT ADVICE
==============

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Date: 09/10/2025

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: EUR 44.865,98
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-11-09

```
PAYMENT ADVICE
==============

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Document Date: 09/11/2025

To
--
Aster Point Services

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Aster Point Services
Amount: EUR 58.300,45
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D012 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Date: 31/12/2025

Reference Box
-------------
Document ID: D012
Document Type: fixed_asset_rollforward
Period: FY 2025

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Vehicles
Asset Tag: OPEN-VEH
Cost: EUR 39.478,04
Useful Life: 48
Current Charge: EUR 9.869,52
Accumulated Depreciation: 9.869,52
Opening Balance: EUR 39.478,04
Additions: 0,00
Disposals: 0,00
Ending Balance: EUR 39.478,04

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D013 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Date: 31/12/2025

Reference Box
-------------
Document ID: D013
Document Type: service_period_memo
Period: FY 2025
Reference: FY 2025

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: FY 2025
Recognized Amount: EUR 6.372,61

Explanation
-----------
Narrative: Accrue unpaid repairs expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D022 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Date: 31/12/2025

Reference Box
-------------
Document ID: D022
Document Type: memo
Period: FY 2025

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
Narrative: The packet may include supporting correspondence gathered during the close 
review.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D022
```

### Document D023 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Date: 31/12/2025

Reference Box
-------------
Document ID: D023
Document Type: memo
Period: FY 2025

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0002
Subject: Quarter-end packet routing note
Audience: All Staff

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
Page marker: D023
```

### Document D026 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
VENDOR STATEMENT
================

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Date: 31/12/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D026
Document Type: vendor_statement
Period: FY 2025

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Oakline Services
Closing Balance: EUR 24.831,69

Statement Lines
---------------
Lines:
  - Reference BILL-0002 | Document Type Open invoice | Amount EUR 24.831,69 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D026
```

### Document D027 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Willow Manufacturing
220 Lake View Road, Bengaluru
Date: 31/12/2025

Reference Box
-------------
Document ID: D027
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0028
Statement Currency: EUR
Opening Balance: EUR 121.254,82
Closing Balance: EUR 76.503,92

Statement Rows
--------------
Rows:
  - Date 10/05/2025 | Description Asset purchase ASSET-0001 | Amount EUR -149.429,06 | 
Running Balance EUR -28.174,24
  - Date 21/06/2025 | Description Loan draw LOAN-0001 | Amount EUR 150.922,02 | Running 
Balance EUR 122.747,78
  - Date 24/07/2025 | Description Vertex Supply Co. receipt RCPT-0002 | Amount EUR -2.154,24
 | Running Balance EUR 120.593,54
  - Date 05/08/2025 | Description Vertex Supply Co. receipt RCPT-0001 | Amount EUR -84,54 | 
Running Balance EUR 120.509,00
  - Date 03/09/2025 | Description Oakline Services receipt RCPT-0003 | Amount EUR -464,37 | 
Running Balance EUR 120.044,63
  - Date 28/09/2025 | Description Payroll PAYRUN-0001 | Amount EUR -56.975,18 | Running 
Balance EUR 63.069,45
  - Date 09/10/2025 | Description Supplier settlement BILL-0001 | Amount EUR -44.865,98 | 
Running Balance EUR 18.203,47
  - Date 09/11/2025 | Description Customer settlement INV-0001 | Amount EUR 58.300,45 | 
Running Balance EUR 76.503,92

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D027
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 65,377.75 | D002, D003 | 2025-02-17 | job_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 5,393.66 | D002, D003 | 2025-02-17 | job_invoice_tax |
| 3 | Repairs Expense | Accounts Payable | 48,136.79 | D004 | 2025-04-08 | supplier_bill |
| 4 | Input Tax Receivable | Accounts Payable | 3,008.55 | D004 | 2025-04-08 | supplier_bill_tax |
| 5 | Fuel Expense | Cash | 84.54 | D005 | 2025-08-05 | fuel_receipt |
| 6 | Cash | Accounts Receivable | 58,300.45 | D006, D003 | 2025-11-09 | customer_payment |
| 7 | Accounts Payable | Cash | 44,865.98 | D007, D004 | 2025-10-09 | supplier_payment |
| 8 | Salaries Expense | Cash | 52,488.07 | D008 | 2025-09-28 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 4,487.11 | D008 | 2025-09-28 | payroll_tax |
| 10 | Utilities Expense | Accounts Payable | 9,502.35 | D009 | 2025-09-19 | utilities_bill |
| 11 | Cash | Loans Payable | 150,922.02 | D010 | 2025-06-21 | loan_draw |
| 12 | Equipment | Cash | 149,429.06 | D011 | 2025-05-10 | equipment_purchase_cash |
| 13 | Equipment | Notes Payable | 182,793.63 | D011 | 2025-05-10 | equipment_purchase_financed |
| 14 | Depreciation Expense | Accumulated Depreciation | 9,869.52 | D012 | 2025-12-31 | depreciation |
| 15 | Repairs Expense | Accrued Expenses | 6,372.61 | D013 | 2025-12-31 | expense_accrual |
| 16 | Repairs Expense | Accounts Payable | 22,939.21 | D014 | 2025-01-28 | supplier_bill |
| 17 | Input Tax Receivable | Accounts Payable | 1,892.48 | D014 | 2025-01-28 | supplier_bill_tax |
| 18 | Fuel Expense | Cash | 2,154.24 | D015 | 2025-07-24 | fuel_receipt |
| 19 | Accounts Receivable | Service Revenue | 42,327.59 | D016, D017 | 2025-01-23 | job_invoice |
| 20 | Accounts Receivable | Sales Tax Payable | 2,645.47 | D016, D017 | 2025-01-23 | job_invoice_tax |
| 21 | Repairs Expense | Accounts Payable | 35,643.32 | D018 | 2025-04-06 | supplier_bill |
| 22 | Input Tax Receivable | Accounts Payable | 2,227.71 | D018 | 2025-04-06 | supplier_bill_tax |
| 23 | Fuel Expense | Cash | 464.37 | D019 | 2025-09-03 | fuel_receipt |
| 24 | Accounts Receivable | Service Revenue | 48,157.39 | D020, D021 | 2025-03-17 | job_invoice |
| 25 | Accounts Receivable | Sales Tax Payable | 3,972.98 | D020, D021 | 2025-03-17 | job_invoice_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 76,503.92
- Accounts Receivable: 139,144.87
- Office Supplies: 6,323.23
- Vehicles: 39,478.04
- Equipment: 368,322.45
- Prepaid Insurance: 6,988.32
- Input Tax Receivable: 7,128.74
- Accumulated Depreciation: -9,869.52

**Liabilities**
- Accounts Payable: 100,778.79
- Accrued Expenses: 13,390.33
- Notes Payable: 199,291.04
- Loans Payable: 184,334.48
- Sales Tax Payable: 12,012.11

**Equity**
- Retained Earnings: -1,800.42
- Owner's Equity: 126,013.72

**Totals:** Assets = 634,020.05; Liabilities = 509,806.75; Equity = 124,213.30
**Balanced (A = L + E):** True

---

## 7. Verification Form

_Fill in your judgement below. For each question, mark one box and add notes where applicable._

### Q1 — Document analogy to real paperwork
We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?
- [ ] Yes — analogous to what an accountant would receive
- [x] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes: Tax label wording doesn't quite match the region. Otherwise reads right.

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
- Notes:
