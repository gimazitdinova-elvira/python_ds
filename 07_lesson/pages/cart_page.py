from selenium.webdriver.common.by import By


class CartPage:

    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        items = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
        return [item.text for item in items]

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        return self
