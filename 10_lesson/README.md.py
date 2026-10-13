# Домашнее задание №10: PageObject + Allure

Проект содержит UI-тесты на Selenium WebDriver с использованием паттерна PageObject
и формированием отчётов через Allure.

## Структура проекта

```
lesson_10/
├── pages/                  # Page Object классы
│   ├── calculator_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── login_page.py
│   └── main_page.py                # Тесты
├── test_calculator.py
│── test_shop.py
├── requirements.txt
└── README.md
```

## Установка зависимостей

```bash
pip install -r requirements.txt
```

Также необходимо установить **Allure Commandline**:

- Windows (через scoop): `scoop install allure`
- macOS (через brew): `brew install allure`
- Linux: скачать архив с https://github.com/allure-framework/allure2/releases

## Запуск тестов с формированием отчёта Allure

Из корня проекта `lesson_10`:

```bash
pytest tests/ --alluredir=allure-results
```

После прогона тестов в папке `allure-results` появятся JSON-файлы с результатами.

## Просмотр сформированного отчёта

```bash
allure serve allure-results
```

Команда сгенерирует HTML-отчёт во временной папке и автоматически откроет его в браузере.

Если нужно сохранить отчёт в отдельную папку:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Что демонстрирует проект

- Паттерн **PageObject**: каждый класс страницы инкапсулирует локаторы и действия.
- **Аннотации типов** для параметров и возвращаемых значений всех методов.
- **Docstrings** для каждого класса и метода.
- **Allure-разметка**:
  - `@allure.title`, `@allure.description`, `@allure.feature`, `@allure.severity` — на тестах.
  - `with allure.step("...")` — для шагов и проверок.
- Тесты:
  - `test_slow_calculator` — Chrome, проверка 7 + 8 = 15.
  - `test_checkout_total` — Firefox, проверка итоговой суммы заказа.
cd 