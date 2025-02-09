import os

import allure
import pytest
from playwright.sync_api import sync_playwright,Page

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


# Integrate it to jenkins

# Step 1: Create a GitHub Personal Access Token (PAT)
# Select the appropriate permissions:
# repo: Full control over private repositories.
# admin:repo_hook: Admin access to manage hooks.
# workflow (optional, for actions on pull requests).
# Provide this token to Jenkins: This token will be used in Jenkins to authenticate your GitHub account.


#  Create GitHub Webhook
# Set Up Webhook in GitHub
# 1. Use a Public Jenkins Server (Recommended for Production)
# If you're working in a production environment or need your Jenkins to be publicly available, you'll want to set up Jenkins on a public server
# (such as AWS, DigitalOcean, or any cloud provider). In this case, you'd replace localhost with your server's public IP address or domain name.
# 2. Use a Service like Ngrok (For Local Development)
# If you're running Jenkins locally and want to test the integration without a public server, you can use a tool like Ngrok. Ngrok creates a tunnel from the public internet to your local machine, allowing GitHub to reach your Jenkins instance.
#
# Steps to Use Ngrok:  ngrok http 8080  - cmd to run
# https://b32a-125-18-36-46.ngrok-free.app/github-webhook/

#  Install GitHub Plugin in Jenkins
# Go to Jenkins Dashboard → Manage Jenkins → Manage Plugins.
# In the Available tab, search for GitHub and install the GitHub plugin.
# Restart Jenkins if prompted to complete the installation.
# 1. github integration ( plugin)

# Step 2: Add GitHub Credentials to Jenkins
# Jenkins will need your GitHub Personal Access Token (PAT) to authenticate and access the repository.
#
# Go to Jenkins Dashboard → Manage Jenkins → Manage Credentials.
# Under (global), click Add Credentials.
# For Kind, select Username with password.
# Username: Your GitHub username.
# Password: The Personal Access Token (PAT) you created in GitHub.
# Click OK to save the credentials.

# Step 3: Create a Jenkins Job for Your Repository
# Now, we will set up a Jenkins job to pull code from your GitHub repository and trigger the build when there's a push event.
#
# Create a New Jenkins Job:
#
# Go to Jenkins Dashboard → New Item.
# Choose Freestyle Project (or Pipeline, depending on your needs).
# Give the job a name (e.g., my-github-project) and click OK.
# Configure the Job:
#
# Under Source Code Management, select Git.
# In the Repository URL, enter the URL of your GitHub repository (e.g., https://github.com/username/repository.git).
# Under Credentials, select the GitHub credentials you added earlier (the ones with your GitHub username and PAT).
# Set Build Triggers:
#
# Under Build Triggers, check the option GitHub hook trigger for GITScm polling. This will allow Jenkins to listen for the webhook events from GitHub and automatically trigger a build when changes are pushed to the repository.
# Configure Build Steps (optional):
#
# Depending on your project, you can add build steps to compile code, run tests, etc. For example, you could add a build step to run mvn clean install for a Maven project or a npm install and npm run build for a Node.js project.
# Save the Job:
# Click Save once you've finished configuring your Jenkins job.

# git is required
# give the path of the git----tools--Git installations---Path to Git executable----C:\Users\VMRanjan\AppData\Local\Programs\Git\bin\git.exe
#




# .........Allure___reprt
#  allure report dependencies----
#  pip install pytest-playwright
#  pip install allure-pytest
#  install latest allure from github page  - https://github.com/allure-framework/allure2/releases
#  extract---till bin add to the path
#  pytest --alluredir=allure-report  ( can change folder name )
# allure serve allure_report  ( to see report in local browser )
#
import os
import shutil
@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    # Define the allure-results directory
    allure_dir = os.path.join(os.getcwd(), 'allure_report')
    # Check if the directory exists, if not create it
    if not os.path.exists(allure_dir):
        os.makedirs(allure_dir)  # Create the directory if it doesn't exist
    # If the directory exists, remove only the files inside the folder, not the folder itself
    if os.path.exists(allure_dir):
        for filename in os.listdir(allure_dir):
            file_path = os.path.join(allure_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

# ..........Capture screenshots and upload in allur report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in Allure report on failure.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':  # Only after the test itself has run
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            try:
                # Access the page fixture from item._request
                page: Page = item._request.getfixturevalue('page')

                # Generate screenshot file name
                file_name = report.nodeid.replace("::", "_") + ".png"

                # Ensure the file path is correct
                screenshot_path = os.path.join(os.getcwd(), "test_failure_screenshots", file_name)

                # Capture screenshot using Playwright's page.screenshot method
                _capture_screenshot(page, screenshot_path)

                # Attach screenshot to the Allure report
                with open(screenshot_path, "rb") as f:
                    allure.attach(f.read(), name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)

            except Exception as e:
                print(f"Error capturing screenshot: {e}")

def _capture_screenshot(page: Page, name: str):
    """Capture a screenshot with Playwright and save it to the specified file."""
    screenshots_dir = os.path.dirname(name)
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    # Capture the screenshot and save it to the file
    page.screenshot(path=name)
    print(f"Screenshot saved at {name}")




# ......................Using GITHUB ACTIONS  ( Artifact report generation )__________________
# Step_By_Step
#  .github-----workflows----test.yml file   ( create under main project name )
#  add test.yml file using allure report using github artifact
# run the test once test is completed
# go to the test and download the artifact i zip file
# extract it -- C:\Users\VMRanjan\Downloads\allure-report ----opne this in cmd
# then run this -- python -m http.server 8000
# then run this -- http://localhost:8000/index.html

#.................using github pages.....................
#