import pytest
from selenium import webdriver
from pages.base_page import BasePage


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver

    driver.quit()
