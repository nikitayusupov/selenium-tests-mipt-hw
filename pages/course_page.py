from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from locators.course_page_locators import CoursePageLocators
from selenium.webdriver.support import expected_conditions as EC


class CoursePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get("https://lectoriy.mipt.ru/course/")
        self.title = self.driver.title
        self.locators = CoursePageLocators()

    def calc_courses_cnt(self):
        ans = 0
        while True:
            courses = self.wait.until(EC.presence_of_all_elements_located(self.locators.COURSE_ITEM))
            ans += len(courses)
            try:
                next_page_link = self.wait.until(EC.presence_of_element_located(self.locators.NEXT)).find_element_by_tag_name('a').get_attribute("href")
            except NoSuchElementException:
                break
            self.driver.get(next_page_link)
        return ans

    # проверить что все лекторы есть в списке лекторов

    def get_courses(self, course_type):
        titles = set()
        assert course_type in ['math', 'phys']
        if course_type == 'math':
            math_label = self.wait.until(EC.presence_of_element_located(self.locators.MATH_LABEL))
            math_label.click()
        elif course_type == 'phys':
            phys_label = self.wait.until(EC.presence_of_element_located(self.locators.PHYS_LABEL))
            phys_label.click()

        submits = self.wait.until(EC.presence_of_all_elements_located(self.locators.SUBMIT))
        submits[2].click()

        while True:
            course_titles = self.wait.until(EC.presence_of_all_elements_located(self.locators.COURSE_TITLE))
            for course_title in course_titles:
                titles.add(course_title.text)
            try:
                next_page_link = self.wait.until(EC.presence_of_element_located(self.locators.NEXT)).find_element_by_tag_name('a').get_attribute("href")
            except NoSuchElementException:
                break
            self.driver.get(next_page_link)

        return titles
