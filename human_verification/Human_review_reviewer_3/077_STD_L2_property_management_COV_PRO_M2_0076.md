# Verification Packet — COV_PRO_M2_0076

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 2
- **Period type:** month
- **Period label:** February 2025
- **Period start → end:** 2025-02-01 → 2025-02-28
- **Entity:** Granite Clinic
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 9
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-02-01_

**Assets**
- Cash: 46,802.49
- Accounts Receivable: 4,837.56
- Prepaid Insurance: 2,209.39

**Liabilities**
- Accounts Payable: 3,676.67
- Accrued Expenses: 1,270.96
- Security Deposits Payable: 2,511.33

**Equity**
- Retained Earnings: 8,924.32
- Owner's Equity: 37,466.16


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-02-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/02/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 46.802,49
  - Section assets | Account Accounts Receivable | Amount EUR 4.837,56
  - Section assets | Account Prepaid Insurance | Amount EUR 2.209,39
  - Section liabilities | Account Accounts Payable | Amount EUR 3.676,67
  - Section liabilities | Account Accrued Expenses | Amount EUR 1.270,96
  - Section liabilities | Account Security Deposits Payable | Amount EUR 2.511,33
  - Section equity | Account Retained Earnings | Amount EUR 8.924,32
  - Section equity | Account Owner's Equity | Amount EUR 37.466,16

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D007 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-02-01

```
RENT ROLL
=========

From
----
Granite Clinic
14 King Street, Pune
Date: 01/02/2025

Reference Box
-------------
Document ID: D007
Document Type: rent_roll
Period: February 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0002
Property: Marina Heights
Period: February 2025
Total Rent: EUR 4.125,69

Tenant Rows
-----------
Rows:
  - Unit C-303 | Tenant Unit B - Romero | Amount EUR 4.125,69

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-02-01

```
MEMO
====

From
----
Granite Clinic
14 King Street, Pune
Document Date: 01/02/2025

Reference Box
-------------
Document ID: D008
Document Type: memo
Period: February 2025

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Document retention reminder
Audience: Finance Team

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
Page marker: D008
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-02-02

```
RENT ROLL
=========

From
----
Granite Clinic
14 King Street, Pune
Document Date: 02/02/2025

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: February 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Park Lane Residences
Period: February 2025
Total Rent: EUR 4.702,89

Tenant Rows
-----------
Rows:
  - Unit A-101 | Tenant Unit A - Ellis | Amount EUR 4.702,89

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-04

```
VENDOR INVOICE
==============

From
----
Granite Clinic
14 King Street, Pune
Date: 04/02/2025

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: February 2025

Terms
-----
Due Date: 17/02/2025

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Maintenance Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 17/02/2025
Total: EUR 4.958,20

Bill Lines
----------
Lines:
  - Description Review pack | Amount EUR 1.098,39
  - Description Support fee | Amount EUR 3.859,81

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D006 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-02-08

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Granite Clinic
14 King Street, Pune
Document Date: 08/02/2025

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D006
Document Type: security_deposit_notice
Period: February 2025

Security Deposit
----------------
Notice Number: DEP-0001
Tenant: Unit D - Khan
Unit: A-101
Amount: EUR 1.622,55
Due Date: 12/02/2025

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-02-24

```
PAYMENT ADVICE
==============

From
----
Granite Clinic
14 King Street, Pune
Document Date: 24/02/2025

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: February 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Beacon Industrial Supply
Amount: EUR 4.958,20
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D004 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-02-25

```
PAYMENT ADVICE
==============

From
----
Granite Clinic
14 King Street, Pune
Date: 25/02/2025

To
--
Unit A - Ellis

Reference Box
-------------
Document ID: D004
Document Type: payment_advice
Period: February 2025
Reference: ROLL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Unit A - Ellis
Amount: EUR 4.702,89
Reference: ROLL-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D009 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-02-28

```
BANK STATEMENT
==============

From
----
Granite Clinic
14 King Street, Pune
Date: 28/02/2025

Reference Box
-------------
Document ID: D009
Document Type: bank_statement
Period: February 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0076
Statement Currency: EUR
Opening Balance: EUR 46.802,49
Closing Balance: EUR 48.169,73

Statement Rows
--------------
Rows:
  - Date 08/02/2025 | Description Security deposit DEP-0001 | Amount EUR 1.622,55 | Running 
Balance EUR 48.425,04
  - Date 24/02/2025 | Description Supplier settlement BILL-0001 | Amount EUR -4.958,20 | 
Running Balance EUR 43.466,84
  - Date 25/02/2025 | Description Customer settlement ROLL-0001 | Amount EUR 4.702,89 | 
Running Balance EUR 48.169,73

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D009
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Rental Revenue | 4,702.89 | D002 | 2025-02-02 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 4,958.20 | D003 | 2025-02-04 | maintenance_bill |
| 3 | Cash | Accounts Receivable | 4,702.89 | D004, D002 | 2025-02-25 | tenant_payment |
| 4 | Accounts Payable | Cash | 4,958.20 | D005, D003 | 2025-02-24 | vendor_payment |
| 5 | Cash | Security Deposits Payable | 1,622.55 | D006 | 2025-02-08 | security_deposit |
| 6 | Accounts Receivable | Rental Revenue | 4,125.69 | D007 | 2025-02-01 | rent_roll |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 48,169.73
- Accounts Receivable: 8,963.25
- Prepaid Insurance: 2,209.39

**Liabilities**
- Accounts Payable: 3,676.67
- Accrued Expenses: 1,270.96
- Security Deposits Payable: 4,133.88

**Equity**
- Retained Earnings: 12,794.70
- Owner's Equity: 37,466.16

**Totals:** Assets = 59,342.37; Liabilities = 9,081.51; Equity = 50,260.86
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
- Notes: Checks out.
