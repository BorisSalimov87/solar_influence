---
type: Задача
status: выполнена
---
# Проверить README по INDEX и AGENTS.md

Готово, когда: `.venv/bin/python src/calc_gec_average.py data/gec-0km-2025.csv` печатает `Средний GEC (uqrg): 1.5762 TECU`; `.venv/bin/python checks/check.py` завершается кодом 1 только с `FAIL: 2 hole times missing in GEC`; `wc -l data/gec-0km-2025-hours.csv` даёт 721; `git diff -- data checks ontology.yaml` пусто; все пути, упомянутые в README, существуют.
Не входит: правка README сверх найденных расхождений; запуск `src/build_specific_gec.py` и `src/plot_gec.py`; коммит.

## Итог
Сверены все числа и пути README с файлами проекта; расхождений нет. Проверено: `.venv/bin/python src/calc_gec_average.py data/gec-0km-2025.csv` → `Средний GEC (uqrg): 1.5762 TECU`; `.venv/bin/python checks/check.py` → код 1, вывод `OK: result file exists`, `OK: all rows have 03:00 or 07:00`, `FAIL: 2 hole times missing in GEC`; `wc -l data/gec-0km-2025-hours.csv` → 721; `git diff --stat -- data checks ontology.yaml` → пусто. `src/build_specific_gec.py` и `src/plot_gec.py` не запускались: производные файлы уже есть.

## Связи
- тип: [[Задача]]
- подзадачаОт: [[Написать документацию по проекту в README.md]]
