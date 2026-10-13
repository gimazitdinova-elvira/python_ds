"""
Page Object для страницы оформления заказа (Checkout).
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Класс описывает страницу оформления заказа."""

    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        :param driver: Экземпляр WebDriver для управления браузером.
        :type driver: WebDriver
        """
        self.driver = driver

    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> "CheckoutPage":
        """
        Заполняет форму оформления заказа и нажимает Continue.

        :param first_name: Имя покупателя.
        :type first_name: str
        :param last_name: Фамилия покупателя.
        :type last_name: str
        :param postal_code: Почтовый индекс.
        :type postal_code: str
        :return: Текущий экземпляр страницы для цепочки вызовов.
        :rtype: CheckoutPage
        """
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        return self

    def get_total(self, timeout: int = 10) -> str:
        """
        Ожидает появления итоговой суммы и возвращает её текст.

        :param timeout: Максимальное время ожидания в секундах.
        :type timeout: int
        :return: Текст итоговой суммы (например, "Total: $58.29").
        :rtype: str
        """
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        return self.driver.find_element(*self.TOTAL_LABEL).text
