from pages.course_page import CoursePage


def test_math_not_phys(browser_is_opened):
    courses_page = CoursePage(*browser_is_opened)
    math_courses = courses_page.get_courses('math')
    print(math_courses)
    courses_page = CoursePage(*browser_is_opened)
    phys_courses = courses_page.get_courses('phys')
    print(phys_courses)
    assert len(math_courses.intersection(phys_courses)) == 0
