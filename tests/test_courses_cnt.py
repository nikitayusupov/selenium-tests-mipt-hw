from pages.course_page import CoursePage
from pages.main_page import MainPage


def test_courses_list(browser_is_opened):
    main_page = MainPage(*browser_is_opened)
    courses_cnt_main = main_page.get_cnt_courses()
    course_page = CoursePage(*browser_is_opened)
    courses_cnt_calc = course_page.calc_courses_cnt()
    assert courses_cnt_calc == courses_cnt_main
