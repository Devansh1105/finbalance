# Verification Packet — COV_HEA_Y1_0070

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 1
- **Period type:** year
- **Period label:** FY 2025-26
- **Period start → end:** 2025-04-01 → 2026-03-31
- **Entity:** Willow Operations
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `none`
- **Document count:** 11
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 108,073.69
- Accounts Receivable: 17,553.23

**Liabilities**
- Accounts Payable: 9,044.53

**Equity**
- Owner's Equity: 116,582.39


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
  - Section assets | Account Cash | Amount EUR 108.073,69
  - Section assets | Account Accounts Receivable | Amount EUR 17.553,23
  - Section liabilities | Account Accounts Payable | Amount EUR 9.044,53
  - Section equity | Account Owner's Equity | Amount EUR 116.582,39

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-21

```
VENDOR INVOICE
==============

From
----
Willow Operations
220 Lake View Road, Bengaluru
Date: 21/04/2025

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2025-26

Terms
-----
Due Date: 11/05/2025

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 11/05/2025
Total: EUR 4.245,99

Bill Lines
----------
Lines:
  - Description Implementation work | Amount EUR 1.175,05
  - Description Support fee | Amount EUR 3.070,94

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-17

```
PATIENT INVOICE
===============

From
----
Willow Operations
220 Lake View Road, Bengaluru
Document Date: 17/08/2025

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D004
Document Type: patient_invoice
Period: FY 2025-26

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Anaya Patel
Payer: CareSure
Service Date: 17/08/2025
Gross Charge: EUR 12.701,31
Patient Due: 2.553,40
Insurer Due: 10.147,91

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D007 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-20

```
PATIENT INVOICE
===============

From
----
Willow Operations
220 Lake View Road, Bengaluru
Date: 20/08/2025

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D007
Document Type: patient_invoice
Period: FY 2025-26

Invoice Summary
---------------
Invoice Number: PTINV-0005
Patient: Marcus Lee
Payer: NorthCover
Service Date: 20/08/2025
Gross Charge: EUR 4.854,21
Patient Due: 1.402,87
Insurer Due: 3.451,34

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D002 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-09-06

```
PATIENT INVOICE
===============

From
----
Willow Operations
220 Lake View Road, Bengaluru
Document Date: 06/09/2025

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D002
Document Type: patient_invoice
Period: FY 2025-26

Invoice Summary
---------------
Invoice Number: PTINV-0001
Patient: Noah Ferreira
Payer: NorthCover
Service Date: 06/09/2025
Gross Charge: EUR 6.780,26
Patient Due: 1.558,11
Insurer Due: 5.222,15

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D006 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-09-07

```
PATIENT INVOICE
===============

From
----
Willow Operations
220 Lake View Road, Bengaluru
Document Date: 07/09/2025

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D006
Document Type: patient_invoice
Period: FY 2025-26

Invoice Summary
---------------
Invoice Number: PTINV-0004
Patient: Ella Santos
Payer: Harbor Health Network
Service Date: 07/09/2025
Gross Charge: EUR 3.817,67
Patient Due: 1.079,64
Insurer Due: 2.738,03

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D008 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-09-07

```
PATIENT INVOICE
===============

From
----
Willow Operations
220 Lake View Road, Bengaluru
Document Date: 07/09/2025

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D008
Document Type: patient_invoice
Period: FY 2025-26

Invoice Summary
---------------
Invoice Number: PTINV-0006
Patient: Noah Ferreira
Payer: Harbor Health Network
Service Date: 07/09/2025
Gross Charge: EUR 4.827,26
Patient Due: 1.398,96
Insurer Due: 3.428,30

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D005 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-25

```
PATIENT INVOICE
===============

From
----
Willow Operations
220 Lake View Road, Bengaluru
Date: 25/11/2025

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D005
Document Type: patient_invoice
Period: FY 2025-26

Invoice Summary
---------------
Invoice Number: PTINV-0003
Patient: Anaya Patel
Payer: NorthCover
Service Date: 25/11/2025
Gross Charge: EUR 9.484,77
Patient Due: 2.247,25
Insurer Due: 7.237,52

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D009 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
MEMO
====

From
----
Willow Operations
220 Lake View Road, Bengaluru
Date: 31/03/2026

Reference Box
-------------
Document ID: D009
Document Type: memo
Period: FY 2025-26

Approval / Context
------------------
Subject: Annual leave policy reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Annual leave policy reminder
Audience: Operations Team

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D010 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
MEMO
====

From
----
Willow Operations
220 Lake View Road, Bengaluru
Date: 31/03/2026

Reference Box
-------------
Document ID: D010
Document Type: memo
Period: FY 2025-26

Approval / Context
------------------
Subject: Annual leave policy reminder

Memo Summary
------------
Memo ID: INFO-0002
Subject: Annual leave policy reminder
Audience: Back Office

Memo Body
---------
Narrative: Please route scanned paperwork to the shared archive after the period binder is 
complete.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D011 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Willow Operations
220 Lake View Road, Bengaluru
Date: 31/03/2026

Reference Box
-------------
Document ID: D011
Document Type: bank_statement
Period: FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0070
Statement Currency: EUR
Opening Balance: EUR 108.073,69
Closing Balance: EUR 108.073,69

Statement Rows
--------------
Rows: None

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D011
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 6,780.26 | D002 | 2025-09-06 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 4,245.99 | D003 | 2025-04-21 | clinic_supplies_bill |
| 3 | Accounts Receivable | Service Revenue | 12,701.31 | D004 | 2025-08-17 | patient_billing |
| 4 | Accounts Receivable | Service Revenue | 9,484.77 | D005 | 2025-11-25 | patient_billing |
| 5 | Accounts Receivable | Service Revenue | 3,817.67 | D006 | 2025-09-07 | patient_billing |
| 6 | Accounts Receivable | Service Revenue | 4,854.21 | D007 | 2025-08-20 | patient_billing |
| 7 | Accounts Receivable | Service Revenue | 4,827.26 | D008 | 2025-09-07 | patient_billing |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 108,073.69
- Accounts Receivable: 60,018.71

**Liabilities**
- Accounts Payable: 13,290.52

**Equity**
- Owner's Equity: 116,582.39
- Retained Earnings: 38,219.49

**Totals:** Assets = 168,092.40; Liabilities = 13,290.52; Equity = 154,801.88
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
