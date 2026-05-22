# Verification Packet — COV_WHO_Y4_0058

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 4
- **Period type:** year
- **Period label:** FY 2025
- **Period start → end:** 2025-01-01 → 2025-12-31
- **Entity:** Willow Retail Group
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 27
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 238,821.42
- Inventory: 171,370.21
- Accounts Receivable: 31,352.50
- Office Supplies: 9,831.77
- Equipment: 49,867.10

**Liabilities**
- Accounts Payable: 52,937.28
- Accrued Expenses: 5,964.29
- Loans Payable: 30,014.64
- Notes Payable: 43,592.82

**Equity**
- Retained Earnings: 77,739.38
- Owner's Equity: 290,994.59


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
  - Section assets | Account Cash | Amount EUR 238.821,42
  - Section assets | Account Inventory | Amount EUR 171.370,21
  - Section assets | Account Accounts Receivable | Amount EUR 31.352,50
  - Section assets | Account Office Supplies | Amount EUR 9.831,77
  - Section assets | Account Equipment | Amount EUR 49.867,10
  - Section liabilities | Account Accounts Payable | Amount EUR 52.937,28
  - Section liabilities | Account Accrued Expenses | Amount EUR 5.964,29
  - Section liabilities | Account Loans Payable | Amount EUR 30.014,64
  - Section liabilities | Account Notes Payable | Amount EUR 43.592,82
  - Section equity | Account Retained Earnings | Amount EUR 77.739,38
  - Section equity | Account Owner's Equity | Amount EUR 290.994,59

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D015 — Tax Regime Notice

- **Type:** `tax_regime_notice`
- **Role:** `support_doc`
- **Date:** 2025-01-26

```
TAX REGIME NOTICE
=================

From
----
Willow Retail Group
75 Market Road, Mumbai
Document Date: 26/01/2025

Reference Box
-------------
Document ID: D015
Document Type: tax_regime_notice
Period: FY 2025

Tax Rule
--------
Notice Number: TAX-0001
Tax Regime: us_sales_tax
Company Jurisdiction: California
Counterparty Jurisdiction: Texas
Tax Rate: 8.25%
Jurisdiction Tax Amount: EUR 9.670,81
Treatment: US purchase sales tax capitalized into inventory cost

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D016 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-26

```
SUPPLIER INVOICE
================

From
----
Willow Retail Group
75 Market Road, Mumbai
Date: 26/01/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: supplier_invoice
Period: FY 2025

Terms
-----
Due Date: 14/02/2025

Supplier Header
---------------
Supplier: Oakline Services
Goods Receipt Ref: GRN-TAX-0001
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: TAXSUP-0001
Due Date: 14/02/2025
Subtotal: EUR 117.221,98
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 9.670,81
Total: EUR 126.892,79

Supplier Bill Lines
-------------------
Lines:
  - Description Widget B | Quantity 1 | Unit Cost EUR 117.221,98 | Amount EUR 117.221,98

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2025-03-08

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Oakline Services
Purchase Ref: PO-0001
Total Quantity: EUR 149,00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Widget A | Quantity 149 | Unit Cost EUR 273,73
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-10

```
SUPPLIER INVOICE
================

From
----
Willow Retail Group
75 Market Road, Mumbai
Date: 10/03/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: FY 2025

Terms
-----
Due Date: 22/03/2025

Supplier Header
---------------
Supplier: Oakline Services
Goods Receipt Ref: GRN-0001
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 22/03/2025
Subtotal: EUR 40.785,77
Tax Label: US Sales Tax
Tax Rate: 6.25%
Tax Amount: EUR 2.549,11
Total: EUR 43.334,88

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 149 | Unit Cost EUR 273,73 | Amount EUR 40.785,77

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D012 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-05-22

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: EUR 52.332,38
Draw Amount: EUR 180.839,53
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 233.171,91
Note: Scheduled lender activity for the selected period.
```

### Document D017 — Tax Exemption Certificate

- **Type:** `tax_exemption_certificate`
- **Role:** `support_doc`
- **Date:** 2025-07-19

```
TAX EXEMPTION CERTIFICATE
=========================

From
----
Willow Retail Group
75 Market Road, Mumbai
Date: 19/07/2025

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D017
Document Type: tax_exemption_certificate
Period: FY 2025

Certificate
-----------
Certificate Number: EXEMPT-0001
Counterparty: Blue Finch Holdings
Tax Regime: us_sales_tax
Effective Date: 01/01/2025
Expiration Date: 31/12/2025
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
- **Date:** 2025-07-19

```
CUSTOMER TAX PROFILE
====================

From
----
Willow Retail Group
75 Market Road, Mumbai
Document Date: 19/07/2025

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D018
Document Type: customer_tax_profile
Period: FY 2025

Tax Profile
-----------
Profile ID: TAXPROF-0001
Customer: Blue Finch Holdings
Customer Jurisdiction: Texas
Company Jurisdiction: California
Same State: False
Exemption Certificate: EXEMPT-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D019 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-19

```
CUSTOMER INVOICE
================

From
----
Willow Retail Group
75 Market Road, Mumbai
Document Date: 19/07/2025

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D019
Document Type: customer_invoice
Period: FY 2025
Shipment Ref: SHP-0002

Terms
-----
Due Date: 06/08/2025

Parties
-------
Customer: Blue Finch Holdings
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 06/08/2025
Subtotal: EUR 165.960,10
Tax Label: US Sales Tax
Tax Rate: 0.00%
Tax Amount: EUR 0,00
Exemption Certificate: EXEMPT-0001
Total: EUR 165.960,10

Line Items
----------
Items:
  - Description Service Bundle | Amount EUR 165.960,10

Shipment Link
-------------
Shipment Ref: SHP-0002

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D023 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-07-19

```
SECONDARY COPY
==============

From
----
Willow Retail Group
75 Market Road, Mumbai
Document Date: 19/07/2025

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D023
Document Type: secondary_copy
Period: FY 2025

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: INV-0002
Counterparty: Blue Finch Holdings
Total: EUR 165.960,10
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D023
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-08-06

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Metro Edge Partners
Shipment Ref: SHP-0001
Billed Amount: EUR 67.169,73
Cost Basis Amount: EUR 34.980,13
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Widget A | Quantity 64 | Unit Price EUR 978,58 | Unit Cost 
EUR 546,56 | Extended Cost EUR 34.980,13
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-06

```
CUSTOMER INVOICE
================

From
----
Willow Retail Group
75 Market Road, Mumbai
Document Date: 06/08/2025

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: FY 2025
Shipment Ref: SHP-0001

Terms
-----
Due Date: 26/08/2025

Parties
-------
Customer: Metro Edge Partners
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 26/08/2025
Subtotal: EUR 62.629,12
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 4.540,61
Total: EUR 67.169,73

Line Items
----------
Items:
  - Description Widget A | Amount EUR 62.629,12

Shipment Link
-------------
Shipment Ref: SHP-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D024 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-08-06

```
SECONDARY COPY
==============

From
----
Willow Retail Group
75 Market Road, Mumbai
Document Date: 06/08/2025

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D024
Document Type: secondary_copy
Period: FY 2025

Copy Summary
------------
Copy ID: COPY-0002
Source Reference: INV-0001
Counterparty: Metro Edge Partners
Total: EUR 67.169,73
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D024
```

### Document D025 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-08-06

```
CANCELLATION NOTE
=================

From
----
Willow Retail Group
75 Market Road, Mumbai
Document Date: 06/08/2025

Reference Box
-------------
Document ID: D025
Document Type: cancellation_note
Period: FY 2025

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
Page marker: D025
```

### Document D026 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-08-06

```
CANCELLATION NOTE
=================

From
----
Willow Retail Group
75 Market Road, Mumbai
Document Date: 06/08/2025

Reference Box
-------------
Document ID: D026
Document Type: cancellation_note
Period: FY 2025

Cancellation Summary
--------------------
Note Number: CNCL-0002
Withdrawn Reference: INV-0001-OLD
Replacement Reference: INV-0001

Background
----------
Narrative: INV-0001-OLD is withdrawn and must not be posted. Use INV-0001 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D026
```

### Document D013 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-16

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Golden State Finance
Asset Name: Display fixtures
Asset Tag: TAG-0001
Useful Life Months: 48
Total: EUR 348.094,13
Paid Cash: EUR 123.250,97
Financed Amount: EUR 224.843,16
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-10-24

```
PAYMENT ADVICE
==============

From
----
Willow Retail Group
75 Market Road, Mumbai
Document Date: 24/10/2025

To
--
Oakline Services

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2025
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: EUR 41.819,99
Reference: SUP-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-11-01

```
PAYMENT ADVICE
==============

From
----
Willow Retail Group
75 Market Road, Mumbai
Date: 01/11/2025

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Metro Edge Partners
Amount: EUR 44.113,81
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D010 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-11-11

```
PAYROLL SUMMARY
===============

From
----
Willow Retail Group
75 Market Road, Mumbai
Document Date: 11/11/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2025
Headcount: 8
Gross Pay: EUR 57.681,07
Employer Tax: 6.657,69
Cash Outflow: EUR 64.338,76

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D011 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-13

```
UTILITY INVOICE
===============

From
----
Willow Retail Group
75 Market Road, Mumbai
Date: 13/11/2025

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: utilities_statement
Period: FY 2025

Terms
-----
Due Date: 26/11/2025

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: FY 2025
Due Date: 26/11/2025
Total: EUR 12.606,09

Charges
-------
Charges:
  - Description Electricity | Amount EUR 4.921,11
  - Description Water | Amount EUR 7.684,98

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0001
Location: Warehouse A

Counted Items
-------------
Items:
  - Sku SKU-0003 | Description Widget B | System Qty 100 | Counted Qty 98 | Unit Cost EUR 
102,67
```

### Document D009 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Willow Retail Group
75 Market Road, Mumbai
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D009
Document Type: inventory_rollforward
Period: FY 2025

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0001
Opening Balance: EUR 3.410,21
Additions: 4.281,21
Usage Or Sales: EUR 2.582,82
Write Down: 205,34
Ending Balance: EUR 4.903,26

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D014 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Willow Retail Group
75 Market Road, Mumbai
Date: 31/12/2025

Reference Box
-------------
Document ID: D014
Document Type: fixed_asset_rollforward
Period: FY 2025

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: EUR 49.867,10
Useful Life: 48
Current Charge: EUR 12.466,80
Accumulated Depreciation: 12.466,80
Opening Balance: EUR 49.867,10
Additions: 0,00
Disposals: 0,00
Ending Balance: EUR 49.867,10

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D020 — AR Aging Summary

- **Type:** `ar_aging_summary`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
AR AGING SUMMARY
================

From
----
Willow Retail Group
75 Market Road, Mumbai
Date: 31/12/2025

Reference Box
-------------
Document ID: D020
Document Type: ar_aging_summary
Period: FY 2025

Aging Summary
-------------
Summary ID: AGING-0001
Period: FY 2025
Total Open: EUR 23.055,92

Customer Lines
--------------
Lines:
  - Customer Metro Edge Partners | Reference INV-0001 | Current EUR 16.448,45 | Past Due 
6.607,47

Notes
-----
Accounts receivable review prepared for collectability assessment.

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D021 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
CREDIT MEMO
===========

From
----
Willow Retail Group
75 Market Road, Mumbai
Date: 31/12/2025

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D021
Document Type: credit_memo
Period: FY 2025
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
Amount: EUR 6.607,47

Footer
------
Internal document packet copy.
Page marker: D021
```

### Document D022 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Willow Retail Group
75 Market Road, Mumbai
Date: 31/12/2025

Reference Box
-------------
Document ID: D022
Document Type: memo
Period: FY 2025

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Document retention reminder
Audience: Back Office

Memo Body
---------
Narrative: Please route scanned paperwork to the shared archive after the period binder is 
complete.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D022
```

### Document D027 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Willow Retail Group
75 Market Road, Mumbai
Date: 31/12/2025

Reference Box
-------------
Document ID: D027
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0058
Statement Currency: EUR
Opening Balance: EUR 238.821,42
Closing Balance: EUR 234.365,04

Statement Rows
--------------
Rows:
  - Date 22/05/2025 | Description Loan draw LOAN-0001 | Amount EUR 180.839,53 | Running 
Balance EUR 419.660,95
  - Date 16/08/2025 | Description Asset purchase ASSET-0001 | Amount EUR -123.250,97 | 
Running Balance EUR 296.409,98
  - Date 24/10/2025 | Description Supplier settlement SUP-0001 | Amount EUR -41.819,99 | 
Running Balance EUR 254.589,99
  - Date 01/11/2025 | Description Customer settlement INV-0001 | Amount EUR 44.113,81 | 
Running Balance EUR 298.703,80
  - Date 11/11/2025 | Description Payroll PAYRUN-0001 | Amount EUR -64.338,76 | Running 
Balance EUR 234.365,04

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D027
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 40,785.77 | D002, D003 | 2025-03-10 | goods_receipt_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 2,549.11 | D002, D003 | 2025-03-10 | goods_receipt_purchase_tax |
| 3 | Accounts Receivable | Sales Revenue | 62,629.12 | D004, D005 | 2025-08-06 | delivery_sale_sale |
| 4 | Cost of Goods Sold | Inventory | 34,980.13 | D004, D005 | 2025-08-06 | delivery_sale_cogs |
| 5 | Accounts Receivable | Sales Tax Payable | 4,540.61 | D004, D005 | 2025-08-06 | delivery_sale_tax |
| 6 | Cash | Accounts Receivable | 44,113.81 | D006, D005 | 2025-11-01 | customer_payment |
| 7 | Accounts Payable | Cash | 41,819.99 | D007, D003 | 2025-10-24 | supplier_payment |
| 8 | Inventory Shrinkage Expense | Inventory | 205.34 | D008, D009 | 2025-12-31 | inventory_adjustment |
| 9 | Salaries Expense | Cash | 57,681.07 | D010 | 2025-11-11 | payroll_gross |
| 10 | Payroll Tax Expense | Cash | 6,657.69 | D010 | 2025-11-11 | payroll_tax |
| 11 | Utilities Expense | Accounts Payable | 12,606.09 | D011 | 2025-11-13 | utilities_bill |
| 12 | Cash | Loans Payable | 180,839.53 | D012 | 2025-05-22 | loan_draw |
| 13 | Equipment | Cash | 123,250.97 | D013 | 2025-08-16 | equipment_purchase_cash |
| 14 | Equipment | Notes Payable | 224,843.16 | D013 | 2025-08-16 | equipment_purchase_financed |
| 15 | Depreciation Expense | Accumulated Depreciation | 12,466.80 | D014 | 2025-12-31 | depreciation |
| 16 | Inventory | Accounts Payable | 126,892.79 | D015, D016 | 2025-01-26 | jurisdictional_tax_invoice_us_purchase_cost_includes_tax |
| 17 | Accounts Receivable | Sales Revenue | 165,960.10 | D017, D018, D019 | 2025-07-19 | jurisdictional_tax_invoice_exempt_sale |
| 18 | Bad Debt Expense | Accounts Receivable | 6,607.47 | D020, D021, D005 | 2025-12-31 | bad_debt_review |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 234,365.04
- Inventory: 303,863.30
- Accounts Receivable: 213,761.05
- Office Supplies: 9,831.77
- Equipment: 397,961.23
- Input Tax Receivable: 2,549.11
- Accumulated Depreciation: -12,466.80

**Liabilities**
- Accounts Payable: 193,951.05
- Accrued Expenses: 5,964.29
- Loans Payable: 210,854.17
- Notes Payable: 268,435.98
- Sales Tax Payable: 4,540.61

**Equity**
- Retained Earnings: 175,124.01
- Owner's Equity: 290,994.59

**Totals:** Assets = 1,149,864.70; Liabilities = 683,746.10; Equity = 466,118.60
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
