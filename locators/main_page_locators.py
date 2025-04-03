from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION = [By.XPATH, "(.//div[@class='accordion__button'])[{}]"]
    ANSWER = [By.XPATH, "(.//div[@class='accordion__panel'])[{}]"]