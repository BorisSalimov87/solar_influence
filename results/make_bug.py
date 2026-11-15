"""Build the buggy copy of src/build_specific_gec.py used for the caught-error demo.

The only change is in load_hole_times(): the parsed hour is replaced by 0, so
03:00/07:00 keys become 00:00 keys while the row count of the filtered file
stays the same. This is written to results/ and never imported by the tests
unless GEC_SRC points to it.
"""

from __future__ import annotations

import difflib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src" / "build_specific_gec.py"
RESULTS = ROOT / "results"
BUGGY = RESULTS / "buggy_build_specific_gec.py"
DIFF = RESULTS / "bug_diff.txt"

OLD = "int(h), int(mi)"
NEW = "0, int(mi)"


def main() -> int:
    text = SOURCE.read_text(encoding="utf-8")
    count = text.count(OLD)
    if count != 1:
        raise SystemExit(f"expected exactly one occurrence of {OLD!r}, found {count}")

    buggy_text = text.replace(OLD, NEW)
    RESULTS.mkdir(exist_ok=True)
    BUGGY.write_text(buggy_text, encoding="utf-8")

    diff = difflib.unified_diff(
        text.splitlines(keepends=True),
        buggy_text.splitlines(keepends=True),
        fromfile="src/build_specific_gec.py",
        tofile="results/buggy_build_specific_gec.py",
    )
    DIFF.write_text("".join(diff), encoding="utf-8")

    print(f"wrote {BUGGY.relative_to(ROOT)}")
    print(f"wrote {DIFF.relative_to(ROOT)}")
    print(f"replaced {OLD!r} -> {NEW!r} ({count} occurrence)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
