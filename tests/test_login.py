import pytest

from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("Admin", "admin123", "success"),
        ("Admin", "wrong123", "failure"),
        ("wronguser", "admin123", "failure"),
        ("wronguser", "wrong123", "failure")
    ]
)
def test_login(driver, username, password, expected):

    login_page = LoginPage(driver)

    login_page.login(username, password)

    if expected == "success":

        assert login_page.is_dashboard_displayed()

    else:

        assert login_page.is_error_displayed()