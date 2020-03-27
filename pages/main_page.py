from selenium.webdriver.common.keys import Keys
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get("https://lectoriy.mipt.ru/")
        self.title = self.driver.title
        self.locators = MainPageLocators()

    def search(self, search_string):
        elem = self.wait.until(EC.presence_of_element_located(self.locators.SEARCH_INPUT))
        elem.clear()
        elem.send_keys(search_string)
        elem.send_keys(Keys.RETURN)

    def get_cnt_courses(self):
        elems = self.wait.until(EC.presence_of_all_elements_located(self.locators.COURSE))
        return int(elems[1].text.split()[0])
