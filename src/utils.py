from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_json_file(path: Path) -> Any:
    """
    Load and parse a JSON file.

    Args:
        path: Path to the JSON file.

    Returns:
        Parsed JSON content.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the JSON is invalid.
        OSError: If the file cannot be read.
    """
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    except FileNotFoundError as err:
        raise FileNotFoundError(
            f"File not found: {err.msg}"
        ) from err

    except json.JSONDecodeError as err:
        raise ValueError(
            f"Invalid JSON in {path}: {err.msg}"
        ) from err

    except OSError as err:
        raise OSError(
            f"Could not read file: {path}"
        ) from err


def write_json_file(path: Path, data: Any) -> None:
    """
    Write data to a JSON file.

    Args:
        path: Destination file path.
        data: Data to serialize.
    """
    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    try:
        with path.open("w", encoding="utf-8") as handle:
            json.dump(
                data,
                handle,
                indent=4,
                ensure_ascii=False
            )

    except OSError as err:
        raise OSError(
            f"Could not write file: {path}"
        ) from err
