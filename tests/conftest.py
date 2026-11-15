"""Shared fixtures for the HW2 verifier tests."""

from __future__ import annotations

import importlib.util
import os
import shutil
import sys
import tempfile
from pathlib import Path
from types import ModuleType

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DEFAULT_SRC = ROOT / "src" / "build_specific_gec.py"


def _load_module(path: Path, name: str) -> ModuleType:
    if not path.is_file():
        raise FileNotFoundError(f"module under test not found: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot create import spec for: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def build_module() -> ModuleType:
    """Load src/build_specific_gec.py, or the copy named by GEC_SRC."""
    raw = os.environ.get("GEC_SRC", str(DEFAULT_SRC))
    path = Path(raw)
    if not path.is_absolute():
        path = ROOT / path
    return _load_module(path, "build_specific_gec_under_test")


@pytest.fixture(scope="session")
def source_gec() -> pd.DataFrame:
    return pd.read_csv(DATA / "gec-0km-2025.csv", sep=r"\s+")


@pytest.fixture(scope="session")
def holes() -> pd.DataFrame:
    return pd.read_csv(DATA / "holes.csv")


@pytest.fixture(scope="session")
def hours() -> pd.DataFrame:
    return pd.read_csv(DATA / "gec-0km-2025-hours.csv", sep=r"\s+")


@pytest.fixture()
def workdir() -> Path:
    """Temporary directory inside results/, removed after the test."""
    results = ROOT / "results"
    results.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(dir=results, prefix="tmp-"))
    try:
        yield tmp
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
