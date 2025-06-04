import allure
import pytest

from data import MainData


class TestMainPage():
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_check_answer(self, main_page, num):

        assert main_page.check_question_answer(num) == MainData.text_answer[num]
