# Verification Packet — COV_FIE_M5_0019

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 5
- **Period type:** month
- **Period label:** September 2024
- **Period start → end:** 2024-09-01 → 2024-09-30
- **Entity:** Summit Property Services
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 18
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-09-01_

**Assets**
- Cash: 47,390.38
- Accounts Receivable: 4,530.31
- Office Supplies: 896.19
- Vehicles: 12,810.69
- Equipment: 9,239.29

**Liabilities**
- Accounts Payable: 3,065.57
- Accrued Expenses: 893.88
- Notes Payable: 4,738.97

**Equity**
- Retained Earnings: 12,291.84
- Owner's Equity: 53,876.60


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-09-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/09/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 47.390,38
  - Section assets | Account Accounts Receivable | Amount EUR 4.530,31
  - Section assets | Account Office Supplies | Amount EUR 896,19
  - Section assets | Account Vehicles | Amount EUR 12.810,69
  - Section assets | Account Equipment | Amount EUR 9.239,29
  - Section liabilities | Account Accounts Payable | Amount EUR 3.065,57
  - Section liabilities | Account Accrued Expenses | Amount EUR 893,88
  - Section liabilities | Account Notes Payable | Amount EUR 4.738,97
  - Section equity | Account Retained Earnings | Amount EUR 12.291,84
  - Section equity | Account Owner's Equity | Amount EUR 53.876,60

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D014 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-09-01

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0002
Customer: Oak Harbor Foods
Job Site: East Tower
Scope: Consulting sprint
Approved Amount: EUR 9.039,06

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D015 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-02

```
CUSTOMER INVOICE
================

From
----
Summit Property Services
18 Marina Avenue, Chennai
Date: 02/09/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D015
Document Type: customer_invoice
Period: September 2024
Contract Ref: CTR-0002
Job Code: JOB-0002

Terms
-----
Due Date: 25/09/2024

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0002
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 25/09/2024
Subtotal: EUR 9.039,06
Tax Label: Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 745,72
Total: EUR 9.784,78

Line Items
----------
Items:
  - Description Support package | Amount EUR 2.833,88
  - Description Follow-up support | Amount EUR 6.205,18

Field Job
---------
Job Code: JOB-0002

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-09-06

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Crescent Labs
Job Site: East Tower
Scope: Support package
Approved Amount: EUR 14.652,73

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D016 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-06

```
SUPPLIER INVOICE
================

From
----
Summit Property Services
18 Marina Avenue, Chennai
Date: 06/09/2024

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: supplier_invoice
Period: September 2024

Terms
-----
Due Date: 18/09/2024

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Expense Category: Repairs Expense
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 18/09/2024
Subtotal: EUR 3.441,28
Tax Label: Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 283,91
Total: EUR 3.725,19

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 14 | Unit Cost EUR 55,71 | 
Amount EUR 779,90
  - Description Preventive maintenance service parts | Quantity 16 | Unit Cost EUR 166,34 | 
Amount EUR 2.661,38

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-07

```
CUSTOMER INVOICE
================

From
----
Summit Property Services
18 Marina Avenue, Chennai
Date: 07/09/2024

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: September 2024
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 21/09/2024

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 21/09/2024
Subtotal: EUR 14.652,73
Tax Label: Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 1.062,32
Total: EUR 15.715,05

Line Items
----------
Items:
  - Description Review pack | Amount EUR 4.424,06
  - Description Follow-up support | Amount EUR 10.228,67

Field Job
---------
Job Code: JOB-0001

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-07

```
SUPPLIER INVOICE
================

From
----
Summit Property Services
18 Marina Avenue, Chennai
Date: 07/09/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: September 2024

Terms
-----
Due Date: 17/09/2024

Supplier Header
---------------
Supplier: Pace Office Mart
Expense Category: Repairs Expense
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 17/09/2024
Subtotal: EUR 1.019,53
Tax Label: Sales Tax
Tax Rate: 9.50%
Tax Amount: EUR 96,86
Total: EUR 1.116,39

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 29 | Unit Cost EUR 10,42 | 
Amount EUR 302,09
  - Description Preventive maintenance service parts | Quantity 11 | Unit Cost EUR 65,22 | 
Amount EUR 717,44

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D011 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-12

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Pace Office Mart
Asset Name: CNC router
Asset Tag: TAG-0001
Useful Life Months: 60
Total: EUR 67.182,42
Paid Cash: EUR 32.824,75
Financed Amount: EUR 34.357,67
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D017 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-09-12

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Golden State Finance
Total: EUR 447,65
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount EUR 161,87
  - Description Fuel Incidentals | Amount EUR 285,78
```

### Document D010 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-15

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: EUR 2.967,74
Draw Amount: EUR 40.663,58
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 43.631,32
Note: Scheduled lender activity for the selected period.
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-09-17

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Prime Utility Desk
Total: EUR 228,60
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount EUR 52,29
  - Description Fuel Incidentals | Amount EUR 176,31
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-20

```
PAYMENT ADVICE
==============

From
----
Summit Property Services
18 Marina Avenue, Chennai
Date: 20/09/2024

To
--
Crescent Labs

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: September 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Crescent Labs
Amount: EUR 13.005,42
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-09-21

```
PAYROLL SUMMARY
===============

From
----
Summit Property Services
18 Marina Avenue, Chennai
Date: 21/09/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: September 2024
Headcount: 7
Gross Pay: EUR 7.936,44
Employer Tax: 822,23
Cash Outflow: EUR 8.758,67

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D013 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-21

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: EUR 14.641,48
Draw Amount: EUR 0,00
Principal Paid: EUR 14.013,42
Interest Paid: EUR 996,64
Ending Principal: EUR 628,06
Note: Scheduled lender activity for the selected period.
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-26

```
PAYMENT ADVICE
==============

From
----
Summit Property Services
18 Marina Avenue, Chennai
Document Date: 26/09/2024

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: September 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Pace Office Mart
Amount: EUR 748,65
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D009 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-27

```
UTILITY INVOICE
===============

From
----
Summit Property Services
18 Marina Avenue, Chennai
Document Date: 27/09/2024

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: utilities_statement
Period: September 2024

Terms
-----
Due Date: 04/10/2024

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: September 2024
Due Date: 04/10/2024
Total: EUR 2.238,58

Charges
-------
Charges:
  - Description Electricity | Amount EUR 983,18
  - Description Water | Amount EUR 1.255,40

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D012 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-09-30

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: EUR 9.239,29
Useful Life Months: 48
Current Period Charge: EUR 192,49
Accumulated Depreciation: 192,49
```

### Document D018 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-09-30

```
BANK STATEMENT
==============

From
----
Summit Property Services
18 Marina Avenue, Chennai
Date: 30/09/2024

Reference Box
-------------
Document ID: D018
Document Type: bank_statement
Period: September 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0019
Statement Currency: EUR
Opening Balance: EUR 47.390,38
Closing Balance: EUR 43.041,00

Statement Rows
--------------
Rows:
  - Date 12/09/2024 | Description Asset purchase ASSET-0001 | Amount EUR -32.824,75 | 
Running Balance EUR 14.565,63
  - Date 12/09/2024 | Description Golden State Finance receipt RCPT-0002 | Amount EUR 
-447,65 | Running Balance EUR 14.117,98
  - Date 15/09/2024 | Description Loan draw LOAN-0001 | Amount EUR 40.663,58 | Running 
Balance EUR 54.781,56
  - Date 17/09/2024 | Description Prime Utility Desk receipt RCPT-0001 | Amount EUR -228,60 
| Running Balance EUR 54.552,96
  - Date 20/09/2024 | Description Customer settlement INV-0001 | Amount EUR 13.005,42 | 
Running Balance EUR 67.558,38
  - Date 21/09/2024 | Description Loan payment LOAN-0002 | Amount EUR -15.010,06 | Running 
Balance EUR 52.548,32
  - Date 21/09/2024 | Description Payroll PAYRUN-0001 | Amount EUR -8.758,67 | Running 
Balance EUR 43.789,65
  - Date 26/09/2024 | Description Supplier settlement BILL-0001 | Amount EUR -748,65 | 
Running Balance EUR 43.041,00

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D018
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 14,652.73 | D002, D003 | 2024-09-07 | job_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 1,062.32 | D002, D003 | 2024-09-07 | job_invoice_tax |
| 3 | Repairs Expense | Accounts Payable | 1,019.53 | D004 | 2024-09-07 | supplier_bill |
| 4 | Input Tax Receivable | Accounts Payable | 96.86 | D004 | 2024-09-07 | supplier_bill_tax |
| 5 | Fuel Expense | Cash | 228.60 | D005 | 2024-09-17 | fuel_receipt |
| 6 | Cash | Accounts Receivable | 13,005.42 | D006, D003 | 2024-09-20 | customer_payment |
| 7 | Accounts Payable | Cash | 748.65 | D007, D004 | 2024-09-26 | supplier_payment |
| 8 | Salaries Expense | Cash | 7,936.44 | D008 | 2024-09-21 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 822.23 | D008 | 2024-09-21 | payroll_tax |
| 10 | Utilities Expense | Accounts Payable | 2,238.58 | D009 | 2024-09-27 | utilities_bill |
| 11 | Cash | Loans Payable | 40,663.58 | D010 | 2024-09-15 | loan_draw |
| 12 | Equipment | Cash | 32,824.75 | D011 | 2024-09-12 | equipment_purchase_cash |
| 13 | Equipment | Notes Payable | 34,357.67 | D011 | 2024-09-12 | equipment_purchase_financed |
| 14 | Depreciation Expense | Accumulated Depreciation | 192.49 | D012 | 2024-09-30 | depreciation |
| 15 | Loans Payable | Cash | 14,013.42 | D013 | 2024-09-21 | loan_repayment_principal |
| 16 | Interest Expense | Cash | 996.64 | D013 | 2024-09-21 | loan_repayment_interest |
| 17 | Accounts Receivable | Service Revenue | 9,039.06 | D014, D015 | 2024-09-02 | job_invoice |
| 18 | Accounts Receivable | Sales Tax Payable | 745.72 | D014, D015 | 2024-09-02 | job_invoice_tax |
| 19 | Repairs Expense | Accounts Payable | 3,441.28 | D016 | 2024-09-06 | supplier_bill |
| 20 | Input Tax Receivable | Accounts Payable | 283.91 | D016 | 2024-09-06 | supplier_bill_tax |
| 21 | Fuel Expense | Cash | 447.65 | D017 | 2024-09-12 | fuel_receipt |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 43,041.00
- Accounts Receivable: 17,024.72
- Office Supplies: 896.19
- Vehicles: 12,810.69
- Equipment: 76,421.71
- Input Tax Receivable: 380.77
- Accumulated Depreciation: -192.49

**Liabilities**
- Accounts Payable: 9,397.08
- Accrued Expenses: 893.88
- Notes Payable: 39,096.64
- Sales Tax Payable: 1,808.04
- Loans Payable: 26,650.16

**Equity**
- Retained Earnings: 18,660.19
- Owner's Equity: 53,876.60

**Totals:** Assets = 150,382.59; Liabilities = 77,845.80; Equity = 72,536.79
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
- Notes: Reviewed — acceptable.
