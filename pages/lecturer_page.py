from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from locators.lecturer_page_locators import LecturerPageLocators
from selenium.webdriver.support import expected_conditions as EC


class LecturerPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get("https://lectoriy.mipt.ru/lecturer")
        self.title = self.driver.title
        self.locators = LecturerPageLocators()

    def get_lec_cnt(self):
        elem = self.wait.until(EC.presence_of_element_located(self.locators.LECTURERS))
        return int(elem.text)

    def calc_lecturers_cnt(self):
        return len(self.get_lecturer_names())

    def get_lecturer_names(self):
        lecturer_names = set()
        while True:
            lecturers = self.wait.until(EC.presence_of_all_elements_located(self.locators.LECTURER_ITEM))
            for lecturer in lecturers:
                lecturer_names.add(lecturer.text.strip())
            try:
                next_page_link = self.wait.until(EC.presence_of_element_located(self.locators.NEXT)).find_element_by_tag_name('a').get_attribute("href")
            except NoSuchElementException:
                break
            self.driver.get(next_page_link)
        return lecturer_names
