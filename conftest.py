import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage


@pytest.fixture
def driver():

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        options=options
    )

    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_driver(driver):

    login_page = LoginPage(driver)

    login_page.login(
        USERNAME,
        PASSWORD
    )

    return driver