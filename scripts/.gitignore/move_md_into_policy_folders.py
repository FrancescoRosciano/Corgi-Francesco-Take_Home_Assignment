from __future__ import annotations

from pathlib import Path
from typing import List, Tuple
import shutil


ROOT = Path("/Users/francescorosciano/Desktop/codes/Corgi_Take_Home_Assignment")
FINAL_DIR = ROOT / "final"
PDF_DIR = FINAL_DIR / "pdfs"


def move_markdown_files() -> Tuple[int, List[str]]:
    moved_count = 0
    leftovers: List[str] = []
    for md_path in PDF_DIR.glob("*.md"):
        base_name = md_path.stem  # filename without .md
        dest_dir = FINAL_DIR / base_name
        if dest_dir.is_dir():
            dest = dest_dir / md_path.name
            try:
                shutil.move(str(md_path), str(dest))
                moved_count += 1
            except Exception:
                leftovers.append(md_path.name)
        else:
            leftovers.append(md_path.name)
    return moved_count, leftovers


def count_md_in_policy_folders() -> int:
    count = 0
    for child in FINAL_DIR.iterdir():
        if child.is_dir() and child.name != "pdfs":
            count += len(list(child.glob("*.md")))
    return count


def main() -> None:
    moved, leftovers = move_markdown_files()
    in_folders = count_md_in_policy_folders()
    print(f"moved={moved}")
    print(f"in_policy_folders={in_folders}")
    if leftovers:
        print("leftovers_in_pdfs:")
        for name in leftovers:
            print(f"- {name}")


if __name__ == "__main__":
    main()



