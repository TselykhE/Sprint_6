import allure


class TestURL():
    @allure.title('Проверка URL Логотипа "Самокат"')
    def test_main_page(self, main_page):
        main_page.click_scooter_button()
        main_page.should_main_page_url()

    @allure.title('Проверка URL Логотипа "Яндекс"')
    def test_dzen_url(self, main_page):
        main_page.click_dzen_button()
        main_page.switching_to_the_tab()
        main_page.wait_for_page_load()
        main_page.should_dzen_url()
