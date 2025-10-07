import pytest
from urls import Urls
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.FORM_FIELDS)
    yield driver
    driver.quit()