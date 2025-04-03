import allure
from conftest import browser
from pages.main_page import MainPage


class TestURL:
    @allure.title('Проверка URL Логотипа "Самокат"')
    def test_main_page(self, browser):
        page = MainPage()
        page.open_browser(browser)
        page.click_scooter_button(browser)
        page.should_main_page_url(browser)

    @allure.title('Проверка URL Логотипа "Яндекс"')
    def test_dzen_url(self, browser):
        page = MainPage()
        page.open_browser(browser)
        page.click_dzen_button(browser)
        page.switching_to_the_tab(browser)
        page.wait_for_page_load(browser)
        page.should_dzen_url(browser)
