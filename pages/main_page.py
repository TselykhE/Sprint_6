import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    @allure.step('Клик по вопросу')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION, num)
        self.scroll_to_the_last_question(MainPageLocators.QUESTION_TO_SCROLL)
        self.click_on_element(locator_q_formatted)

    @allure.step('Получение ответа')
    def get_answer(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER, num)
        return self.get_text_answer(locator_a_formatted)

    @allure.step('Получение текста ответа')
    def check_question_answer(self, num):
        self.click_to_question(num)
        return self.get_answer(num)

    @allure.step('Проверка ответа')
    def check_answer(self, num, text_answer):
        self.click_to_question(num)
        text = self.get_answer(num)
        return text == text_answer

    @allure.step("Клик по кнопке Заказать в шапке лендинга")
    def click_first_button(self):
        self.find_element_and_wait(MainPageLocators.ORDER_BUTTON_HEADER).click()

    @allure.step("Клик по кнопке Заказать в центре")
    def click_second_button(self):
        element = self.find_element_and_wait(MainPageLocators.ORDER_CENTER_BUTTON)
        if element.is_displayed():
            self.scroll_to_element(element)
            element.click()
        else:
            raise AssertionError("Элемент не отображается на странице.")
