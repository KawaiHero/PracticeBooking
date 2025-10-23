from selenium.webdriver.common.by import By

class HomePageLocators:
    MAIN_LOGO = (By.CSS_SELECTOR, '[data-testid="header-booking-logo"]')
    SEARCH_BOX = (By.CSS_SELECTOR, '[data-testid="searchbox-layout-wide"]')

class SearchLocators:
    SEARCH_PLACE = (By.CSS_SELECTOR, '[data-testid="destination-container"] [id=":rh:"]')
    DATA_FIELD = (By.CSS_SELECTOR, '[data-testid="date-display-field-start"]')
    DATE_23 = (By.CSS_SELECTOR, '[data-date="2025-10-23"]')
    DATE_26 = (By.CSS_SELECTOR, '[data-date="2025-10-26"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    SEARCH_RESULT = (By.CSS_SELECTOR, '[data-testid="property-card"]')
    FINDED_DIRECTION = (By.CSS_SELECTOR, '[class="d4a98186ec bcadb1ad26 caf6a23fb4"] h1')
    SEARCH_BOX_ALERT = (By.CSS_SELECTOR, '[data-testid="searchbox-alert"]')
    RESULT_TITLE = (By.CSS_SELECTOR, '[data-testid="title"]')
    RESULT_PRICE = (By.CSS_SELECTOR, '[data-testid="price-and-discounted-price"]')
    RESULT_AVAILABILITY = (By.CSS_SELECTOR, '[data-testid="availability-cta-btn"]')