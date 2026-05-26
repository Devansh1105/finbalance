# Verification Packet — COV_PRO_Y3_0012

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 3
- **Period type:** year
- **Period label:** FY 2025
- **Period start → end:** 2025-01-01 → 2025-12-31
- **Entity:** Pioneer Clinic
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 24
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 93,854.55
- Accounts Receivable: 10,903.13
- Prepaid Rent: 9,213.01
- Prepaid Insurance: 2,833.63
- Office Supplies: 2,984.19

**Liabilities**
- Accounts Payable: 6,707.67
- Accrued Expenses: 3,091.06
- Unearned Revenue: 7,169.69

**Equity**
- Retained Earnings: 9,642.62
- Owner's Equity: 93,177.47


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
  - Section assets | Account Cash | Amount $93,854.55
  - Section assets | Account Accounts Receivable | Amount $10,903.13
  - Section assets | Account Prepaid Rent | Amount $9,213.01
  - Section assets | Account Prepaid Insurance | Amount $2,833.63
  - Section assets | Account Office Supplies | Amount $2,984.19
  - Section liabilities | Account Accounts Payable | Amount $6,707.67
  - Section liabilities | Account Accrued Expenses | Amount $3,091.06
  - Section liabilities | Account Unearned Revenue | Amount $7,169.69
  - Section equity | Account Retained Earnings | Amount $9,642.62
  - Section equity | Account Owner's Equity | Amount $93,177.47

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2025-01-14

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Prime Utility Desk
Property: Cedar Plaza
Service Start: 2025-01-14
Service End: 2025-04-13
Total: $22,682.46
Monthly Amount: $7,560.82

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-21

```
VENDOR INVOICE
==============

From
----
Pioneer Clinic
75 Market Road, Mumbai
Date: 2025-01-21

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2025

Terms
-----
Due Date: 2025-01-31

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-01-31
Total: $30,766.70

Bill Lines
----------
Lines:
  - Description Implementation work | Amount $9,068.04
  - Description Support fee | Amount $21,698.66

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D013 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-21

```
CUSTOMER INVOICE
================

From
----
Pioneer Clinic
75 Market Road, Mumbai
Document Date: 2025-01-21

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D013
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0003

Terms
-----
Due Date: 2025-02-07

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 2025-02-07
Total: $13,406.85

Line Items
----------
Items:
  - Description Implementation work | Amount $5,797.09
  - Description Milestone 1 work | Amount $7,609.76

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D020 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-01-21

```
SECONDARY COPY
==============

From
----
Pioneer Clinic
75 Market Road, Mumbai
Document Date: 2025-01-21

To
--
Oakline Services

Reference Box
-------------
Document ID: D020
Document Type: secondary_copy
Period: FY 2025

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0001
Counterparty: Oakline Services
Total: $30,766.70
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D022 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-01-21

```
CANCELLATION NOTE
=================

From
----
Pioneer Clinic
75 Market Road, Mumbai
Document Date: 2025-01-21

Reference Box
-------------
Document ID: D022
Document Type: cancellation_note
Period: FY 2025

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0003-OLD
Replacement Reference: INV-0003

Background
----------
Narrative: INV-0003-OLD is withdrawn and must not be posted. Use INV-0003 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D010 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2025-03-20

```
RETAINER AGREEMENT MEMO
=======================

From
----
Pioneer Clinic
75 Market Road, Mumbai
Document Date: 2025-03-20

Reference Box
-------------
Document ID: D010
Document Type: retainer_agreement_memo
Period: FY 2025
Reference: RET-CTR-0001

Approval / Context
------------------
Subject: Retainer engagement

Memo Summary
------------
Memo ID: RET-0001
Subject: Retainer engagement
Reference: RET-CTR-0001
Contract Months: 12
Total Contract Value: $104,191.36

Explanation
-----------
Narrative: Customer Crescent Labs agreed to a service package spanning 12 months.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-20

```
CUSTOMER INVOICE
================

From
----
Pioneer Clinic
75 Market Road, Mumbai
Document Date: 2025-03-20

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0002

Terms
-----
Due Date: 2025-03-30

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-03-30
Total: $104,191.36

Line Items
----------
Items:
  - Description Enterprise License | Amount $33,444.96
  - Description Service coverage under contract | Amount $70,746.40

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D014 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-24

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Pioneer Clinic
75 Market Road, Mumbai
Date: 2025-03-24

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D014
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0004

Terms
-----
Due Date: 2025-04-12

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0004

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 2025-04-12
Total: $27,258.47

Line Items
----------
Items:
  - Description Consulting sprint | Amount $8,873.59
  - Description Milestone 2 work | Amount $18,384.88

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-04

```
CUSTOMER INVOICE
================

From
----
Pioneer Clinic
75 Market Road, Mumbai
Document Date: 2025-04-04

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-04-14

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-04-14
Total: $26,604.78

Line Items
----------
Items:
  - Description Consulting sprint | Amount $7,088.87
  - Description Follow-up support | Amount $19,515.91

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D017 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-08-12

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Pace Office Mart
Total: $402.90
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Office Supplies Expense | Amount $117.44
  - Description Office Supplies follow-up | Amount $285.46
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-08-19

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Pace Office Mart
Total: $1,553.78
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $403.63
  - Description Travel Incidentals | Amount $1,150.15
```

### Document D015 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-19

```
CUSTOMER INVOICE
================

From
----
Pioneer Clinic
75 Market Road, Mumbai
Document Date: 2025-08-19

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D015
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0005

Terms
-----
Due Date: 2025-09-10

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0005

Invoice Details
---------------
Invoice Number: INV-0005
Due Date: 2025-09-10
Total: $15,660.89

Line Items
----------
Items:
  - Description Monthly retainer | Amount $6,777.73
  - Description Milestone 3 work | Amount $8,883.16

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D016 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-10-24

```
PAYMENT ADVICE
==============

From
----
Pioneer Clinic
75 Market Road, Mumbai
Document Date: 2025-10-24

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D016
Document Type: payment_advice
Period: FY 2025
Reference: Multiple invoice allocation

Payment Details
---------------
Advice Number: PAY-0003
Counterparty: Blue Finch Holdings
Amount: $49,460.74
Reference: Multiple invoice allocation
Payment Method: Wire
Payment For: Combined settlement against several invoices

Allocation Details
------------------
Allocations:
  - Reference INV-0003 | Allocated Amount $13,406.85 | Status Closed
  - Reference INV-0004 | Allocated Amount $27,258.47 | Status Closed
  - Reference INV-0005 | Allocated Amount $8,795.42 | Status Partially paid

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-10-25

```
PAYROLL SUMMARY
===============

From
----
Pioneer Clinic
75 Market Road, Mumbai
Date: 2025-10-25

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2025
Headcount: 9
Gross Pay: $29,092.02
Employer Tax: 2,920.87
Cash Outflow: $32,012.89

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-11-06

```
PAYMENT ADVICE
==============

From
----
Pioneer Clinic
75 Market Road, Mumbai
Date: 2025-11-06

To
--
Oakline Services

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: $30,766.70
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-11-20

```
PAYMENT ADVICE
==============

From
----
Pioneer Clinic
75 Market Road, Mumbai
Date: 2025-11-20

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: $26,604.78
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
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
Pioneer Clinic
75 Market Road, Mumbai
Date: 2025-12-31

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: FY 2025
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: $7,560.82

Explanation
-----------
Narrative: One month of rent has expired and should be expensed this period.

Footer
------
Internal document packet copy.
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
Pioneer Clinic
75 Market Road, Mumbai
Date: 2025-12-31

Reference Box
-------------
Document ID: D012
Document Type: revenue_recognition_schedule
Period: FY 2025

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0002
Period: FY 2025
Opening Deferred: $104,191.36
Added Deferred: $0.00
Released This Period: 104,191.36
Ending Deferred: $0.00

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
Pioneer Clinic
75 Market Road, Mumbai
Document Date: 2025-12-31

Reference Box
-------------
Document ID: D018
Document Type: reclassification_memo
Period: FY 2025

Correction Summary
------------------
Memo ID: RECLASS-0001
Original Reference: RCPT-0002
From Account: Office Supplies Expense
To Account: Travel Expense
Amount: $402.90

Explanation
-----------
Narrative: Review of the card packet showed the spend belonged in a different expense 
category.

Notes
-----
Approved during the period-end account review.

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D019 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Pioneer Clinic
75 Market Road, Mumbai
Document Date: 2025-12-31

Reference Box
-------------
Document ID: D019
Document Type: service_period_memo
Period: FY 2025
Reference: FY 2025

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: FY 2025
Recognized Amount: $5,751.95

Explanation
-----------
Narrative: Accrue unpaid utilities expense incurred before period end.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D021 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Pioneer Clinic
75 Market Road, Mumbai
Date: 2025-12-31

Reference Box
-------------
Document ID: D021
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
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D021
```

### Document D023 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Pioneer Clinic
75 Market Road, Mumbai
Date: 2025-12-31

Reference Box
-------------
Document ID: D023
Document Type: memo
Period: FY 2025

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0002
Subject: Quarter-end packet routing note
Audience: All Staff

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D024 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Pioneer Clinic
75 Market Road, Mumbai
Date: 2025-12-31

Reference Box
-------------
Document ID: D024
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0012
Statement Currency: USD
Opening Balance: $93,854.55
Closing Balance: $82,501.34

Statement Rows
--------------
Rows:
  - Date 2025-01-14 | Description Rent prepayment PRE-0001 | Amount $-22,682.46 | Running 
Balance $71,172.09
  - Date 2025-08-12 | Description Pace Office Mart receipt RCPT-0002 | Amount $-402.90 | 
Running Balance $70,769.19
  - Date 2025-08-19 | Description Pace Office Mart receipt RCPT-0001 | Amount $-1,553.78 | 
Running Balance $69,215.41
  - Date 2025-10-24 | Description Combined customer settlement PAY-0003 | Amount $49,460.74 
| Running Balance $118,676.15
  - Date 2025-10-25 | Description Payroll PAYRUN-0001 | Amount $-32,012.89 | Running Balance
 $86,663.26
  - Date 2025-11-06 | Description Supplier settlement BILL-0001 | Amount $-30,766.70 | 
Running Balance $55,896.56
  - Date 2025-11-20 | Description Customer settlement INV-0001 | Amount $26,604.78 | Running
 Balance $82,501.34

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D024
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 26,604.78 | D002 | 2025-04-04 | service_invoice |
| 2 | Office Supplies Expense | Accounts Payable | 30,766.70 | D003 | 2025-01-21 | vendor_bill |
| 3 | Travel Expense | Cash | 1,553.78 | D004 | 2025-08-19 | expense_receipt |
| 4 | Cash | Accounts Receivable | 26,604.78 | D005, D002 | 2025-11-20 | customer_payment |
| 5 | Accounts Payable | Cash | 30,766.70 | D006, D003 | 2025-11-06 | supplier_payment |
| 6 | Salaries Expense | Cash | 29,092.02 | D007 | 2025-10-25 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 2,920.87 | D007 | 2025-10-25 | payroll_tax |
| 8 | Prepaid Rent | Cash | 22,682.46 | D008 | 2025-01-14 | prepaid_rent_purchase |
| 9 | Rent Expense | Prepaid Rent | 7,560.82 | D008, D009 | 2025-12-31 | prepaid_rent_release |
| 10 | Accounts Receivable | Unearned Revenue | 104,191.36 | D010, D011 | 2025-03-20 | retainer_invoice |
| 11 | Unearned Revenue | Service Revenue | 104,191.36 | D012, D011 | 2025-12-31 | retainer_release |
| 12 | Accounts Receivable | Service Revenue | 13,406.85 | D013 | 2025-01-21 | multi_invoice_payment_invoice_1 |
| 13 | Accounts Receivable | Service Revenue | 27,258.47 | D014 | 2025-03-24 | multi_invoice_payment_invoice_2 |
| 14 | Accounts Receivable | Service Revenue | 15,660.89 | D015 | 2025-08-19 | multi_invoice_payment_invoice_3 |
| 15 | Cash | Accounts Receivable | 13,406.85 | D016, D013 | 2025-10-24 | multi_invoice_payment_INV-0003 |
| 16 | Cash | Accounts Receivable | 27,258.47 | D016, D014 | 2025-10-24 | multi_invoice_payment_INV-0004 |
| 17 | Cash | Accounts Receivable | 8,795.42 | D016, D015 | 2025-10-24 | multi_invoice_payment_INV-0005 |
| 18 | Office Supplies Expense | Cash | 402.90 | D017 | 2025-08-12 | reclassification_correction_original |
| 19 | Travel Expense | Office Supplies Expense | 402.90 | D018, D017 | 2025-12-31 | reclassification_correction_correction |
| 20 | Utilities Expense | Accrued Expenses | 5,751.95 | D019 | 2025-12-31 | expense_accrual |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 82,501.34
- Accounts Receivable: 121,959.96
- Prepaid Rent: 24,334.65
- Prepaid Insurance: 2,833.63
- Office Supplies: 2,984.19

**Liabilities**
- Accounts Payable: 6,707.67
- Accrued Expenses: 8,843.01
- Unearned Revenue: 7,169.69

**Equity**
- Retained Earnings: 118,715.93
- Owner's Equity: 93,177.47

**Totals:** Assets = 234,613.77; Liabilities = 22,720.37; Equity = 211,893.40
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
- Notes: Looks fine for benchmark use.
