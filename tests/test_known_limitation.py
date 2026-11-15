"""The known 2025-11-26 gap must stay visible instead of being patched."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEY = ["Year", "Month", "Day", "Hour", "Minute"]
MISSING_KEYS = {(2025, 11, 26, 3, 0), (2025, 11, 26, 7, 0)}


def keys(frame) -> set[tuple[int, int, int, int, int]]:
    return {
        tuple(int(value) for value in row)
        for row in frame[KEY].to_numpy()
    }


def hole_keys(holes) -> set[tuple[int, int, int, int, int]]:
    result = set()
    for value in holes["date"]:
        date_part, time_part = value.split("T")
        year, month, day = date_part.split("-")
        hour, minute, _ = time_part.split(":")
        result.add((int(year), int(month), int(day), int(hour), int(minute)))
    return result


def test_check_script_reports_exactly_the_known_failures() -> None:
    result = subprocess.run(
        [sys.executable, "checks/check.py"],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        capture_output=True,
    )

    lines = result.stdout.splitlines()
    assert result.returncode == 1
    assert "OK: result file exists" in lines
    assert "OK: all rows have 03:00 or 07:00" in lines
    assert lines.count("FAIL: 2 hole times missing in GEC") == 1


def test_the_missing_moments_are_the_two_slots_of_2025_11_26(
    hours, holes
) -> None:
    assert hole_keys(holes) - keys(hours) == MISSING_KEYS
