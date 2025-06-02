import allure
import pytest

from pages.main_page import MainPage
from data import MainData, Urls
from tests.base_test import BaseTest


class TestMainPage(BaseTest):
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_check_answer(self, num):
        page = MainPage(self.driver)
        page.open_browser(Urls.MAIN_PAGE_URL)

        assert page.check_question_answer(num) == MainData.text_answer[num]
