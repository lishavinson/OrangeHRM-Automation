from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            20
        )

        self.logger = get_logger(
            self.__class__.__name__
        )

    # ==========================================
    # WAIT FOR ELEMENT
    # ==========================================

    def wait_for_element(self, locator):

        self.logger.info(
            f"Waiting for element: {locator}"
        )

        return self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

    # ==========================================
    # WAIT FOR CLICKABLE
    # ==========================================

    def wait_for_clickable(self, locator):

        self.logger.info(
            f"Waiting for clickable element: {locator}"
        )

        return self.wait.until(
            EC.element_to_be_clickable(
                locator
            )
        )

    # ==========================================
    # CLICK
    # ==========================================

    def click(self, locator):

        self.logger.info(
            f"Clicking element: {locator}"
        )

        element = self.wait_for_clickable(
            locator
        )

        element.click()

    # ==========================================
    # TYPE
    # ==========================================

    def type_text(self, locator, text):

        self.logger.info(
            f"Entering text into: {locator}"
        )

        element = self.wait_for_element(
            locator
        )

        element.clear()
        element.send_keys(text)

    # ==========================================
    # GET TEXT
    # ==========================================

    def get_text(self, locator):

        element = self.wait_for_element(
            locator
        )

        return element.text

    # ==========================================
    # IS DISPLAYED
    # ==========================================

    def is_displayed(self, locator):

        try:

            element = self.wait_for_element(
                locator
            )

            return element.is_displayed()

        except Exception:

            return False