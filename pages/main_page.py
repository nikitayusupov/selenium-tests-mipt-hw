from selenium.webdriver.common.keys import Keys
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions


class MainPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get("https://lectoriy.mipt.ru/")
        self.title = self.driver.title
        self.locators = MainPageLocators()

    def search(self, search_string):
        elem = self.wait.until(expected_conditions.presence_of_element_located(self.locators.SEARCH_INPUT))
        elem.clear()
        elem.send_keys(search_string)
        elem.send_keys(Keys.RETURN)
        
