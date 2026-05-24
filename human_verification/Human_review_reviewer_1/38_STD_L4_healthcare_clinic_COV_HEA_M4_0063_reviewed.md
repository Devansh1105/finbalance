# Verification Packet — COV_HEA_M4_0063

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** January 2024
- **Period start → end:** 2024-01-01 → 2024-01-31
- **Entity:** Cedar Software
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 15
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-01-01_

**Assets**
- Cash: 28,586.08
- Accounts Receivable: 7,257.61
- Prepaid Insurance: 2,416.28
- Office Supplies: 787.35
- Equipment: 19,729.25

**Liabilities**
- Accounts Payable: 4,772.05
- Accrued Expenses: 1,086.32
- Loans Payable: 13,344.22

**Equity**
- Retained Earnings: 12,167.60
- Owner's Equity: 27,406.38


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
  - Section assets | Account Cash | Amount $28,586.08
  - Section assets | Account Accounts Receivable | Amount $7,257.61
  - Section assets | Account Prepaid Insurance | Amount $2,416.28
  - Section assets | Account Office Supplies | Amount $787.35
  - Section assets | Account Equipment | Amount $19,729.25
  - Section liabilities | Account Accounts Payable | Amount $4,772.05
  - Section liabilities | Account Accrued Expenses | Amount $1,086.32
  - Section liabilities | Account Loans Payable | Amount $13,344.22
  - Section equity | Account Retained Earnings | Amount $12,167.60
  - Section equity | Account Owner's Equity | Amount $27,406.38

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-01-04

```
VENDOR INVOICE
==============

From
----
Cedar Software
90 Hill Park, Hyderabad
Date: 2024-01-04

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: January 2024

Terms
-----
Due Date: 2024-01-22

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-01-22
Total: $9,977.99

Bill Lines
----------
Lines:
  - Description Review pack | Amount $4,381.34
  - Description Support fee | Amount $5,596.65

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D013 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-01-06

```
VENDOR INVOICE
==============

From
----
Cedar Software
90 Hill Park, Hyderabad
Date: 2024-01-06

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D013
Document Type: vendor_invoice
Period: January 2024

Terms
-----
Due Date: 2024-01-17

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0003
Due Date: 2024-01-17
Total: $6,973.82

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $2,116.55
  - Description Support fee | Amount $4,857.27

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D011 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-01-07

```
VENDOR INVOICE
==============

From
----
Cedar Software
90 Hill Park, Hyderabad
Document Date: 2024-01-07

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: vendor_invoice
Period: January 2024

Terms
-----
Due Date: 2024-01-25

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 2024-01-25
Total: $7,604.40

Bill Lines
----------
Lines:
  - Description Review pack | Amount $3,000.70
  - Description Support fee | Amount $4,603.70

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D014 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-01-07

```
SECONDARY COPY
==============

From
----
Cedar Software
90 Hill Park, Hyderabad
Document Date: 2024-01-07

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D014
Document Type: secondary_copy
Period: January 2024

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0002
Counterparty: Beacon Industrial Supply
Total: $7,604.40
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D008 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-01-12

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Beacon Industrial Supply
Asset Name: Display fixtures
Asset Tag: TAG-0001
Useful Life Months: 48
Total: $65,670.17
Paid Cash: $24,012.07
Financed Amount: $41,658.10
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D007 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-01-16

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: $3,845.64
Draw Amount: $30,383.28
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $34,228.92
Note: Scheduled lender activity for the selected period.
```

### Document D010 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-01-18

```
PATIENT INVOICE
===============

From
----
Cedar Software
90 Hill Park, Hyderabad
Document Date: 2024-01-18

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D010
Document Type: patient_invoice
Period: January 2024

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Marcus Lee
Payer: Unity Health Plan
Service Date: 2024-01-18
Gross Charge: $972.31
Patient Due: 314.66
Insurer Due: 657.65

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D002 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-01-19

```
PATIENT INVOICE
===============

From
----
Cedar Software
90 Hill Park, Hyderabad
Document Date: 2024-01-19

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D002
Document Type: patient_invoice
Period: January 2024

Invoice Summary
---------------
Invoice Number: PTINV-0001
Patient: Anaya Patel
Payer: NorthCover
Service Date: 2024-01-19
Gross Charge: $3,867.58
Patient Due: 1,172.09
Insurer Due: 2,695.49

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D012 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-01-20

```
PATIENT INVOICE
===============

From
----
Cedar Software
90 Hill Park, Hyderabad
Document Date: 2024-01-20

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D012
Document Type: patient_invoice
Period: January 2024

Invoice Summary
---------------
Invoice Number: PTINV-0003
Patient: Anaya Patel
Payer: CareSure
Service Date: 2024-01-20
Gross Charge: $3,388.03
Patient Due: 560.04
Insurer Due: 2,827.99

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D006 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-01-22

```
PAYROLL SUMMARY
===============

From
----
Cedar Software
90 Hill Park, Hyderabad
Date: 2024-01-22

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: January 2024
Headcount: 12
Gross Pay: $13,937.26
Employer Tax: 1,920.72
Cash Outflow: $15,857.98

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D005 — Insurer Remittance

- **Type:** `insurer_remittance`
- **Role:** `posting_doc`
- **Date:** 2024-01-27

```
INSURER REMITTANCE
==================

From
----
Cedar Software
90 Hill Park, Hyderabad
Document Date: 2024-01-27

Reference Box
-------------
Document ID: D005
Document Type: insurer_remittance
Period: January 2024

Remittance Summary
------------------
Remittance Number: REM-0001
Payer: NorthCover
Claim Reference: PTINV-0001
Approved Amount: $2,695.49
Paid Amount: $2,695.49
Payment Date: 2024-01-27

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D004 — Copay Receipt

- **Type:** `copay_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-01-28

```
COPAY RECEIPT
=============

From
----
Cedar Software
90 Hill Park, Hyderabad
Document Date: 2024-01-28

To
--
Anaya Patel
Patient billing contact

Copay Receipt
-------------
Receipt Number: COPAY-0001
Patient: Anaya Patel
Amount: $1,172.09
Reference Invoice: PTINV-0001
Payment Method: Online

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D009 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-01-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: $19,729.25
Useful Life Months: 48
Current Period Charge: $411.03
Accumulated Depreciation: 411.03
```

### Document D015 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-01-31

```
BANK STATEMENT
==============

From
----
Cedar Software
90 Hill Park, Hyderabad
Date: 2024-01-31

Reference Box
-------------
Document ID: D015
Document Type: bank_statement
Period: January 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0063
Statement Currency: USD
Opening Balance: $28,586.08
Closing Balance: $22,966.89

Statement Rows
--------------
Rows:
  - Date 2024-01-12 | Description Asset purchase ASSET-0001 | Amount $-24,012.07 | Running 
Balance $4,574.01
  - Date 2024-01-16 | Description Loan draw LOAN-0001 | Amount $30,383.28 | Running Balance 
$34,957.29
  - Date 2024-01-22 | Description Payroll PAYRUN-0001 | Amount $-15,857.98 | Running Balance
 $19,099.31
  - Date 2024-01-27 | Description Insurer remittance PTINV-0001 | Amount $2,695.49 | Running
 Balance $21,794.80
  - Date 2024-01-28 | Description Copay receipt COPAY-0001 | Amount $1,172.09 | Running 
Balance $22,966.89

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D015
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 3,867.58 | D002 | 2024-01-19 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 9,977.99 | D003 | 2024-01-04 | clinic_supplies_bill |
| 3 | Cash | Accounts Receivable | 1,172.09 | D004, D002 | 2024-01-28 | copay_collection |
| 4 | Cash | Accounts Receivable | 2,695.49 | D005, D002 | 2024-01-27 | insurer_remittance |
| 5 | Salaries Expense | Cash | 13,937.26 | D006 | 2024-01-22 | payroll_gross |
| 6 | Payroll Tax Expense | Cash | 1,920.72 | D006 | 2024-01-22 | payroll_tax |
| 7 | Cash | Loans Payable | 30,383.28 | D007 | 2024-01-16 | loan_draw |
| 8 | Equipment | Cash | 24,012.07 | D008 | 2024-01-12 | equipment_purchase_cash |
| 9 | Equipment | Notes Payable | 41,658.10 | D008 | 2024-01-12 | equipment_purchase_financed |
| 10 | Depreciation Expense | Accumulated Depreciation | 411.03 | D009 | 2024-01-31 | depreciation |
| 11 | Accounts Receivable | Service Revenue | 972.31 | D010 | 2024-01-18 | patient_billing |
| 12 | Office Supplies Expense | Accounts Payable | 7,604.40 | D011 | 2024-01-07 | clinic_supplies_bill |
| 13 | Accounts Receivable | Service Revenue | 3,388.03 | D012 | 2024-01-20 | patient_billing |
| 14 | Office Supplies Expense | Accounts Payable | 6,973.82 | D013 | 2024-01-06 | clinic_supplies_bill |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 22,966.89
- Accounts Receivable: 11,617.95
- Prepaid Insurance: 2,416.28
- Office Supplies: 787.35
- Equipment: 85,399.42
- Accumulated Depreciation: -411.03

**Liabilities**
- Accounts Payable: 29,328.26
- Accrued Expenses: 1,086.32
- Loans Payable: 43,727.50
- Notes Payable: 41,658.10

**Equity**
- Retained Earnings: -20,429.70
- Owner's Equity: 27,406.38

**Totals:** Assets = 122,776.86; Liabilities = 115,800.18; Equity = 6,976.68
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
- [ ] Yes — entries match what I would book
- [x] Mostly — minor account / amount issues (please describe)
- [ ] No — significant errors (missing entries, wrong entries, wrong amounts)
- Notes: Three vendor invoices (D003, D011, D013) have consulting sprint and review pack line items coded to Office Supplies Expense. Not wrong per the document label, but classification is debatable.

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
- [ ] Acceptable as ground truth for benchmark evaluation
- [x] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes: Acceptable with the classification caveat noted.
