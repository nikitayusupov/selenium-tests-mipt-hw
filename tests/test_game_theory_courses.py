from pages.game_theory_page import GameTheoryPage


def test_courses_list(browser_is_opened):
    game_theory_page = GameTheoryPage(*browser_is_opened)
    courses = game_theory_page.get_tab_desc('courses')
    assert len(courses) == 1
    assert 'Теория Игр' in courses[0]
