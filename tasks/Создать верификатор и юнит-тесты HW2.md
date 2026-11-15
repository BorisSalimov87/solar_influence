---
type: Задача
status: выполнена
---
# Создать верификатор и юнит-тесты HW2

Запрос пользователя: «Plan file: hw2-verifier-plan.md
Read this file first and treat it as the source of truth for implementation.»

Готово, когда: `.venv/bin/python -m pytest tests -q` из корня проекта даёт код 0 и все тесты passed; в `results/` лежат вывод «до» (код 1) и «после» (код 0) пойманной ошибки, журнал прогона, окружение, детерминизм и базовая линия `checks/check.py`; `REPORT.md` следует `REPORT_TEMPLATE.md` и содержит 10 разделов; `AGENTS.md`, `README.md`, `INDEX.md`, `STATUS.md`, `diary.md` обновлены; все 5 подзадач выполнены с разделом «Итог».
Не входит: изменение `METHOD.md`, `data/`, `checks/`, `ontology.yaml`, `src/`; запуск `src/build_specific_gec.py`; установка зависимостей; коммит и метка `hw2`; `check_week6.py`; Lean.

## План
- Каркас тестов и тесты load_hole_times
- Тесты filter_gec
- Тесты calc_gec_average
- Верификационные тесты данных
- Прогон, пойманная ошибка, отчёт и документация

## Итог
Все 5 подзадач выполнены. `tests/` — 45 тестов (9 `load_hole_times`, 9 `filter_gec`, 9 `calc_gec_average`, 16 договор о данных, 2 известное ограничение); `.venv/bin/python -m pytest tests -q` → код 0, `45 passed` около 6 с. В `results/` — журнал прогона, окружение, 3 повтора (разброс 0), базовая линия `checks/check.py` (код 1, `FAIL: 2 hole times missing in GEC`), дерево подцелей, журнал попыток, diff и выводы «до» (`7 failed, 38 passed`) и «после» (`45 passed`). `REPORT.md` содержит 10 разделов; `AGENTS.md`, `README.md`, `INDEX.md`, `STATUS.md`, `diary.md` обновлены. `data/`, `checks/`, `src/`, `METHOD.md`, `ontology.yaml` не изменялись; коммит и метка `hw2` исключены пользователем.

## Связи
- тип: [[Задача]]
