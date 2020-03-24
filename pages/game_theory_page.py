from selenium.webdriver.common.keys import Keys
from locators.game_theory_page_locators import GameTheoryPageLocators
from selenium.webdriver.support import expected_conditions


class GameTheoryPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get("https://lectoriy.mipt.ru/search?s=теория+игр")
        self.title = self.driver.title
        self.locators = GameTheoryPageLocators()

    def get_tab_desc(self, tab_name):
        assert tab_name in ['lecturers', 'courses']
        if tab_name == 'lecturers':
            locator = self.locators.LECTURERS
        elif tab_name == 'courses':
            locator = self.locators.COURSES
        elem = self.wait.until(expected_conditions.presence_of_element_located(locator))
        elem.click()
        active_tab = self.wait.until(expected_conditions.presence_of_element_located(self.locators.ACTIVE_TAB))
        items = active_tab.find_elements_by_xpath('//*[@class="result-item item"]')
        return [item.text for item in items if len(item.text) > 0]
