from selenium.webdriver.support.expected_conditions import alert_is_present

from .base_page import BasePage
from .locators import SearchLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(BasePage):
    def alert_accept(self):
        wait = WebDriverWait(self.browser, 5).until(EC.alert_is_present())
        wait.accept()

    def should_be_search_result(self):
        result = self.browser.find_elements(*SearchLocators.SEARCH_RESULT)
        assert len(result) > 0, 'The search result is empty'

    def should_be_exact_search_direction(self):
        direction = self.browser.find_element(*SearchLocators.SEARCH_PLACE)
        direction.send_keys('Warsaw')
        data_field = self.browser.find_element(*SearchLocators.DATA_FIELD)
        data_field.click()
        self.browser.find_element(*SearchLocators.DATE_23).click()
        self.browser.find_element(*SearchLocators.DATE_26).click()
        self.browser.find_element(*SearchLocators.SEARCH_BUTTON).click()
        finded_direction = self.browser.find_element(*SearchLocators.FINDED_DIRECTION)
        assert 'Warsaw' in finded_direction.text

    def should_be_exact_parametrs_in_URL(self):
        assert 'checkin' and 'group_adults' and 'checkout' in self.browser.current_url, "There is wrong data in URL!"

    def search_should_not_be_work_with_empty_data(self):
        direction = self.browser.find_element(*SearchLocators.SEARCH_PLACE)
        direction.send_keys(' ')
        self.browser.find_element(*SearchLocators.SEARCH_BUTTON).click()
        assert self.is_element_present(*SearchLocators.SEARCH_BOX_ALERT), 'The alert does not appear'

    def should_be_actual_results(self):
        assert self.is_element_present(*SearchLocators.RESULT_TITLE) \
               and self.is_element_present(*SearchLocators.RESULT_PRICE)\
               and self.is_element_present(*SearchLocators.RESULT_AVAILABILITY), 'The search result is not expected'

