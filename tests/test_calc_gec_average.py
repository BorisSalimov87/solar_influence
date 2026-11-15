"""Tests for the src/calc_gec_average.py command-line script."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SCRIPT = ROOT / "src" / "calc_gec_average.py"


def run_script(*args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=cwd,
        text=True,
        encoding="utf-8",
        capture_output=True,
    )


def write_csv(path: Path, text: str) -> Path:
    path.write_text(text, encoding="utf-8")
    return path


def test_synthetic_values_give_exact_mean(workdir: Path) -> None:
    path = write_csv(workdir / "small.csv", "uqrg\n1\n2\n3\n")

    result = run_script(str(path))

    assert result.returncode == 0
    assert result.stdout == "Средний GEC (uqrg): 2.0000 TECU\n"
    assert result.stderr == ""


def test_real_source_mean_matches_independent_pandas_calculation() -> None:
    source = DATA / "gec-0km-2025.csv"

    result = run_script(str(source))

    expected_mean = pd.read_csv(source, sep=r"\s+")["uqrg"].mean()
    assert result.returncode == 0
    assert result.stdout == f"Средний GEC (uqrg): {expected_mean:.4f} TECU\n"
    assert result.stdout == "Средний GEC (uqrg): 1.5762 TECU\n"


def test_no_arguments_returns_code_2_and_usage() -> None:
    result = run_script()

    assert result.returncode == 2
    assert result.stdout == ""
    assert "Использование: calc_gec_average.py <путь к CSV>" in result.stderr


def test_missing_file_returns_code_1(workdir: Path) -> None:
    missing = workdir / "absent.csv"

    result = run_script(str(missing))

    assert result.returncode == 1
    assert result.stdout == ""
    assert "файл не найден" in result.stderr


def test_missing_uqrg_column_returns_code_1(workdir: Path) -> None:
    path = write_csv(workdir / "no_uqrg.csv", "value\n1\n2\n3\n")

    result = run_script(str(path))

    assert result.returncode == 1
    assert result.stdout == ""
    assert "нет колонки uqrg" in result.stderr


def test_non_numeric_values_are_ignored(workdir: Path) -> None:
    path = write_csv(workdir / "mixed.csv", "uqrg\n1\nabc\n3\n")

    result = run_script(str(path))

    assert result.returncode == 0
    assert result.stdout == "Средний GEC (uqrg): 2.0000 TECU\n"


def test_all_non_numeric_values_return_code_1(workdir: Path) -> None:
    path = write_csv(workdir / "text_only.csv", "uqrg\nabc\ndef\n")

    result = run_script(str(path))

    assert result.returncode == 1
    assert result.stdout == ""
    assert "нет числовых значений" in result.stderr


def test_output_is_a_single_formatted_line(workdir: Path) -> None:
    path = write_csv(workdir / "one.csv", "uqrg\n7.5\n")

    result = run_script(str(path))

    assert result.returncode == 0
    assert result.stderr == ""
    assert result.stdout.count("\n") == 1
    assert re.fullmatch(
        r"Средний GEC \(uqrg\): -?\d+\.\d{4} TECU\n", result.stdout
    )


def test_script_does_not_create_or_change_files_in_data() -> None:
    def snapshot() -> dict[str, tuple[int, int]]:
        return {
            entry.name: (entry.stat().st_size, entry.stat().st_mtime_ns)
            for entry in sorted(DATA.iterdir())
            if entry.is_file()
        }

    before = snapshot()

    result = run_script("data/gec-0km-2025.csv")

    after = snapshot()
    assert result.returncode == 0
    assert after == before
