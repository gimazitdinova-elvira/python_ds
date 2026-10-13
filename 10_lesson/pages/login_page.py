"""
Page Object для страницы авторизации Sauce Demo.
URL: https://www.saucedemo.com/
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Класс описывает страницу входа в интернет-магазин Sauce Demo."""

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        :param driver: Экземпляр WebDriver для управления браузером.
        :type driver: WebDriver
        """
        self.driver = driver

    def open(self) -> "LoginPage":
        """
        Открывает страницу авторизации.

        :return: Текущий экземпляр страницы для цепочки вызовов.
        :rtype: LoginPage
        """
        self.driver.get(self.URL)
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        """
        Выполняет вход с указанными учётными данными.

        :param username: Имя пользователя.
        :type username: str
        :param password: Пароль.
        :type password: str
        :return: Текущий экземпляр страницы для цепочки вызовов.
        :rtype: LoginPage
        """
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self