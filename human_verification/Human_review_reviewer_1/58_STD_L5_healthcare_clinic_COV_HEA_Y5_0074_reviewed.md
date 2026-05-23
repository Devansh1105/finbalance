# Verification Packet — COV_HEA_Y5_0074

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 5
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Harbor Retail Group
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 32
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 251,776.06
- Accounts Receivable: 40,024.13
- Prepaid Insurance: 15,113.26
- Office Supplies: 3,018.71
- Equipment: 110,741.84

**Liabilities**
- Accounts Payable: 25,167.71
- Accrued Expenses: 4,359.09
- Loans Payable: 39,886.89

**Equity**
- Retained Earnings: 27,199.45
- Owner's Equity: 324,060.86


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
  - Section assets | Account Cash | Amount GBP 251,776.06
  - Section assets | Account Accounts Receivable | Amount GBP 40,024.13
  - Section assets | Account Prepaid Insurance | Amount GBP 15,113.26
  - Section assets | Account Office Supplies | Amount GBP 3,018.71
  - Section assets | Account Equipment | Amount GBP 110,741.84
  - Section liabilities | Account Accounts Payable | Amount GBP 25,167.71
  - Section liabilities | Account Accrued Expenses | Amount GBP 4,359.09
  - Section liabilities | Account Loans Payable | Amount GBP 39,886.89
  - Section equity | Account Retained Earnings | Amount GBP 27,199.45
  - Section equity | Account Owner's Equity | Amount GBP 324,060.86

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D027 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-20

```
VENDOR INVOICE
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 20/04/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D027
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 01/05/2024

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0008
Due Date: 01/05/2024
Total: GBP 47,269.20

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount GBP 18,025.71
  - Description Support fee | Amount GBP 29,243.49

Footer
------
Generated for synthetic accounting research use.
Page marker: D027
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-11

```
VENDOR INVOICE
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 11/05/2024

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 31/05/2024

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 31/05/2024
Total: GBP 41,197.46

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount GBP 15,886.33
  - Description Support fee | Amount GBP 25,311.13

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D031 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-05-11

```
SECONDARY COPY
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 11/05/2024

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D031
Document Type: secondary_copy
Period: FY 2024-25

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0001
Counterparty: Beacon Industrial Supply
Total: GBP 41,197.46
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D031
```

### Document D015 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-16

```
VENDOR INVOICE
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 16/05/2024

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D015
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 27/05/2024

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0003
Due Date: 27/05/2024
Total: GBP 45,528.53

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount GBP 12,356.69
  - Description Support fee | Amount GBP 33,171.84

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D024 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-18

```
VENDOR INVOICE
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 18/05/2024

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D024
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 29/05/2024

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0006
Due Date: 29/05/2024
Total: GBP 22,360.67

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount GBP 9,627.42
  - Description Support fee | Amount GBP 12,733.25

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D020 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-08

```
VENDOR INVOICE
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 08/06/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D020
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 29/06/2024

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0004
Due Date: 29/06/2024
Total: GBP 18,328.79

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 7,514.91
  - Description Support fee | Amount GBP 10,813.88

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D022 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-13

```
VENDOR INVOICE
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 13/06/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D022
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 26/06/2024

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0005
Due Date: 26/06/2024
Total: GBP 26,739.96

Bill Lines
----------
Lines:
  - Description Review pack | Amount GBP 10,698.44
  - Description Support fee | Amount GBP 16,041.52

Footer
------
Internal document packet copy.
Page marker: D022
```

### Document D012 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-14

```
VENDOR INVOICE
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 14/06/2024

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 03/07/2024

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 03/07/2024
Total: GBP 23,162.70

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount GBP 6,584.26
  - Description Support fee | Amount GBP 16,578.44

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D026 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-25

```
VENDOR INVOICE
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 25/06/2024

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D026
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 12/07/2024

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0007
Due Date: 12/07/2024
Total: GBP 52,462.12

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 11,445.59
  - Description Support fee | Amount GBP 41,016.53

Footer
------
Generated for synthetic accounting research use.
Page marker: D026
```

### Document D007 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-08-06

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: GBP 66,466.58
Draw Amount: GBP 122,290.51
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 188,757.09
Note: Scheduled lender activity for the selected period.
```

### Document D016 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-10

```
PATIENT INVOICE
===============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 10/08/2024

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D016
Document Type: patient_invoice
Period: FY 2024-25

Invoice Summary
---------------
Invoice Number: PTINV-0004
Patient: Anaya Patel
Payer: Unity Health Plan
Service Date: 10/08/2024
Gross Charge: GBP 11,063.78
Patient Due: 3,382.60
Insurer Due: 7,681.18

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D013 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-21

```
PATIENT INVOICE
===============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 21/08/2024

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D013
Document Type: patient_invoice
Period: FY 2024-25

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Marcus Lee
Payer: NorthCover
Service Date: 21/08/2024
Gross Charge: GBP 11,032.73
Patient Due: 2,437.85
Insurer Due: 8,594.88

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D021 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-23

```
PATIENT INVOICE
===============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 23/08/2024

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D021
Document Type: patient_invoice
Period: FY 2024-25

Invoice Summary
---------------
Invoice Number: PTINV-0008
Patient: Anaya Patel
Payer: NorthCover
Service Date: 23/08/2024
Gross Charge: GBP 13,551.41
Patient Due: 3,929.80
Insurer Due: 9,621.61

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D023 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-26

```
PATIENT INVOICE
===============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 26/08/2024

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D023
Document Type: patient_invoice
Period: FY 2024-25

Invoice Summary
---------------
Invoice Number: PTINV-0009
Patient: Marcus Lee
Payer: Unity Health Plan
Service Date: 26/08/2024
Gross Charge: GBP 7,634.73
Patient Due: 1,921.69
Insurer Due: 5,713.04

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D019 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-08

```
PATIENT INVOICE
===============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 08/09/2024

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D019
Document Type: patient_invoice
Period: FY 2024-25

Invoice Summary
---------------
Invoice Number: PTINV-0007
Patient: Anaya Patel
Payer: Harbor Health Network
Service Date: 08/09/2024
Gross Charge: GBP 13,793.16
Patient Due: 4,694.32
Insurer Due: 9,098.84

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D017 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-19

```
PATIENT INVOICE
===============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 19/09/2024

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D017
Document Type: patient_invoice
Period: FY 2024-25

Invoice Summary
---------------
Invoice Number: PTINV-0005
Patient: Ella Santos
Payer: NorthCover
Service Date: 19/09/2024
Gross Charge: GBP 7,175.83
Patient Due: 1,558.72
Insurer Due: 5,617.11

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D008 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-30

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Beacon Industrial Supply
Asset Name: CNC router
Asset Tag: TAG-0001
Useful Life Months: 36
Total: GBP 226,562.48
Paid Cash: GBP 46,585.59
Financed Amount: GBP 179,976.89
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D014 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-10-22

```
PATIENT INVOICE
===============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 22/10/2024

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D014
Document Type: patient_invoice
Period: FY 2024-25

Invoice Summary
---------------
Invoice Number: PTINV-0003
Patient: Noah Ferreira
Payer: NorthCover
Service Date: 22/10/2024
Gross Charge: GBP 21,996.81
Patient Due: 5,878.60
Insurer Due: 16,118.21

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D002 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-08

```
PATIENT INVOICE
===============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 08/11/2024

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D002
Document Type: patient_invoice
Period: FY 2024-25

Invoice Summary
---------------
Invoice Number: PTINV-0001
Patient: Ella Santos
Payer: NorthCover
Service Date: 08/11/2024
Gross Charge: GBP 8,541.52
Patient Due: 2,103.98
Insurer Due: 6,437.54

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D018 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-10

```
PATIENT INVOICE
===============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 10/11/2024

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D018
Document Type: patient_invoice
Period: FY 2024-25

Invoice Summary
---------------
Invoice Number: PTINV-0006
Patient: Ella Santos
Payer: Harbor Health Network
Service Date: 10/11/2024
Gross Charge: GBP 14,583.19
Patient Due: 2,209.10
Insurer Due: 12,374.09

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D025 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-20

```
PATIENT INVOICE
===============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 20/11/2024

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D025
Document Type: patient_invoice
Period: FY 2024-25

Invoice Summary
---------------
Invoice Number: PTINV-0010
Patient: Ella Santos
Payer: Unity Health Plan
Service Date: 20/11/2024
Gross Charge: GBP 13,436.14
Patient Due: 4,452.59
Insurer Due: 8,983.55

Footer
------
Internal document packet copy.
Page marker: D025
```

### Document D005 — Insurer Remittance

- **Type:** `insurer_remittance`
- **Role:** `posting_doc`
- **Date:** 2024-12-08

```
INSURER REMITTANCE
==================

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 08/12/2024

Reference Box
-------------
Document ID: D005
Document Type: insurer_remittance
Period: FY 2024-25

Remittance Summary
------------------
Remittance Number: REM-0001
Payer: NorthCover
Claim Reference: PTINV-0001
Approved Amount: GBP 6,437.54
Paid Amount: GBP 6,437.54
Payment Date: 08/12/2024

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D010 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-01-01

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: GBP 283,657.40
Draw Amount: GBP 0.00
Principal Paid: GBP 46,864.50
Interest Paid: GBP 5,857.39
Ending Principal: GBP 236,792.90
Note: Scheduled lender activity for the selected period.
```

### Document D006 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-01-13

```
PAYROLL SUMMARY
===============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 13/01/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024-25
Headcount: 7
Gross Pay: GBP 96,053.76
Employer Tax: 7,996.37
Cash Outflow: GBP 104,050.13

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D004 — Copay Receipt

- **Type:** `copay_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-01-22

```
COPAY RECEIPT
=============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 22/01/2025

To
--
Ella Santos
Patient billing contact

Copay Receipt
-------------
Receipt Number: COPAY-0001
Patient: Ella Santos
Amount: GBP 2,103.98
Reference Invoice: PTINV-0001
Payment Method: Card

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D009 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 31/03/2025

Reference Box
-------------
Document ID: D009
Document Type: fixed_asset_rollforward
Period: FY 2024-25

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: CNC router
Asset Tag: TAG-0001
Cost: GBP 226,562.48
Useful Life: 36
Current Charge: GBP 75,520.80
Accumulated Depreciation: 75,520.80
Opening Balance: GBP 226,562.48
Additions: 0.00
Disposals: 0.00
Ending Balance: GBP 226,562.48

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D011 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D011
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
Recognized Amount: GBP 17,232.53

Explanation
-----------
Narrative: Accrue unpaid office supplies expense incurred before period end.

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D028 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Harbor Retail Group
75 Market Road, Mumbai
Date: 31/03/2025

Reference Box
-------------
Document ID: D028
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Document retention reminder
Audience: Operations Team

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
Page marker: D028
```

### Document D029 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
VENDOR STATEMENT
================

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 31/03/2025

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D029
Document Type: vendor_statement
Period: FY 2024-25

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Meridian Support LLP
Closing Balance: GBP 23,162.70

Statement Lines
---------------
Lines:
  - Reference BILL-0002 | Document Type Open invoice | Amount GBP 23,162.70 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D029
```

### Document D030 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
VENDOR STATEMENT
================

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 31/03/2025

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D030
Document Type: vendor_statement
Period: FY 2024-25

Statement Header
----------------
Statement Number: VSTMT-0002
Vendor: Pace Office Mart
Closing Balance: GBP 26,739.96

Statement Lines
---------------
Lines:
  - Reference BILL-0005 | Document Type Open invoice | Amount GBP 26,739.96 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D030
```

### Document D032 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Harbor Retail Group
75 Market Road, Mumbai
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D032
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0074
Statement Currency: GBP
Opening Balance: GBP 251,776.06
Closing Balance: GBP 179,250.48

Statement Rows
--------------
Rows:
  - Date 06/08/2024 | Description Loan draw LOAN-0001 | Amount GBP 122,290.51 | Running 
Balance GBP 374,066.57
  - Date 30/09/2024 | Description Asset purchase ASSET-0001 | Amount GBP -46,585.59 | 
Running Balance GBP 327,480.98
  - Date 08/12/2024 | Description Insurer remittance PTINV-0001 | Amount GBP 6,437.54 | 
Running Balance GBP 333,918.52
  - Date 01/01/2025 | Description Loan payment LOAN-0002 | Amount GBP -52,721.89 | Running 
Balance GBP 281,196.63
  - Date 13/01/2025 | Description Payroll PAYRUN-0001 | Amount GBP -104,050.13 | Running 
Balance GBP 177,146.50
  - Date 22/01/2025 | Description Copay receipt COPAY-0001 | Amount GBP 2,103.98 | Running 
Balance GBP 179,250.48

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D032
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 8,541.52 | D002 | 2024-11-08 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 41,197.46 | D003 | 2024-05-11 | clinic_supplies_bill |
| 3 | Cash | Accounts Receivable | 2,103.98 | D004, D002 | 2025-01-22 | copay_collection |
| 4 | Cash | Accounts Receivable | 6,437.54 | D005, D002 | 2024-12-08 | insurer_remittance |
| 5 | Salaries Expense | Cash | 96,053.76 | D006 | 2025-01-13 | payroll_gross |
| 6 | Payroll Tax Expense | Cash | 7,996.37 | D006 | 2025-01-13 | payroll_tax |
| 7 | Cash | Loans Payable | 122,290.51 | D007 | 2024-08-06 | loan_draw |
| 8 | Equipment | Cash | 46,585.59 | D008 | 2024-09-30 | equipment_purchase_cash |
| 9 | Equipment | Notes Payable | 179,976.89 | D008 | 2024-09-30 | equipment_purchase_financed |
| 10 | Depreciation Expense | Accumulated Depreciation | 75,520.80 | D009 | 2025-03-31 | depreciation |
| 11 | Loans Payable | Cash | 46,864.50 | D010 | 2025-01-01 | loan_repayment_principal |
| 12 | Interest Expense | Cash | 5,857.39 | D010 | 2025-01-01 | loan_repayment_interest |
| 13 | Office Supplies Expense | Accrued Expenses | 17,232.53 | D011 | 2025-03-31 | expense_accrual |
| 14 | Office Supplies Expense | Accounts Payable | 23,162.70 | D012 | 2024-06-14 | clinic_supplies_bill |
| 15 | Accounts Receivable | Service Revenue | 11,032.73 | D013 | 2024-08-21 | patient_billing |
| 16 | Accounts Receivable | Service Revenue | 21,996.81 | D014 | 2024-10-22 | patient_billing |
| 17 | Office Supplies Expense | Accounts Payable | 45,528.53 | D015 | 2024-05-16 | clinic_supplies_bill |
| 18 | Accounts Receivable | Service Revenue | 11,063.78 | D016 | 2024-08-10 | patient_billing |
| 19 | Accounts Receivable | Service Revenue | 7,175.83 | D017 | 2024-09-19 | patient_billing |
| 20 | Accounts Receivable | Service Revenue | 14,583.19 | D018 | 2024-11-10 | patient_billing |
| 21 | Accounts Receivable | Service Revenue | 13,793.16 | D019 | 2024-09-08 | patient_billing |
| 22 | Office Supplies Expense | Accounts Payable | 18,328.79 | D020 | 2024-06-08 | clinic_supplies_bill |
| 23 | Accounts Receivable | Service Revenue | 13,551.41 | D021 | 2024-08-23 | patient_billing |
| 24 | Office Supplies Expense | Accounts Payable | 26,739.96 | D022 | 2024-06-13 | clinic_supplies_bill |
| 25 | Accounts Receivable | Service Revenue | 7,634.73 | D023 | 2024-08-26 | patient_billing |
| 26 | Office Supplies Expense | Accounts Payable | 22,360.67 | D024 | 2024-05-18 | clinic_supplies_bill |
| 27 | Accounts Receivable | Service Revenue | 13,436.14 | D025 | 2024-11-20 | patient_billing |
| 28 | Office Supplies Expense | Accounts Payable | 52,462.12 | D026 | 2024-06-25 | clinic_supplies_bill |
| 29 | Office Supplies Expense | Accounts Payable | 47,269.20 | D027 | 2024-04-20 | clinic_supplies_bill |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 179,250.48
- Accounts Receivable: 154,291.91
- Prepaid Insurance: 15,113.26
- Office Supplies: 3,018.71
- Equipment: 337,304.32
- Accumulated Depreciation: -75,520.80

**Liabilities**
- Accounts Payable: 302,217.14
- Accrued Expenses: 21,591.62
- Loans Payable: 115,312.90
- Notes Payable: 179,976.89

**Equity**
- Retained Earnings: -329,701.53
- Owner's Equity: 324,060.86

**Totals:** Assets = 613,457.88; Liabilities = 619,098.55; Equity = -5,640.67
**Balanced (A = L + E):** True

---

## 7. Verification Form

_Fill in your judgement below. For each question, mark one box and add notes where applicable._

### Q1 — Document analogy to real paperwork
We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?
- [ ] Yes — analogous to what an accountant would receive
- [x] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes: Some line items lack description detail but amounts and party info are present.

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
- Notes: Acceptable as ground truth.
