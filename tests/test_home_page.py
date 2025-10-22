from pages.home_page import HomePage
from pages.locators import HomePageLocators


def test_user_can_see_search_box_in_home_page(browser):
    link = 'https://www.booking.com'
    page = HomePage(browser, link)
    page.open()
    page.should_be_home_page()
    page.should_be_search_box_in_home_page()