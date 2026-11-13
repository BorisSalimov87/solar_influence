"""Correlate coronal-hole area with GEC shifted by solar-wind transit time."""

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
GEC_PATH = DATA_DIR / "gec-0km-2025-hours.csv"
HOLES_PATH = DATA_DIR / "holes.csv"

AU_KM = 149_597_870.7
MAX_INTERP_GAP = pd.Timedelta(hours=24)
EPOCH = pd.Timestamp("2000-01-01T12:00:00")


def load_gec(path: Path) -> tuple[pd.DatetimeIndex, np.ndarray]:
    """Read the GEC series and build naive UTC timestamps from calendar fields.

    Данные: data/gec-0km-2025-hours.csv (пробелы, столбцы Year … uqrg).
    Проверка: часы только 03:00 и 07:00, 720 строк, нет 2025-11-26.
    Используется в: main().
    """
    gec = pd.read_csv(path, sep=r"\s+")
    calendar = gec[["Year", "Month", "Day", "Hour", "Minute"]].rename(
        columns={
            "Year": "year",
            "Month": "month",
            "Day": "day",
            "Hour": "hour",
            "Minute": "minute",
        }
    )
    frame = pd.DataFrame(
        {
            "time": pd.to_datetime(calendar),
            "uqrg": gec["uqrg"].to_numpy(dtype=float),
        }
    ).sort_values("time")
    return pd.DatetimeIndex(frame["time"]), frame["uqrg"].to_numpy(dtype=float)


def load_holes(path: Path) -> tuple[pd.DatetimeIndex, np.ndarray]:
    """Read the coronal-hole area series and its naive UTC timestamps.

    Данные: data/holes.csv, столбцы date и area_holes.
    Проверка: 722 строки, время только 03:00:00 и 07:00:00.
    Используется в: main().
    """
    holes = pd.read_csv(path)
    frame = pd.DataFrame(
        {
            "time": pd.to_datetime(holes["date"]),
            "area_holes": holes["area_holes"].to_numpy(dtype=float),
        }
    ).sort_values("time")
    return pd.DatetimeIndex(frame["time"]), frame["area_holes"].to_numpy(dtype=float)


def earth_sun_distance_km(times: pd.DatetimeIndex) -> np.ndarray:
    """Compute the Sun-Earth distance in km for each moment.

    Данные: моменты времени из data/holes.csv.
    Проверка: 0.983 AU <= R <= 1.017 AU, среднее около 1 AU.
    Используется в: shifted_targets().
    """
    days = np.asarray(times - EPOCH, dtype="timedelta64[ns]") / np.timedelta64(
        1, "D"
    )
    mean_anomaly = np.deg2rad((357.528 + 0.9856003 * days) % 360.0)
    r_au = (
        1.00014
        - 0.01671 * np.cos(mean_anomaly)
        - 0.00014 * np.cos(2.0 * mean_anomaly)
    )
    return r_au * AU_KM


def shifted_targets(
    holes_time: pd.DatetimeIndex, speed_km_s: float
) -> tuple[pd.DatetimeIndex, np.ndarray, np.ndarray]:
    """Shift hole times by the solar-wind transit time at the given speed.

    Данные: моменты из data/holes.csv и скорость ветра из CLI.
    Проверка: среднее dt около 4.3 сут при 400 км/с.
    Используется в: compute_correlation().
    """
    distance_km = earth_sun_distance_km(holes_time)
    dt_s = distance_km / speed_km_s
    targets = holes_time + pd.to_timedelta(dt_s, unit="s")
    return targets, dt_s, distance_km


def interpolate_gec(
    gec_time: pd.DatetimeIndex, gec_uqrg: np.ndarray, targets: pd.DatetimeIndex
) -> np.ndarray:
    """Linearly interpolate GEC at shifted targets, rejecting large gaps.

    Данные: ряд data/gec-0km-2025-hours.csv и сдвинутые моменты.
    Проверка: NaN вместо экстраполяции и вместо разрыва > 24 ч.
    Используется в: compute_correlation().
    """
    gec_ns = np.asarray(gec_time, dtype="datetime64[ns]")
    target_ns = np.asarray(targets, dtype="datetime64[ns]")
    result = np.full(target_ns.shape, np.nan, dtype=float)
    if len(gec_ns) < 2:
        return result

    idx = np.searchsorted(gec_ns, target_ns, side="left")
    inside = (idx > 0) & (idx < len(gec_ns))
    i = idx[inside]
    t0 = gec_ns[i - 1]
    t1 = gec_ns[i]
    span_s = (t1 - t0) / np.timedelta64(1, "s")
    offset_s = (target_ns[inside] - t0) / np.timedelta64(1, "s")
    weight = np.divide(
        offset_s, span_s, out=np.zeros_like(offset_s), where=span_s > 0
    )
    values = gec_uqrg[i - 1] + (gec_uqrg[i] - gec_uqrg[i - 1]) * weight
    good = (span_s > 0) & (span_s <= MAX_INTERP_GAP.total_seconds())

    partial = result[inside]
    partial[good] = values[good]
    result[inside] = partial
    return result


def compute_correlation(
    holes_time: pd.DatetimeIndex,
    area_holes: np.ndarray,
    gec_time: pd.DatetimeIndex,
    gec_uqrg: np.ndarray,
    speed_km_s: float,
) -> tuple[float, int, float, float]:
    """Compute Pearson r between area_holes(t) and uqrg(t + dt).

    Данные: ряды data/holes.csv и data/gec-0km-2025-hours.csv.
    Проверка: r конечный и лежит в [-1, 1]; N <= 720.
    Используется в: main().
    """
    targets, dt_s, distance_km = shifted_targets(holes_time, speed_km_s)
    gec_interp = interpolate_gec(gec_time, gec_uqrg, targets)
    mask = np.isfinite(gec_interp) & np.isfinite(area_holes)
    n = int(mask.sum())
    if n < 3:
        raise ValueError(f"Need at least 3 valid pairs, got {n}")
    r = float(np.corrcoef(area_holes[mask], gec_interp[mask])[0, 1])
    return r, n, float(np.mean(dt_s[mask])), float(np.mean(distance_km[mask]))


def main() -> None:
    """Read the two series, apply the transit-time shift and print Pearson r.

    Данные: data/holes.csv и data/gec-0km-2025-hours.csv, скорость из CLI.
    Проверка: запуск из корня проекта, код 0 и конечный r в [-1, 1].
    Используется в: самостоятельный запуск; результат читает человек.
    """
    parser = argparse.ArgumentParser(
        description="Pearson r between coronal-hole area and shifted GEC."
    )
    parser.add_argument(
        "speed_km_s", type=float, help="solar wind speed in km/s (must be > 0)"
    )
    args = parser.parse_args()
    if args.speed_km_s <= 0:
        parser.error("speed_km_s must be positive")

    holes_time, area_holes = load_holes(HOLES_PATH)
    gec_time, gec_uqrg = load_gec(GEC_PATH)
    r, n, mean_dt_s, mean_distance_km = compute_correlation(
        holes_time, area_holes, gec_time, gec_uqrg, args.speed_km_s
    )

    print(f"Solar wind speed: {args.speed_km_s:.1f} km/s")
    print(f"Mean Sun-Earth distance: {mean_distance_km / AU_KM:.5f} AU")
    print(f"Mean transit time: {mean_dt_s / 86400.0:.4f} d")
    print(f"Pairs: {n} of {len(holes_time)}")
    print(f"Pearson r (area_holes(t) vs uqrg(t+dt)): {r:+.6f}")


if __name__ == "__main__":
    main()
