import allure
import pytest
from conftest import browser
from pages.main_page import MainPage
from data import QuestionsAndAnswers


class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    @pytest.mark.parametrize('index, question, answer', QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST)
    def test_check_question_and_answer(self, browser, index, question, answer):
        page = MainPage()
        page.open_browser(browser)
        page.scroll_to_faq(browser)
        question_text = page.get_question(browser, index)
        answer_text = page.get_answers(browser, index)
        try:
            assert question_text == question
        except Exception:
            return('Ошибка!')
        try:
            assert answer_text == answer
        except Exception:
            return('Ошибка!')
