from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://httpbin.qa-territory.online/links/10")
    driver.maximize_window()

    all_links = driver.find_elements(By.TAG_NAME, "a")
    expected_count = 9
    actual_count = len(all_links)
    assert actual_count == expected_count, \
        f"Ожидалось {expected_count} ссылок, найдено {actual_count}"

    for i, link in enumerate(all_links):
        assert link.is_displayed(), f"Ссылка с индексом {i} не отображается"
    print("✅ Все ссылки отображаются")

    first_link_text = all_links[0].text
    assert "1" in first_link_text, \
        f"Текст первой ссылки ('{first_link_text}') не содержит '1'"

    print(f"✅ Первая ссылка содержит '1': '{first_link_text}'")
    print(f"✅ Все проверки пройдены! Найдено {actual_count} ссылок.")

    driver.quit()




