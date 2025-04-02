import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_google_no_results(driver):
    # Открываем Google
    driver.get("http://www.google.com")

    # Ищем поле поиска
    search_box = driver.find_element(By.NAME, "q")

    # Вводим редкий поисковый запрос
    search_box.send_keys("sldjkfhngo;liehgjehftyh")
    search_box.send_keys(Keys.RETURN)

    # Ожидаем, пока загрузятся результаты
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "botstuff")))

    # Проверяем, есть ли блоки результатов (обычно у них класс "g")
    results = driver.find_elements(By.CLASS_NAME, "g")

    # Проверяем, что результатов нет
    assert len(results) == 0, "Ожидалось, что результатов не будет, но они найдены!"
