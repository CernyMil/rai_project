import json
from pathlib import Path
from typing import List, TypeVar


T = TypeVar("T")

DATA_DIR = Path(__file__).parent.parent.parent / "input_data"

def load_list(filename: str, expected_type: type[T]) -> List[T]:
    """Loads a JSON file and verifies that it contains a list of items of the expected type."""
    path = DATA_DIR / filename
    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError(f"{filename} must contain a JSON list")

    for item in data:
        if not isinstance(item, expected_type):
            raise ValueError(
                f"Invalid item type in {filename}: {item!r}"
            )

    return data
