import pytest
#from selene import browser
from selenium import webdriver

# @pytest.fixture()
# def setting_browser():
#     browser.config.window_height = 1080  # задает высоту окна браузера
#     browser.config.window_width = 1920  # задает ширину окна браузера
#
#     yield

#browser.quit() # закрывает браузер после выполнения теста

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