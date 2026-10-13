"""
Page Object для главной страницы магазина (список товаров).
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    """Класс описывает главную страницу интернет-магазина."""

    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        :param driver: Экземпляр WebDriver для управления браузером.
        :type driver: WebDriver
        """
        self.driver = driver

    def add_to_cart(self, item_id: str) -> "MainPage":
        """
        Добавляет товар в корзину по его идентификатору.

        :param item_id: Идентификатор товара (например, "sauce-labs-backpack").
        :type item_id: str
        :return: Текущий экземпляр страницы для цепочки вызовов.
        :rtype: MainPage
        """
        button = self.driver.find_element(
            By.CSS_SELECTOR, f"#add-to-cart-{item_id}"
        )
        button.click()
        return self

    def go_to_cart(self) -> "MainPage":
        """
        Переходит на страницу корзины.

        :return: Текущий экземпляр страницы для цепочки вызовов.
        :rtype: MainPage
        """
        self.driver.find_element(*self.CART_LINK).click()
        return self