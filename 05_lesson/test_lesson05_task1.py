from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://httpbin.qa-territory.online')
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    assert driver.current_url == "https://httpbin.qa-territory.online/forms/post"
    driver.back()
    assert driver.current_url == "https://httpbin.qa-territory.online/"

    driver.quit()






