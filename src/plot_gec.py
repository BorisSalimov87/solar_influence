"""Plot GEC (Global Electron Content) from CSV data."""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "gec-0km-2025.csv"
OUT_PATH = Path(__file__).resolve().parent.parent / "cache" / "plot" / "gec.png"

MONTHS_RU = (
    "янв", "фев", "мар", "апр", "май", "июн",
    "июл", "авг", "сен", "окт", "ноя", "дек",
)


def format_month_ru(value, _position):
    """Return the Russian short month name for a matplotlib date value."""
    month = mdates.num2date(value).month
    return MONTHS_RU[month - 1]


def main() -> None:
    """Plot the 2025 GEC series and save it to cache/plot/gec.png.

    Данные: data/gec-0km-2025.csv, столбцы UnixTimestamp (UTC) и uqrg (TECU).
    Проверка: визуальное сравнение с эталонным графиком, запись в diary.md
    от 2025-11-03; автоматической проверки нет.
    Используется в: самостоятельный запуск; результат читает человек.
    """
    base_font = plt.rcParams["font.size"]
    plt.rcParams.update(
        {
            "font.size": base_font * 2,
            "axes.labelsize": base_font * 2,
            "axes.titlesize": base_font * 2,
            "xtick.labelsize": base_font * 2,
            "ytick.labelsize": base_font * 2,
            "legend.fontsize": base_font * 2,
            "font.family": "DejaVu Sans",
        }
    )

    df = pd.read_csv(DATA_PATH, sep=r"\s+")
    df["time"] = pd.to_datetime(df["UnixTimestamp"], unit="s", utc=True)

    fig, ax = plt.subplots(figsize=(14, 4))
    ax.plot(df["time"], df["uqrg"], color="steelblue", linewidth=0.8)

    ax.set_xlabel("Время")
    ax.set_ylabel("ПЭС, TECU")

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(format_month_ru))
    fig.autofmt_xdate()
    plt.grid()
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PATH, dpi=150, bbox_inches="tight")
    
    plt.close(fig)
    print(f"Saved → {OUT_PATH}")


if __name__ == "__main__":
    main()