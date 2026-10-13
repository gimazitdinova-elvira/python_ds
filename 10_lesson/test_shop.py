"""
Тест оформления заказа в интернет-магазине Sauce Demo с использованием Allure.
"""

import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Проверка итоговой суммы заказа из трёх товаров")
@allure.description(
    "Тест авторизуется на saucedemo.com, добавляет три товара в корзину, "
    "переходит к оформлению заказа, заполняет форму и проверяет, "
    "что итоговая сумма равна 'Total: $58.29'."
)
def test_checkout_total() -> None:
    """Проверяет корректность итоговой суммы при оформлении заказа."""

    options = Options()
    driver = webdriver.Firefox(options=options)

    try:
        with allure.step("Открыть страницу авторизации"):
            login_page = LoginPage(driver)
            login_page.open()

        with allure.step("Авторизоваться как standard_user"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить три товара в корзину"):
            main_page = MainPage(driver)
            main_page.add_to_cart("sauce-labs-backpack")
            main_page.add_to_cart("sauce-labs-bolt-t-shirt")
            main_page.add_to_cart("sauce-labs-onesie")

        with allure.step("Перейти в корзину"):
            main_page.go_to_cart()

        with allure.step("Нажать кнопку Checkout"):
            cart_page = CartPage(driver)
            cart_page.click_checkout()

        with allure.step("Заполнить форму оформления заказа"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_form("Ivan", "Ivanov", "123456")

        with allure.step("Получить итоговую сумму заказа"):
            total = checkout_page.get_total()

        with allure.step(f"Проверить, что итог равен 'Total: $58.29' (получено: '{total}')"):
            assert total == "Total: $58.29", (
                f"Ожидалось 'Total: $58.29', получено '{total}'"
            )
    finally:
        driver.quit()
