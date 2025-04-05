import allure
from data import Urls
from pages.main_page import MainPage
from tests.base_test import BaseTest


class TestURL(BaseTest):
    @allure.title('Проверка URL Логотипа "Самокат"')
    def test_main_page(self):
        page = MainPage(self.driver)
        page.open_browser(Urls.MAIN_PAGE_URL)
        page.click_scooter_button()
        page.should_main_page_url()

    @allure.title('Проверка URL Логотипа "Яндекс"')
    def test_dzen_url(self):
        page = MainPage(self.driver)
        page.open_browser(Urls.MAIN_PAGE_URL)
        page.click_dzen_button()
        page.switching_to_the_tab()
        page.wait_for_page_load()
        page.should_dzen_url()
