# Verification Packet — COV_FIE_M4_0018

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** October 2025
- **Period start → end:** 2025-10-01 → 2025-10-31
- **Entity:** Northwind Clinic
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 15
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-10-01_

**Assets**
- Cash: 37,885.39
- Accounts Receivable: 7,580.52
- Office Supplies: 1,603.46
- Vehicles: 7,854.60
- Equipment: 5,828.12

**Liabilities**
- Accounts Payable: 1,831.23
- Accrued Expenses: 900.20
- Notes Payable: 6,749.28

**Equity**
- Retained Earnings: 7,416.53
- Owner's Equity: 43,854.85


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-10-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-10-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $37,885.39
  - Section assets | Account Accounts Receivable | Amount $7,580.52
  - Section assets | Account Office Supplies | Amount $1,603.46
  - Section assets | Account Vehicles | Amount $7,854.60
  - Section assets | Account Equipment | Amount $5,828.12
  - Section liabilities | Account Accounts Payable | Amount $1,831.23
  - Section liabilities | Account Accrued Expenses | Amount $900.20
  - Section liabilities | Account Notes Payable | Amount $6,749.28
  - Section equity | Account Retained Earnings | Amount $7,416.53
  - Section equity | Account Owner's Equity | Amount $43,854.85

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2025-10-02

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Riverfront Group
Job Site: East Tower
Scope: Consulting sprint
Approved Amount: $4,838.85

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-03

```
CUSTOMER INVOICE
================

From
----
Northwind Clinic
220 Lake View Road, Bengaluru
Date: 2025-10-03

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: October 2025
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 2025-10-25

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-10-25
Total: $4,838.85

Line Items
----------
Items:
  - Description Implementation work | Amount $1,629.33
  - Description Follow-up support | Amount $3,209.52

Field Job
---------
Job Code: JOB-0001

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D014 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-10-03

```
CANCELLATION NOTE
=================

From
----
Northwind Clinic
220 Lake View Road, Bengaluru
Document Date: 2025-10-03

Reference Box
-------------
Document ID: D014
Document Type: cancellation_note
Period: October 2025

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0001-OLD
Replacement Reference: INV-0001

Background
----------
Narrative: INV-0001-OLD is withdrawn and must not be posted. Use INV-0001 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D004 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-05

```
SUPPLIER INVOICE
================

From
----
Northwind Clinic
220 Lake View Road, Bengaluru
Document Date: 2025-10-05

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: October 2025

Terms
-----
Due Date: 2025-10-26

Supplier Header
---------------
Supplier: Oakline Services
Expense Category: Repairs Expense
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 2025-10-26
Total: $6,916.95

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 28 | Unit Cost $65.23 | Amount 
$1,826.52
  - Description Preventive maintenance service parts | Quantity 8 | Unit Cost $636.30 | 
Amount $5,090.43

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D013 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-09

```
SUPPLIER INVOICE
================

From
----
Northwind Clinic
220 Lake View Road, Bengaluru
Date: 2025-10-09

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D013
Document Type: supplier_invoice
Period: October 2025

Terms
-----
Due Date: 2025-10-22

Supplier Header
---------------
Supplier: Prime Utility Desk
Expense Category: Repairs Expense
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 2025-10-22
Total: $9,383.44

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 29 | Unit Cost $75.47 | Amount 
$2,188.74
  - Description Preventive maintenance service parts | Quantity 27 | Unit Cost $266.47 | 
Amount $7,194.70

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-10-13

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Golden State Finance
Total: $83.04
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount $23.22
  - Description Fuel Incidentals | Amount $59.82
```

### Document D010 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-10-18

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $10,312.77
Draw Amount: $23,044.55
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $33,357.32
Note: Scheduled lender activity for the selected period.
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-10-21

```
PAYMENT ADVICE
==============

From
----
Northwind Clinic
220 Lake View Road, Bengaluru
Document Date: 2025-10-21

To
--
Oakline Services

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: October 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: $5,816.77
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D011 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-21

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Golden State Finance
Asset Name: Office laptops
Asset Tag: TAG-0001
Useful Life Months: 60
Total: $31,517.87
Paid Cash: $10,657.21
Financed Amount: $20,860.66
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-10-22

```
PAYMENT ADVICE
==============

From
----
Northwind Clinic
220 Lake View Road, Bengaluru
Date: 2025-10-22

To
--
Riverfront Group

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: October 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: $3,460.41
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-10-23

```
PAYROLL SUMMARY
===============

From
----
Northwind Clinic
220 Lake View Road, Bengaluru
Date: 2025-10-23

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: October 2025
Headcount: 9
Gross Pay: $12,503.56
Employer Tax: 1,068.77
Cash Outflow: $13,572.33

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D009 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-10-26

```
UTILITY INVOICE
===============

From
----
Northwind Clinic
220 Lake View Road, Bengaluru
Date: 2025-10-26

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: utilities_statement
Period: October 2025

Terms
-----
Due Date: 2025-11-13

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: October 2025
Due Date: 2025-11-13
Total: $1,213.85

Charges
-------
Charges:
  - Description Electricity | Amount $479.26
  - Description Water | Amount $734.59

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D012 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-10-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: $5,828.12
Useful Life Months: 48
Current Period Charge: $121.42
Accumulated Depreciation: 121.42
```

### Document D015 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-10-31

```
BANK STATEMENT
==============

From
----
Northwind Clinic
220 Lake View Road, Bengaluru
Date: 2025-10-31

Reference Box
-------------
Document ID: D015
Document Type: bank_statement
Period: October 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0018
Statement Currency: USD
Opening Balance: $37,885.39
Closing Balance: $34,261.00

Statement Rows
--------------
Rows:
  - Date 2025-10-13 | Description Golden State Finance receipt RCPT-0001 | Amount $-83.04 | 
Running Balance $37,802.35
  - Date 2025-10-18 | Description Loan draw LOAN-0001 | Amount $23,044.55 | Running Balance 
$60,846.90
  - Date 2025-10-21 | Description Asset purchase ASSET-0001 | Amount $-10,657.21 | Running 
Balance $50,189.69
  - Date 2025-10-21 | Description Supplier settlement BILL-0001 | Amount $-5,816.77 | 
Running Balance $44,372.92
  - Date 2025-10-22 | Description Customer settlement INV-0001 | Amount $3,460.41 | Running 
Balance $47,833.33
  - Date 2025-10-23 | Description Payroll PAYRUN-0001 | Amount $-13,572.33 | Running Balance
 $34,261.00

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
| 1 | Accounts Receivable | Service Revenue | 4,838.85 | D002, D003 | 2025-10-03 | job_invoice |
| 2 | Repairs Expense | Accounts Payable | 6,916.95 | D004 | 2025-10-05 | supplier_bill |
| 3 | Fuel Expense | Cash | 83.04 | D005 | 2025-10-13 | fuel_receipt |
| 4 | Cash | Accounts Receivable | 3,460.41 | D006, D003 | 2025-10-22 | customer_payment |
| 5 | Accounts Payable | Cash | 5,816.77 | D007, D004 | 2025-10-21 | supplier_payment |
| 6 | Salaries Expense | Cash | 12,503.56 | D008 | 2025-10-23 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 1,068.77 | D008 | 2025-10-23 | payroll_tax |
| 8 | Utilities Expense | Accounts Payable | 1,213.85 | D009 | 2025-10-26 | utilities_bill |
| 9 | Cash | Loans Payable | 23,044.55 | D010 | 2025-10-18 | loan_draw |
| 10 | Equipment | Cash | 10,657.21 | D011 | 2025-10-21 | equipment_purchase_cash |
| 11 | Equipment | Notes Payable | 20,860.66 | D011 | 2025-10-21 | equipment_purchase_financed |
| 12 | Depreciation Expense | Accumulated Depreciation | 121.42 | D012 | 2025-10-31 | depreciation |
| 13 | Repairs Expense | Accounts Payable | 9,383.44 | D013 | 2025-10-09 | supplier_bill |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 34,261.00
- Accounts Receivable: 8,958.96
- Office Supplies: 1,603.46
- Vehicles: 7,854.60
- Equipment: 37,345.99
- Accumulated Depreciation: -121.42

**Liabilities**
- Accounts Payable: 13,528.70
- Accrued Expenses: 900.20
- Notes Payable: 27,609.94
- Loans Payable: 23,044.55

**Equity**
- Retained Earnings: -19,035.65
- Owner's Equity: 43,854.85

**Totals:** Assets = 89,902.59; Liabilities = 65,083.39; Equity = 24,819.20
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
- Notes: Reviewed, no material concerns.
