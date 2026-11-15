"""Tests for load_hole_times() from src/build_specific_gec.py."""

from __future__ import annotations

import pandas as pd
import pytest

CANONICAL_ROWS = [
    ("2025-01-01T03:00:00", "I", 3000, 0.36975887972001364),
    ("2025-01-01T07:00:00", "I", 3000, 0.33914059739624386),
    ("2025-01-02T03:00:00", "I", 3000, 0.3815441482389),
    ("2025-01-02T07:00:00", "I", 3000, 0.3801475615135822),
    ("2025-01-03T03:00:00", "I", 3000, 0.39712194418252633),
]

CANONICAL_SET = {
    (2025, 1, 1, 3, 0),
    (2025, 1, 1, 7, 0),
    (2025, 1, 2, 3, 0),
    (2025, 1, 2, 7, 0),
    (2025, 1, 3, 3, 0),
}


def make_holes(rows: list[tuple[str, str, int, float]]) -> pd.DataFrame:
    return pd.DataFrame(rows, columns=["date", "polariz", "freq", "area_holes"])


def test_method_canonical_case(build_module) -> None:
    """The exact five rows from METHOD.md map to the exact five keys."""
    result = build_module.load_hole_times(make_holes(CANONICAL_ROWS))
    assert result == CANONICAL_SET


def test_method_mutation_breaks_the_test(build_module) -> None:
    """METHOD requires that changing 03:00 to 03:30 makes the test fail."""
    rows = list(CANONICAL_ROWS)
    rows[0] = ("2025-01-01T03:30:00", "I", 3000, 0.36975887972001364)

    result = build_module.load_hole_times(make_holes(rows))

    assert result != CANONICAL_SET
    assert (2025, 1, 1, 3, 30) in result
    assert (2025, 1, 1, 3, 0) not in result


def test_seconds_are_ignored(build_module) -> None:
    """Only hour and minute form the key, so seconds do not change it."""
    rows = [
        ("2025-02-03T07:00:59", "I", 3000, 0.1),
        ("2025-02-03T03:00:01", "I", 3000, 0.2),
    ]
    result = build_module.load_hole_times(make_holes(rows))
    assert result == {(2025, 2, 3, 7, 0), (2025, 2, 3, 3, 0)}


def test_duplicate_dates_collapse(build_module) -> None:
    """A set is returned, so repeated moments count once."""
    rows = [
        ("2025-03-04T03:00:00", "I", 3000, 0.1),
        ("2025-03-04T03:00:00", "I", 3000, 0.2),
        ("2025-03-04T07:00:00", "I", 3000, 0.3),
    ]
    result = build_module.load_hole_times(make_holes(rows))
    assert result == {(2025, 3, 4, 3, 0), (2025, 3, 4, 7, 0)}


def test_other_columns_do_not_matter(build_module) -> None:
    """polariz, freq and area_holes are payload, not part of the key."""
    rows = [
        ("2025-04-05T03:00:00", "V", 5000, 0.0),
        ("2025-04-05T07:00:00", "I", 12000, 0.777),
    ]
    result = build_module.load_hole_times(make_holes(rows))
    assert result == {(2025, 4, 5, 3, 0), (2025, 4, 5, 7, 0)}


def test_years_months_and_leading_zeros(build_module) -> None:
    """Dates from different years and months keep their numeric fields."""
    rows = [
        ("2024-12-31T23:59:00", "I", 3000, 0.1),
        ("2025-01-09T00:00:00", "I", 3000, 0.2),
        ("2025-10-10T07:00:00", "I", 3000, 0.3),
    ]
    result = build_module.load_hole_times(make_holes(rows))
    assert result == {
        (2024, 12, 31, 23, 59),
        (2025, 1, 9, 0, 0),
        (2025, 10, 10, 7, 0),
    }


def test_result_is_set_of_five_ints(build_module) -> None:
    """The declared return type is set[tuple[int, int, int, int, int]]."""
    result = build_module.load_hole_times(make_holes(CANONICAL_ROWS))

    assert isinstance(result, set)
    for key in result:
        assert isinstance(key, tuple)
        assert len(key) == 5
        assert all(type(value) is int for value in key)


def test_empty_date_column_gives_empty_set(build_module) -> None:
    """No rows means no keys."""
    holes = pd.DataFrame(
        {
            "date": pd.Series([], dtype="object"),
            "polariz": pd.Series([], dtype="object"),
            "freq": pd.Series([], dtype="object"),
            "area_holes": pd.Series([], dtype="float64"),
        }
    )
    assert build_module.load_hole_times(holes) == set()


def test_malformed_date_raises_value_error(build_module) -> None:
    """A date without the T separator is rejected instead of silently skipped."""
    rows = [("2025-01-01", "I", 3000, 0.1)]
    with pytest.raises(ValueError):
        build_module.load_hole_times(make_holes(rows))
