"""Filter GEC 2025 to only the time moments present in holes.csv."""

import pandas as pd


def load_hole_times(holes: pd.DataFrame) -> set[tuple[int, int, int, int, int]]:
    """Build a set of (Year, Month, Day, Hour, Minute) tuples from the date column.

    Данные: data/holes.csv, столбец date.
    Проверка: checks/check.py.
    Используется в: filter_gec().
    """
    hole_times = set()
    for d in holes["date"]:
        # d is like "2025-01-01T03:00:00"
        date_part, time_part = d.split("T")
        y, m, day = date_part.split("-")
        h, mi, _ = time_part.split(":")
        hole_times.add((int(y), int(m), int(day), int(h), int(mi)))
    return hole_times


def filter_gec(
    gec: pd.DataFrame, hole_times: set[tuple[int, int, int, int, int]]
) -> pd.DataFrame:
    """Select GEC rows whose time moment occurs in hole_times.

    Данные: data/gec-0km-2025.csv (пробелы, 15-минутный ряд, UTC) и результат
    load_hole_times().
    Проверка: checks/check.py.
    Используется в: main().
    """
    mask = gec.apply(
        lambda row: (row["Year"], row["Month"], row["Day"], row["Hour"], row["Minute"])
        in hole_times,
        axis=1,
    )
    return gec[mask].copy()


def main() -> None:
    """Read both CSVs, filter GEC and write the result.

    Данные: data/gec-0km-2025.csv и data/holes.csv.
    Проверка: checks/check.py (ожидаемо красный на 2025-11-26).
    Используется в: запуск из корня проекта.
    """
    gec = pd.read_csv("data/gec-0km-2025.csv", sep=r"\s+")
    holes = pd.read_csv("data/holes.csv")
    hole_times = load_hole_times(holes)
    result = filter_gec(gec, hole_times)
    result.to_csv("data/gec-0km-2025-hours.csv", index=False, sep=" ")
    print(f"Wrote {len(result)} rows to data/gec-0km-2025-hours.csv")


if __name__ == "__main__":
    main()
