from selenium.webdriver.common.by import By

class BasePageLocators:
    COOKIES_ACCEPT = (By.CSS_SELECTOR, 'button[aria-label="Accept"], #onetrust-accept-btn-handler, button:has([data-cookie-banner="accept"])')

class HomePageLocators:
    MAIN_LOGO = (By.CSS_SELECTOR, '[data-testid="header-booking-logo"]')
    SEARCH_BOX = (By.CSS_SELECTOR, '[data-testid="searchbox-layout-wide"]')

class SearchLocators:
    SEARCH_PLACE = (By.CSS_SELECTOR, '[data-testid="destination-container"] input, [data-testid="destination-input"]')
    DATA_FIELD = (By.CSS_SELECTOR, '[data-testid="date-display-field-start"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

    SEARCH_RESULT = (By.CSS_SELECTOR, '[data-testid="search-results"]')
    RESULT_CARD = (By.CSS_SELECTOR, '[data-testid="property-card"]')
    RESULT_TITLE = (By.CSS_SELECTOR, '[data-testid="title"]')
    RESULT_PRICE = (By.CSS_SELECTOR, '[data-testid="price-and-discounted-price"], [data-testid="price"]')
    RESULT_AVAILABILITY = (By.CSS_SELECTOR, '[data-testid="availability-cta"]')
    SEARCH_BOX_ALERT = (By.CSS_SELECTOR, '[data-testid="searchbox-alert"]')
    RESULT_PAGE_TITLE = (By.CSS_SELECTOR, '[data-testid="PropertyHeaderDesktop-wrapper"] h2')
    RESULT_PAGE_ROOMS_TABLE = (By.CSS_SELECTOR, '[id="rooms_table"]')