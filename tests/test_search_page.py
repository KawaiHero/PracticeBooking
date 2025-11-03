from pages.locators import SearchLocators
from pages.search import SearchPage
import pytest

BASE = "https://www.booking.com/"

def test_user_can_use_search_box(browser):
    page = SearchPage(browser, BASE)
    page.open_and_accept()
    page.close_entry_window()
    page.search_city_with_dates("Warsaw", nights=3)
    page.wait_results_loaded(min_cards=1)
    assert page.url_has_dates_and_adults()
    assert page.cards_count() > 0

def test_user_cannot_use_empty_search(browser):
    page = SearchPage(browser, BASE)
    page.open_and_accept()
    page.close_entry_window()
    page.submit()
    assert page.is_element_present(*SearchLocators.SEARCH_BOX_ALERT) or not page.url_has_dates_and_adults()

@pytest.mark.parametrize("city", ["Warsaw", "Kraków", "Gdańsk"])
def test_results_have_basic_elements(browser, city):
    page = SearchPage(browser, BASE)
    page.open_and_accept()
    page.close_entry_window()
    page.search_city_with_dates(city, nights=2)
    page.wait_results_loaded(min_cards=1)
    assert page.safe_get_text(SearchLocators.RESULT_TITLE) != ""
    raw = page.safe_get_text(SearchLocators.RESULT_PRICE)
    price = int(''.join(ch for ch in raw if ch.isdigit()))
    assert price > 0
    assert page.is_element_present(*SearchLocators.RESULT_AVAILABILITY)