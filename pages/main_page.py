import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    @allure.step("Открыть вопрос")
    def open_question(self, question_number):
        question_locator = MainPageLocators.question_number(question_number)
        self.scroll_to_element(MainPageLocators.FAQ)
        self.wait_for_open_window(question_locator)
        self.scroll_to_element(question_locator).click()

    @allure.step("Сравни текст ответа")
    def check_answer_text(self, expected_text, answer_number):
        answer_locator = MainPageLocators.answer_number(answer_number)
        self.wait_for_open_window(answer_locator)
        actual_text = self.get_text_answer(answer_locator)
        return actual_text == expected_text
