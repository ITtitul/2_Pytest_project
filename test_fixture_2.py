import pytest


@pytest.fixture()
def setting_browser():
    browser.config.window_height = 1000
    browser.config.window_width = 1920

    yeild
    browser.quit()