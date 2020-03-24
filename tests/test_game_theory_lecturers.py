from pages.game_theory_page import GameTheoryPage


def test_courses_list(browser_is_opened):
    game_theory_page = GameTheoryPage(*browser_is_opened)
    lecturers = game_theory_page.get_tab_desc('lecturers')
    assert len(lecturers) == 2
    assert 'Мусатов Даниил Владимирович' in lecturers[0]
    assert 'Савватеев Алексей Владимирович' in lecturers[1]
