from selenium.webdriver.common.by import By


class GameTheoryPageLocators:
    def __init__(self):
        self.LECTURERS = (By.XPATH, '//a[@href="#lecturers"]')
        self.COURSES = (By.XPATH, '//a[@href="#courses"]')
        self.ACTIVE_TAB = (By.XPATH, '//*[@class="result-tab tab-pane active"]')
