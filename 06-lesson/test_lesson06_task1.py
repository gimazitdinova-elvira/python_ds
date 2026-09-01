from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 20)
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    wait = WebDriverWait(driver, 20)
    hello_text_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    driver.save_screenshot("screenshots/dynamic_loading.png")

    actual_text = hello_text_element.text
    assert actual_text == "Hello World!", f"Expected 'Hello World!', but got '{actual_text}'"

    print("Тест успешно пройден!")

    driver.quit()






