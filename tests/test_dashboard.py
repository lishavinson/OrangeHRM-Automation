from pages.dashboard_page import DashboardPage


def test_dashboard_display(logged_in_driver):

    dashboard = DashboardPage(logged_in_driver)

    assert dashboard.is_dashboard_displayed()