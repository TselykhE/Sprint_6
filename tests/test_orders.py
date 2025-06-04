import allure
import pytest
from data import OrderData


class TestOrderPage():
    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize('button_method, data_order', [('click_first_button', OrderData.FIRST_ORDER),
                                                           ('click_second_button', OrderData.SECOND_ORDER)])
    def test_make_an_order(self, main_page, order_page, button_method, data_order):
        getattr(main_page, button_method)()
        order_page.user_rent_order(**data_order)
        assert "Заказ оформлен" in order_page.confirmation_window()
