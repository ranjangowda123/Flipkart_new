import pytest
from playwright.sync_api import sync_playwright

#Using a Custom Command-Line Argument to Select the Browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chromium")

@pytest.fixture(scope="session")
# @pytest.fixture(params=['chromium','firefox'])    # for browser run using fixture
def page(request):
    browser_type = request.config.getoption("browser_name")       #Using a Custom Command-Line Argument to Select the Browser
    with sync_playwright() as playwright:
        # browser_type = request.param  # for browser run using fixture
        browser = getattr(playwright, browser_type).launch(headless=False, slow_mo=400)   # for browser run using fixture and Custom Command-Line Argument
        page = browser.new_page()
        page.goto("https://www.myntra.com/", wait_until="load")
        yield page   # allows the page to be returned to the test, and the test can interact with it, Pass the page object to the test, it's just how pytest handles fixtures.
        browser.close()


def test_wright(page):  # When you write test_wright(page), pytest automatically detects that you are requesting a fixture named page because the test function has a parameter named page.
    pass




