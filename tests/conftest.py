import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

from data import Urls
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture
def get_driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver

    driver.quit()

@pytest.fixture
def main_page(get_driver):
    page = MainPage(get_driver)
    page.open_browser(Urls.MAIN_PAGE_URL)
    return page

@pytest.fixture
def order_page(get_driver):
    page = OrderPage(get_driver)
    return page
