git import re

from playwright.sync_api import Page, expect, Locator, sync_playwright

from epam_page import EpamPage


def test_search_lviv_location(page: Page):
    epam_page = EpamPage(page)
    epam_page.open_epam_com()  #Open Epam.com page

    expect(page).to_have_title(re.compile("^EPAM"))  # check if page have title EPAM

    epam_page.click_careers()  # Moving to Careers page

    expect(page).to_have_title(re.compile('EPAM Careers$'))  # check if page have title EPAM Careers

    epam_page.click_location_dropdown()  # Clicking on Location dropdoun

    expect(page.locator('.select2-results')).to_contain_text(re.compile('Ukraine'))  # check if Ukraine option is in the list

    epam_page.click_ukraine_option()  # click Ukraine option

    expect(page.locator('li[aria-label="Ukraine"]')).to_contain_text('Lviv')  # check if Ukraine option is in the list

    epam_page.click_lviv_option()  # click Lviv option

    expect(page.locator('.select2-selection__rendered')).to_contain_text('Lviv')  # Check if Lviv is populated into the field

    epam_page.click_find_button()  # Click find button

    expect(page.locator('.search-result__heading-23')).to_contain_text(re.compile(r"We found \d\d job openings for you")) # Check if page contain the text. Will fail if page doesn't contain page.
