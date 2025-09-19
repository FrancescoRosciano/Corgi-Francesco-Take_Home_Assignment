from __future__ import annotations

import json
from pathlib import Path
from typing import Tuple


ROOT = Path("/Users/francescorosciano/Desktop/codes/Corgi_Take_Home_Assignment")
FINAL_DIR = ROOT / "final"


def convert_json_to_txt(base_dir: Path) -> Tuple[int, int]:
    created = 0
    errors = 0
    for json_path in base_dir.rglob("*.json"):
        try:
            # Keep same basename, change suffix to .txt
            txt_path = json_path.with_suffix(".txt")
            # Read JSON and pretty-print into text file
            with json_path.open("r", encoding="utf-8") as jf:
                data = json.load(jf)
            with txt_path.open("w", encoding="utf-8") as tf:
                json.dump(data, tf, indent=2, ensure_ascii=False)
            created += 1
        except Exception:
            errors += 1
            continue
    return created, errors


def main() -> None:
    created, errors = convert_json_to_txt(FINAL_DIR)
    print(f"txt_created={created}")
    print(f"errors={errors}")


if __name__ == "__main__":
    main()



