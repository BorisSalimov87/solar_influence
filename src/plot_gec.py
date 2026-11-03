"""Plot GEC (Global Electron Content) from CSV data."""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "gec-0km-2025.csv"
OUT_PATH = Path(__file__).resolve().parent.parent / "cache" / "plot" / "gec.png"


def main() -> None:
    df = pd.read_csv(DATA_PATH, sep=r"\s+")
    df["time"] = pd.to_datetime(df["UnixTimestamp"], unit="s", utc=True)

    fig, ax = plt.subplots(figsize=(14, 4))
    ax.plot(df["time"], df["uqrg"], color="steelblue", linewidth=0.8)

    ax.set_xlabel("Time")
    ax.set_ylabel("GEC, TECU")

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
    fig.autofmt_xdate()

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PATH, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved → {OUT_PATH}")


if __name__ == "__main__":
    main()