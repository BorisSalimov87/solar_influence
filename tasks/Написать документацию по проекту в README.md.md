---
type: Задача
status: выполнена
---
# Написать документацию по проекту в README.md

Запрос пользователя: «Заменить однострочный
  `README.md` краткой документацией на русском — назначение проекта, воспроизводимые
  команды, описание трёх CSV, ссылки на подробные документы; `AGENTS.md` и
  `ontology.yaml` не дублировать.»

Готово, когда: `README.md` содержит разделы «Быстрый старт», «Данные», «Документация», строки `1.5762 TECU` и `FAIL: 2 hole times missing in GEC`; обе подзадачи выполнены; `git diff -- data checks ontology.yaml` пусто.
Не входит: изменение `AGENTS.md`, `ontology.yaml`, `data/`, `checks/`; повторный запуск `src/build_specific_gec.py` и `src/plot_gec.py`; коммит.

## План
- Написать раздел «Быстрый старт» в README.md
- Проверить README по INDEX и AGENTS.md

## Итог
Подзадача «Написать раздел «Быстрый старт» в README.md» выполнена: `README.md` заменён краткой документацией (назначение, четыре команды, таблица трёх CSV, известное падение `checks/check.py`, ссылки на подробные документы), в `INDEX.md` добавлена строка про `README.md`. Подзадача «Проверить README по INDEX и AGENTS.md» выполнена: средний GEC пересчитан (1.5762 TECU), `checks/check.py` даёт код 1 только с `FAIL: 2 hole times missing in GEC`, в hours-файле 721 строка с шапкой, `git diff -- data checks ontology.yaml` пусто. `AGENTS.md`, `ontology.yaml`, `data/`, `checks/` не изменялись, коммит не создан.

## Связи
- тип: [[Задача]]
