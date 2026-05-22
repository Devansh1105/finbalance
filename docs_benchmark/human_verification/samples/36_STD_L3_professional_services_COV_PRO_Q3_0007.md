# Verification Packet — COV_PRO_Q3_0007

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 3
- **Period type:** quarter
- **Period label:** Q4 FY 2025
- **Period start → end:** 2025-10-01 → 2025-12-31
- **Entity:** Harbor Property Services
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 20
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-10-01_

**Assets**
- Cash: 24,182.14
- Accounts Receivable: 6,904.39
- Prepaid Rent: 3,260.39
- Prepaid Insurance: 1,837.24
- Office Supplies: 1,364.99

**Liabilities**
- Accounts Payable: 2,495.07
- Accrued Expenses: 799.57
- Unearned Revenue: 2,697.66

**Equity**
- Retained Earnings: 5,747.72
- Owner's Equity: 25,809.13


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
Statement Date: 01/10/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 24.182,14
  - Section assets | Account Accounts Receivable | Amount EUR 6.904,39
  - Section assets | Account Prepaid Rent | Amount EUR 3.260,39
  - Section assets | Account Prepaid Insurance | Amount EUR 1.837,24
  - Section assets | Account Office Supplies | Amount EUR 1.364,99
  - Section liabilities | Account Accounts Payable | Amount EUR 2.495,07
  - Section liabilities | Account Accrued Expenses | Amount EUR 799,57
  - Section liabilities | Account Unearned Revenue | Amount EUR 2.697,66
  - Section equity | Account Retained Earnings | Amount EUR 5.747,72
  - Section equity | Account Owner's Equity | Amount EUR 25.809,13

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2025-10-01

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Prime Utility Desk
Property: Cedar Plaza
Service Start: 01/10/2025
Service End: 31/12/2025
Total: EUR 12.619,46
Monthly Amount: EUR 4.206,49

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D013 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-08

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Date: 08/10/2025

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D013
Document Type: customer_invoice
Period: Q4 FY 2025
Contract Ref: CTR-0003

Terms
-----
Due Date: 24/10/2025

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 24/10/2025
Total: EUR 4.076,41

Line Items
----------
Items:
  - Description Review pack | Amount EUR 1.686,61
  - Description Milestone 1 work | Amount EUR 2.389,80

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D014 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-15

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Date: 15/10/2025

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D014
Document Type: customer_invoice
Period: Q4 FY 2025
Contract Ref: CTR-0004

Terms
-----
Due Date: 04/11/2025

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0004

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 04/11/2025
Total: EUR 9.623,54

Line Items
----------
Items:
  - Description Support package | Amount EUR 2.096,43
  - Description Milestone 2 work | Amount EUR 7.527,11

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D010 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2025-10-18

```
RETAINER AGREEMENT MEMO
=======================

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Document Date: 18/10/2025

Reference Box
-------------
Document ID: D010
Document Type: retainer_agreement_memo
Period: Q4 FY 2025
Reference: RET-CTR-0001

Approval / Context
------------------
Subject: Retainer engagement

Memo Summary
------------
Memo ID: RET-0001
Subject: Retainer engagement
Reference: RET-CTR-0001
Contract Months: 6
Total Contract Value: EUR 72.984,25

Explanation
-----------
Narrative: Customer Crescent Labs agreed to a service package spanning 6 months.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-18

```
CUSTOMER INVOICE
================

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Date: 18/10/2025

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: Q4 FY 2025
Contract Ref: CTR-0002

Terms
-----
Due Date: 28/10/2025

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0002
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 28/10/2025
Subtotal: EUR 66.652,28
Tax Label: Sales Tax
Tax Rate: 9.50%
Tax Amount: EUR 6.331,97
Total: EUR 72.984,25

Line Items
----------
Items:
  - Description Team Support Plan | Amount EUR 18.293,16
  - Description Service coverage under contract | Amount EUR 48.359,12

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-22

```
VENDOR INVOICE
==============

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Date: 22/10/2025

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 04/11/2025

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 04/11/2025
Subtotal: EUR 7.775,17
Tax Label: Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 641,45
Total: EUR 8.416,62

Bill Lines
----------
Lines:
  - Description Implementation work | Amount EUR 2.502,74
  - Description Support fee | Amount EUR 5.272,43

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-26

```
CUSTOMER INVOICE
================

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Document Date: 26/10/2025

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: Q4 FY 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 19/11/2025

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 19/11/2025
Subtotal: EUR 15.692,50
Tax Label: Sales Tax
Tax Rate: 5.00%
Tax Amount: EUR 784,62
Total: EUR 16.477,12

Line Items
----------
Items:
  - Description Support package | Amount EUR 3.947,68
  - Description Follow-up support | Amount EUR 11.744,82

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D019 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-10-26

```
CANCELLATION NOTE
=================

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Date: 26/10/2025

Reference Box
-------------
Document ID: D019
Document Type: cancellation_note
Period: Q4 FY 2025

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
Internal document packet copy.
Page marker: D019
```

### Document D015 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-05

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Date: 05/11/2025

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D015
Document Type: customer_invoice
Period: Q4 FY 2025
Contract Ref: CTR-0005

Terms
-----
Due Date: 18/11/2025

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0005

Invoice Details
---------------
Invoice Number: INV-0005
Due Date: 18/11/2025
Total: EUR 12.422,63

Line Items
----------
Items:
  - Description Review pack | Amount EUR 3.538,08
  - Description Milestone 3 work | Amount EUR 8.884,55

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D017 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-11-10

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Prime Utility Desk
Total: EUR 284,36
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Office Supplies Expense | Amount EUR 64,17
  - Description Office Supplies follow-up | Amount EUR 220,19
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-11-26

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Golden State Finance
Total: EUR 457,89
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount EUR 178,99
  - Description Travel Incidentals | Amount EUR 278,90
```

### Document D016 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-01

```
PAYMENT ADVICE
==============

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Date: 01/12/2025

To
--
Riverfront Group

Reference Box
-------------
Document ID: D016
Document Type: payment_advice
Period: Q4 FY 2025
Reference: Multiple invoice allocation

Payment Details
---------------
Advice Number: PAY-0003
Counterparty: Riverfront Group
Amount: EUR 20.500,28
Reference: Multiple invoice allocation
Payment Method: ACH
Payment For: Combined settlement against several invoices

Allocation Details
------------------
Allocations:
  - Reference INV-0003 | Allocated Amount EUR 4.076,41 | Status Closed
  - Reference INV-0004 | Allocated Amount EUR 9.623,54 | Status Closed
  - Reference INV-0005 | Allocated Amount EUR 6.800,33 | Status Partially paid

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-12-10

```
PAYROLL SUMMARY
===============

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Document Date: 10/12/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q4 FY 2025
Headcount: 4
Gross Pay: EUR 7.213,17
Employer Tax: 977,67
Cash Outflow: EUR 8.190,84

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-18

```
PAYMENT ADVICE
==============

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Date: 18/12/2025

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q4 FY 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Maple Ridge Trading
Amount: EUR 16.477,12
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-18

```
PAYMENT ADVICE
==============

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Date: 18/12/2025

To
--
Golden State Finance

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q4 FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Golden State Finance
Amount: EUR 8.416,62
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: Q4 FY 2025
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: EUR 4.206,49

Explanation
-----------
Narrative: One month of rent has expired and should be expensed this period.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D012 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D012
Document Type: revenue_recognition_schedule
Period: Q4 FY 2025

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0002
Period: Q4 FY 2025
Opening Deferred: EUR 66.652,28
Added Deferred: EUR 0,00
Released This Period: 33.326,14
Ending Deferred: EUR 33.326,14

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D018 — Reclassification Memo

- **Type:** `reclassification_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
RECLASSIFICATION MEMO
=====================

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D018
Document Type: reclassification_memo
Period: Q4 FY 2025

Correction Summary
------------------
Memo ID: RECLASS-0001
Original Reference: RCPT-0002
From Account: Office Supplies Expense
To Account: Travel Expense
Amount: EUR 284,36

Explanation
-----------
Narrative: Review of the card packet showed the spend belonged in a different expense 
category.

Notes
-----
Approved during the period-end account review.

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Harbor Property Services
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: Q4 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0007
Statement Currency: EUR
Opening Balance: EUR 24.182,14
Closing Balance: EUR 31.190,37

Statement Rows
--------------
Rows:
  - Date 01/10/2025 | Description Rent prepayment PRE-0001 | Amount EUR -12.619,46 | Running
 Balance EUR 11.562,68
  - Date 10/11/2025 | Description Prime Utility Desk receipt RCPT-0002 | Amount EUR -284,36 
| Running Balance EUR 11.278,32
  - Date 26/11/2025 | Description Golden State Finance receipt RCPT-0001 | Amount EUR 
-457,89 | Running Balance EUR 10.820,43
  - Date 01/12/2025 | Description Combined customer settlement PAY-0003 | Amount EUR 
20.500,28 | Running Balance EUR 31.320,71
  - Date 10/12/2025 | Description Payroll PAYRUN-0001 | Amount EUR -8.190,84 | Running 
Balance EUR 23.129,87
  - Date 18/12/2025 | Description Customer settlement INV-0001 | Amount EUR 16.477,12 | 
Running Balance EUR 39.606,99
  - Date 18/12/2025 | Description Supplier settlement BILL-0001 | Amount EUR -8.416,62 | 
Running Balance EUR 31.190,37

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D020
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 15,692.50 | D002 | 2025-10-26 | service_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 784.62 | D002 | 2025-10-26 | service_invoice_tax |
| 3 | Office Supplies Expense | Accounts Payable | 7,775.17 | D003 | 2025-10-22 | vendor_bill |
| 4 | Input Tax Receivable | Accounts Payable | 641.45 | D003 | 2025-10-22 | vendor_bill_tax |
| 5 | Travel Expense | Cash | 457.89 | D004 | 2025-11-26 | expense_receipt |
| 6 | Cash | Accounts Receivable | 16,477.12 | D005, D002 | 2025-12-18 | customer_payment |
| 7 | Accounts Payable | Cash | 8,416.62 | D006, D003 | 2025-12-18 | supplier_payment |
| 8 | Salaries Expense | Cash | 7,213.17 | D007 | 2025-12-10 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 977.67 | D007 | 2025-12-10 | payroll_tax |
| 10 | Prepaid Rent | Cash | 12,619.46 | D008 | 2025-10-01 | prepaid_rent_purchase |
| 11 | Rent Expense | Prepaid Rent | 4,206.49 | D008, D009 | 2025-12-31 | prepaid_rent_release |
| 12 | Accounts Receivable | Unearned Revenue | 66,652.28 | D010, D011 | 2025-10-18 | retainer_invoice |
| 13 | Accounts Receivable | Sales Tax Payable | 6,331.97 | D010, D011 | 2025-10-18 | retainer_invoice_tax |
| 14 | Unearned Revenue | Service Revenue | 33,326.14 | D012, D011 | 2025-12-31 | retainer_release |
| 15 | Accounts Receivable | Service Revenue | 4,076.41 | D013 | 2025-10-08 | multi_invoice_payment_invoice_1 |
| 16 | Accounts Receivable | Service Revenue | 9,623.54 | D014 | 2025-10-15 | multi_invoice_payment_invoice_2 |
| 17 | Accounts Receivable | Service Revenue | 12,422.63 | D015 | 2025-11-05 | multi_invoice_payment_invoice_3 |
| 18 | Cash | Accounts Receivable | 4,076.41 | D016, D013 | 2025-12-01 | multi_invoice_payment_INV-0003 |
| 19 | Cash | Accounts Receivable | 9,623.54 | D016, D014 | 2025-12-01 | multi_invoice_payment_INV-0004 |
| 20 | Cash | Accounts Receivable | 6,800.33 | D016, D015 | 2025-12-01 | multi_invoice_payment_INV-0005 |
| 21 | Office Supplies Expense | Cash | 284.36 | D017 | 2025-11-10 | reclassification_correction_original |
| 22 | Travel Expense | Office Supplies Expense | 284.36 | D018, D017 | 2025-12-31 | reclassification_correction_correction |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 31,190.37
- Accounts Receivable: 85,510.94
- Prepaid Rent: 11,673.36
- Prepaid Insurance: 1,837.24
- Office Supplies: 1,364.99
- Input Tax Receivable: 641.45

**Liabilities**
- Accounts Payable: 2,495.07
- Accrued Expenses: 799.57
- Unearned Revenue: 36,023.80
- Sales Tax Payable: 7,116.59

**Equity**
- Retained Earnings: 59,974.19
- Owner's Equity: 25,809.13

**Totals:** Assets = 132,218.35; Liabilities = 46,435.03; Equity = 85,783.32
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
