# Verification Packet — COV_PRO_Y2_0086

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 2
- **Period type:** year
- **Period label:** FY 2025
- **Period start → end:** 2025-01-01 → 2025-12-31
- **Entity:** Pioneer Property Services
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 16
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 178,510.34
- Accounts Receivable: 17,962.80
- Prepaid Insurance: 8,008.34

**Liabilities**
- Accounts Payable: 8,068.98
- Accrued Expenses: 1,959.65
- Security Deposits Payable: 7,984.31

**Equity**
- Retained Earnings: 26,064.15
- Owner's Equity: 160,404.39


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
  - Section assets | Account Cash | Amount GBP 178,510.34
  - Section assets | Account Accounts Receivable | Amount GBP 17,962.80
  - Section assets | Account Prepaid Insurance | Amount GBP 8,008.34
  - Section liabilities | Account Accounts Payable | Amount GBP 8,068.98
  - Section liabilities | Account Accrued Expenses | Amount GBP 1,959.65
  - Section liabilities | Account Security Deposits Payable | Amount GBP 7,984.31
  - Section equity | Account Retained Earnings | Amount GBP 26,064.15
  - Section equity | Account Owner's Equity | Amount GBP 160,404.39

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D011 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-01-08

```
RENT ROLL
=========

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Document Date: 08/01/2025

Reference Box
-------------
Document ID: D011
Document Type: rent_roll
Period: FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0004
Property: Cedar Plaza
Period: FY 2025
Total Rent: GBP 15,828.91

Tenant Rows
-----------
Rows:
  - Unit D-404 | Tenant Unit B - Romero | Amount GBP 15,828.91

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-01-11

```
RENT ROLL
=========

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Date: 11/01/2025

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Harbor View Offices
Period: FY 2025
Total Rent: GBP 22,065.34

Tenant Rows
-----------
Rows:
  - Unit C-303 | Tenant Unit D - Khan | Amount GBP 22,065.34

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D010 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-01-11

```
RENT ROLL
=========

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Date: 11/01/2025

Reference Box
-------------
Document ID: D010
Document Type: rent_roll
Period: FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0003
Property: Harbor View Offices
Period: FY 2025
Total Rent: GBP 26,211.17

Tenant Rows
-----------
Rows:
  - Unit D-404 | Tenant Unit D - Khan | Amount GBP 26,211.17

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D009 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-01-15

```
RENT ROLL
=========

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Document Date: 15/01/2025

Reference Box
-------------
Document ID: D009
Document Type: rent_roll
Period: FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0002
Property: Park Lane Residences
Period: FY 2025
Total Rent: GBP 20,707.56

Tenant Rows
-----------
Rows:
  - Unit D-404 | Tenant Unit A - Ellis | Amount GBP 20,707.56

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D012 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-01-16

```
RENT ROLL
=========

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Date: 16/01/2025

Reference Box
-------------
Document ID: D012
Document Type: rent_roll
Period: FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0005
Property: Park Lane Residences
Period: FY 2025
Total Rent: GBP 13,779.00

Tenant Rows
-----------
Rows:
  - Unit C-303 | Tenant Unit A - Ellis | Amount GBP 13,779.00

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D006 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-02-22

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Document Date: 22/02/2025

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D006
Document Type: security_deposit_notice
Period: FY 2025

Security Deposit
----------------
Notice Number: DEP-0001
Tenant: Unit D - Khan
Unit: D-404
Amount: GBP 19,128.46
Due Date: 02/03/2025

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-27

```
VENDOR INVOICE
==============

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Document Date: 27/02/2025

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2025

Terms
-----
Due Date: 11/03/2025

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Maintenance Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 11/03/2025
Total: GBP 12,140.71

Bill Lines
----------
Lines:
  - Description Support package | Amount GBP 4,972.58
  - Description Support fee | Amount GBP 7,168.13

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D013 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-02-27

```
SECONDARY COPY
==============

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Date: 27/02/2025

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D013
Document Type: secondary_copy
Period: FY 2025

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0001
Counterparty: Beacon Industrial Supply
Total: GBP 12,140.71
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D014 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-02-27

```
SECONDARY COPY
==============

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Date: 27/02/2025

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D014
Document Type: secondary_copy
Period: FY 2025

Copy Summary
------------
Copy ID: COPY-0002
Source Reference: BILL-0001
Counterparty: Beacon Industrial Supply
Total: GBP 12,140.71
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D008 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-03-03

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Date: 03/03/2025

To
--
Unit A - Ellis

Reference Box
-------------
Document ID: D008
Document Type: security_deposit_notice
Period: FY 2025

Security Deposit
----------------
Notice Number: DEP-0002
Tenant: Unit A - Ellis
Unit: D-404
Amount: GBP 19,747.08
Due Date: 08/03/2025

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D004 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-09-13

```
PAYMENT ADVICE
==============

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Document Date: 13/09/2025

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D004
Document Type: payment_advice
Period: FY 2025
Reference: ROLL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Unit D - Khan
Amount: GBP 22,065.34
Reference: ROLL-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D007 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `adjustment_doc`
- **Date:** 2025-11-16

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Document Date: 16/11/2025

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D007
Document Type: security_deposit_notice
Period: FY 2025

Security Deposit
----------------
Notice Number: DEPREF-0001
Tenant: Unit D - Khan
Unit: D-404
Amount: GBP 17,619.54
Due Date: 16/11/2025

Notes
-----
Refund of previously collected security deposit DEP-0001.

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-11-17

```
PAYMENT ADVICE
==============

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Date: 17/11/2025

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Beacon Industrial Supply
Amount: GBP 12,140.71
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D015 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D015
Document Type: memo
Period: FY 2025

Approval / Context
------------------
Subject: Scanning checklist for back-office staff

Memo Summary
------------
Memo ID: INFO-0001
Subject: Scanning checklist for back-office staff
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
Page marker: D015
```

### Document D016 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Pioneer Property Services
220 Lake View Road, Bengaluru
Date: 31/12/2025

Reference Box
-------------
Document ID: D016
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0086
Statement Currency: GBP
Opening Balance: GBP 178,510.34
Closing Balance: GBP 209,690.97

Statement Rows
--------------
Rows:
  - Date 22/02/2025 | Description Security deposit DEP-0001 | Amount GBP 19,128.46 | Running
 Balance GBP 197,638.80
  - Date 03/03/2025 | Description Security deposit DEP-0002 | Amount GBP 19,747.08 | Running
 Balance GBP 217,385.88
  - Date 13/09/2025 | Description Customer settlement ROLL-0001 | Amount GBP 22,065.34 | 
Running Balance GBP 239,451.22
  - Date 16/11/2025 | Description Security deposit refund DEP-0001 | Amount GBP -17,619.54 |
 Running Balance GBP 221,831.68
  - Date 17/11/2025 | Description Supplier settlement BILL-0001 | Amount GBP -12,140.71 | 
Running Balance GBP 209,690.97

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D016
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Rental Revenue | 22,065.34 | D002 | 2025-01-11 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 12,140.71 | D003 | 2025-02-27 | maintenance_bill |
| 3 | Cash | Accounts Receivable | 22,065.34 | D004, D002 | 2025-09-13 | tenant_payment |
| 4 | Accounts Payable | Cash | 12,140.71 | D005, D003 | 2025-11-17 | vendor_payment |
| 5 | Cash | Security Deposits Payable | 19,128.46 | D006 | 2025-02-22 | security_deposit |
| 6 | Security Deposits Payable | Cash | 17,619.54 | D007, D006 | 2025-11-16 | security_deposit_refund |
| 7 | Cash | Security Deposits Payable | 19,747.08 | D008 | 2025-03-03 | security_deposit |
| 8 | Accounts Receivable | Rental Revenue | 20,707.56 | D009 | 2025-01-15 | rent_roll |
| 9 | Accounts Receivable | Rental Revenue | 26,211.17 | D010 | 2025-01-11 | rent_roll |
| 10 | Accounts Receivable | Rental Revenue | 15,828.91 | D011 | 2025-01-08 | rent_roll |
| 11 | Accounts Receivable | Rental Revenue | 13,779.00 | D012 | 2025-01-16 | rent_roll |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 209,690.97
- Accounts Receivable: 94,489.44
- Prepaid Insurance: 8,008.34

**Liabilities**
- Accounts Payable: 8,068.98
- Accrued Expenses: 1,959.65
- Security Deposits Payable: 29,240.31

**Equity**
- Retained Earnings: 112,515.42
- Owner's Equity: 160,404.39

**Totals:** Assets = 312,188.75; Liabilities = 39,268.94; Equity = 272,919.81
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
- Notes: Entries agree with the support.
