import allure

from locators.order_locators import OrderLocators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super(OrderPage, self).__init__(driver)

    @allure.step("Клик по кнопке Заказать в шапке лендинга")
    def click_first_button(self):
        self.find_element_and_wait(OrderLocators.ORDER_BUTTON_HEADER).click()

    @allure.step("Клик по кнопке Заказать в центре")
    def click_second_button(self):
        element = self.find_element_and_wait(OrderLocators.ORDER_CENTER_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Заполнение поля Имя")
    def user_name(self, name):
        self.find_element_and_wait(OrderLocators.NAME).send_keys(name)

    @allure.step("Заполнение поля Фамилия")
    def user_last_name(self, last_name):
        self.find_element_and_wait(OrderLocators.LAST_NAME).send_keys(last_name)

    @allure.step("Заполнение поля Адрес")
    def user_address(self, address):
        self.find_element_and_wait(OrderLocators.ADDRESS).send_keys(address)

    @allure.step("Заполнение поля Метро")
    def metro(self, metro):
        self.find_element_and_wait(OrderLocators.METRO).send_keys(metro)
        self.find_element_and_wait(OrderLocators.LIST_STATION).click()

    @allure.step("Заполнение поля Телефон")
    def user_phone(self, phone):
        self.find_element_and_wait(OrderLocators.NUMBER).send_keys(phone)

    @allure.step('Клик по кнопке "Далее" в форме информации о пользователе')
    def click_button_next(self):
        self.find_element_and_wait(OrderLocators.NEXT_BUTTON).click()

    @allure.step("Заполнение поля Дата доставки")
    def date_of_delivery(self, data):
        (self.find_element_and_wait(OrderLocators.DATE_DELIVERY)
         .send_keys(data, Keys.ENTER))

    @allure.step("Заполнение поля Время аренды")
    def rental_time(self, day):
        self.find_element_and_wait(OrderLocators.RENT_TIME).click()
        select_rent_time_locator = (OrderLocators.SELECT_RENT_TIME[0], OrderLocators.SELECT_RENT_TIME[1].format(day))
        self.find_element_and_wait(select_rent_time_locator).click()

    @allure.step("Выбор цвета")
    def checkbox_color(self, color):
        if color == 'чёрный жемчуг':
            self.find_element_and_wait(OrderLocators.BLACK_COLOR_CHECKBOX).click()
        elif color == 'серая безысходность':
            self.find_element_and_wait(OrderLocators.GREY_COLOR_CHECKBOX).click()

    @allure.step("Заполнение поля Комментарии к заказу")
    def comment_for_courier(self, comment):
        self.find_element_and_wait(OrderLocators.COMMENT).send_keys(comment)

    @allure.step("Клик по кнопке Заказать")
    def click_button_order(self):
        self.find_element_and_wait(OrderLocators.ORDER_BUTTON).click()

    @allure.step("Клик по кнопке 'Да' в окне подтверждения заказа")
    def click_button_confirmations(self):
        self.find_element_and_wait(OrderLocators.YES_BUTTON).click()

    @allure.step("Проверка текста в окне подтверждения заказа")
    def confirmation_window(self):
        text = self.find_element_and_wait(OrderLocators.ORDER_COMPLETED).text
        assert 'Заказ оформлен' in text

    @allure.step("Полный позитивный сценарий")
    def user_rent_order(self, name, last_name, address, metro, number, delivery_date, rent_days, colour, comment):
        self.user_name(name)
        self.user_last_name(last_name)
        self.user_address(address)
        self.metro(metro)
        self.user_phone(number)
        self.click_button_next()
        self.date_of_delivery(delivery_date)
        self.rental_time(rent_days)
        self.checkbox_color(colour)
        self.comment_for_courier(comment)
        self.click_button_order()
        self.click_button_confirmations()
        self.confirmation_window()
