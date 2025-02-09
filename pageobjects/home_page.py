from playwright.sync_api import Page

class HomePage:

    def __init__(self,page:Page):
        self.page = page

    search_field = "input[class='desktop-searchBar']"
    search_button = "a.desktop-submit"
    product = ":nth-match(li.product-base, 3)"


    def enter_into_search_field(self):
        self.page.wait_for_selector(self.search_field,state="visible")
        self.page.locator(self.search_field).fill("men jackets")

    def click_on_search_button(self):
        self.page.locator(self.search_button).click()

    def click_on_the_product(self):
        self.page.locator(self.product).click()



