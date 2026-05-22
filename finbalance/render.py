"""Simple PDF rendering and OCR-text generation for synthetic documents."""

from __future__ import annotations

import textwrap
from pathlib import Path

from finbalance.schemas import ensure_parent


PAGE_WIDTH = 92
LINES_PER_PAGE = 44


def wrap_lines(lines: list[str], width: int = PAGE_WIDTH) -> list[str]:
    wrapped: list[str] = []
    for line in lines:
        if not line:
            wrapped.append("")
            continue
        wrapped.extend(textwrap.wrap(line, width=width, replace_whitespace=False, drop_whitespace=False) or [""])
    return wrapped


def make_ocr_text(lines: list[str]) -> str:
    wrapped = wrap_lines(lines)
    return "\n".join(wrapped).strip()


def write_text_pdf(path: str | Path, lines: list[str]) -> Path:
    path = ensure_parent(path)
    wrapped = wrap_lines(lines)
    pages = [wrapped[i:i + LINES_PER_PAGE] for i in range(0, len(wrapped), LINES_PER_PAGE)] or [[]]
    pdf_bytes = _build_pdf_bytes(pages)
    Path(path).write_bytes(pdf_bytes)
    return Path(path)


def _escape_pdf_text(line: str) -> str:
    return line.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _build_pdf_bytes(pages: list[list[str]]) -> bytes:
    objects: list[bytes] = []
    page_numbers: list[int] = []
    font_obj = 3
    next_obj = 4

    for page_lines in pages:
        page_obj = next_obj
        content_obj = next_obj + 1
        page_numbers.append(page_obj)
        content = _build_page_stream(page_lines)
        objects.append(
            (
                f"{page_obj} 0 obj\n"
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
                f"/Resources << /Font << /F1 {font_obj} 0 R >> >> /Contents {content_obj} 0 R >>\n"
                f"endobj\n"
            ).encode("ascii")
        )
        objects.append(
            (
                f"{content_obj} 0 obj\n"
                f"<< /Length {len(content)} >>\n"
                f"stream\n"
            ).encode("ascii")
            + content
            + b"\nendstream\nendobj\n"
        )
        next_obj += 2

    kids = " ".join(f"{obj} 0 R" for obj in page_numbers)
    catalog = b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n"
    pages_obj = f"2 0 obj\n<< /Type /Pages /Kids [ {kids} ] /Count {len(page_numbers)} >>\nendobj\n".encode("ascii")
    font = b"3 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n"

    output = bytearray(b"%PDF-1.4\n")
    object_bytes = [catalog, pages_obj, font, *objects]
    offsets = [0]
    for part in object_bytes:
        offsets.append(len(output))
        output.extend(part)

    xref_offset = len(output)
    object_count = len(object_bytes)
    output.extend(f"xref\n0 {object_count + 1}\n".encode("ascii"))
    output.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.extend(
        (
            f"trailer\n<< /Size {object_count + 1} /Root 1 0 R >>\n"
            f"startxref\n{xref_offset}\n%%EOF\n"
        ).encode("ascii")
    )
    return bytes(output)


def _build_page_stream(page_lines: list[str]) -> bytes:
    text_lines = ["BT", "/F1 10 Tf", "50 760 Td", "14 TL"]
    for idx, line in enumerate(page_lines):
        escaped = _escape_pdf_text(line)
        if idx == 0:
            text_lines.append(f"({escaped}) Tj")
        else:
            text_lines.append("T*")
            text_lines.append(f"({escaped}) Tj")
    text_lines.append("ET")
    return "\n".join(text_lines).encode("ascii", errors="ignore")
