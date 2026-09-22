from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_total():
    options = Options()
    driver = webdriver.Firefox(options=options)

    try:
        login_page = LoginPage(driver)
        login_page.open()

        login_page.login("standard_user", "secret_sauce")

        main_page = MainPage(driver)
        main_page.add_to_cart("sauce-labs-backpack")
        main_page.add_to_cart("sauce-labs-bolt-t-shirt")
        main_page.add_to_cart("sauce-labs-onesie")

        main_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Ivan", "Ivanov", "123456")

        total = checkout_page.get_total()

        assert total == "Total: $58.29", (
            f"Ожидалось 'Total: $58.29', получено '{total}'"
        )
    finally:
        driver.quit()
