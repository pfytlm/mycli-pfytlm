import json
import os
from pathlib import Path


def get_data_path() -> Path:
    home = Path(os.environ.get("MYCLI_DATA_DIR", Path.home() / ".mycli"))
    home.mkdir(parents=True, exist_ok=True)
    return home / "todos.json"


def load_items() -> list[dict]:
    path = get_data_path()
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_items(items: list[dict]) -> None:
    path = get_data_path()
    with path.open("w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
