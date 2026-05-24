# Dataset Splits

The repository keeps the original folder names for backward compatibility with
existing results and scripts:

- `coverage/` is the paper's **core evaluation split**. It contains 143 records:
  one record per industry × period type × difficulty cell, plus one forced
  inconsistency packet per negative-control code.
- `main/` is the **large generated split**. It contains 1052 records and is
  intended for training, stress testing, and downstream studies rather than the
  headline paper tables.

Both splits are generated from the same human-authored business scenarios,
document schemas, accounting policies, tax/FX assumptions, distractor templates,
and inconsistency perturbations. Given those fixed rules and a seed, labels are
computed by deterministic ledger replay.
