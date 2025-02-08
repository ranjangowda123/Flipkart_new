from playwright.sync_api import Page

class HomePage:

    def __init__(self,page:Page):
        self.page = page

    search_field = "Search for products, brands and more"
    search_button = "a.desktop-submit"
    product = ":nth-match(li.product-base, 3)"


    def enter_into_search_field(self):
        self.page.get_by_placeholder(self.search_field).fill("men jackets",timeout=400000)

    def click_on_search_button(self):
        self.page.locator(self.search_button).click()

    def click_on_the_product(self):
        self.page.locator(self.product).click()



