from selenium.webdriver.common.by import By


class MainPageLocators:
    def __init__(self):
        self.SEARCH_INPUT = (By.NAME, "s")
        self.COURSE = (By.XPATH, '//a[@href="/course"]')
