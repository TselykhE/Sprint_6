import allure
from selenium.webdriver import ActionChains

from data import Urls
from locators.logo_locators import LogoLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('Открытие страницы')
    def open_browser(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента на странице с ожиданием')
    def find_element_and_wait(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Скролл к элементу')
    def scroll_to_element(self, locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', locator)

    @allure.step('Скролл к последнему вопросу')
    def scroll_to_the_last_question(self, locator):
        element = self.find_element_and_wait(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ожидание открытия окна')
    def wait_for_open_window(self, locator):
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(locator))

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step("Получить текст ответа")
    def get_text_answer(self, locator):
        return self.find_element_and_wait(locator).text

    @allure.step("Форматирование локаторов")
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)

        return method, locator

    @allure.step("Клик по лого 'Самокат'")
    def click_scooter_button(self):
        self.driver.find_element(*LogoLocators.SCOOTER_BUTTON).click()

    @allure.step("Клик по лого 'Дзен'")
    def click_dzen_button(self):
        self.driver.find_element(*LogoLocators.YANDEX_BUTTON).click()

    @allure.step("Переключение вкладки")
    def switching_to_the_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Ожидание загрузки страницы Дзен")
    def wait_for_page_load(self):
        WebDriverWait(self.driver, 10).until(ec.url_to_be(Urls.DZEN_URL))

    @allure.step("Проверка URL вкладки 'Дзен'")
    def should_dzen_url(self):
        assert self.driver.current_url == Urls.DZEN_URL

    @allure.step("Проверка URL после клика по логотипу 'Самокат'")
    def should_main_page_url(self):
        assert self.driver.current_url == Urls.MAIN_PAGE_URL
