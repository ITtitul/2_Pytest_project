import pytest
import time
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


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
    "viewport": {
        "width": 1920,
        "height": 1000
    }
}


# Открываем страницу
def test_google_search(driver):

    driver.get("http://www.google.com")


    # Ищем элемент
    search_box = driver.find_element(By.NAME, "q")


    # Вводим запрос в поисковую строку
    search_box.send_keys("sldjkfhngo;liehgjehftyh")
    time.sleep(5)


    # Отправляем запрос
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)


    # Проверяем загрузку страницы
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "botstuff")))