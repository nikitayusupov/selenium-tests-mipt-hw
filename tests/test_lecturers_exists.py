from pages.lecture_page import LecturePage
from pages.lecturer_page import LecturerPage


def test_lecturers(browser_is_opened):
    lecture_page = LecturePage(*browser_is_opened)
    lecturer_names_from_lectures = lecture_page.get_lecturer_names()
    print(lecturer_names_from_lectures)
    lecturer_page = LecturerPage(*browser_is_opened)
    lecturer_names_from_lecturers = lecturer_page.get_lecturer_names()
    print(lecturer_names_from_lecturers)
    assert lecturer_names_from_lectures <= lecturer_names_from_lecturers
