"""
Page Object для страницы корзины.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс описывает страницу корзины интернет-магазина."""

    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        :param driver: Экземпляр WebDriver для управления браузером.
        :type driver: WebDriver
        """
        self.driver = driver

    def get_cart_items(self) -> list[str]:
        """
        Возвращает список названий товаров в корзине.

        :return: Список названий товаров.
        :rtype: list[str]
        """
        items = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
        return [item.text for item in items]

    def click_checkout(self) -> "CartPage":
        """
        Нажимает кнопку оформления заказа (Checkout).

        :return: Текущий экземпляр страницы для цепочки вызовов.
        :rtype: CartPage
        """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        return self
