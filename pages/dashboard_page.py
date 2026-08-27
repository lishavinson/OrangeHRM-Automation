from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ==================================================
    # LOCATORS
    # ==================================================

    dashboard_heading = (
        By.XPATH,
        "//h6[normalize-space()='Dashboard']"
    )

    pim_menu = (
        By.XPATH,
        "//span[normalize-space()='PIM']"
    )

    # ==================================================
    # METHODS
    # ==================================================

    def is_dashboard_displayed(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.dashboard_heading
            )
        ).is_displayed()

    def click_pim(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.pim_menu
            )
        ).click()