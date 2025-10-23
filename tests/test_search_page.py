from pages.search import SearchPage
import time

def test_user_can_use_search_box(browser):
    link = 'https://www.booking.com'
    page = SearchPage(browser, link)
    page.open()
    time.sleep(1)
    #page.alert_accept()
    page.should_be_exact_search_direction()
    page.should_be_search_result()
    page.should_be_exact_parametrs_in_URL()

def test_user_can_not_use_empty_search_box(browser):
    link = 'https://www.booking.com'
    page = SearchPage(browser, link)
    page.open()
    time.sleep(1)
    page.search_should_not_be_work_with_empty_data()

def test_user_can_see_results(browser):
    link = 'https://www.booking.com'
    page = SearchPage(browser, link)
    page.open()
    time.sleep(1)
    page.should_be_exact_search_direction()
    page.should_be_actual_results()