from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_DISPLAY = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(str(seconds))
        return self

    def click_button(self, label):
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{label}']"
        )
        button.click()
        return self

    def get_result(self, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.RESULT_DISPLAY, "15")
        )
        return self.driver.find_element(*self.RESULT_DISPLAY).text