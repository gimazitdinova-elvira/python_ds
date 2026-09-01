from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_session_storage_auth():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://gitflic.ru/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    user1_cookie = {
        "name": "SESSION",
        "value": "Y2E3OGY1OWMtYzY3My00NWYwLTg3OTctNzU5ZTg1NWE4MWFl",
        'domain': '.gitflic.ru',
        "path": "/"
    }

    driver.add_cookie(user1_cookie)
    print("Cookie пользователя 1 установлены")

    driver.refresh()

    driver.get("https://gitflic.ru/user/gde_papa46000")

    url_user1 = driver.current_url
    print(f"URL пользователя 1: {url_user1}")

    driver.delete_all_cookies()
    print("Куки очищены")

    user2_cookie = {
        "name": "SESSION",
        "value": "MGIyM2NhN2UtZDNlYy00YjZiLWFmODAtNjM5MGFlYmNhZGJm",
        'domain': '.gitflic.ru',
        "path": "/"
    }

    driver.add_cookie(user2_cookie)
    print("Cookie пользователя 2 установлены")

    driver.refresh()

    driver.get("https://gitflic.ru/user/gde_papa47000")

    url_user2 = driver.current_url
    print(f"URL пользователя 2: {url_user2}")

    assert url_user1 != url_user2, "URL пользователей совпадают!"
    print("Тест пройден: URL разных пользователей различаются")

    driver.quit()








