# import pytest
# from playwright.sync_api import sync_playwright
#
#
#
# @pytest.fixture(scope="function")
# def page():
#     # def on_load(ranjan):  # to record the event that occurs when particular execution is happened
#     #     print("Fetch all the API calls ",ranjan) # to record the event that occurs when particular execution is happened
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False, slow_mo=300)
#         return browser.new_page()
#         # context = browser.new_context(record_video_dir="videos/")  # to perform recording we need to create new browser context since we cant do record via page ( single page)
#         # page = context.new_page()  # to perform recording
#         # context = browser.new_context()  # to trace
#         # context.tracing.start(     # cmd to open playwright show-trace trace.zip
#         #     name="test",
#         #     screenshots=True,       # to see frame by frame
#         #     snapshots=True,         # snapshots of the website
#         #     sources=True,           # source code of each action
#         # )
#         # page = context.new_page() # to trace
#         # page = browser.new_page()
#         # page.on("request",on_load)    # to record the event that occurs when particular execution is happened
#         # page.goto("https://www.myntra.com/", wait_until="load")
#         # page.screenshot(path="test.jpg",full_page=True)    # to take screenshot
#         # page.remove_listener("request", on_load) # to stop the event listener when it is used only for single requests
#
#         # context.tracing.stop(path="trace.zip")   # to stop traceing it should be before browser close at the end
#
# def test_website(page):
#     pass


# After completion of the test,
# create git repo and connect with it using jenkins
#