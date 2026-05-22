# Verification Packet — COV_HEA_M2_0061

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 2
- **Period type:** month
- **Period label:** December 2024
- **Period start → end:** 2024-12-01 → 2024-12-31
- **Entity:** Harbor Builders
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 8
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-12-01_

**Assets**
- Cash: 33,467.65
- Accounts Receivable: 5,632.48
- Prepaid Insurance: 2,241.48
- Office Supplies: 574.90

**Liabilities**
- Accounts Payable: 4,089.24
- Accrued Expenses: 1,199.25

**Equity**
- Retained Earnings: 12,609.36
- Owner's Equity: 24,018.66


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-12-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/12/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 33.467,65
  - Section assets | Account Accounts Receivable | Amount EUR 5.632,48
  - Section assets | Account Prepaid Insurance | Amount EUR 2.241,48
  - Section assets | Account Office Supplies | Amount EUR 574,90
  - Section liabilities | Account Accounts Payable | Amount EUR 4.089,24
  - Section liabilities | Account Accrued Expenses | Amount EUR 1.199,25
  - Section equity | Account Retained Earnings | Amount EUR 12.609,36
  - Section equity | Account Owner's Equity | Amount EUR 24.018,66

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-09

```
VENDOR INVOICE
==============

From
----
Harbor Builders
75 Market Road, Mumbai
Date: 09/12/2024

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: December 2024

Terms
-----
Due Date: 27/12/2024

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 27/12/2024
Total: EUR 2.337,68

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount EUR 997,46
  - Description Support fee | Amount EUR 1.340,22

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D002 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-13

```
PATIENT INVOICE
===============

From
----
Harbor Builders
75 Market Road, Mumbai
Date: 13/12/2024

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D002
Document Type: patient_invoice
Period: December 2024

Invoice Summary
---------------
Invoice Number: PTINV-0001
Patient: Marcus Lee
Payer: CareSure
Service Date: 13/12/2024
Gross Charge: EUR 1.593,55
Patient Due: 423,99
Insurer Due: 1.169,56

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D007 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-16

```
PATIENT INVOICE
===============

From
----
Harbor Builders
75 Market Road, Mumbai
Document Date: 16/12/2024

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D007
Document Type: patient_invoice
Period: December 2024

Invoice Summary
---------------
Invoice Number: PTINV-0003
Patient: Ella Santos
Payer: CareSure
Service Date: 16/12/2024
Gross Charge: EUR 1.907,43
Patient Due: 418,90
Insurer Due: 1.488,53

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D006 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-21

```
PATIENT INVOICE
===============

From
----
Harbor Builders
75 Market Road, Mumbai
Document Date: 21/12/2024

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D006
Document Type: patient_invoice
Period: December 2024

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Ella Santos
Payer: CareSure
Service Date: 21/12/2024
Gross Charge: EUR 1.908,40
Patient Due: 341,81
Insurer Due: 1.566,59

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D005 — Insurer Remittance

- **Type:** `insurer_remittance`
- **Role:** `posting_doc`
- **Date:** 2024-12-24

```
INSURER REMITTANCE
==================

From
----
Harbor Builders
75 Market Road, Mumbai
Date: 24/12/2024

Reference Box
-------------
Document ID: D005
Document Type: insurer_remittance
Period: December 2024

Remittance Summary
------------------
Remittance Number: REM-0001
Payer: CareSure
Claim Reference: PTINV-0001
Approved Amount: EUR 1.169,56
Paid Amount: EUR 1.169,56
Payment Date: 24/12/2024

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D004 — Copay Receipt

- **Type:** `copay_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-12-28

```
COPAY RECEIPT
=============

From
----
Harbor Builders
75 Market Road, Mumbai
Date: 28/12/2024

To
--
Marcus Lee
Patient billing contact

Copay Receipt
-------------
Receipt Number: COPAY-0001
Patient: Marcus Lee
Amount: EUR 423,99
Reference Invoice: PTINV-0001
Payment Method: Online

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D008 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Harbor Builders
75 Market Road, Mumbai
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D008
Document Type: bank_statement
Period: December 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0061
Statement Currency: EUR
Opening Balance: EUR 33.467,65
Closing Balance: EUR 35.061,20

Statement Rows
--------------
Rows:
  - Date 24/12/2024 | Description Insurer remittance PTINV-0001 | Amount EUR 1.169,56 | 
Running Balance EUR 34.637,21
  - Date 28/12/2024 | Description Copay receipt COPAY-0001 | Amount EUR 423,99 | Running 
Balance EUR 35.061,20

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 1,593.55 | D002 | 2024-12-13 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 2,337.68 | D003 | 2024-12-09 | clinic_supplies_bill |
| 3 | Cash | Accounts Receivable | 423.99 | D004, D002 | 2024-12-28 | copay_collection |
| 4 | Cash | Accounts Receivable | 1,169.56 | D005, D002 | 2024-12-24 | insurer_remittance |
| 5 | Accounts Receivable | Service Revenue | 1,908.40 | D006 | 2024-12-21 | patient_billing |
| 6 | Accounts Receivable | Service Revenue | 1,907.43 | D007 | 2024-12-16 | patient_billing |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 35,061.20
- Accounts Receivable: 9,448.31
- Prepaid Insurance: 2,241.48
- Office Supplies: 574.90

**Liabilities**
- Accounts Payable: 6,426.92
- Accrued Expenses: 1,199.25

**Equity**
- Retained Earnings: 15,681.06
- Owner's Equity: 24,018.66

**Totals:** Assets = 47,325.89; Liabilities = 7,626.17; Equity = 39,699.72
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
