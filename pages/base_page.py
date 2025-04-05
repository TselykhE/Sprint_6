import allure

from data import Urls
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as eс


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы')
    def open_browser(self, url):
        self.driver.get(url)

    @allure.step('Скролл к элементу')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 3).until(eс.visibility_of_element_located(element))
        return self.driver.execute_script("arguments[0].scrollIntoView()", element)

    @allure.step('Ожидание открытия окна')
    def wait_for_open_window(self, locator):
        WebDriverWait(self.driver, 3).until(eс.element_to_be_clickable(locator))

    @allure.step('Поиск элемента на странице')
    def find_element(self, locator):
        WebDriverWait(self.driver, 3).until(eс.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Получить текст ответа")
    def get_text_answer(self, locator):
        element = WebDriverWait(self.driver, 3).until(eс.visibility_of_element_located(locator))
        return element.text

    @allure.step("Клик по лого 'Самокат'")
    def click_scooter_button(self):
        self.driver.find_element(*BasePageLocators.SCOOTER_BUTTON).click()

    @allure.step("Клик по лого 'Дзен'")
    def click_dzen_button(self):
        self.driver.find_element(*BasePageLocators.YANDEX_BUTTON).click()

    @allure.step("Переключение вкладки")
    def switching_to_the_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Ожидание загрузки страницы Дзен")
    def wait_for_page_load(self):
        WebDriverWait(self.driver, 10).until(
            eс.url_to_be(Urls.DZEN_URL))

    @allure.step("Проверка URL вкладки 'Дзен'")
    def should_dzen_url(self):
        assert self.driver.current_url == Urls.DZEN_URL

    @allure.step("Проверка URL после клика по логотипу 'Самокат'")
    def should_main_page_url(self):
        assert self.driver.current_url == Urls.MAIN_PAGE_URL
