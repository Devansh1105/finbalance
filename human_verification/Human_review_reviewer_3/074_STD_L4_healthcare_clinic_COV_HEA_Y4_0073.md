# Verification Packet — COV_HEA_Y4_0073

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 4
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Harbor Software
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 25
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 202,964.43
- Accounts Receivable: 18,480.18
- Prepaid Insurance: 6,509.84
- Office Supplies: 2,534.87
- Equipment: 63,188.75

**Liabilities**
- Accounts Payable: 19,021.13
- Accrued Expenses: 6,399.42
- Loans Payable: 37,412.06

**Equity**
- Retained Earnings: 22,848.96
- Owner's Equity: 207,996.50


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
  - Section assets | Account Cash | Amount EUR 202.964,43
  - Section assets | Account Accounts Receivable | Amount EUR 18.480,18
  - Section assets | Account Prepaid Insurance | Amount EUR 6.509,84
  - Section assets | Account Office Supplies | Amount EUR 2.534,87
  - Section assets | Account Equipment | Amount EUR 63.188,75
  - Section liabilities | Account Accounts Payable | Amount EUR 19.021,13
  - Section liabilities | Account Accrued Expenses | Amount EUR 6.399,42
  - Section liabilities | Account Loans Payable | Amount EUR 37.412,06
  - Section equity | Account Retained Earnings | Amount EUR 22.848,96
  - Section equity | Account Owner's Equity | Amount EUR 207.996,50

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D011 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-25

```
VENDOR INVOICE
==============

From
----
Harbor Software
14 King Street, Pune
Document Date: 25/04/2024

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 09/05/2024

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 09/05/2024
Total: EUR 15.622,19

Bill Lines
----------
Lines:
  - Description Review pack | Amount EUR 4.197,02
  - Description Support fee | Amount EUR 11.425,17

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D013 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-27

```
VENDOR INVOICE
==============

From
----
Harbor Software
14 King Street, Pune
Document Date: 27/04/2024

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D013
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 15/05/2024

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0003
Due Date: 15/05/2024
Total: EUR 31.278,10

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount EUR 12.564,43
  - Description Support fee | Amount EUR 18.713,67

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D020 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-11

```
VENDOR INVOICE
==============

From
----
Harbor Software
14 King Street, Pune
Date: 11/05/2024

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D020
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 30/05/2024

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0007
Due Date: 30/05/2024
Total: EUR 38.374,44

Bill Lines
----------
Lines:
  - Description Support package | Amount EUR 8.842,95
  - Description Support fee | Amount EUR 29.531,49

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-12

```
VENDOR INVOICE
==============

From
----
Harbor Software
14 King Street, Pune
Date: 12/05/2024

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
Due Date: 02/06/2024

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 02/06/2024
Total: EUR 34.931,11

Bill Lines
----------
Lines:
  - Description Support package | Amount EUR 10.501,73
  - Description Support fee | Amount EUR 24.429,38

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D018 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-08

```
VENDOR INVOICE
==============

From
----
Harbor Software
14 King Street, Pune
Document Date: 08/06/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D018
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 19/06/2024

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0006
Due Date: 19/06/2024
Total: EUR 13.901,98

Bill Lines
----------
Lines:
  - Description Implementation work | Amount EUR 2.875,74
  - Description Support fee | Amount EUR 11.026,24

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D016 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-23

```
VENDOR INVOICE
==============

From
----
Harbor Software
14 King Street, Pune
Date: 23/06/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 04/07/2024

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0005
Due Date: 04/07/2024
Total: EUR 9.362,43

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount EUR 3.945,61
  - Description Support fee | Amount EUR 5.416,82

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D015 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-27

```
VENDOR INVOICE
==============

From
----
Harbor Software
14 King Street, Pune
Date: 27/06/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D015
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 15/07/2024

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0004
Due Date: 15/07/2024
Total: EUR 33.152,31

Bill Lines
----------
Lines:
  - Description Implementation work | Amount EUR 9.175,11
  - Description Support fee | Amount EUR 23.977,20

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D008 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-08

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Prime Utility Desk
Asset Name: CNC router
Asset Tag: TAG-0001
Useful Life Months: 24
Total: EUR 84.208,90
Paid Cash: EUR 18.878,60
Financed Amount: EUR 65.330,30
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D017 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-25

```
PATIENT INVOICE
===============

From
----
Harbor Software
14 King Street, Pune
Document Date: 25/09/2024

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D017
Document Type: patient_invoice
Period: FY 2024-25

Invoice Summary
---------------
Invoice Number: PTINV-0004
Patient: Noah Ferreira
Payer: CareSure
Service Date: 25/09/2024
Gross Charge: EUR 18.312,56
Patient Due: 3.082,87
Insurer Due: 15.229,69

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D021 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-02

```
PATIENT INVOICE
===============

From
----
Harbor Software
14 King Street, Pune
Date: 02/11/2024

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
Invoice Number: PTINV-0006
Patient: Anaya Patel
Payer: Unity Health Plan
Service Date: 02/11/2024
Gross Charge: EUR 16.863,88
Patient Due: 3.320,19
Insurer Due: 13.543,69

Footer
------
Internal document packet copy.
Page marker: D021
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
Harbor Software
14 King Street, Pune
Date: 08/11/2024

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
Payer: Unity Health Plan
Service Date: 08/11/2024
Gross Charge: EUR 11.339,76
Patient Due: 3.283,97
Insurer Due: 8.055,79

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D012 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-09

```
PATIENT INVOICE
===============

From
----
Harbor Software
14 King Street, Pune
Date: 09/11/2024

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D012
Document Type: patient_invoice
Period: FY 2024-25

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Marcus Lee
Payer: CareSure
Service Date: 09/11/2024
Gross Charge: EUR 11.882,89
Patient Due: 2.066,29
Insurer Due: 9.816,60

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D019 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-18

```
PATIENT INVOICE
===============

From
----
Harbor Software
14 King Street, Pune
Document Date: 18/11/2024

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
Invoice Number: PTINV-0005
Patient: Anaya Patel
Payer: Unity Health Plan
Service Date: 18/11/2024
Gross Charge: EUR 4.679,16
Patient Due: 1.487,02
Insurer Due: 3.192,14

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D007 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-12-03

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: EUR 32.496,12
Draw Amount: EUR 232.598,78
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 265.094,90
Note: Scheduled lender activity for the selected period.
```

### Document D014 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-03

```
PATIENT INVOICE
===============

From
----
Harbor Software
14 King Street, Pune
Date: 03/12/2024

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D014
Document Type: patient_invoice
Period: FY 2024-25

Invoice Summary
---------------
Invoice Number: PTINV-0003
Patient: Marcus Lee
Payer: NorthCover
Service Date: 03/12/2024
Gross Charge: EUR 10.640,11
Patient Due: 3.648,19
Insurer Due: 6.991,92

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D023 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-12-03

```
SECONDARY COPY
==============

From
----
Harbor Software
14 King Street, Pune
Document Date: 03/12/2024

To
--
Marcus Lee

Reference Box
-------------
Document ID: D023
Document Type: secondary_copy
Period: FY 2024-25

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: PTINV-0003
Counterparty: Marcus Lee
Total: EUR 10.640,11
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D023
```

### Document D005 — Insurer Remittance

- **Type:** `insurer_remittance`
- **Role:** `posting_doc`
- **Date:** 2024-12-28

```
INSURER REMITTANCE
==================

From
----
Harbor Software
14 King Street, Pune
Date: 28/12/2024

Reference Box
-------------
Document ID: D005
Document Type: insurer_remittance
Period: FY 2024-25

Remittance Summary
------------------
Remittance Number: REM-0001
Payer: Unity Health Plan
Claim Reference: PTINV-0001
Approved Amount: EUR 8.055,79
Paid Amount: EUR 8.055,79
Payment Date: 28/12/2024

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D004 — Copay Receipt

- **Type:** `copay_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-01-29

```
COPAY RECEIPT
=============

From
----
Harbor Software
14 King Street, Pune
Date: 29/01/2025

To
--
Ella Santos
Patient billing contact

Copay Receipt
-------------
Receipt Number: COPAY-0001
Patient: Ella Santos
Amount: EUR 3.283,97
Reference Invoice: PTINV-0001
Payment Method: Cash

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D006 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-02-20

```
PAYROLL SUMMARY
===============

From
----
Harbor Software
14 King Street, Pune
Date: 20/02/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024-25
Headcount: 8
Gross Pay: EUR 84.165,66
Employer Tax: 10.016,12
Cash Outflow: EUR 94.181,78

Footer
------
Internal document packet copy.
Page marker: D006
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
Harbor Software
14 King Street, Pune
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D009
Document Type: fixed_asset_rollforward
Period: FY 2024-25

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: EUR 63.188,75
Useful Life: 48
Current Charge: EUR 15.797,16
Accumulated Depreciation: 15.797,16
Opening Balance: EUR 63.188,75
Additions: 0,00
Disposals: 0,00
Ending Balance: EUR 63.188,75

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D010 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Harbor Software
14 King Street, Pune
Date: 31/03/2025

Reference Box
-------------
Document ID: D010
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
Recognized Amount: EUR 3.634,59

Explanation
-----------
Narrative: Accrue unpaid office supplies expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D022 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Harbor Software
14 King Street, Pune
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D022
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0001
Subject: Quarter-end packet routing note
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
Page marker: D022
```

### Document D024 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Harbor Software
14 King Street, Pune
Date: 31/03/2025

Reference Box
-------------
Document ID: D024
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Scanning checklist for back-office staff

Memo Summary
------------
Memo ID: INFO-0002
Subject: Scanning checklist for back-office staff
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
Page marker: D024
```

### Document D025 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Harbor Software
14 King Street, Pune
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D025
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0073
Statement Currency: EUR
Opening Balance: EUR 202.964,43
Closing Balance: EUR 333.842,59

Statement Rows
--------------
Rows:
  - Date 08/09/2024 | Description Asset purchase ASSET-0001 | Amount EUR -18.878,60 | 
Running Balance EUR 184.085,83
  - Date 03/12/2024 | Description Loan draw LOAN-0001 | Amount EUR 232.598,78 | Running 
Balance EUR 416.684,61
  - Date 28/12/2024 | Description Insurer remittance PTINV-0001 | Amount EUR 8.055,79 | 
Running Balance EUR 424.740,40
  - Date 29/01/2025 | Description Copay receipt COPAY-0001 | Amount EUR 3.283,97 | Running 
Balance EUR 428.024,37
  - Date 20/02/2025 | Description Payroll PAYRUN-0001 | Amount EUR -94.181,78 | Running 
Balance EUR 333.842,59

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D025
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 11,339.76 | D002 | 2024-11-08 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 34,931.11 | D003 | 2024-05-12 | clinic_supplies_bill |
| 3 | Cash | Accounts Receivable | 3,283.97 | D004, D002 | 2025-01-29 | copay_collection |
| 4 | Cash | Accounts Receivable | 8,055.79 | D005, D002 | 2024-12-28 | insurer_remittance |
| 5 | Salaries Expense | Cash | 84,165.66 | D006 | 2025-02-20 | payroll_gross |
| 6 | Payroll Tax Expense | Cash | 10,016.12 | D006 | 2025-02-20 | payroll_tax |
| 7 | Cash | Loans Payable | 232,598.78 | D007 | 2024-12-03 | loan_draw |
| 8 | Equipment | Cash | 18,878.60 | D008 | 2024-09-08 | equipment_purchase_cash |
| 9 | Equipment | Notes Payable | 65,330.30 | D008 | 2024-09-08 | equipment_purchase_financed |
| 10 | Depreciation Expense | Accumulated Depreciation | 15,797.16 | D009 | 2025-03-31 | depreciation |
| 11 | Office Supplies Expense | Accrued Expenses | 3,634.59 | D010 | 2025-03-31 | expense_accrual |
| 12 | Office Supplies Expense | Accounts Payable | 15,622.19 | D011 | 2024-04-25 | clinic_supplies_bill |
| 13 | Accounts Receivable | Service Revenue | 11,882.89 | D012 | 2024-11-09 | patient_billing |
| 14 | Office Supplies Expense | Accounts Payable | 31,278.10 | D013 | 2024-04-27 | clinic_supplies_bill |
| 15 | Accounts Receivable | Service Revenue | 10,640.11 | D014 | 2024-12-03 | patient_billing |
| 16 | Office Supplies Expense | Accounts Payable | 33,152.31 | D015 | 2024-06-27 | clinic_supplies_bill |
| 17 | Office Supplies Expense | Accounts Payable | 9,362.43 | D016 | 2024-06-23 | clinic_supplies_bill |
| 18 | Accounts Receivable | Service Revenue | 18,312.56 | D017 | 2024-09-25 | patient_billing |
| 19 | Office Supplies Expense | Accounts Payable | 13,901.98 | D018 | 2024-06-08 | clinic_supplies_bill |
| 20 | Accounts Receivable | Service Revenue | 4,679.16 | D019 | 2024-11-18 | patient_billing |
| 21 | Office Supplies Expense | Accounts Payable | 38,374.44 | D020 | 2024-05-11 | clinic_supplies_bill |
| 22 | Accounts Receivable | Service Revenue | 16,863.88 | D021 | 2024-11-02 | patient_billing |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 333,842.59
- Accounts Receivable: 80,858.78
- Prepaid Insurance: 6,509.84
- Office Supplies: 2,534.87
- Equipment: 147,397.65
- Accumulated Depreciation: -15,797.16

**Liabilities**
- Accounts Payable: 195,643.69
- Accrued Expenses: 10,034.01
- Loans Payable: 270,010.84
- Notes Payable: 65,330.30

**Equity**
- Retained Earnings: -193,668.77
- Owner's Equity: 207,996.50

**Totals:** Assets = 555,346.57; Liabilities = 541,018.84; Equity = 14,327.73
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
- Notes:
