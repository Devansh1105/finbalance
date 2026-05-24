# FinBalance Dataset License

Unless otherwise stated, the FinBalance generated benchmark data is released
under the Creative Commons Attribution 4.0 International License (CC BY 4.0):

https://creativecommons.org/licenses/by/4.0/

This applies to:

- generated JSON/JSONL benchmark records in `data/`;
- generated OCR text and generated PDF-style document artifacts;
- generated labels, expected journal entries, expected balance sheets, and
  inconsistency labels;
- sample manifests and human-verification packets in `human_verification/`.

CC BY 4.0 permits copying, redistribution, adaptation, and commercial use, as
long as appropriate attribution is given.

## Code License

Source code, scripts, tests, and evaluation/figure-generation utilities are
licensed separately under Apache-2.0. See `LICENSE`.

## Model Outputs and Provider Data

Raw model outputs and non-secret response metadata from the paper runs may be
released as evaluation artifacts for reproducibility. They are not part of the
CC BY 4.0 dataset license above and remain subject to the terms of the
model/API providers used to generate them.

API keys, local API logs, billing-account information, and any provider fields
that cannot be redistributed under provider terms are excluded or redacted.
Evaluation scripts may produce such artifacts locally in `results/`; users are
responsible for complying with the terms of the model/API providers they use.

Aggregate metrics, tables, and figures derived from completed evaluations may
be released with the paper materials, but they do not grant rights to the
underlying provider services.

## Synthetic Content and Third-Party IP

The benchmark uses synthetic company names, synthetic counterparties, generated
document text, and author-created document templates. It does not contain real
customer records, real production accounting documents, PII, or third-party
proprietary document templates.

## Hidden Evaluation Data

The paper does not rely on a hidden evaluation split. If a future hidden
leaderboard split is created, its public release artifacts will use the same
CC BY 4.0 data license unless a release notice states otherwise.
