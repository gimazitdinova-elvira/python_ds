"""
Тест для проверки работы медленного калькулятора с использованием Allure.
"""

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка медленного калькулятора: 7 + 8 = 15")
@allure.description(
    "Тест открывает страницу медленного калькулятора, устанавливает задержку 45 секунд, "
    "выполняет сложение 7 + 8 и проверяет, что результат равен 15."
)
def test_slow_calculator() -> None:
    """Проверяет, что калькулятор корректно считает 7 + 8 с задержкой."""

    options = Options()
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    try:
        with allure.step("Открыть страницу калькулятора"):
            page = CalculatorPage(driver)
            page.open()

        with allure.step("Установить задержку 45 секунд"):
            page.set_delay(45)

        with allure.step("Выполнить вычисление: 7 + 8 ="):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
            page.click_button("=")

        with allure.step("Дождаться результата и получить его"):
            result = page.get_result(timeout=50)

        with allure.step(f"Проверить, что результат равен 15 (получено: {result})"):
            assert result == "15", f"Ожидалось 15, получено {result}"
    finally:
        driver.quit()