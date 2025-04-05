import allure
import pytest
from data import OrderData, Urls
from pages.order_page import OrderPage
from tests.base_test import BaseTest


class TestOrderPage(BaseTest):
    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize('button_method, data_order', [('click_first_button', OrderData.FIRST_ORDER),
                                                           ('click_second_button', OrderData.SECOND_ORDER)])
    def test_make_an_order(self, data_order, button_method):
        page = OrderPage(self.driver)
        page.open_browser(Urls.MAIN_PAGE_URL)
        getattr(page, button_method)()
        page.user_rent_order(**data_order)
        page.confirmation_window()
