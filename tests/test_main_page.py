import allure
import pytest

from pages.main_page import MainPage
from data import QuestionsAndAnswers, Urls
from tests.base_test import BaseTest


class TestMainPage(BaseTest):
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    @pytest.mark.parametrize('index, question, answer', QuestionsAndAnswers.QUESTIONS)
    def test_check_question_and_answer(self, question_number, expected_text):
        page = MainPage(self.driver)
        page.open_browser(Urls.MAIN_PAGE_URL)
        page.open_question(question_number)

        assert page.check_answer_text(expected_text,question_number)
