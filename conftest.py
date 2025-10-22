import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language: e.g. --language=fr or --language=ru"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run in headless mode"
    )

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    headless = request.config.getoption("headless")
    print(f"\nstart browser for test.. language={user_language}")

    options = Options()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": user_language}
    )
    if headless:
        options.add_argument("--headless")


    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()
