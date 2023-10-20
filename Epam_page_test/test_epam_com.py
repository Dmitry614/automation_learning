import re

from playwright.sync_api import Page, expect, Locator, sync_playwright

from epam_page import EpamPage


def test_search_lviv_location(page: Page):
    epam_page = EpamPage(page)
    epam_page.open_epam_com()  #Open Epam.com page

    expect(page).to_have_title(re.compile("^EPAM"))  # check if page have title EPAM

    epam_page.click_careers()  # Moving to Careers page

    expect(page).to_have_title(re.compile('EPAM Careers$'))  # check if page have title EPAM Careers

    epam_page.click_location_dropdown()  # Clicking on Location dropdoun

    expect(epam_page.selected_results).to_contain_text(epam_page.country)  # check if Ukraine option is in the list

    epam_page.click_ukraine_option()  # click Ukraine option

    expect(epam_page.city_label).to_contain_text(epam_page.city)  # check if Lviv option is in the list

    epam_page.click_lviv_option()  # click Lviv option

    expect(epam_page.text_field).to_contain_text(epam_page.city)  # Check if Lviv is populated into the field

    epam_page.click_find_button()  # Click find button

    # expect(epam_page.test_test).to_contain_text(re.compile(r"We found \d+ job openings for you")) # Check if page contain the text. Will fail if page doesn't contain page.
