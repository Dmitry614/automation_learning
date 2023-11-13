import re


from playwright.sync_api import Page, expect, Locator, sync_playwright

from test_set import EpamPage


def test_one(page: Page):  # Check the title is correct
    epam_page = EpamPage(page)
    epam_page.check_title()


def test_two(page: Page):  # Check the ability to switch Light / Dark mode
    epam_page = EpamPage(page)
    epam_page.open_epam_com()
    epam_page.check_theme_switcher()


def test_three(page: Page):  # Check that allow to change language to UA
    epam_page = EpamPage(page)
    epam_page.open_epam_com()
    epam_page.click_language_button()
    epam_page.check_language_label()


def test_four(page: Page):  # Check the policies list
    epam_page = EpamPage(page)
    epam_page.check_policies()


def test_five(page: Page):  # Check that allow to switch location list by region
    epam_page = EpamPage(page)
    epam_page.open_epam_com()
    epam_page.check_regions()


def test_six(page: Page):  # Check the search function
    epam_page = EpamPage(page)
    epam_page.check_search()


def test_seven(page: Page):  # Check form's fields validation
    epam_page = EpamPage(page)
    epam_page.open_contacts()
    epam_page.check_fields()


def test_eight(page: Page):  # Check that the Company logo on the header lead to the main page
    epam_page = EpamPage(page)
    epam_page.open_about()
    epam_page.logo_check()


def test_nine(page: Page):  # Check that allows to download report
    epam_page = EpamPage(page)
    epam_page.open_about()
    epam_page.download_file()
