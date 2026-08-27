from pages.pim_page import PIMPage


def test_add_employee(logged_in_driver):

    pim = PIMPage(logged_in_driver)

    pim.click_pim()

    assert pim.verify_pim_page()

    pim.add_employee(
        "Lisha",
        "PV",
        "Tester"
    )

def test_search_employee(logged_in_driver):

    pim = PIMPage(logged_in_driver)

    pim.click_pim()

    assert pim.verify_pim_page()

    pim.search_employee("Lisha")

    assert pim.is_employee_displayed("Lisha")


def test_edit_employee(logged_in_driver):

    pim = PIMPage(logged_in_driver)

    pim.click_pim()

    assert pim.verify_pim_page()

    pim.search_employee("Lisha")

    assert pim.is_employee_displayed("Lisha")

    pim.click_edit("Lisha")

    assert pim.verify_personal_details_page()


def test_delete_employee(logged_in_driver):

    pim = PIMPage(logged_in_driver)

    pim.click_pim()

    assert pim.verify_pim_page()

    pim.search_employee("Lisha")

    assert pim.is_employee_displayed("Lisha")

    pim.click_delete("Lisha")

    pim.confirm_delete()

    assert pim.verify_employee_deleted("Lisha")
