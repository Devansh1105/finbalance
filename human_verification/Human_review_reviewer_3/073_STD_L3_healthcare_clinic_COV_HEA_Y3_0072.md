# Verification Packet — COV_HEA_Y3_0072

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 3
- **Period type:** year
- **Period label:** FY 2024
- **Period start → end:** 2024-01-01 → 2024-12-31
- **Entity:** Granite Distribution
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 20
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-01-01_

**Assets**
- Cash: 137,140.44
- Accounts Receivable: 20,672.76
- Prepaid Insurance: 7,605.08
- Office Supplies: 4,033.76

**Liabilities**
- Accounts Payable: 16,349.28
- Accrued Expenses: 7,312.03

**Equity**
- Retained Earnings: 35,563.30
- Owner's Equity: 110,227.43


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
Statement Date: 2024-01-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $137,140.44
  - Section assets | Account Accounts Receivable | Amount $20,672.76
  - Section assets | Account Prepaid Insurance | Amount $7,605.08
  - Section assets | Account Office Supplies | Amount $4,033.76
  - Section liabilities | Account Accounts Payable | Amount $16,349.28
  - Section liabilities | Account Accrued Expenses | Amount $7,312.03
  - Section equity | Account Retained Earnings | Amount $35,563.30
  - Section equity | Account Owner's Equity | Amount $110,227.43

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D009 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-01-29

```
VENDOR INVOICE
==============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Document Date: 2024-01-29

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-02-09

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 2024-02-09
Total: $23,110.11

Bill Lines
----------
Lines:
  - Description Review pack | Amount $6,655.76
  - Description Support fee | Amount $16,454.35

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D014 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-07

```
VENDOR INVOICE
==============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Document Date: 2024-02-07

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D014
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-02-27

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0006
Due Date: 2024-02-27
Total: $12,664.09

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount $5,198.46
  - Description Support fee | Amount $7,465.63

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D012 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-19

```
VENDOR INVOICE
==============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Date: 2024-03-19

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-04-05

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0005
Due Date: 2024-04-05
Total: $12,365.42

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $4,045.65
  - Description Support fee | Amount $8,319.77

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D011 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-21

```
VENDOR INVOICE
==============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Date: 2024-03-21

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-04-11

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0004
Due Date: 2024-04-11
Total: $3,497.26

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $934.42
  - Description Support fee | Amount $2,562.84

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D017 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-03-21

```
SECONDARY COPY
==============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Date: 2024-03-21

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D017
Document Type: secondary_copy
Period: FY 2024

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0004
Counterparty: Vertex Supply Co.
Total: $3,497.26
Copy Context: Forwarded copy attached to the customer correspondence bundle.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D018 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-03-21

```
SECONDARY COPY
==============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Document Date: 2024-03-21

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D018
Document Type: secondary_copy
Period: FY 2024

Copy Summary
------------
Copy ID: COPY-0002
Source Reference: BILL-0004
Counterparty: Vertex Supply Co.
Total: $3,497.26
Copy Context: Forwarded copy attached to the customer correspondence bundle.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D010 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-31

```
VENDOR INVOICE
==============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Document Date: 2024-03-31

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-04-18

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0003
Due Date: 2024-04-18
Total: $30,024.50

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount $7,969.47
  - Description Support fee | Amount $22,055.03

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D016 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-05

```
VENDOR INVOICE
==============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Document Date: 2024-04-05

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-04-24

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0007
Due Date: 2024-04-24
Total: $37,786.50

Bill Lines
----------
Lines:
  - Description Implementation work | Amount $9,248.55
  - Description Support fee | Amount $28,537.95

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-10

```
VENDOR INVOICE
==============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Date: 2024-04-10

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-04-23

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-04-23
Total: $15,256.42

Bill Lines
----------
Lines:
  - Description Support package | Amount $6,060.53
  - Description Support fee | Amount $9,195.89

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D015 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-13

```
PATIENT INVOICE
===============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Document Date: 2024-05-13

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D015
Document Type: patient_invoice
Period: FY 2024

Invoice Summary
---------------
Invoice Number: PTINV-0004
Patient: Noah Ferreira
Payer: Harbor Health Network
Service Date: 2024-05-13
Gross Charge: $10,509.83
Patient Due: 2,025.87
Insurer Due: 8,483.96

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D013 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-02

```
PATIENT INVOICE
===============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Date: 2024-07-02

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D013
Document Type: patient_invoice
Period: FY 2024

Invoice Summary
---------------
Invoice Number: PTINV-0003
Patient: Ella Santos
Payer: CareSure
Service Date: 2024-07-02
Gross Charge: $4,518.64
Patient Due: 1,373.11
Insurer Due: 3,145.53

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D008 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-04

```
PATIENT INVOICE
===============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Date: 2024-07-04

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D008
Document Type: patient_invoice
Period: FY 2024

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Ella Santos
Payer: CareSure
Service Date: 2024-07-04
Gross Charge: $5,966.24
Patient Due: 1,140.95
Insurer Due: 4,825.29

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D002 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-12

```
PATIENT INVOICE
===============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Date: 2024-07-12

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D002
Document Type: patient_invoice
Period: FY 2024

Invoice Summary
---------------
Invoice Number: PTINV-0001
Patient: Anaya Patel
Payer: CareSure
Service Date: 2024-07-12
Gross Charge: $15,220.48
Patient Due: 4,036.35
Insurer Due: 11,184.13

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D006 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-09-12

```
PAYROLL SUMMARY
===============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Date: 2024-09-12

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024
Headcount: 6
Gross Pay: $25,256.35
Employer Tax: 3,297.28
Cash Outflow: $28,553.63

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D004 — Copay Receipt

- **Type:** `copay_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-09-15

```
COPAY RECEIPT
=============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Date: 2024-09-15

To
--
Anaya Patel
Patient billing contact

Copay Receipt
-------------
Receipt Number: COPAY-0001
Patient: Anaya Patel
Amount: $4,036.35
Reference Invoice: PTINV-0001
Payment Method: Online

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D005 — Insurer Remittance

- **Type:** `insurer_remittance`
- **Role:** `posting_doc`
- **Date:** 2024-09-22

```
INSURER REMITTANCE
==================

From
----
Granite Distribution
90 Hill Park, Hyderabad
Document Date: 2024-09-22

Reference Box
-------------
Document ID: D005
Document Type: insurer_remittance
Period: FY 2024

Remittance Summary
------------------
Remittance Number: REM-0001
Payer: CareSure
Claim Reference: PTINV-0001
Approved Amount: $11,184.13
Paid Amount: $11,184.13
Payment Date: 2024-09-22

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D007 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Granite Distribution
90 Hill Park, Hyderabad
Document Date: 2024-12-31

Reference Box
-------------
Document ID: D007
Document Type: service_period_memo
Period: FY 2024
Reference: FY 2024

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: FY 2024
Recognized Amount: $6,462.20

Explanation
-----------
Narrative: Accrue unpaid office supplies expense incurred before period end.

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D019 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
MEMO
====

From
----
Granite Distribution
90 Hill Park, Hyderabad
Document Date: 2024-12-31

Reference Box
-------------
Document ID: D019
Document Type: memo
Period: FY 2024

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
Narrative: Please route scanned paperwork to the shared archive after the period binder is 
complete.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Granite Distribution
90 Hill Park, Hyderabad
Date: 2024-12-31

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0072
Statement Currency: USD
Opening Balance: $137,140.44
Closing Balance: $123,807.29

Statement Rows
--------------
Rows:
  - Date 2024-09-12 | Description Payroll PAYRUN-0001 | Amount $-28,553.63 | Running Balance
 $108,586.81
  - Date 2024-09-15 | Description Copay receipt COPAY-0001 | Amount $4,036.35 | Running 
Balance $112,623.16
  - Date 2024-09-22 | Description Insurer remittance PTINV-0001 | Amount $11,184.13 | 
Running Balance $123,807.29

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D020
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 15,220.48 | D002 | 2024-07-12 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 15,256.42 | D003 | 2024-04-10 | clinic_supplies_bill |
| 3 | Cash | Accounts Receivable | 4,036.35 | D004, D002 | 2024-09-15 | copay_collection |
| 4 | Cash | Accounts Receivable | 11,184.13 | D005, D002 | 2024-09-22 | insurer_remittance |
| 5 | Salaries Expense | Cash | 25,256.35 | D006 | 2024-09-12 | payroll_gross |
| 6 | Payroll Tax Expense | Cash | 3,297.28 | D006 | 2024-09-12 | payroll_tax |
| 7 | Office Supplies Expense | Accrued Expenses | 6,462.20 | D007 | 2024-12-31 | expense_accrual |
| 8 | Accounts Receivable | Service Revenue | 5,966.24 | D008 | 2024-07-04 | patient_billing |
| 9 | Office Supplies Expense | Accounts Payable | 23,110.11 | D009 | 2024-01-29 | clinic_supplies_bill |
| 10 | Office Supplies Expense | Accounts Payable | 30,024.50 | D010 | 2024-03-31 | clinic_supplies_bill |
| 11 | Office Supplies Expense | Accounts Payable | 3,497.26 | D011 | 2024-03-21 | clinic_supplies_bill |
| 12 | Office Supplies Expense | Accounts Payable | 12,365.42 | D012 | 2024-03-19 | clinic_supplies_bill |
| 13 | Accounts Receivable | Service Revenue | 4,518.64 | D013 | 2024-07-02 | patient_billing |
| 14 | Office Supplies Expense | Accounts Payable | 12,664.09 | D014 | 2024-02-07 | clinic_supplies_bill |
| 15 | Accounts Receivable | Service Revenue | 10,509.83 | D015 | 2024-05-13 | patient_billing |
| 16 | Office Supplies Expense | Accounts Payable | 37,786.50 | D016 | 2024-04-05 | clinic_supplies_bill |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 123,807.29
- Accounts Receivable: 41,667.47
- Prepaid Insurance: 7,605.08
- Office Supplies: 4,033.76

**Liabilities**
- Accounts Payable: 151,053.58
- Accrued Expenses: 13,774.23

**Equity**
- Retained Earnings: -97,941.64
- Owner's Equity: 110,227.43

**Totals:** Assets = 177,113.60; Liabilities = 164,827.81; Equity = 12,285.79
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
- Notes: Looks fine for benchmark use.
