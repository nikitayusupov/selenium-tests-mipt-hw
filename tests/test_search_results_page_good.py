from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


def test_lectoriy_search_good(browser_is_opened):
    lectoriy_main_page = MainPage(*browser_is_opened)
    assert "Физтех" in lectoriy_main_page.title
    lectoriy_main_page.search("теория игр")
    search_results_page = SearchResultsPage(*browser_is_opened)
    assert search_results_page.results_found()
    
