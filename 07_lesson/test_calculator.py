
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


def test_slow_calculator():
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        page = CalculatorPage(driver)
        page.open()
        page.set_delay(45)
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

        result = page.get_result(timeout=50)
        assert result == "15", f"Ожидалось 15, получено {result}"
    finally:
        driver.quit()