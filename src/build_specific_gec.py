"""Filter GEC 2025 to only the time moments present in holes.csv."""

import pandas as pd

# Read GEC (space-separated, 15-min resolution)
gec = pd.read_csv("data/gec-0km-2025.csv", sep=r"\s+")

# Read holes (comma-separated)
holes = pd.read_csv("data/holes.csv")

# Build a set of (Year, Month, Day, Hour, Minute) tuples from holes
hole_times = set()
for d in holes["date"]:
    # d is like "2025-01-01T03:00:00"
    date_part, time_part = d.split("T")
    y, m, day = date_part.split("-")
    h, mi, _ = time_part.split(":")
    hole_times.add((int(y), int(m), int(day), int(h), int(mi)))

# Filter GEC rows
mask = gec.apply(
    lambda row: (row["Year"], row["Month"], row["Day"], row["Hour"], row["Minute"]) in hole_times,
    axis=1,
)
result = gec[mask].copy()

# Write output (space-separated, matching source format)
result.to_csv("data/gec-0km-2025-hours.csv", index=False, sep=" ")
print(f"Wrote {len(result)} rows to data/gec-0km-2025-hours.csv")