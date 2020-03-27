from pages.lecturer_page import LecturerPage


def test_lecturers(browser_is_opened):
    lec_page = LecturerPage(*browser_is_opened)
    lec_cnt = lec_page.get_lec_cnt()
    print(lec_cnt)
    lec_cnt_calc = lec_page.calc_lecturers_cnt()
    print(lec_cnt_calc)
    assert lec_cnt_calc == lec_cnt
