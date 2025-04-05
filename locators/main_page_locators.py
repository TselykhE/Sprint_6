from selenium.webdriver.common.by import By


class MainPageLocators:

    FAQ = (By.CLASS_NAME, "Home_FAQ__3uVm4")

    @staticmethod
    def question_number(quest):
        return By.XPATH, f"//div[@id='accordion__heading-{quest}']"

    @staticmethod
    def answer_number(quest):
        return By.XPATH, f"//div[@id='accordion__panel-{quest}']//p"