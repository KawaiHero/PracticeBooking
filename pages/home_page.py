from .base_page import BasePage
from .locators import HomePageLocators

class HomePage(BasePage):
    def should_be_home_page(self):
        assert self.is_element_present(*HomePageLocators.MAIN_LOGO), 'The main logo does not appear'

    def should_be_search_box_in_home_page(self):
        assert self.is_element_present(*HomePageLocators.SEARCH_BOX), 'The search box does not appear'


