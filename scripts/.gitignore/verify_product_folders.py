from __future__ import annotations

import csv
import json
import re
import unicodedata
from pathlib import Path


ROOT = Path("/Users/francescorosciano/Desktop/codes/Corgi_Take_Home_Assignment")
CSV_PATH = ROOT / "analysis" / "tech_eo_catalog_merged.csv"
FINAL_DIR = ROOT / "final"


def sanitize_name(name: str) -> str:
    s = unicodedata.normalize("NFKC", name or "")
    s = re.sub(r"[\u2010-\u2015\u2212\uFE58\uFE63\uFF0D]", "-", s)
    s = s.replace("/", " - ").replace("\\", " - ").replace(":", " - ")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def main() -> None:
    # Prefer verifying against CSV if present; otherwise verify all folders in FINAL_DIR.
    rows = []
    if CSV_PATH.exists():
        with CSV_PATH.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                carrier = (row.get("Carrier / MGA") or "").strip()
                program = (row.get("Program/Product name") or "").strip()
                if not carrier or not program:
                    continue
                rows.append((carrier, program))

    folders = []
    if rows:
        for carrier, program in rows:
            s_carrier = sanitize_name(carrier)
            s_program = sanitize_name(program)
            folders.append(FINAL_DIR / f"{s_carrier} - {s_program}")
    else:
        folders = [
            p for p in FINAL_DIR.iterdir() if p.is_dir() and p.name != "pdfs"
        ]

    missing_folders = []
    missing_metadata = []
    summaries = []

    for folder in folders:
        if not folder.exists():
            missing_folders.append(folder.name)
            continue
        meta_path = folder / "metadata.json"
        has_meta = meta_path.exists()
        if not has_meta:
            missing_metadata.append(folder.name)
        pdfs = [p.name for p in folder.glob("*.pdf")]
        # Attempt to load metadata to ensure it's valid JSON if present
        if has_meta:
            try:
                json.loads(meta_path.read_text(encoding="utf-8"))
            except Exception:
                has_meta = False
        summaries.append((folder.name, len(pdfs), has_meta))

    print(f"folder_total={len(folders)}")
    print(f"missing_folders={len(missing_folders)}")
    print(f"missing_metadata={len(missing_metadata)}")
    for name, pdf_count, has_meta in sorted(summaries):
        print(f"{name}\tpdfs={pdf_count}\tmetadata={'yes' if has_meta else 'no'}")


if __name__ == "__main__":
    main()


