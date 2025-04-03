import allure
from conftest import browser
from conftest import base_page


class TestURL:
    @allure.title('Проверка URL Логотипа "Самокат"')
    def test_main_page(self, browser, base_page):
        base_page.open_browser(browser)
        base_page.click_order_button(browser)
        base_page.click_scooter_button(browser)
        base_page.should_main_page_url(browser)

    @allure.title('Проверка URL Логотипа "Яндекс"')
    def test_dzen_url(self, browser, base_page):
        base_page.open_browser(browser)
        base_page.click_dzen_button(browser)
        base_page.switching_to_the_tab(browser)
        base_page.wait_for_page_load(browser)
        base_page.should_dzen_url(browser)
