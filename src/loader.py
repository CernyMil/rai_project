import json
from pathlib import Path
from typing import List, TypeVar
import logging

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING)

T = TypeVar("T")

DATA_DIR = Path(__file__).parent.parent / "input_data"
logger.info(f"Data directory set to: {DATA_DIR}")


def load_list(filename: str, expected_type: type[T]) -> List[T]:
    path = DATA_DIR / filename
    logger.info(f"Loading data from: {path}")
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
