"""
Page Object для страницы медленного калькулятора.
URL: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Класс описывает страницу калькулятора с настраиваемой задержкой."""

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_DISPLAY = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        :param driver: Экземпляр WebDriver для управления браузером.
        :type driver: WebDriver
        """
        self.driver = driver

    def open(self) -> "CalculatorPage":
        """
        Открывает страницу калькулятора в браузере.

        :return: Текущий экземпляр страницы для цепочки вызовов.
        :rtype: CalculatorPage
        """
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds: int) -> "CalculatorPage":
        """
        Устанавливает значение задержки вычисления.

        :param seconds: Задержка в секундах.
        :type seconds: int
        :return: Текущий экземпляр страницы для цепочки вызовов.
        :rtype: CalculatorPage
        """
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(str(seconds))
        return self

    def click_button(self, label: str) -> "CalculatorPage":
        """
        Кликает по кнопке калькулятора с указанной меткой.

        :param label: Текст на кнопке (например, "7", "+", "=").
        :type label: str
        :return: Текущий экземпляр страницы для цепочки вызовов.
        :rtype: CalculatorPage
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{label}']"
        )
        button.click()
        return self

    def get_result(self, timeout: int = 50) -> str:
        """
        Ожидает появления результата "15" на экране и возвращает его.

        :param timeout: Максимальное время ожидания в секундах.
        :type timeout: int
        :return: Текст результата с экрана калькулятора.
        :rtype: str
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.RESULT_DISPLAY, "15")
        )
        return self.driver.find_element(*self.RESULT_DISPLAY).text
