"""Disease description lookup for PlantMD predictions."""

import csv
from pathlib import Path

FALLBACK_DESCRIPTION = "No description available for this class yet."


def load_descriptions(path: str | Path) -> dict[str, str]:
    """Parse the label,description CSV (quoted, with a header row) into a lookup dict.

    `path` is required rather than defaulted: once this package is installed
    (e.g. via `pip install .` in the Docker build), its own file location no
    longer has any fixed relationship to the repo's `models/` directory, so
    the caller (app.py) must resolve and pass the correct path itself.
    """
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        return {row["label"]: row["description"] for row in reader}


def format_description(
    top_result: tuple[str, float], descriptions: dict[str, str]
) -> tuple[str, str]:
    """Build a (header, body) pair for the top prediction, falling back gracefully if unknown."""
    label, confidence = top_result
    header = f"{label} : {confidence}%"
    body = descriptions.get(label, FALLBACK_DESCRIPTION)
    return header, body
