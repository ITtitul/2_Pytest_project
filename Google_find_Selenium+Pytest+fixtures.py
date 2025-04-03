import time
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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