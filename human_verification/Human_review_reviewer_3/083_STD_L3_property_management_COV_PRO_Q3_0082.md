# Verification Packet — COV_PRO_Q3_0082

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 3
- **Period type:** quarter
- **Period label:** Q2 FY 2024-25
- **Period start → end:** 2024-07-01 → 2024-09-30
- **Entity:** Atlas Operations
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 13
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-07-01_

**Assets**
- Cash: 40,734.42
- Accounts Receivable: 12,542.99
- Prepaid Insurance: 1,691.06

**Liabilities**
- Accounts Payable: 4,613.06
- Accrued Expenses: 1,160.51
- Security Deposits Payable: 4,062.16

**Equity**
- Retained Earnings: 15,700.75
- Owner's Equity: 29,431.99


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-07-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/07/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 40.734,42
  - Section assets | Account Accounts Receivable | Amount EUR 12.542,99
  - Section assets | Account Prepaid Insurance | Amount EUR 1.691,06
  - Section liabilities | Account Accounts Payable | Amount EUR 4.613,06
  - Section liabilities | Account Accrued Expenses | Amount EUR 1.160,51
  - Section liabilities | Account Security Deposits Payable | Amount EUR 4.062,16
  - Section equity | Account Retained Earnings | Amount EUR 15.700,75
  - Section equity | Account Owner's Equity | Amount EUR 29.431,99

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D012 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-05

```
VENDOR INVOICE
==============

From
----
Atlas Operations
18 Marina Avenue, Chennai
Date: 05/07/2024

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: vendor_invoice
Period: Q2 FY 2024-25

Terms
-----
Due Date: 17/07/2024

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Maintenance Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0003
Due Date: 17/07/2024
Total: EUR 7.048,90

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount EUR 2.241,78
  - Description Support fee | Amount EUR 4.807,12

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-07-07

```
RENT ROLL
=========

From
----
Atlas Operations
18 Marina Avenue, Chennai
Document Date: 07/07/2024

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: Q2 FY 2024-25

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Cedar Plaza
Period: Q2 FY 2024-25
Total Rent: EUR 10.303,99

Tenant Rows
-----------
Rows:
  - Unit A-101 | Tenant Unit B - Romero | Amount EUR 10.303,99

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D010 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-07-08

```
RENT ROLL
=========

From
----
Atlas Operations
18 Marina Avenue, Chennai
Date: 08/07/2024

Reference Box
-------------
Document ID: D010
Document Type: rent_roll
Period: Q2 FY 2024-25

Rent Roll Summary
-----------------
Roll Number: ROLL-0002
Property: Harbor View Offices
Period: Q2 FY 2024-25
Total Rent: EUR 7.110,43

Tenant Rows
-----------
Rows:
  - Unit D-404 | Tenant Unit D - Khan | Amount EUR 7.110,43

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-17

```
VENDOR INVOICE
==============

From
----
Atlas Operations
18 Marina Avenue, Chennai
Document Date: 17/07/2024

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q2 FY 2024-25

Terms
-----
Due Date: 03/08/2024

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Maintenance Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 03/08/2024
Total: EUR 10.994,67

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount EUR 3.866,82
  - Description Support fee | Amount EUR 7.127,85

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D006 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2024-07-19

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Atlas Operations
18 Marina Avenue, Chennai
Date: 19/07/2024

To
--
Unit A - Ellis

Reference Box
-------------
Document ID: D006
Document Type: security_deposit_notice
Period: Q2 FY 2024-25

Security Deposit
----------------
Notice Number: DEP-0001
Tenant: Unit A - Ellis
Unit: D-404
Amount: EUR 9.775,91
Due Date: 28/07/2024

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D011 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-25

```
VENDOR INVOICE
==============

From
----
Atlas Operations
18 Marina Avenue, Chennai
Date: 25/07/2024

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: vendor_invoice
Period: Q2 FY 2024-25

Terms
-----
Due Date: 14/08/2024

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Maintenance Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 14/08/2024
Total: EUR 14.410,59

Bill Lines
----------
Lines:
  - Description Review pack | Amount EUR 3.739,96
  - Description Support fee | Amount EUR 10.670,63

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D008 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-02

```
UTILITY INVOICE
===============

From
----
Atlas Operations
18 Marina Avenue, Chennai
Document Date: 02/09/2024

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: utilities_statement
Period: Q2 FY 2024-25

Terms
-----
Due Date: 09/09/2024

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: Q2 FY 2024-25
Due Date: 09/09/2024
Total: EUR 846,94

Charges
-------
Charges:
  - Description Electricity | Amount EUR 337,76
  - Description Water | Amount EUR 509,18

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-07

```
PAYMENT ADVICE
==============

From
----
Atlas Operations
18 Marina Avenue, Chennai
Document Date: 07/09/2024

To
--
Golden State Finance

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q2 FY 2024-25
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Golden State Finance
Amount: EUR 10.994,67
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
- **Date:** 2024-09-17

```
PAYMENT ADVICE
==============

From
----
Atlas Operations
18 Marina Avenue, Chennai
Date: 17/09/2024

To
--
Unit B - Romero

Reference Box
-------------
Document ID: D004
Document Type: payment_advice
Period: Q2 FY 2024-25
Reference: ROLL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Unit B - Romero
Amount: EUR 10.303,99
Reference: ROLL-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D009 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `adjustment_doc`
- **Date:** 2024-09-17

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Atlas Operations
18 Marina Avenue, Chennai
Document Date: 17/09/2024

To
--
Unit A - Ellis

Reference Box
-------------
Document ID: D009
Document Type: security_deposit_notice
Period: Q2 FY 2024-25

Security Deposit
----------------
Notice Number: DEPREF-0001
Tenant: Unit A - Ellis
Unit: A-101
Amount: EUR 7.013,21
Due Date: 17/09/2024

Notes
-----
Refund of previously collected security deposit DEP-0001.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-09-18

```
PAYROLL SUMMARY
===============

From
----
Atlas Operations
18 Marina Avenue, Chennai
Date: 18/09/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q2 FY 2024-25
Headcount: 10
Gross Pay: EUR 27.637,36
Employer Tax: 2.794,02
Cash Outflow: EUR 30.431,38

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D013 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-09-30

```
BANK STATEMENT
==============

From
----
Atlas Operations
18 Marina Avenue, Chennai
Date: 30/09/2024

Reference Box
-------------
Document ID: D013
Document Type: bank_statement
Period: Q2 FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0082
Statement Currency: EUR
Opening Balance: EUR 40.734,42
Closing Balance: EUR 12.375,06

Statement Rows
--------------
Rows:
  - Date 19/07/2024 | Description Security deposit DEP-0001 | Amount EUR 9.775,91 | Running 
Balance EUR 50.510,33
  - Date 07/09/2024 | Description Supplier settlement BILL-0001 | Amount EUR -10.994,67 | 
Running Balance EUR 39.515,66
  - Date 17/09/2024 | Description Customer settlement ROLL-0001 | Amount EUR 10.303,99 | 
Running Balance EUR 49.819,65
  - Date 17/09/2024 | Description Security deposit refund DEP-0001 | Amount EUR -7.013,21 | 
Running Balance EUR 42.806,44
  - Date 18/09/2024 | Description Payroll PAYRUN-0001 | Amount EUR -30.431,38 | Running 
Balance EUR 12.375,06

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D013
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Rental Revenue | 10,303.99 | D002 | 2024-07-07 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 10,994.67 | D003 | 2024-07-17 | maintenance_bill |
| 3 | Cash | Accounts Receivable | 10,303.99 | D004, D002 | 2024-09-17 | tenant_payment |
| 4 | Accounts Payable | Cash | 10,994.67 | D005, D003 | 2024-09-07 | vendor_payment |
| 5 | Cash | Security Deposits Payable | 9,775.91 | D006 | 2024-07-19 | security_deposit |
| 6 | Salaries Expense | Cash | 27,637.36 | D007 | 2024-09-18 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 2,794.02 | D007 | 2024-09-18 | payroll_tax |
| 8 | Utilities Expense | Accounts Payable | 846.94 | D008 | 2024-09-02 | utilities_bill |
| 9 | Security Deposits Payable | Cash | 7,013.21 | D009, D006 | 2024-09-17 | security_deposit_refund |
| 10 | Accounts Receivable | Rental Revenue | 7,110.43 | D010 | 2024-07-08 | rent_roll |
| 11 | Maintenance Expense | Accounts Payable | 14,410.59 | D011 | 2024-07-25 | maintenance_bill |
| 12 | Maintenance Expense | Accounts Payable | 7,048.90 | D012 | 2024-07-05 | maintenance_bill |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 12,375.06
- Accounts Receivable: 19,653.42
- Prepaid Insurance: 1,691.06

**Liabilities**
- Accounts Payable: 26,919.49
- Accrued Expenses: 1,160.51
- Security Deposits Payable: 6,824.86

**Equity**
- Retained Earnings: -30,617.31
- Owner's Equity: 29,431.99

**Totals:** Assets = 33,719.54; Liabilities = 34,904.86; Equity = -1,185.32
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
- Notes: Good to use.
