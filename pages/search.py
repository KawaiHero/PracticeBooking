from .base_page import BasePage
from .locators import SearchLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, timedelta
from urllib.parse import urlparse, parse_qs

class SearchPage(BasePage):
    def open_and_accept(self):
        self.open()
        self.accept_cookies_if_present()


    def should_be_search_result(self):
        result = self.browser.find_elements(*SearchLocators.SEARCH_RESULT)
        assert len(result) > 0, 'The search result is empty'

    def set_destination(self, city: str):
        field = self.wait_clickable(SearchLocators.SEARCH_PLACE)
        field.clear()
        field.send_keys(city)

    def open_calendar(self):
        self.click(SearchLocators.DATA_FIELD)

    def set_dates(self, checkin: date, checkout: date):
        self.open_calendar()
        self.pick_date(checkin.isoformat())
        self.pick_date(checkout.isoformat())

    def submit(self):
        self.click(SearchLocators.SEARCH_BUTTON)

    def search_city_with_dates(self, city: str, nights: int = 3):
        checkin = date.today() + timedelta(days=1)
        checkout = checkin + timedelta(days=nights)
        self.set_destination(city)
        self.set_dates(checkin, checkout)
        self.submit()

    def wait_results_loaded(self, min_cards=1, timeout=20):
        self.wait_visible(SearchLocators.SEARCH_RESULT, timeout)
        WebDriverWait(self.browser, timeout).until(
            lambda d: len(d.find_elements(*SearchLocators.RESULT_CARD)) >= min_cards
        )

    def url_has_dates_and_adults(self):
        qs = parse_qs(urlparse(self.browser.current_url).query)
        return all(k in qs for k in ("checkin", "checkout", "group_adults"))

    def should_be_exact_parametrs_in_URL(self):
        assert 'checkin' and 'group_adults' and 'checkout' in self.browser.current_url,\
            "There is wrong data in URL!"

    def search_should_not_be_work_with_empty_data(self):
        direction = self.browser.find_element(*SearchLocators.SEARCH_PLACE)
        direction.send_keys(' ')
        self.browser.find_element(*SearchLocators.SEARCH_BUTTON).click()
        assert self.is_element_present(*SearchLocators.SEARCH_BOX_ALERT), \
            'The alert does not appear'

    def should_be_actual_results(self):
        assert self.is_element_present(*SearchLocators.RESULT_TITLE) \
               and self.is_element_present(*SearchLocators.RESULT_PRICE)\
               and self.is_element_present(*SearchLocators.RESULT_AVAILABILITY), \
            'The search result is not expected'

    def wait_results_loaded(self, min_cards: int = 1, timeout: int = 20):
            WebDriverWait(self.browser, timeout).until(
                lambda d: len(d.find_elements(*SearchLocators.RESULT_CARD)) >= min_cards
            )

    def cards_count(self) -> int:
            return len(self.browser.find_elements(*SearchLocators.RESULT_CARD))
