from selenium.webdriver.common.keys import Keys
from locators.search_page_locators import SearchPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


class SearchResultsPage:
    def __init__(self, driver, wait):
        self.page_source = driver.page_source
        self.wait = wait
        self.driver = driver
        self.locators = SearchPageLocators()

    def results_found(self):
        elem = self.wait.until(expected_conditions.presence_of_element_located(self.locators.SEARCH_MENU))
        try:
            elem.find_element_by_xpath(self.locators.SEARCH_NONE_HIDE[1])
            return True
        except NoSuchElementException:
            return False

