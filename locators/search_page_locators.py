from selenium.webdriver.common.by import By


class SearchPageLocators:
    def __init__(self):
        self.SEARCH_NONE_HIDE = (By.XPATH, '//*[@class="search-none hide"]')
        self.SEARCH_MENU = (By.CLASS_NAME, 'search-menu')
