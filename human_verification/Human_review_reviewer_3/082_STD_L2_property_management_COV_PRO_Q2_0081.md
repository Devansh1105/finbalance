# Verification Packet — COV_PRO_Q2_0081

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 2
- **Period type:** quarter
- **Period label:** Q1 FY 2025
- **Period start → end:** 2025-01-01 → 2025-03-31
- **Entity:** Beacon Clinic
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 11
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 72,067.44
- Accounts Receivable: 7,903.65
- Prepaid Insurance: 1,580.03

**Liabilities**
- Accounts Payable: 4,604.58
- Accrued Expenses: 1,155.78
- Security Deposits Payable: 6,866.81

**Equity**
- Retained Earnings: 8,243.96
- Owner's Equity: 60,679.99


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
Statement Date: 2025-01-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $72,067.44
  - Section assets | Account Accounts Receivable | Amount $7,903.65
  - Section assets | Account Prepaid Insurance | Amount $1,580.03
  - Section liabilities | Account Accounts Payable | Amount $4,604.58
  - Section liabilities | Account Accrued Expenses | Amount $1,155.78
  - Section liabilities | Account Security Deposits Payable | Amount $6,866.81
  - Section equity | Account Retained Earnings | Amount $8,243.96
  - Section equity | Account Owner's Equity | Amount $60,679.99

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D009 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-01-01

```
RENT ROLL
=========

From
----
Beacon Clinic
14 King Street, Pune
Document Date: 2025-01-01

Reference Box
-------------
Document ID: D009
Document Type: rent_roll
Period: Q1 FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0002
Property: Park Lane Residences
Period: Q1 FY 2025
Total Rent: $12,377.52

Tenant Rows
-----------
Rows:
  - Unit A-101 | Tenant Unit B - Romero | Amount $12,377.52

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-01-06

```
RENT ROLL
=========

From
----
Beacon Clinic
14 King Street, Pune
Document Date: 2025-01-06

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: Q1 FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Cedar Plaza
Period: Q1 FY 2025
Total Rent: $12,316.18

Tenant Rows
-----------
Rows:
  - Unit A-101 | Tenant Unit D - Khan | Amount $12,316.18

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-09

```
VENDOR INVOICE
==============

From
----
Beacon Clinic
14 King Street, Pune
Date: 2025-01-09

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q1 FY 2025

Terms
-----
Due Date: 2025-01-25

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Maintenance Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-01-25
Total: $13,499.14

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount $3,684.60
  - Description Support fee | Amount $9,814.54

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D010 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-01-09

```
SECONDARY COPY
==============

From
----
Beacon Clinic
14 King Street, Pune
Document Date: 2025-01-09

To
--
Oakline Services

Reference Box
-------------
Document ID: D010
Document Type: secondary_copy
Period: Q1 FY 2025

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0001
Counterparty: Oakline Services
Total: $13,499.14
Copy Context: Forwarded copy attached to the customer correspondence bundle.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D006 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-01-15

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Beacon Clinic
14 King Street, Pune
Date: 2025-01-15

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D006
Document Type: security_deposit_notice
Period: Q1 FY 2025

Security Deposit
----------------
Notice Number: DEP-0001
Tenant: Unit D - Khan
Unit: C-303
Amount: $4,264.92
Due Date: 2025-01-18

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D008 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-01-22

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Beacon Clinic
14 King Street, Pune
Document Date: 2025-01-22

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D008
Document Type: security_deposit_notice
Period: Q1 FY 2025

Security Deposit
----------------
Notice Number: DEP-0002
Tenant: Unit D - Khan
Unit: D-404
Amount: $6,501.94
Due Date: 2025-01-30

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-03-03

```
PAYMENT ADVICE
==============

From
----
Beacon Clinic
14 King Street, Pune
Date: 2025-03-03

To
--
Oakline Services

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q1 FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: $13,499.14
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D004 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-03-10

```
PAYMENT ADVICE
==============

From
----
Beacon Clinic
14 King Street, Pune
Document Date: 2025-03-10

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D004
Document Type: payment_advice
Period: Q1 FY 2025
Reference: ROLL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Unit D - Khan
Amount: $12,316.18
Reference: ROLL-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D007 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-22

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Beacon Clinic
14 King Street, Pune
Date: 2025-03-22

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D007
Document Type: security_deposit_notice
Period: Q1 FY 2025

Security Deposit
----------------
Notice Number: DEPREF-0001
Tenant: Unit D - Khan
Unit: D-404
Amount: $3,494.98
Due Date: 2025-03-22

Notes
-----
Refund of previously collected security deposit DEP-0001.

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D011 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Beacon Clinic
14 King Street, Pune
Date: 2025-03-31

Reference Box
-------------
Document ID: D011
Document Type: bank_statement
Period: Q1 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0081
Statement Currency: USD
Opening Balance: $72,067.44
Closing Balance: $78,156.36

Statement Rows
--------------
Rows:
  - Date 2025-01-15 | Description Security deposit DEP-0001 | Amount $4,264.92 | Running 
Balance $76,332.36
  - Date 2025-01-22 | Description Security deposit DEP-0002 | Amount $6,501.94 | Running 
Balance $82,834.30
  - Date 2025-03-03 | Description Supplier settlement BILL-0001 | Amount $-13,499.14 | 
Running Balance $69,335.16
  - Date 2025-03-10 | Description Customer settlement ROLL-0001 | Amount $12,316.18 | 
Running Balance $81,651.34
  - Date 2025-03-22 | Description Security deposit refund DEP-0001 | Amount $-3,494.98 | 
Running Balance $78,156.36

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
| 1 | Accounts Receivable | Rental Revenue | 12,316.18 | D002 | 2025-01-06 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 13,499.14 | D003 | 2025-01-09 | maintenance_bill |
| 3 | Cash | Accounts Receivable | 12,316.18 | D004, D002 | 2025-03-10 | tenant_payment |
| 4 | Accounts Payable | Cash | 13,499.14 | D005, D003 | 2025-03-03 | vendor_payment |
| 5 | Cash | Security Deposits Payable | 4,264.92 | D006 | 2025-01-15 | security_deposit |
| 6 | Security Deposits Payable | Cash | 3,494.98 | D007, D006 | 2025-03-22 | security_deposit_refund |
| 7 | Cash | Security Deposits Payable | 6,501.94 | D008 | 2025-01-22 | security_deposit |
| 8 | Accounts Receivable | Rental Revenue | 12,377.52 | D009 | 2025-01-01 | rent_roll |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 78,156.36
- Accounts Receivable: 20,281.17
- Prepaid Insurance: 1,580.03

**Liabilities**
- Accounts Payable: 4,604.58
- Accrued Expenses: 1,155.78
- Security Deposits Payable: 14,138.69

**Equity**
- Retained Earnings: 19,438.52
- Owner's Equity: 60,679.99

**Totals:** Assets = 100,017.56; Liabilities = 19,899.05; Equity = 80,118.51
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
- Notes: All foots correctly.
