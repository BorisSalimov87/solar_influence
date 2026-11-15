"""Tests for filter_gec() from src/build_specific_gec.py."""

from __future__ import annotations

import pandas as pd

COLUMNS = [
    "Year",
    "Month",
    "Day",
    "DOY",
    "Hour",
    "Minute",
    "UnixTimestamp",
    "uqrg",
]

ROWS = [
    (2025, 1, 1, 3, 0, 1230768000, 1.10),
    (2025, 1, 1, 3, 15, 1230768900, 1.15),
    (2025, 1, 1, 7, 0, 1230786000, 1.70),
    (2025, 1, 2, 3, 0, 1230836400, 1.30),
    (2025, 1, 2, 7, 0, 1230850800, 1.80),
    (2025, 1, 3, 0, 0, 1230912000, 1.05),
]


def make_gec() -> pd.DataFrame:
    return pd.DataFrame(
        [
            (year, month, day, day, hour, minute, unix, uqrg)
            for year, month, day, hour, minute, unix, uqrg in ROWS
        ],
        columns=COLUMNS,
    )


def keys(frame: pd.DataFrame) -> list[tuple[int, int, int, int, int]]:
    return list(
        zip(
            frame["Year"].tolist(),
            frame["Month"].tolist(),
            frame["Day"].tolist(),
            frame["Hour"].tolist(),
            frame["Minute"].tolist(),
        )
    )


def test_selects_exact_intersection(build_module) -> None:
    gec = make_gec()
    hole_times = {
        (2025, 1, 1, 3, 0),
        (2025, 1, 1, 3, 15),
        (2025, 1, 2, 7, 0),
        (2025, 5, 5, 3, 0),
    }

    result = build_module.filter_gec(gec, hole_times)

    assert keys(result) == [
        (2025, 1, 1, 3, 0),
        (2025, 1, 1, 3, 15),
        (2025, 1, 2, 7, 0),
    ]


def test_preserves_source_row_order(build_module) -> None:
    gec = make_gec().iloc[[4, 0, 3]].reset_index(drop=True)
    hole_times = {(2025, 1, 1, 3, 0), (2025, 1, 2, 3, 0), (2025, 1, 2, 7, 0)}

    result = build_module.filter_gec(gec, hole_times)

    assert keys(result) == [
        (2025, 1, 2, 7, 0),
        (2025, 1, 1, 3, 0),
        (2025, 1, 2, 3, 0),
    ]


def test_payload_values_are_unchanged(build_module) -> None:
    gec = make_gec()
    hole_times = {(2025, 1, 1, 7, 0), (2025, 1, 2, 3, 0)}

    result = build_module.filter_gec(gec, hole_times)

    assert result["uqrg"].tolist() == [1.70, 1.30]
    assert result["UnixTimestamp"].tolist() == [1230786000, 1230836400]
    assert result["DOY"].tolist() == [1, 2]


def test_minute_is_significant(build_module) -> None:
    gec = make_gec()

    result = build_module.filter_gec(gec, {(2025, 1, 1, 3, 15)})

    assert keys(result) == [(2025, 1, 1, 3, 15)]
    assert (2025, 1, 1, 3, 0) not in keys(result)


def test_empty_hole_times_gives_empty_frame_with_columns(build_module) -> None:
    gec = make_gec()

    result = build_module.filter_gec(gec, set())

    assert len(result) == 0
    assert list(result.columns) == COLUMNS


def test_empty_source_gives_empty_result(build_module) -> None:
    gec = make_gec().iloc[0:0]

    result = build_module.filter_gec(gec, {(2025, 1, 1, 3, 0)})

    assert len(result) == 0


def test_result_is_an_independent_copy(build_module) -> None:
    gec = make_gec()
    original = gec.copy(deep=True)

    result = build_module.filter_gec(gec, {(2025, 1, 1, 3, 0)})
    result.loc[result.index[0], "uqrg"] = 999.0

    pd.testing.assert_frame_equal(gec, original)
    assert 999.0 not in gec["uqrg"].tolist()


def test_result_is_a_subset_of_source(build_module) -> None:
    gec = make_gec()
    hole_times = {(2025, 1, 1, 3, 0), (2025, 1, 2, 7, 0), (2030, 1, 1, 3, 0)}

    result = build_module.filter_gec(gec, hole_times)

    assert set(keys(result)) <= set(keys(gec))


def test_all_keys_returns_whole_source(build_module) -> None:
    gec = make_gec()

    result = build_module.filter_gec(gec, set(keys(gec)))

    pd.testing.assert_frame_equal(result, gec)
