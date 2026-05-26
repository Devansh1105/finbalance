# Verification Packet — COV_WHO_Q5_0054

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 5
- **Period type:** quarter
- **Period label:** Q4 FY 2026-27
- **Period start → end:** 2026-01-01 → 2026-03-31
- **Entity:** Summit Builders
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 24
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2026-01-01_

**Assets**
- Cash: 147,277.97
- Inventory: 76,573.41
- Accounts Receivable: 12,607.04
- Office Supplies: 2,473.15
- Equipment: 15,313.40

**Liabilities**
- Accounts Payable: 30,733.00
- Accrued Expenses: 3,755.20
- Loans Payable: 15,050.86
- Notes Payable: 20,548.29

**Equity**
- Retained Earnings: 25,713.96
- Owner's Equity: 158,443.66


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2026-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2026-01-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $147,277.97
  - Section assets | Account Inventory | Amount $76,573.41
  - Section assets | Account Accounts Receivable | Amount $12,607.04
  - Section assets | Account Office Supplies | Amount $2,473.15
  - Section assets | Account Equipment | Amount $15,313.40
  - Section liabilities | Account Accounts Payable | Amount $30,733.00
  - Section liabilities | Account Accrued Expenses | Amount $3,755.20
  - Section liabilities | Account Loans Payable | Amount $15,050.86
  - Section liabilities | Account Notes Payable | Amount $20,548.29
  - Section equity | Account Retained Earnings | Amount $25,713.96
  - Section equity | Account Owner's Equity | Amount $158,443.66

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2026-01-06

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Vertex Supply Co.
Purchase Ref: PO-0001
Total Quantity: $96.00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Widget B | Quantity 96 | Unit Cost $117.34
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-01-08

```
SUPPLIER INVOICE
================

From
----
Summit Builders
18 Marina Avenue, Chennai
Date: 2026-01-08

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: Q4 FY 2026-27

Terms
-----
Due Date: 2026-01-23

Supplier Header
---------------
Supplier: Vertex Supply Co.
Goods Receipt Ref: GRN-0001
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 2026-01-23
Total: $11,264.64

Supplier Bill Lines
-------------------
Lines:
  - Description Widget B | Quantity 96 | Unit Cost $117.34 | Amount $11,264.64

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D015 — Tax Regime Notice

- **Type:** `tax_regime_notice`
- **Role:** `support_doc`
- **Date:** 2026-01-14

```
TAX REGIME NOTICE
=================

From
----
Summit Builders
18 Marina Avenue, Chennai
Date: 2026-01-14

Reference Box
-------------
Document ID: D015
Document Type: tax_regime_notice
Period: Q4 FY 2026-27

Tax Rule
--------
Notice Number: TAX-0001
Tax Regime: us_sales_tax
Company Jurisdiction: California
Counterparty Jurisdiction: California
Tax Rate: 7.25%
Jurisdiction Tax Amount: $5,036.40
Treatment: US purchase sales tax capitalized into inventory cost

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D016 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-01-14

```
SUPPLIER INVOICE
================

From
----
Summit Builders
18 Marina Avenue, Chennai
Document Date: 2026-01-14

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: supplier_invoice
Period: Q4 FY 2026-27

Terms
-----
Due Date: 2026-01-31

Supplier Header
---------------
Supplier: Vertex Supply Co.
Goods Receipt Ref: GRN-TAX-0001
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: TAXSUP-0001
Due Date: 2026-01-31
Subtotal: $69,467.52
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: $5,036.40
Total: $74,503.92

Supplier Bill Lines
-------------------
Lines:
  - Description Premium Kit | Quantity 1 | Unit Cost $69,467.52 | Amount $69,467.52

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2026-02-02

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Metro Edge Partners
Shipment Ref: SHP-0001
Billed Amount: $23,569.52
Cost Basis Amount: $16,699.78
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Premium Kit | Quantity 52 | Unit Price $453.26 | Unit Cost 
$321.15 | Extended Cost $16,699.78
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-02-02

```
CUSTOMER INVOICE
================

From
----
Summit Builders
18 Marina Avenue, Chennai
Document Date: 2026-02-02

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: Q4 FY 2026-27
Shipment Ref: SHP-0001

Terms
-----
Due Date: 2026-02-21

Parties
-------
Customer: Metro Edge Partners
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2026-02-21
Total: $23,569.52

Line Items
----------
Items:
  - Description Premium Kit | Amount $23,569.52

Shipment Link
-------------
Shipment Ref: SHP-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D012 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2026-02-10

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $18,788.96
Draw Amount: $222,082.72
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $240,871.68
Note: Scheduled lender activity for the selected period.
```

### Document D013 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-02-18

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Oakline Services
Asset Name: Ultrasound console
Asset Tag: TAG-0001
Useful Life Months: 36
Total: $84,796.88
Paid Cash: $31,417.55
Financed Amount: $53,379.33
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D017 — Tax Exemption Certificate

- **Type:** `tax_exemption_certificate`
- **Role:** `support_doc`
- **Date:** 2026-02-25

```
TAX EXEMPTION CERTIFICATE
=========================

From
----
Summit Builders
18 Marina Avenue, Chennai
Date: 2026-02-25

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D017
Document Type: tax_exemption_certificate
Period: Q4 FY 2026-27

Certificate
-----------
Certificate Number: EXEMPT-0001
Counterparty: Maple Ridge Trading
Tax Regime: us_sales_tax
Effective Date: 2026-01-01
Expiration Date: 2026-03-31
Exemption Status: Valid
Exempt Reason: Resale exemption certificate overrides default invoice tax treatment.

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D018 — Customer Tax Profile

- **Type:** `customer_tax_profile`
- **Role:** `support_doc`
- **Date:** 2026-02-25

```
CUSTOMER TAX PROFILE
====================

From
----
Summit Builders
18 Marina Avenue, Chennai
Document Date: 2026-02-25

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D018
Document Type: customer_tax_profile
Period: Q4 FY 2026-27

Tax Profile
-----------
Profile ID: TAXPROF-0001
Customer: Maple Ridge Trading
Customer Jurisdiction: California
Company Jurisdiction: California
Same State: True
Exemption Certificate: EXEMPT-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D019 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-02-25

```
CUSTOMER INVOICE
================

From
----
Summit Builders
18 Marina Avenue, Chennai
Date: 2026-02-25

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D019
Document Type: customer_invoice
Period: Q4 FY 2026-27
Shipment Ref: SHP-0002

Terms
-----
Due Date: 2026-03-09

Parties
-------
Customer: Maple Ridge Trading
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2026-03-09
Subtotal: $93,581.20
Tax Label: US Sales Tax
Tax Rate: 0.00%
Tax Amount: $0.00
Exemption Certificate: EXEMPT-0001
Total: $93,581.20

Line Items
----------
Items:
  - Description Refill Pack | Amount $93,581.20

Shipment Link
-------------
Shipment Ref: SHP-0002

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D020 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2026-03-03

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Stonebridge Finance
Opening Principal: $33,705.91
Draw Amount: $0.00
Principal Paid: $31,468.47
Interest Paid: $3,330.12
Ending Principal: $2,237.44
Note: Scheduled lender activity for the selected period.
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-03-08

```
PAYMENT ADVICE
==============

From
----
Summit Builders
18 Marina Avenue, Chennai
Date: 2026-03-08

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: Q4 FY 2026-27
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: $10,256.43
Reference: SUP-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-03-10

```
PAYMENT ADVICE
==============

From
----
Summit Builders
18 Marina Avenue, Chennai
Document Date: 2026-03-10

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q4 FY 2026-27
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Metro Edge Partners
Amount: $19,921.77
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D010 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2026-03-22

```
PAYROLL SUMMARY
===============

From
----
Summit Builders
18 Marina Avenue, Chennai
Document Date: 2026-03-22

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q4 FY 2026-27
Headcount: 12
Gross Pay: $54,939.72
Employer Tax: 5,567.72
Cash Outflow: $60,507.44

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D011 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2026-03-22

```
UTILITY INVOICE
===============

From
----
Summit Builders
18 Marina Avenue, Chennai
Date: 2026-03-22

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: utilities_statement
Period: Q4 FY 2026-27

Terms
-----
Due Date: 2026-04-04

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: Q4 FY 2026-27
Due Date: 2026-04-04
Total: $6,233.47

Charges
-------
Charges:
  - Description Electricity | Amount $1,391.77
  - Description Water | Amount $4,841.70

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0001
Location: Front store

Counted Items
-------------
Items:
  - Sku SKU-0003 | Description Premium Kit | System Qty 100 | Counted Qty 89 | Unit Cost 
$38.85
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: $427.35
Reference Sheet: COUNT-0001
```

### Document D014 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: $15,313.40
Useful Life Months: 48
Current Period Charge: $957.09
Accumulated Depreciation: 957.09
```

### Document D021 — AR Aging Summary

- **Type:** `ar_aging_summary`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
AR AGING SUMMARY
================

From
----
Summit Builders
18 Marina Avenue, Chennai
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D021
Document Type: ar_aging_summary
Period: Q4 FY 2026-27

Aging Summary
-------------
Summary ID: AGING-0001
Period: Q4 FY 2026-27
Total Open: $3,647.75

Customer Lines
--------------
Lines:
  - Customer Metro Edge Partners | Reference INV-0001 | Current $1,893.45 | Past Due 
1,754.30

Notes
-----
Accounts receivable review prepared for collectability assessment.

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D022 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
CREDIT MEMO
===========

From
----
Summit Builders
18 Marina Avenue, Chennai
Document Date: 2026-03-31

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D022
Document Type: credit_memo
Period: Q4 FY 2026-27
Reference: INV-0001

Approval / Context
------------------
Reason: Bad debt writeoff approved after aging review

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Metro Edge Partners
Reference: INV-0001
Reason: Bad debt writeoff approved after aging review
Amount: $1,754.30

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D023 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
VENDOR STATEMENT
================

From
----
Summit Builders
18 Marina Avenue, Chennai
Document Date: 2026-03-31

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D023
Document Type: vendor_statement
Period: Q4 FY 2026-27

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Vertex Supply Co.
Closing Balance: $75,512.13

Statement Lines
---------------
Lines:
  - Reference SUP-0001 | Document Type Open invoice | Amount $1,008.21 | Status Outstanding
  - Reference TAXSUP-0001 | Document Type Open invoice | Amount $74,503.92 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D023
```

### Document D024 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Summit Builders
18 Marina Avenue, Chennai
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D024
Document Type: bank_statement
Period: Q4 FY 2026-27

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0054
Statement Currency: USD
Opening Balance: $147,277.97
Closing Balance: $252,302.45

Statement Rows
--------------
Rows:
  - Date 2026-02-10 | Description Loan draw LOAN-0001 | Amount $222,082.72 | Running Balance
 $369,360.69
  - Date 2026-02-18 | Description Asset purchase ASSET-0001 | Amount $-31,417.55 | Running 
Balance $337,943.14
  - Date 2026-03-03 | Description Loan payment LOAN-0002 | Amount $-34,798.59 | Running 
Balance $303,144.55
  - Date 2026-03-08 | Description Supplier settlement SUP-0001 | Amount $-10,256.43 | 
Running Balance $292,888.12
  - Date 2026-03-10 | Description Customer settlement INV-0001 | Amount $19,921.77 | Running
 Balance $312,809.89
  - Date 2026-03-22 | Description Payroll PAYRUN-0001 | Amount $-60,507.44 | Running Balance
 $252,302.45

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D024
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 11,264.64 | D002, D003 | 2026-01-08 | goods_receipt_purchase |
| 2 | Accounts Receivable | Sales Revenue | 23,569.52 | D004, D005 | 2026-02-02 | delivery_sale_sale |
| 3 | Cost of Goods Sold | Inventory | 16,699.78 | D004, D005 | 2026-02-02 | delivery_sale_cogs |
| 4 | Cash | Accounts Receivable | 19,921.77 | D006, D005 | 2026-03-10 | customer_payment |
| 5 | Accounts Payable | Cash | 10,256.43 | D007, D003 | 2026-03-08 | supplier_payment |
| 6 | Inventory Shrinkage Expense | Inventory | 427.35 | D008, D009 | 2026-03-31 | inventory_adjustment |
| 7 | Salaries Expense | Cash | 54,939.72 | D010 | 2026-03-22 | payroll_gross |
| 8 | Payroll Tax Expense | Cash | 5,567.72 | D010 | 2026-03-22 | payroll_tax |
| 9 | Utilities Expense | Accounts Payable | 6,233.47 | D011 | 2026-03-22 | utilities_bill |
| 10 | Cash | Loans Payable | 222,082.72 | D012 | 2026-02-10 | loan_draw |
| 11 | Equipment | Cash | 31,417.55 | D013 | 2026-02-18 | equipment_purchase_cash |
| 12 | Equipment | Notes Payable | 53,379.33 | D013 | 2026-02-18 | equipment_purchase_financed |
| 13 | Depreciation Expense | Accumulated Depreciation | 957.09 | D014 | 2026-03-31 | depreciation |
| 14 | Inventory | Accounts Payable | 74,503.92 | D015, D016 | 2026-01-14 | jurisdictional_tax_invoice_us_purchase_cost_includes_tax |
| 15 | Accounts Receivable | Sales Revenue | 93,581.20 | D017, D018, D019 | 2026-02-25 | jurisdictional_tax_invoice_exempt_sale |
| 16 | Loans Payable | Cash | 31,468.47 | D020 | 2026-03-03 | loan_repayment_principal |
| 17 | Interest Expense | Cash | 3,330.12 | D020 | 2026-03-03 | loan_repayment_interest |
| 18 | Bad Debt Expense | Accounts Receivable | 1,754.30 | D021, D022, D005 | 2026-03-31 | bad_debt_review |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 252,302.45
- Inventory: 145,214.84
- Accounts Receivable: 108,081.69
- Office Supplies: 2,473.15
- Equipment: 100,110.28
- Accumulated Depreciation: -957.09

**Liabilities**
- Accounts Payable: 112,478.60
- Accrued Expenses: 3,755.20
- Loans Payable: 205,665.11
- Notes Payable: 73,927.62

**Equity**
- Retained Earnings: 52,955.13
- Owner's Equity: 158,443.66

**Totals:** Assets = 607,225.32; Liabilities = 395,826.53; Equity = 211,398.79
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
- Notes: Fine as ground truth.
