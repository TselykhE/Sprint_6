import allure
import pytest
from data import OrderData
from pages.order_page import OrderPage
from conftest import browser


class TestOrderPage:
    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize('button_method, data_order', [('click_first_button', OrderData.FIRST_ORDER),
                                                           ('click_second_button', OrderData.SECOND_ORDER)])
    def test_make_an_order(self, browser, data_order, button_method):
        page = OrderPage()
        page.open_browser(browser)
        getattr(page, button_method)(browser)
        page.user_rent_order(browser, **data_order)
        page.confirmation_window(browser)
