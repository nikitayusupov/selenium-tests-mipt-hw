from selenium.webdriver.common.by import By


class LecturerPageLocators:
    def __init__(self):
        pass
        self.LECTURERS = (By.TAG_NAME, 'sup')
        self.LECTURER_ITEM = (By.CLASS_NAME, 'lecturer-item')
        self.NEXT = (By.CLASS_NAME, 'next')
