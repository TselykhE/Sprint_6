from selenium.webdriver.common.by import By


class MainPageLocators:

    ORDER_BUTTON_HEADER = By.XPATH, "//button[text()='Заказать']"
    ORDER_CENTER_BUTTON = By.CLASS_NAME, "Home_FinishButton__1_cWm"
        # By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]//button")

    QUESTION = By.XPATH, "//div[@id='accordion__heading-{}']"
    ANSWER = By.XPATH, "//div[@id='accordion__panel-{}']"
    QUESTION_TO_SCROLL = By.XPATH, "//div[@id='accordion__heading-7']"
