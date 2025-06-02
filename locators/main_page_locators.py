from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION = By.XPATH, "//div[@id='accordion__heading-{}']"
    ANSWER = By.XPATH, "//div[@id='accordion__panel-{}']"
    QUESTION_TO_SCROLL = By.XPATH, "//div[@id='accordion__heading-7']"
