from selenium.webdriver.common.by import By


class LecturePageLocators:
    def __init__(self):
        pass
        # self.LECTURERS = (By.TAG_NAME, 'sup')
        self.LECTURER = (By.CLASS_NAME, 'object-lecturers')
        self.NEXT = (By.CLASS_NAME, 'next')
