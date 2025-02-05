# # installation step by step ( starting --- github actions )
# # pip install playwright
# # python -m playwright install ( for browsers)
# # pip install pytest
# # pip install pytest-playwright
# # create one package and start writing scripts
# #  Pytest  ( framework )
# # POM
# # github repo
# # github actions
# import pytest
# from playwright.sync_api import Page
#
#
# # class Testflipkart():
# def test_login(page:Page):
#         page.get_by_placeholder("Search for products, brands and more").fill("men jackets")
#         page.locator("a.desktop-submit").click()
#         with page.expect_popup() as new_page:
#             page.locator(":nth-match(li.product-base, 3)").click()  # 1st way
#         new_page = new_page.value  # .value helps me to helps you access and interact with the new popup after Playwright finishes waiting for it to appear.
#         # to find elements based in index using :nth-match ( we can use text also ) 3 ways
#         # page.locator('li.product-base:nth-of-type(3)').click();  # 2nd way
#         # page.locator('li.product-base:nth-child(3)').click();   # 3rd way
#         new_page.locator("//span[text()='WISHLIST']")
#         # context.tracing.stop(path="trace.zip")   # to stop traceing it should be before browser close
#
