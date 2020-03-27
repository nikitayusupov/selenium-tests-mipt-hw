from selenium.webdriver.common.by import By


class CoursePageLocators:
    def __init__(self):
        pass
        self.COURSE_ITEM = (By.CLASS_NAME, 'object-item')
        self.NEXT = (By.CLASS_NAME, 'next')
        self.MATH_LABEL = (By.XPATH, '//label[@for="category5"]')
        self.PHYS_LABEL = (By.XPATH, '//label[@for="category6"]')
        self.SUBMIT = (By.XPATH, '//button[@type="submit"]')
        self.COURSE_TITLE = (By.CLASS_NAME, 'object-title')
        # self.SEARCH_INPUT = (By.NAME, "s")
        # self.COURSE = (By.XPATH, '//a[@href="/course"]')
