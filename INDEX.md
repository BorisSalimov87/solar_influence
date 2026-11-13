# INDEX.md — где что лежит

- `AGENTS.md` — правила работы агента в проекте.
- `STATUS.md` — где работа сейчас; читать в начале сессии.
- `diary.md` — журнал проекта; только дописывается.
- `cascade.sh` — каскадное сжатие статьи: части → L1 → L2 → L3.
- `data/holes.csv` — площадь областей, похожих на CH, по моментам времени; только чтение.
- `data/gec-0km-2025.csv` — исходный 15-минутный ряд GEC за 2025 г.; только чтение.
- `data/gec-0km-2025-hours.csv` — GEC только для моментов из `data/holes.csv`; 720 строк, нет 2025-11-26.
- `src/build_specific_gec.py` — фильтр GEC: `load_hole_times()`, `filter_gec()`, `main()`.
- `src/plot_gec.py` — график GEC, `main()`; пишет `cache/plot/gec.png`.
- `src/build_holes_gec_correlation.py` — Pearson r между `area_holes(t)` и
  `uqrg(t+dt)` при заданной скорости ветра (км/с); без записи файлов.
- `checks/check.py` — проверка `data/gec-0km-2025-hours.csv`; только чтение.
- `paper/Signature of the coronal hole near.pdf` — статья-кейс.
- `paper/Signature of the coronal hole near.txt` — текст статьи из PDF.
- `paper/parts/` — статья, разбитая на части для `cascade.sh`.
- `memory/L1.md` — реферат статьи по частям; `memory/L1/` — отдельные части.
- `memory/L2.md` — 10 тезисов статьи со сверкой; читать вместо PDF.
- `memory/L3.md` — главный результат статьи одной строкой.
- `cache/plot/gec.png` — график GEC.
