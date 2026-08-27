from selenium.webdriver.common.by import By

from utils.base_page import BasePage


class LoginPage(BasePage):

    # ==========================================
    # LOCATORS
    # ==========================================

    username = (
        By.NAME,
        "username"
    )

    password = (
        By.NAME,
        "password"
    )

    login_button = (
        By.XPATH,
        "//button[@type='submit']"
    )

    dashboard_heading = (
        By.XPATH,
        "//h6[normalize-space()='Dashboard']"
    )

    error_message = (
        By.XPATH,
        "//p[contains(@class,'oxd-alert-content-text')]"
    )

    # ==========================================
    # ACTIONS
    # ==========================================

    def enter_username(self, username):

        self.logger.info(
            f"Entering username: {username}"
        )

        self.type_text(
            self.username,
            username
        )

    def enter_password(self, password):

        self.logger.info(
            "Entering password"
        )

        self.type_text(
            self.password,
            password
        )

    def click_login(self):

        self.logger.info(
            "Clicking Login button"
        )

        self.click(
            self.login_button
        )

    def login(self, username, password):

        self.logger.info(
            f"Starting login for user: {username}"
        )

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        self.logger.info(
            "Login action completed"
        )

    # ==========================================
    # VERIFICATION
    # ==========================================

    def is_dashboard_displayed(self):

        return self.is_displayed(
            self.dashboard_heading
        )

    def is_error_displayed(self):

        return self.is_displayed(
            self.error_message
        )