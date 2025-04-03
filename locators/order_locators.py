from selenium.webdriver.common.by import By


class OrderLocators:
    ORDER_BUTTON_HEADER = [By.XPATH, "//button[text()='Заказать']"]
    ORDER_CENTER_BUTTON = [By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]//button"]

    # Данные пользователя
    NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    LAST_NAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    LIST_STATION = [By.XPATH, "//li[@data-index='0']"]
    NUMBER = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]

    # Окно "Про аренду"
    DATE_DELIVERY = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    RENT_TIME = [By.XPATH, '//div[text()="* Срок аренды"]']
    SELECT_RENT_TIME = [By.XPATH, '//div[text()="{}"]']
    BLACK_COLOR_CHECKBOX = [By.XPATH, '//label[@for="black"]']
    GREY_COLOR_CHECKBOX = [By.XPATH, '//label[@for="grey"]']
    COMMENT = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']
    YES_BUTTON = [By.XPATH, ".//button[text()='Да']"]

    # Текст окна "Заказ оформлен"
    ORDER_COMPLETED = [By.XPATH, '//div[contains(text(), "Заказ оформлен")]']
