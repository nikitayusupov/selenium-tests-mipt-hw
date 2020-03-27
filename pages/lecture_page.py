from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from locators.lecture_page_locators import LecturePageLocators
from selenium.webdriver.support import expected_conditions as EC


class LecturePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get("https://lectoriy.mipt.ru/lecture")
        self.title = self.driver.title
        self.locators = LecturePageLocators()

    def get_lecturer_names(self):
        lecturer_names = set()
        while True:
            lecturers = self.wait.until(EC.presence_of_all_elements_located(self.locators.LECTURER))
            for lecturer in lecturers:
                for name in lecturer.text.split(','):
                    lecturer_names.add(name.strip())
            try:
                next_page_link = self.wait.until(EC.presence_of_element_located(self.locators.NEXT)).find_element_by_tag_name('a').get_attribute("href")
            except NoSuchElementException:
                break
            self.driver.get(next_page_link)
        return lecturer_names
