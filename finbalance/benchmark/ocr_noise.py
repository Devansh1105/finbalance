"""Deterministic OCR-noise perturbation for the noise-robustness ablation.

Applies graded, seeded corruption to a document's OCR text so that every run
sees the identical perturbation for a given (record, document, rate) triple.
The corruption menu mirrors common OCR engine failure modes:

- character substitutions drawn from a confusion table (0/O, 1/l/I, 5/S, ...)
- character deletions
- token splits (spurious whitespace inside a token)
- token merges (lost whitespace between tokens)

Whole-line dropout is deliberately excluded from the graded sweep: dropping a
line can silently remove the only evidence for a gold posting, which would
confound OCR robustness with unanswerability. Character-level corruption
degrades evidence but leaves it present in the packet.

Noise touches only the OCR text body; document ids, types, and titles stay
clean, matching a pipeline where metadata comes from the file system while
content comes from the OCR engine.
"""

from __future__ import annotations

import random

# Symmetric confusion pairs seen in printed-document OCR output.
_CONFUSIONS = {
    "0": "O",
    "O": "0",
    "1": "l",
    "l": "1",
    "I": "1",
    "5": "S",
    "S": "5",
    "8": "B",
    "B": "8",
    "6": "b",
    "b": "6",
    "2": "Z",
    "Z": "2",
    "g": "9",
    "9": "g",
    "e": "c",
    "c": "e",
    "a": "o",
    "o": "a",
    "u": "v",
    "v": "u",
    "n": "r",
    "r": "n",
    ".": ",",
    ",": ".",
}


def perturb_ocr_text(text: str, *, rate: float, seed_key: str) -> str:
    """Corrupt ``text`` at roughly ``rate`` corruption events per character.

    ``seed_key`` should uniquely identify the (record, document, rate) triple
    so that repeated runs and resumed runs see identical noise.
    """
    if rate <= 0:
        return text
    rng = random.Random(seed_key)
    out_lines: list[str] = []
    for line in text.split("\n"):
        chars: list[str] = []
        for ch in line:
            roll = rng.random()
            if roll >= rate:
                chars.append(ch)
                continue
            event = rng.random()
            if event < 0.55:
                chars.append(_CONFUSIONS.get(ch, ch))
            elif event < 0.75:
                continue  # deletion
            elif event < 0.90:
                if ch != " ":
                    chars.append(ch)
                    chars.append(" ")  # token split
                else:
                    chars.append(ch)
            else:
                if ch == " ":
                    continue  # token merge
                chars.append(ch)
        out_lines.append("".join(chars))
    return "\n".join(out_lines)
