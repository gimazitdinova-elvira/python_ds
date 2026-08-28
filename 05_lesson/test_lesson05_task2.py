from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_form_submission():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://httpbin.qa-territory.online/forms/post')
    driver.maximize_window()

    driver.find_element(By.NAME, "custname").send_keys('Эльвира')
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert driver.current_url != "https://httpbin.qa-territory.online/forms/post"

    driver.quit()







