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




# So once after test is completed github and cicd using jenkins
# create one repo in github
# git init   - is used to initialize a new Git repository in your project directory
# In test files, add .gitignore file - and add the files which are not required to github repo ( .env files are * )
# git log - to check we have any commits
# git status - if we commit somthing to check   ( it will show untracked files )
# git add . - to add all the files
# git add filename - add only particular file
# git commit -m "new project"  - give any messsage saying what changes have done here
# verify using git log
# git remote -v - check whether any repo is initialized
# git remote add origin https://github.com/ranjangowda123/Flipkart_new.git
# verify using git remote -v
# git push
# git push --set-upstream origin master
# git checkout -b feature/jenkins - create new branch
# push to new branch -  git push --set-upstream origin feature/jenkins
# git diff - to see what arr the changes done
# then again add to new branch git add .
# then commit, push
# Then if there are multiple branches if we need to push our updated changes from one branch to another
# Pull request from github page----processs
# Then again we need to do in cmd---that code is merged
# git checkout oldbranch name
# git pull