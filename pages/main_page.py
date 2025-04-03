import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import browser
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Скролл к вопросам")
    def scroll_to_faq(self, browser):
        element = browser.find_element(By.CLASS_NAME, "accordion")
        browser.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Извлечение вопроса")
    def get_question(self, browser, index):
        question_locator = (MainPageLocators.QUESTION[0], MainPageLocators.QUESTION[1].format(index))
        question = WebDriverWait(browser, 3).until(ec.element_to_be_clickable(question_locator))
        question.click()
        return question.text

    @allure.step("Извлечение ответа")
    def get_answers(self, browser, index):
        answers_locator = (MainPageLocators.ANSWER[0], MainPageLocators.ANSWER[1].format(index))
        answers = browser.find_element(*answers_locator)
        return answers.text
