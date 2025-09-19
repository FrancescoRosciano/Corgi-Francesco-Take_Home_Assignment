from __future__ import annotations

from pathlib import Path


ROOT = Path("/Users/francescorosciano/Desktop/codes/Corgi_Take_Home_Assignment")
FINAL_DIR = ROOT / "final"


def count_json(base: Path) -> int:
    return sum(1 for _ in base.rglob("*.json"))


def main() -> None:
    before = count_json(FINAL_DIR)
    print(f"json_before={before}")
    for p in FINAL_DIR.rglob("*.json"):
        try:
            p.unlink()
            print(f"deleted: {p}")
        except Exception as e:
            print(f"error_deleting: {p} -> {e}")
    after = count_json(FINAL_DIR)
    print(f"json_after={after}")


if __name__ == "__main__":
    main()



