from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # =========================================================
    # PIM
    # =========================================================

    pim_menu = (
        By.XPATH,
        "//span[normalize-space()='PIM']"
    )

    pim_heading = (
        By.XPATH,
        "//h6[normalize-space()='PIM']"
    )

    # =========================================================
    # ADD EMPLOYEE
    # =========================================================

    add_employee_link = (
        By.XPATH,
        "//a[normalize-space()='Add Employee']"
    )

    add_employee_heading = (
        By.XPATH,
        "//h6[normalize-space()='Add Employee']"
    )

    first_name = (
        By.NAME,
        "firstName"
    )

    middle_name = (
        By.NAME,
        "middleName"
    )

    last_name = (
        By.NAME,
        "lastName"
    )

    save_button = (
        By.XPATH,
        "//button[normalize-space()='Save']"
    )

    # =========================================================
    # SEARCH
    # =========================================================

    employee_name_input = (
        By.XPATH,
        "//label[normalize-space()='Employee Name']"
        "/following::input[@placeholder='Type for hints...'][1]"
    )

    search_button = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )

    reset_button = (
        By.XPATH,
        "//button[normalize-space()='Reset']"
    )

    table_body = (
        By.XPATH,
        "//div[contains(@class,'oxd-table-body')]"
    )

    # =========================================================
    # PERSONAL DETAILS
    # =========================================================

    personal_details_heading = (
        By.XPATH,
        "//h6[normalize-space()='Personal Details']"
    )

    # =========================================================
    # DELETE
    # =========================================================

    confirm_delete_button = (
        By.XPATH,
        "//button[normalize-space()='Yes, Delete']"
    )

    # =========================================================
    # PIM METHODS
    # =========================================================

    def click_pim(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.pim_menu
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.pim_heading
            )
        )

    def verify_pim_page(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.pim_heading
            )
        ).is_displayed()

    # =========================================================
    # ADD EMPLOYEE
    # =========================================================

    def add_employee(self, first_name, middle_name, last_name):

        self.wait.until(
            EC.element_to_be_clickable(
                self.add_employee_link
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.add_employee_heading
            )
        )

        first = self.wait.until(
            EC.visibility_of_element_located(
                self.first_name
            )
        )

        first.clear()
        first.send_keys(first_name)

        middle = self.wait.until(
            EC.visibility_of_element_located(
                self.middle_name
            )
        )

        middle.clear()
        middle.send_keys(middle_name)

        last = self.wait.until(
            EC.visibility_of_element_located(
                self.last_name
            )
        )

        last.clear()
        last.send_keys(last_name)

        save = self.wait.until(
            EC.element_to_be_clickable(
                self.save_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            save
        )

        save.click()

        # Wait until employee details page loads
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//h6[contains(normalize-space(),'Personal Details')]"
                )
            )
        )

    # =========================================================
    # SEARCH EMPLOYEE
    # =========================================================

    def search_employee(self, employee_name):

        # Go to PIM list if necessary
        self.wait.until(
            EC.visibility_of_element_located(
                self.pim_heading
            )
        )

        # Employee Name field
        name_box = self.wait.until(
            EC.visibility_of_element_located(
                self.employee_name_input
            )
        )

        name_box.clear()
        name_box.send_keys(employee_name)

        # -----------------------------------------------------
        # Try autocomplete
        # -----------------------------------------------------

        try:

            suggestion = WebDriverWait(
                self.driver,
                5
            ).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//div[contains(@class,'oxd-autocomplete-option')]"
                    )
                )
            )

            suggestion.click()

        except:

            # Autocomplete may not appear.
            # Continue with entered text.
            pass

        # -----------------------------------------------------
        # Click Search
        # -----------------------------------------------------

        search = self.wait.until(
            EC.element_to_be_clickable(
                self.search_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            search
        )

        search.click()

        # Wait for table
        self.wait.until(
            EC.visibility_of_element_located(
                self.table_body
            )
        )

    # =========================================================
    # EMPLOYEE ROW
    # =========================================================

    def employee_row(self, employee_name):

        return (
            By.XPATH,
            "//div[contains(@class,'oxd-table-body')]"
            "//div[contains(@class,'oxd-table-row')]"
            f"[contains(translate(normalize-space(.),"
            f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
            f"'abcdefghijklmnopqrstuvwxyz'),"
            f"'{employee_name.lower()}')]"
        )

    # =========================================================
    # VERIFY EMPLOYEE
    # =========================================================

    def is_employee_displayed(self, employee_name):

        try:

            row = self.wait.until(
                EC.visibility_of_element_located(
                    self.employee_row(employee_name)
                )
            )

            return row.is_displayed()

        except:

            return False

    # =========================================================
    # EDIT EMPLOYEE
    # =========================================================

    def click_edit(self, employee_name):

        # First find employee row
        row = self.wait.until(
            EC.visibility_of_element_located(
                self.employee_row(employee_name)
            )
        )

        # Find buttons inside that row
        buttons = row.find_elements(
            By.XPATH,
            ".//button"
        )

        if len(buttons) < 1:
            raise Exception(
                f"Edit button not found for employee: {employee_name}"
            )

        # First button = Edit
        edit_button = buttons[0]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            edit_button
        )

        self.wait.until(
            lambda driver:
            edit_button.is_displayed()
            and edit_button.is_enabled()
        )

        self.driver.execute_script(
            "arguments[0].click();",
            edit_button
        )

        # Wait for Personal Details
        self.wait.until(
            EC.visibility_of_element_located(
                self.personal_details_heading
            )
        )

    # =========================================================
    # VERIFY EDIT PAGE
    # =========================================================

    def verify_personal_details_page(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.personal_details_heading
            )
        ).is_displayed()

    # =========================================================
    # DELETE EMPLOYEE
    # =========================================================

    def click_delete(self, employee_name):

        # Find employee row
        row = self.wait.until(
            EC.visibility_of_element_located(
                self.employee_row(employee_name)
            )
        )

        # Find buttons
        buttons = row.find_elements(
            By.XPATH,
            ".//button"
        )

        if len(buttons) < 2:
            raise Exception(
                f"Delete button not found for employee: {employee_name}"
            )

        # Second button = Delete
        delete_button = buttons[1]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            delete_button
        )

        self.wait.until(
            lambda driver:
            delete_button.is_displayed()
            and delete_button.is_enabled()
        )

        self.driver.execute_script(
            "arguments[0].click();",
            delete_button
        )

    # =========================================================
    # CONFIRM DELETE
    # =========================================================

    def confirm_delete(self):

        confirm = self.wait.until(
            EC.element_to_be_clickable(
                self.confirm_delete_button
            )
        )

        confirm.click()

    # =========================================================
    # VERIFY DELETE
    # =========================================================

    def verify_employee_deleted(self, employee_name):

        try:

            self.wait.until(
                EC.invisibility_of_element_located(
                    self.employee_row(employee_name)
                )
            )

            return True

        except:

            return False