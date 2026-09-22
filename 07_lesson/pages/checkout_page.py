from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        return self

    def get_total(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        return self.driver.find_element(*self.TOTAL_LABEL).text
