# Verification Packet — COV_PRO_Y5_0089

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 5
- **Period type:** year
- **Period label:** FY 2025-26
- **Period start → end:** 2025-04-01 → 2026-03-31
- **Entity:** Pioneer Builders
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 34
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 189,695.56
- Accounts Receivable: 23,448.08
- Prepaid Insurance: 6,513.18
- Equipment: 41,443.31

**Liabilities**
- Accounts Payable: 19,682.28
- Accrued Expenses: 7,104.99
- Security Deposits Payable: 14,743.08
- Loans Payable: 13,763.15

**Equity**
- Retained Earnings: 39,518.29
- Owner's Equity: 166,288.34


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
  - Section assets | Account Cash | Amount GBP 189,695.56
  - Section assets | Account Accounts Receivable | Amount GBP 23,448.08
  - Section assets | Account Prepaid Insurance | Amount GBP 6,513.18
  - Section assets | Account Equipment | Amount GBP 41,443.31
  - Section liabilities | Account Accounts Payable | Amount GBP 19,682.28
  - Section liabilities | Account Accrued Expenses | Amount GBP 7,104.99
  - Section liabilities | Account Security Deposits Payable | Amount GBP 14,743.08
  - Section liabilities | Account Loans Payable | Amount GBP 13,763.15
  - Section equity | Account Retained Earnings | Amount GBP 39,518.29
  - Section equity | Account Owner's Equity | Amount GBP 166,288.34

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-04-03

```
RENT ROLL
=========

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 03/04/2025

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: FY 2025-26

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Park Lane Residences
Period: FY 2025-26
Total Rent: GBP 25,314.39

Tenant Rows
-----------
Rows:
  - Unit A-101 | Tenant Unit B - Romero | Amount GBP 25,314.39

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D009 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2025-04-03

```
INSURANCE NOTICE
================

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 03/04/2025

To
--
Beacon General
Vendor remittance address on file

Terms
-----
Service Start: 03/04/2025
Service End: 02/07/2025

Coverage Notice
---------------
Notice Number: PRE-0001
Carrier: Beacon General
Covered Item: Harbor View Offices
Coverage Start: 03/04/2025
Coverage End: 02/07/2025
Total Premium: GBP 60,694.62
Monthly Amount: GBP 20,231.54

Notes
-----
Insurance coverage paid in advance and tracked for later release.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D016 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-04-17

```
RENT ROLL
=========

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 17/04/2025

Reference Box
-------------
Document ID: D016
Document Type: rent_roll
Period: FY 2025-26

Rent Roll Summary
-----------------
Roll Number: ROLL-0002
Property: Park Lane Residences
Period: FY 2025-26
Total Rent: GBP 35,081.05

Tenant Rows
-----------
Rows:
  - Unit A-101 | Tenant Unit A - Ellis | Amount GBP 35,081.05

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D021 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-04-19

```
RENT ROLL
=========

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 19/04/2025

Reference Box
-------------
Document ID: D021
Document Type: rent_roll
Period: FY 2025-26

Rent Roll Summary
-----------------
Roll Number: ROLL-0003
Property: Cedar Plaza
Period: FY 2025-26
Total Rent: GBP 45,449.51

Tenant Rows
-----------
Rows:
  - Unit C-303 | Tenant Unit B - Romero | Amount GBP 45,449.51

Footer
------
Internal document packet copy.
Page marker: D021
```

### Document D022 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-04-23

```
RENT ROLL
=========

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 23/04/2025

Reference Box
-------------
Document ID: D022
Document Type: rent_roll
Period: FY 2025-26

Rent Roll Summary
-----------------
Roll Number: ROLL-0004
Property: Marina Heights
Period: FY 2025-26
Total Rent: GBP 41,444.01

Tenant Rows
-----------
Rows:
  - Unit D-404 | Tenant Unit B - Romero | Amount GBP 41,444.01

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-04

```
VENDOR INVOICE
==============

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 04/05/2025

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2025-26

Terms
-----
Due Date: 16/05/2025

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Maintenance Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 16/05/2025
Total: GBP 35,911.64

Bill Lines
----------
Lines:
  - Description Support package | Amount GBP 10,583.97
  - Description Support fee | Amount GBP 25,327.67

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D027 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-05-08

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 08/05/2025

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D027
Document Type: security_deposit_notice
Period: FY 2025-26

Security Deposit
----------------
Notice Number: DEP-0007
Tenant: Unit D - Khan
Unit: D-404
Amount: GBP 31,354.21
Due Date: 13/05/2025

Footer
------
Generated for synthetic accounting research use.
Page marker: D027
```

### Document D018 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-05-14

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 14/05/2025

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D018
Document Type: security_deposit_notice
Period: FY 2025-26

Security Deposit
----------------
Notice Number: DEP-0003
Tenant: Unit D - Khan
Unit: A-101
Amount: GBP 20,209.42
Due Date: 21/05/2025

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D006 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-05-25

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 25/05/2025

To
--
Unit A - Ellis

Reference Box
-------------
Document ID: D006
Document Type: security_deposit_notice
Period: FY 2025-26

Security Deposit
----------------
Notice Number: DEP-0001
Tenant: Unit A - Ellis
Unit: B-202
Amount: GBP 10,401.98
Due Date: 02/06/2025

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D017 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-14

```
VENDOR INVOICE
==============

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 14/06/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D017
Document Type: vendor_invoice
Period: FY 2025-26

Terms
-----
Due Date: 03/07/2025

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Maintenance Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 03/07/2025
Total: GBP 18,082.60

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 5,319.08
  - Description Support fee | Amount GBP 12,763.52

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D023 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-06-18

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 18/06/2025

To
--
Unit B - Romero

Reference Box
-------------
Document ID: D023
Document Type: security_deposit_notice
Period: FY 2025-26

Security Deposit
----------------
Notice Number: DEP-0006
Tenant: Unit B - Romero
Unit: C-303
Amount: GBP 26,967.63
Due Date: 22/06/2025

Footer
------
Generated for synthetic accounting research use.
Page marker: D023
```

### Document D019 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-06-19

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 19/06/2025

To
--
Unit C - Shah

Reference Box
-------------
Document ID: D019
Document Type: security_deposit_notice
Period: FY 2025-26

Security Deposit
----------------
Notice Number: DEP-0004
Tenant: Unit C - Shah
Unit: B-202
Amount: GBP 26,342.90
Due Date: 27/06/2025

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D025 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-26

```
VENDOR INVOICE
==============

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 26/06/2025

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D025
Document Type: vendor_invoice
Period: FY 2025-26

Terms
-----
Due Date: 10/07/2025

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Maintenance Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0004
Due Date: 10/07/2025
Total: GBP 39,809.78

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 14,881.92
  - Description Support fee | Amount GBP 24,927.86

Footer
------
Generated for synthetic accounting research use.
Page marker: D025
```

### Document D028 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-06-26

```
SECONDARY COPY
==============

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 26/06/2025

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D028
Document Type: secondary_copy
Period: FY 2025-26

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0004
Counterparty: Meridian Support LLP
Total: GBP 39,809.78
Copy Context: Forwarded copy attached to the customer correspondence bundle.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D028
```

### Document D030 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-06-26

```
SECONDARY COPY
==============

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 26/06/2025

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D030
Document Type: secondary_copy
Period: FY 2025-26

Copy Summary
------------
Copy ID: COPY-0002
Source Reference: BILL-0004
Counterparty: Meridian Support LLP
Total: GBP 39,809.78
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D030
```

### Document D020 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-07-03

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 03/07/2025

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D020
Document Type: security_deposit_notice
Period: FY 2025-26

Security Deposit
----------------
Notice Number: DEP-0005
Tenant: Unit D - Khan
Unit: A-101
Amount: GBP 23,556.21
Due Date: 08/07/2025

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D024 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-03

```
VENDOR INVOICE
==============

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 03/07/2025

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D024
Document Type: vendor_invoice
Period: FY 2025-26

Terms
-----
Due Date: 13/07/2025

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Maintenance Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0003
Due Date: 13/07/2025
Total: GBP 27,288.69

Bill Lines
----------
Lines:
  - Description Implementation work | Amount GBP 11,831.68
  - Description Support fee | Amount GBP 15,457.01

Footer
------
Generated for synthetic accounting research use.
Page marker: D024
```

### Document D031 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-07-03

```
SECONDARY COPY
==============

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 03/07/2025

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D031
Document Type: secondary_copy
Period: FY 2025-26

Copy Summary
------------
Copy ID: COPY-0003
Source Reference: BILL-0003
Counterparty: Vertex Supply Co.
Total: GBP 27,288.69
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D031
```

### Document D032 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-07-03

```
SECONDARY COPY
==============

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 03/07/2025

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D032
Document Type: secondary_copy
Period: FY 2025-26

Copy Summary
------------
Copy ID: COPY-0004
Source Reference: BILL-0003
Counterparty: Vertex Supply Co.
Total: GBP 27,288.69
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D032
```

### Document D026 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-04

```
VENDOR INVOICE
==============

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 04/07/2025

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D026
Document Type: vendor_invoice
Period: FY 2025-26

Terms
-----
Due Date: 24/07/2025

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Maintenance Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0005
Due Date: 24/07/2025
Total: GBP 46,363.74

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 16,792.61
  - Description Support fee | Amount GBP 29,571.13

Footer
------
Internal document packet copy.
Page marker: D026
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-27

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Meridian Support LLP
Asset Name: Office laptops
Asset Tag: TAG-0001
Useful Life Months: 24
Total: GBP 311,032.86
Paid Cash: GBP 86,393.22
Financed Amount: GBP 224,639.64
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-01

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: GBP 11,466.04
Draw Amount: GBP 446,798.82
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 458,264.86
Note: Scheduled lender activity for the selected period.
```

### Document D014 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-08

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: First City Bank
Opening Principal: GBP 78,720.45
Draw Amount: GBP 0.00
Principal Paid: GBP 52,129.57
Interest Paid: GBP 3,772.40
Ending Principal: GBP 26,590.88
Note: Scheduled lender activity for the selected period.
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-25

```
PAYMENT ADVICE
==============

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 25/12/2025

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2025-26
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Beacon Industrial Supply
Amount: GBP 35,191.14
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D008 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-28

```
UTILITY INVOICE
===============

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 28/12/2025

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: utilities_statement
Period: FY 2025-26

Terms
-----
Due Date: 12/01/2026

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: FY 2025-26
Due Date: 12/01/2026
Total: GBP 8,728.01

Charges
-------
Charges:
  - Description Electricity | Amount GBP 3,528.16
  - Description Water | Amount GBP 5,199.85

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D004 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-01-16

```
PAYMENT ADVICE
==============

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 16/01/2026

To
--
Unit B - Romero

Reference Box
-------------
Document ID: D004
Document Type: payment_advice
Period: FY 2025-26
Reference: ROLL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Unit B - Romero
Amount: GBP 24,984.34
Reference: ROLL-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D015 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `adjustment_doc`
- **Date:** 2026-01-26

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 26/01/2026

To
--
Unit A - Ellis

Reference Box
-------------
Document ID: D015
Document Type: security_deposit_notice
Period: FY 2025-26

Security Deposit
----------------
Notice Number: DEPREF-0001
Tenant: Unit A - Ellis
Unit: B-202
Amount: GBP 8,100.19
Due Date: 26/01/2026

Notes
-----
Refund of previously collected security deposit DEP-0001.

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2026-02-10

```
PAYROLL SUMMARY
===============

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 10/02/2026

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2025-26
Headcount: 12
Gross Pay: GBP 99,551.04
Employer Tax: 8,426.54
Cash Outflow: GBP 107,977.58

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D010 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 31/03/2026

Reference Box
-------------
Document ID: D010
Document Type: service_period_memo
Period: FY 2025-26
Reference: PRE-0001

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Insurance coverage release
Reference: PRE-0001
Recognized Amount: GBP 20,231.54

Explanation
-----------
Narrative: One month of insurance coverage has expired and should be expensed this period.

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D013 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 31/03/2026

Reference Box
-------------
Document ID: D013
Document Type: fixed_asset_rollforward
Period: FY 2025-26

Asset Rollforward
-----------------
Schedule ID: DEP-0002
Asset Name: Office laptops
Asset Tag: TAG-0001
Cost: GBP 311,032.86
Useful Life: 24
Current Charge: GBP 155,516.40
Accumulated Depreciation: 155,516.40
Opening Balance: GBP 311,032.86
Additions: 0.00
Disposals: 0.00
Ending Balance: GBP 311,032.86

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D029 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
VENDOR STATEMENT
================

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 31/03/2026

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D029
Document Type: vendor_statement
Period: FY 2025-26

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Metro Water
Closing Balance: GBP 8,728.01

Statement Lines
---------------
Lines:
  - Reference UTIL-0001 | Document Type Open invoice | Amount GBP 8,728.01 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D029
```

### Document D033 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
MEMO
====

From
----
Pioneer Builders
75 Market Road, Mumbai
Document Date: 31/03/2026

Reference Box
-------------
Document ID: D033
Document Type: memo
Period: FY 2025-26

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Document retention reminder
Audience: All Staff

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
Page marker: D033
```

### Document D034 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Pioneer Builders
75 Market Road, Mumbai
Date: 31/03/2026

Reference Box
-------------
Document ID: D034
Document Type: bank_statement
Period: FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0089
Statement Currency: GBP
Opening Balance: GBP 189,695.56
Closing Balance: GBP 446,052.35

Statement Rows
--------------
Rows:
  - Date 03/04/2025 | Description Insurance coverage prepayment PRE-0001 | Amount GBP 
-60,694.62 | Running Balance GBP 129,000.94
  - Date 08/05/2025 | Description Security deposit DEP-0007 | Amount GBP 31,354.21 | Running
 Balance GBP 160,355.15
  - Date 14/05/2025 | Description Security deposit DEP-0003 | Amount GBP 20,209.42 | Running
 Balance GBP 180,564.57
  - Date 25/05/2025 | Description Security deposit DEP-0001 | Amount GBP 10,401.98 | Running
 Balance GBP 190,966.55
  - Date 18/06/2025 | Description Security deposit DEP-0006 | Amount GBP 26,967.63 | Running
 Balance GBP 217,934.18
  - Date 19/06/2025 | Description Security deposit DEP-0004 | Amount GBP 26,342.90 | Running
 Balance GBP 244,277.08
  - Date 03/07/2025 | Description Security deposit DEP-0005 | Amount GBP 23,556.21 | Running
 Balance GBP 267,833.29
  - Date 27/10/2025 | Description Asset purchase ASSET-0001 | Amount GBP -86,393.22 | 
Running Balance GBP 181,440.07
  - Date 01/11/2025 | Description Loan draw LOAN-0001 | Amount GBP 446,798.82 | Running 
Balance GBP 628,238.89
  - Date 08/12/2025 | Description Loan payment LOAN-0002 | Amount GBP -55,901.97 | Running 
Balance GBP 572,336.92
  - Date 25/12/2025 | Description Supplier settlement BILL-0001 | Amount GBP -35,191.14 | 
Running Balance GBP 537,145.78
  - Date 16/01/2026 | Description Customer settlement ROLL-0001 | Amount GBP 24,984.34 | 
Running Balance GBP 562,130.12
  - Date 26/01/2026 | Description Security deposit refund DEP-0001 | Amount GBP -8,100.19 | 
Running Balance GBP 554,029.93
  - Date 10/02/2026 | Description Payroll PAYRUN-0001 | Amount GBP -107,977.58 | Running 
Balance GBP 446,052.35

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D034
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Rental Revenue | 25,314.39 | D002 | 2025-04-03 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 35,911.64 | D003 | 2025-05-04 | maintenance_bill |
| 3 | Cash | Accounts Receivable | 24,984.34 | D004, D002 | 2026-01-16 | tenant_payment |
| 4 | Accounts Payable | Cash | 35,191.14 | D005, D003 | 2025-12-25 | vendor_payment |
| 5 | Cash | Security Deposits Payable | 10,401.98 | D006 | 2025-05-25 | security_deposit |
| 6 | Salaries Expense | Cash | 99,551.04 | D007 | 2026-02-10 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 8,426.54 | D007 | 2026-02-10 | payroll_tax |
| 8 | Utilities Expense | Accounts Payable | 8,728.01 | D008 | 2025-12-28 | utilities_bill |
| 9 | Prepaid Insurance | Cash | 60,694.62 | D009 | 2025-04-03 | prepaid_insurance_purchase |
| 10 | Insurance Expense | Prepaid Insurance | 20,231.54 | D009, D010 | 2026-03-31 | prepaid_insurance_release |
| 11 | Cash | Loans Payable | 446,798.82 | D011 | 2025-11-01 | loan_draw |
| 12 | Equipment | Cash | 86,393.22 | D012 | 2025-10-27 | equipment_purchase_cash |
| 13 | Equipment | Notes Payable | 224,639.64 | D012 | 2025-10-27 | equipment_purchase_financed |
| 14 | Depreciation Expense | Accumulated Depreciation | 155,516.40 | D013 | 2026-03-31 | depreciation |
| 15 | Loans Payable | Cash | 52,129.57 | D014 | 2025-12-08 | loan_repayment_principal |
| 16 | Interest Expense | Cash | 3,772.40 | D014 | 2025-12-08 | loan_repayment_interest |
| 17 | Security Deposits Payable | Cash | 8,100.19 | D015, D006 | 2026-01-26 | security_deposit_refund |
| 18 | Accounts Receivable | Rental Revenue | 35,081.05 | D016 | 2025-04-17 | rent_roll |
| 19 | Maintenance Expense | Accounts Payable | 18,082.60 | D017 | 2025-06-14 | maintenance_bill |
| 20 | Cash | Security Deposits Payable | 20,209.42 | D018 | 2025-05-14 | security_deposit |
| 21 | Cash | Security Deposits Payable | 26,342.90 | D019 | 2025-06-19 | security_deposit |
| 22 | Cash | Security Deposits Payable | 23,556.21 | D020 | 2025-07-03 | security_deposit |
| 23 | Accounts Receivable | Rental Revenue | 45,449.51 | D021 | 2025-04-19 | rent_roll |
| 24 | Accounts Receivable | Rental Revenue | 41,444.01 | D022 | 2025-04-23 | rent_roll |
| 25 | Cash | Security Deposits Payable | 26,967.63 | D023 | 2025-06-18 | security_deposit |
| 26 | Maintenance Expense | Accounts Payable | 27,288.69 | D024 | 2025-07-03 | maintenance_bill |
| 27 | Maintenance Expense | Accounts Payable | 39,809.78 | D025 | 2025-06-26 | maintenance_bill |
| 28 | Maintenance Expense | Accounts Payable | 46,363.74 | D026 | 2025-07-04 | maintenance_bill |
| 29 | Cash | Security Deposits Payable | 31,354.21 | D027 | 2025-05-08 | security_deposit |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 446,052.35
- Accounts Receivable: 145,752.70
- Prepaid Insurance: 46,976.26
- Equipment: 352,476.17
- Accumulated Depreciation: -155,516.40

**Liabilities**
- Accounts Payable: 160,675.60
- Accrued Expenses: 7,104.99
- Security Deposits Payable: 145,475.24
- Loans Payable: 408,432.40
- Notes Payable: 224,639.64

**Equity**
- Retained Earnings: -276,875.13
- Owner's Equity: 166,288.34

**Totals:** Assets = 835,741.08; Liabilities = 946,327.87; Equity = -110,586.79
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
