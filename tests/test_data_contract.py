"""Data-contract tests for the GEC and coronal-hole CSV files."""

from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

KEY = ["Year", "Month", "Day", "Hour", "Minute"]
GEC_COLUMNS = [
    "Year",
    "Month",
    "Day",
    "DOY",
    "Hour",
    "Minute",
    "UnixTimestamp",
    "uqrg",
]
MISSING_KEYS = {(2025, 11, 26, 3, 0), (2025, 11, 26, 7, 0)}


def key_tuples(frame: pd.DataFrame) -> list[tuple[int, int, int, int, int]]:
    return [tuple(int(value) for value in row) for row in frame[KEY].to_numpy()]


def hole_tuples(holes: pd.DataFrame) -> list[tuple[int, int, int, int, int]]:
    result = []
    for value in holes["date"]:
        date_part, time_part = value.split("T")
        year, month, day = date_part.split("-")
        hour, minute, _ = time_part.split(":")
        result.append((int(year), int(month), int(day), int(hour), int(minute)))
    return result


def test_source_columns(source_gec: pd.DataFrame) -> None:
    assert list(source_gec.columns) == GEC_COLUMNS


def test_source_row_count(source_gec: pd.DataFrame) -> None:
    assert len(source_gec) == 34944


def test_source_has_full_15_minute_grid_minus_missing_day(
    source_gec: pd.DataFrame,
) -> None:
    slots = set(range(0, 24 * 60, 15))
    for _, day_group in source_gec.groupby(["Year", "Month", "Day"]):
        minutes = set((day_group["Hour"] * 60 + day_group["Minute"]).tolist())
        assert minutes == slots

    calendar = pd.to_datetime(source_gec[KEY[:3]].rename(columns=str.lower))
    days = set(calendar.dt.date)
    expected = set(pd.date_range("2025-01-01", "2025-12-31").date) - {
        date(2025, 11, 26)
    }
    assert days == expected


def test_source_keys_are_unique_and_timestamps_step_by_15_minutes(
    source_gec: pd.DataFrame,
) -> None:
    assert len(set(key_tuples(source_gec))) == len(source_gec)
    assert source_gec["UnixTimestamp"].is_monotonic_increasing
    assert source_gec["UnixTimestamp"].is_unique
    diffs = set(source_gec["UnixTimestamp"].diff().dropna().astype("int64").tolist())
    assert diffs == {900, 87300}


def test_source_timestamps_match_calendar_fields_in_utc(
    source_gec: pd.DataFrame,
) -> None:
    calendar = pd.to_datetime(source_gec[KEY].rename(columns=str.lower))
    seconds = (calendar - pd.Timestamp("1970-01-01")) // pd.Timedelta(seconds=1)
    assert (seconds.astype("int64") == source_gec["UnixTimestamp"]).all()
    assert (calendar.dt.day_of_year == source_gec["DOY"]).all()


def test_source_uqrg_is_finite_and_positive(source_gec: pd.DataFrame) -> None:
    values = source_gec["uqrg"]
    assert not values.isna().any()
    assert np.isfinite(values).all()
    assert (values > 0).all()
    assert (values < 10).all()


def test_holes_columns_and_row_count(holes: pd.DataFrame) -> None:
    assert list(holes.columns) == ["date", "polariz", "freq", "area_holes"]
    assert len(holes) == 722


def test_holes_polarization_and_frequency_are_constant(holes: pd.DataFrame) -> None:
    assert set(holes["polariz"]) == {"I"}
    assert set(holes["freq"]) == {3000}


def test_holes_area_is_a_dimensionless_ratio(holes: pd.DataFrame) -> None:
    areas = holes["area_holes"]
    assert np.isfinite(areas).all()
    assert (areas >= 0).all()
    assert (areas <= 1).all()


def test_holes_moments_are_only_0300_and_0700(holes: pd.DataFrame) -> None:
    moments = {(key[3], key[4]) for key in hole_tuples(holes)}
    assert moments == {(3, 0), (7, 0)}


def test_holes_dates_are_unique_with_one_or_two_moments(holes: pd.DataFrame) -> None:
    keys = hole_tuples(holes)
    assert holes["date"].is_unique
    assert len(set(keys)) == len(holes)

    per_day = pd.Series([key[:3] for key in keys]).value_counts()
    assert per_day.min() == 1
    assert per_day.max() == 2
    assert len(per_day) == 364
    assert int((per_day == 1).sum()) == 6
    assert (2025, 1, 27) not in set(per_day.index)


def test_hours_columns_and_row_count(
    hours: pd.DataFrame, source_gec: pd.DataFrame
) -> None:
    assert list(hours.columns) == list(source_gec.columns)
    assert len(hours) == 720


def test_hours_keys_equal_holes_keys_minus_missing_day(
    hours: pd.DataFrame, holes: pd.DataFrame
) -> None:
    hours_keys = set(key_tuples(hours))
    holes_keys = set(hole_tuples(holes))
    assert hours_keys == holes_keys - MISSING_KEYS
    assert len(hours_keys) == 720


def test_hours_rows_equal_source_rows_by_key(
    hours: pd.DataFrame, source_gec: pd.DataFrame
) -> None:
    merged = hours.merge(source_gec, on=KEY, suffixes=("_hours", "_source"))
    assert len(merged) == len(hours)
    assert (merged["DOY_hours"] == merged["DOY_source"]).all()
    assert (merged["UnixTimestamp_hours"] == merged["UnixTimestamp_source"]).all()
    assert (merged["uqrg_hours"] == merged["uqrg_source"]).all()

    hours_keys = key_tuples(hours)
    source_order = [
        key for key in key_tuples(source_gec) if key in set(hours_keys)
    ]
    assert hours_keys == source_order


def test_hours_equals_in_memory_filter_pipeline(
    build_module,
    source_gec: pd.DataFrame,
    holes: pd.DataFrame,
    hours: pd.DataFrame,
) -> None:
    hole_times = build_module.load_hole_times(holes)
    expected = build_module.filter_gec(source_gec, hole_times).reset_index(drop=True)
    pd.testing.assert_frame_equal(expected, hours)


def test_hours_is_a_strict_subset_of_source(
    hours: pd.DataFrame, source_gec: pd.DataFrame, holes: pd.DataFrame
) -> None:
    hours_keys = set(key_tuples(hours))
    source_keys = set(key_tuples(source_gec))
    holes_keys = set(hole_tuples(holes))
    assert hours_keys < source_keys
    assert hours_keys == source_keys & holes_keys
    assert holes_keys - hours_keys == MISSING_KEYS
