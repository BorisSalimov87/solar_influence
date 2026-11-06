"""Verify data/gec-0km-2025-hours.csv against holes.csv."""

import sys
from pathlib import Path

import pandas as pd

result_path = Path("data/gec-0km-2025-hours.csv")
holes_path = Path("data/holes.csv")

# 1. File exists
if not result_path.exists():
    print("FAIL: data/gec-0km-2025-hours.csv does not exist")
    sys.exit(1)
print("OK: result file exists")

# 2. Read both files
gec = pd.read_csv(result_path, sep=r"\s+")
holes = pd.read_csv(holes_path)

# 3. Check each row's time is 03:00 or 07:00
for _, row in gec.iterrows():
    h, m = int(row["Hour"]), int(row["Minute"])
    if (h, m) not in ((3, 0), (7, 0)):
        print(f"FAIL: row has time {h:02d}:{m:02d}, expected 03:00 or 07:00")
        sys.exit(1)
print("OK: all rows have 03:00 or 07:00")

# 4. Check set of time moments matches holes.csv dates
gec_times = set()
for _, row in gec.iterrows():
    gec_times.add((int(row["Year"]), int(row["Month"]), int(row["Day"]),
                   int(row["Hour"]), int(row["Minute"])))

hole_times = set()
for d in holes["date"]:
    date_part, time_part = d.split("T")
    y, m, day = date_part.split("-")
    h, mi, _ = time_part.split(":")
    hole_times.add((int(y), int(m), int(day), int(h), int(mi)))

if gec_times != hole_times:
    missing_in_gec = hole_times - gec_times
    extra_in_gec = gec_times - hole_times
    if missing_in_gec:
        print(f"FAIL: {len(missing_in_gec)} hole times missing in GEC")
    if extra_in_gec:
        print(f"FAIL: {len(extra_in_gec)} extra times in GEC")
    sys.exit(1)

print(f"OK: {len(gec_times)} time moments match holes.csv exactly")
print("ALL CHECKS PASSED")