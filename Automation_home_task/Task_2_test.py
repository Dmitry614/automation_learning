import re


from playwright.sync_api import Page, expect, Locator, sync_playwright

from epam_page_set import DemoWebshop


def test_one(page: Page):  # Verify that allows register and login a User
    dw = DemoWebshop(page)
    dw.open_site()
    dw.verify_registration()
    dw.verify_login()


def test_two(page: Page):  # Verify that ‘Computers’ group has 3 sub-groups with correct names
    dw = DemoWebshop(page)
    dw.open_site()
    dw.verify_sub_categories()


def test_three(page: Page):  # Verify that allows sorting items (different options) and changing number of items on page
    dw = DemoWebshop(page)
    dw.verify_sort_by()
    dw.verify_display_on_page()


def test_four(page: Page):  # •	Verify that allows adding an item to the Wishlist
    dw = DemoWebshop(page)
    dw.verify_add_to_wishlist()


def test_five(page: Page):  # •	Verify that allows adding and removing an item to/from the card
    dw = DemoWebshop(page)
    dw.verify_cart()


def test_six(page: Page):  # •	Verify that allows checkout an item
    dw = DemoWebshop(page)
    dw.verify_checkout()
