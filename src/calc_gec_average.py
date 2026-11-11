"""Average GEC (uqrg column) for a GEC CSV file given by path."""

import sys
from pathlib import Path

import pandas as pd


def main() -> int:
    r"""Print the mean uqrg of the CSV at sys.argv[1].

    Данные: CSV с колонкой uqrg (TECU), например data/gec-0km-2025.csv;
    разделитель — пробелы, читается с sep=r"\s+".
    Проверка: запуск на data/gec-0km-2025.csv; независимый пересчёт в
    notes/Расчёт среднего GEC по исходному ряду.md.
    Используется в: сравнении средних GEC по двум файлам.

    Коды возврата: 0 — успех, 1 — нет файла или колонки, 2 — неверное число
    аргументов. Файлы не пишет, данные не меняет.
    """
    if len(sys.argv) != 2:
        print("Использование: calc_gec_average.py <путь к CSV>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Ошибка: файл не найден: {path}", file=sys.stderr)
        return 1

    try:
        df = pd.read_csv(path, sep=r"\s+")
    except Exception as exc:
        print(f"Ошибка: не удалось прочитать {path}: {exc}", file=sys.stderr)
        return 1

    if "uqrg" not in df.columns:
        print("Ошибка: в файле нет колонки uqrg", file=sys.stderr)
        return 1

    values = pd.to_numeric(df["uqrg"], errors="coerce").dropna()
    if values.empty:
        print("Ошибка: в колонке uqrg нет числовых значений", file=sys.stderr)
        return 1

    print(f"Средний GEC (uqrg): {values.mean():.4f} TECU")
    return 0


if __name__ == "__main__":
    sys.exit(main())
