"""Create product folders from CSV, copy PDFs, and generate metadata.json.

This script reads analysis/tech_eo_catalog_merged.csv and, for each row,
creates a folder named "[Carrier] - [Product name]" under final/, copies any
matching PDFs from final/pdfs (matching prefix), and writes a metadata.json
file containing pertinent CSV fields and the list of copied PDF filenames.
"""

from __future__ import annotations

import csv
import json
import os
import re
import shutil
import unicodedata
from pathlib import Path
from typing import Any, Dict, List


ROOT: Path = Path(
    "/Users/francescorosciano/Desktop/codes/Corgi_Take_Home_Assignment"
)
CSV_PATH: Path = ROOT / "analysis" / "tech_eo_catalog_merged.csv"
PDF_DIR: Path = ROOT / "final" / "pdfs"
OUT_DIR: Path = ROOT / "final"


def sanitize_name(name: str) -> str:
    """Normalize and sanitize strings for filesystem usage.

    - Normalize to NFKC to fold compatible characters
    - Replace various unicode hyphens with ASCII hyphen
    - Replace slashes and colons with spaced hyphens
    - Collapse whitespace
    """

    if name is None:
        return ""
    s = unicodedata.normalize("NFKC", name)
    # Replace many hyphen-like unicode codepoints with ASCII hyphen
    s = re.sub(r"[\u2010-\u2015\u2212\uFE58\uFE63\uFF0D]", "-", s)
    # Replace slashes and colons with hyphen spacing
    s = s.replace("/", " - ").replace("\\", " - ").replace(":", " - ")
    # Collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s


def load_pdf_filenames(pdf_dir: Path) -> List[str]:
    return sorted(
        [f.name for f in pdf_dir.iterdir() if f.is_file() and f.suffix.lower() == ".pdf"]
    )


def find_matching_pdfs(prefix: str, pdf_filenames: List[str]) -> List[str]:
    """Return PDFs whose filename starts with the given prefix.

    The match is a simple startswith on the filename (not path).
    """

    return [fn for fn in pdf_filenames if fn.startswith(prefix)]


def write_metadata_json(folder_path: Path, data: Dict[str, Any]) -> None:
    with (folder_path / "metadata.json").open("w", encoding="utf-8") as jf:
        json.dump(data, jf, indent=2, ensure_ascii=False)


def main() -> None:
    pdf_files: List[str] = load_pdf_filenames(PDF_DIR)

    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=2):  # start=2 accounts for header line
            carrier = (row.get("Carrier / MGA") or "").strip()
            program = (row.get("Program/Product name") or "").strip()
            if not carrier or not program:
                continue

            s_carrier = sanitize_name(carrier)
            s_program = sanitize_name(program)
            folder_name = f"{s_carrier} - {s_program}"
            folder_path = OUT_DIR / folder_name
            folder_path.mkdir(parents=True, exist_ok=True)

            prefix = f"{s_carrier} - {s_program}"
            matched = find_matching_pdfs(prefix, pdf_files)

            copied: List[str] = []
            for fname in matched:
                src = PDF_DIR / fname
                dst = folder_path / fname
                try:
                    if src.exists():
                        if not dst.exists():
                            shutil.copy2(src, dst)
                        copied.append(fname)
                except Exception:
                    # Skip on error, but continue processing others
                    pass

            metadata: Dict[str, Any] = {
                "carrier": carrier,
                "program": program,
                "paper": row.get("Paper"),
                "states_available": row.get("States available"),
                "form_codes_and_edition": row.get("Form code(s) & edition date"),
                "specimen_pdf_link": row.get("Specimen/wording PDF link"),
                "product_page_link": row.get("Product/coverage page link"),
                "min_max_limit": row.get("Min/Max limit"),
                "target_segments": row.get("Target segments"),
                "notable_features": row.get("Notable features"),
                "last_verified_date": row.get("Last verified date"),
                "pdf_files": copied,
                "source_csv_row": idx,
            }
            write_metadata_json(folder_path, metadata)


if __name__ == "__main__":
    main()



