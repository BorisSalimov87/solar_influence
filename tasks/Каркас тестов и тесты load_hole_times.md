---
type: Задача
status: выполнена
---
# Каркас тестов и тесты load_hole_times

Готово, когда: `.venv/bin/python -m pytest tests/test_load_hole_times.py -q` даёт код 0; в `tests/` есть `conftest.py` с загрузкой модуля по `GEC_SRC`; 9 тестов покрывают канонический кейс из `METHOD.md`, мутацию 03:00 → 03:30 (тест падает) и ещё 3–5 кейсов.
Не входит: тесты `filter_gec`, `calc_gec_average`, данные; запуск `src/build_specific_gec.py`.

## Итог
Создан `tests/conftest.py`: загрузка `src/build_specific_gec.py` по `GEC_SRC` через `importlib`, фикстуры `source_gec`, `holes`, `hours`, `workdir`. Создан `tests/test_load_hole_times.py` с 9 тестами: канонический кейс из `METHOD.md`, мутация 03:00 → 03:30 (множество другое), секунды игнорируются, дубликаты схлопываются, посторонние столбцы не влияют, разные годы/ведущие нули, тип результата, пустой столбец, битая дата → `ValueError`. Проверка: `.venv/bin/python -m pytest tests/test_load_hole_times.py -q` → код 0, `9 passed`.

## Связи
- тип: [[Задача]]
- подзадачаОт: [[Создать верификатор и юнит-тесты HW2]]
