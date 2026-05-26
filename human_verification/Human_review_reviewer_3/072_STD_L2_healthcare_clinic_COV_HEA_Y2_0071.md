# Verification Packet — COV_HEA_Y2_0071

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 2
- **Period type:** year
- **Period label:** FY 2025
- **Period start → end:** 2025-01-01 → 2025-12-31
- **Entity:** Atlas Manufacturing
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 14
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 112,285.39
- Accounts Receivable: 9,365.87
- Prepaid Insurance: 4,914.92
- Office Supplies: 3,145.36

**Liabilities**
- Accounts Payable: 7,122.30
- Accrued Expenses: 3,816.57

**Equity**
- Retained Earnings: 28,532.43
- Owner's Equity: 90,240.24


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
  - Section assets | Account Cash | Amount GBP 112,285.39
  - Section assets | Account Accounts Receivable | Amount GBP 9,365.87
  - Section assets | Account Prepaid Insurance | Amount GBP 4,914.92
  - Section assets | Account Office Supplies | Amount GBP 3,145.36
  - Section liabilities | Account Accounts Payable | Amount GBP 7,122.30
  - Section liabilities | Account Accrued Expenses | Amount GBP 3,816.57
  - Section equity | Account Retained Earnings | Amount GBP 28,532.43
  - Section equity | Account Owner's Equity | Amount GBP 90,240.24

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-21

```
VENDOR INVOICE
==============

From
----
Atlas Manufacturing
90 Hill Park, Hyderabad
Date: 21/01/2025

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2025

Terms
-----
Due Date: 11/02/2025

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 11/02/2025
Total: GBP 16,353.74

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 6,173.48
  - Description Support fee | Amount GBP 10,180.26

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D006 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-04

```
PATIENT INVOICE
===============

From
----
Atlas Manufacturing
90 Hill Park, Hyderabad
Document Date: 04/05/2025

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D006
Document Type: patient_invoice
Period: FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Marcus Lee
Payer: Harbor Health Network
Service Date: 04/05/2025
Gross Charge: GBP 12,331.49
Patient Due: 3,123.41
Insurer Due: 9,208.08

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D007 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-25

```
PATIENT INVOICE
===============

From
----
Atlas Manufacturing
90 Hill Park, Hyderabad
Date: 25/05/2025

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D007
Document Type: patient_invoice
Period: FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0003
Patient: Marcus Lee
Payer: NorthCover
Service Date: 25/05/2025
Gross Charge: GBP 9,209.91
Patient Due: 2,987.93
Insurer Due: 6,221.98

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D011 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-01

```
PATIENT INVOICE
===============

From
----
Atlas Manufacturing
90 Hill Park, Hyderabad
Document Date: 01/06/2025

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D011
Document Type: patient_invoice
Period: FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0007
Patient: Marcus Lee
Payer: Unity Health Plan
Service Date: 01/06/2025
Gross Charge: GBP 8,565.67
Patient Due: 2,393.15
Insurer Due: 6,172.52

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D010 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-05

```
PATIENT INVOICE
===============

From
----
Atlas Manufacturing
90 Hill Park, Hyderabad
Date: 05/06/2025

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D010
Document Type: patient_invoice
Period: FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0006
Patient: Ella Santos
Payer: NorthCover
Service Date: 05/06/2025
Gross Charge: GBP 6,936.25
Patient Due: 2,133.38
Insurer Due: 4,802.87

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D012 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-18

```
PATIENT INVOICE
===============

From
----
Atlas Manufacturing
90 Hill Park, Hyderabad
Document Date: 18/06/2025

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D012
Document Type: patient_invoice
Period: FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0008
Patient: Ella Santos
Payer: NorthCover
Service Date: 18/06/2025
Gross Charge: GBP 7,008.17
Patient Due: 1,401.34
Insurer Due: 5,606.83

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D009 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-26

```
PATIENT INVOICE
===============

From
----
Atlas Manufacturing
90 Hill Park, Hyderabad
Date: 26/06/2025

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D009
Document Type: patient_invoice
Period: FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0005
Patient: Marcus Lee
Payer: Harbor Health Network
Service Date: 26/06/2025
Gross Charge: GBP 4,969.67
Patient Due: 1,368.00
Insurer Due: 3,601.67

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D002 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-06

```
PATIENT INVOICE
===============

From
----
Atlas Manufacturing
90 Hill Park, Hyderabad
Date: 06/07/2025

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D002
Document Type: patient_invoice
Period: FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0001
Patient: Noah Ferreira
Payer: NorthCover
Service Date: 06/07/2025
Gross Charge: GBP 10,935.56
Patient Due: 2,063.14
Insurer Due: 8,872.42

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D008 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-14

```
PATIENT INVOICE
===============

From
----
Atlas Manufacturing
90 Hill Park, Hyderabad
Date: 14/07/2025

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D008
Document Type: patient_invoice
Period: FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0004
Patient: Marcus Lee
Payer: CareSure
Service Date: 14/07/2025
Gross Charge: GBP 11,086.72
Patient Due: 1,896.52
Insurer Due: 9,190.20

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D005 — Insurer Remittance

- **Type:** `insurer_remittance`
- **Role:** `posting_doc`
- **Date:** 2025-09-24

```
INSURER REMITTANCE
==================

From
----
Atlas Manufacturing
90 Hill Park, Hyderabad
Date: 24/09/2025

Reference Box
-------------
Document ID: D005
Document Type: insurer_remittance
Period: FY 2025

Remittance Summary
------------------
Remittance Number: REM-0001
Payer: NorthCover
Claim Reference: PTINV-0001
Approved Amount: GBP 8,872.42
Paid Amount: GBP 8,872.42
Payment Date: 24/09/2025

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D004 — Copay Receipt

- **Type:** `copay_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-11-22

```
COPAY RECEIPT
=============

From
----
Atlas Manufacturing
90 Hill Park, Hyderabad
Date: 22/11/2025

To
--
Noah Ferreira
Patient billing contact

Copay Receipt
-------------
Receipt Number: COPAY-0001
Patient: Noah Ferreira
Amount: GBP 2,063.14
Reference Invoice: PTINV-0001
Payment Method: Card

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D013 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
VENDOR STATEMENT
================

From
----
Atlas Manufacturing
90 Hill Park, Hyderabad
Document Date: 31/12/2025

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D013
Document Type: vendor_statement
Period: FY 2025

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Vertex Supply Co.
Closing Balance: GBP 16,353.74

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount GBP 16,353.74 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D014 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Atlas Manufacturing
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D014
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0071
Statement Currency: GBP
Opening Balance: GBP 112,285.39
Closing Balance: GBP 123,220.95

Statement Rows
--------------
Rows:
  - Date 24/09/2025 | Description Insurer remittance PTINV-0001 | Amount GBP 8,872.42 | 
Running Balance GBP 121,157.81
  - Date 22/11/2025 | Description Copay receipt COPAY-0001 | Amount GBP 2,063.14 | Running 
Balance GBP 123,220.95

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D014
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 10,935.56 | D002 | 2025-07-06 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 16,353.74 | D003 | 2025-01-21 | clinic_supplies_bill |
| 3 | Cash | Accounts Receivable | 2,063.14 | D004, D002 | 2025-11-22 | copay_collection |
| 4 | Cash | Accounts Receivable | 8,872.42 | D005, D002 | 2025-09-24 | insurer_remittance |
| 5 | Accounts Receivable | Service Revenue | 12,331.49 | D006 | 2025-05-04 | patient_billing |
| 6 | Accounts Receivable | Service Revenue | 9,209.91 | D007 | 2025-05-25 | patient_billing |
| 7 | Accounts Receivable | Service Revenue | 11,086.72 | D008 | 2025-07-14 | patient_billing |
| 8 | Accounts Receivable | Service Revenue | 4,969.67 | D009 | 2025-06-26 | patient_billing |
| 9 | Accounts Receivable | Service Revenue | 6,936.25 | D010 | 2025-06-05 | patient_billing |
| 10 | Accounts Receivable | Service Revenue | 8,565.67 | D011 | 2025-06-01 | patient_billing |
| 11 | Accounts Receivable | Service Revenue | 7,008.17 | D012 | 2025-06-18 | patient_billing |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 123,220.95
- Accounts Receivable: 69,473.75
- Prepaid Insurance: 4,914.92
- Office Supplies: 3,145.36

**Liabilities**
- Accounts Payable: 23,476.04
- Accrued Expenses: 3,816.57

**Equity**
- Retained Earnings: 83,222.13
- Owner's Equity: 90,240.24

**Totals:** Assets = 200,754.98; Liabilities = 27,292.61; Equity = 173,462.37
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
- [ ] Yes, doc_refs are correct
- [x] Mostly correct with minor mismatches
- [ ] Doc_refs are systematically wrong
- Notes: Minor ref mismatch on the accrual reversal. Doesn't change the posting.

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
