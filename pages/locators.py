from selenium.webdriver.common.by import By

class HomePageLocators:
    MAIN_LOGO = (By.CSS_SELECTOR, '[data-testid="header-booking-logo"]')
    SEARCH = (By.CSS_SELECTOR, '[data-testid="searchbox-layout-wide"]')