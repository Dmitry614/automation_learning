git import re

from playwright.sync_api import Page, expect, Locator, sync_playwright

from epam_page import EpamPage


def test_search_lviv_location(page: Page):
    epam_page = EpamPage(page)
    epam_page.open_epam_com()

    expect(page).to_have_title(re.compile("^EPAM"))  #

    epam_page.click_careers()  #

    expect(page).to_have_title(re.compile('EPAM Careers$'))  #

    epam_page.click_location_dropdown()  #

    expect(page.locator('.select2-results')).to_contain_text(re.compile('Ukraine'))  #

    epam_page.click_ukraine_option()  #

    expect(page.locator('li[aria-label="Ukraine"]')).to_contain_text('Lviv')  #

    epam_page.click_lviv_option()  #

    expect(page.locator('.select2-selection__rendered')).to_contain_text('Lviv')  #

    epam_page.click_find_button()  #

    expect(page.locator('.search-result__heading-23')).to_contain_text(re.compile(r"We found \d\d job openings for you"))
