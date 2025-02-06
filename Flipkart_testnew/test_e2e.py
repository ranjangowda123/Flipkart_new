from playwright.sync_api import Page

from pageobjects.home_page import HomePage


def test_login(page: Page):  # because i need Page object so am importing and sending into page object fixture
    home = HomePage(page)
    home.enter_into_search_field()
    home.click_on_search_button()
    with page.expect_popup() as new_page:    # with is the context manager
        home.click_on_the_product()
    new_page = new_page.value
    new_page.locator("//span[text()='WISHLIST']").click()
# new line
#