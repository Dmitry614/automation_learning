import re


from playwright.sync_api import Page, expect, Locator, sync_playwright

from epam_page_set import EpamPage


def test_one(page: Page):
    epam_page = EpamPage(page)
    epam_page.open_epam_com()

    expect(page).to_have_title(
        "EPAM | Software Engineering & Product Development Services")


def test_two(page: Page):
    epam_page = EpamPage(page)
    epam_page.open_epam_com()
    epam_page.click_theme_switcher()
    expect(epam_page.header).to_have_css("--header-background-color", epam_page.header_light)
    epam_page.click_theme_switcher()
    expect(epam_page.header).to_have_css("--header-background-color", epam_page.header_dark)


def test_three(page: Page):
    epam_page = EpamPage(page)
    epam_page.open_epam_com()
    epam_page.click_language_button()
    expect(epam_page.location_list).to_contain_text(epam_page.country)
    epam_page.click_language_label()
    expect(page).to_have_title('EPAM Ukraine - найбільша ІТ-компанія в Україні | Вакансії ')


def test_four(page: Page):
    epam_page = EpamPage(page)
    epam_page.open_epam_com()
    expect(epam_page.policies).to_contain_text(epam_page.policies_values)


def test_five(page: Page):
    epam_page = EpamPage(page)
    epam_page.open_epam_com()
    expect(epam_page.our_locations).to_contain_text(epam_page.locations)
    epam_page.click_emea()
    expect(page.locator('.tabs-23__link').get_by_text("EMEA")).to_have_attribute("aria-selected", "true")
    epam_page.click_apac()
    expect(page.locator('.tabs-23__link').get_by_text("APAC")).to_have_attribute("aria-selected", "true")
    epam_page.click_americas()
    expect(page.locator('.tabs-23__link').get_by_text("AMERICAS")).to_have_attribute("aria-selected", "true")


def test_six(page: Page):
    epam_page = EpamPage(page)
    epam_page.open_epam_com()
    epam_page.search()
    expect(epam_page.results_counter).to_contain_text(re.compile(r'\d+ results for "AI"'))


def test_seven(page: Page):
    epam_page = EpamPage(page)
    epam_page.open_contacts()
    epam_page.check_fields()
    expect(epam_page.required_field_1).to_have_attribute("aria-invalid", "true")
    expect(epam_page.required_field_2).to_have_attribute("aria-invalid", "true")
    expect(epam_page.required_field_3).to_have_attribute("aria-invalid", "true")
    expect(epam_page.required_field_4).to_have_attribute("aria-invalid", "true")
    expect(epam_page.required_field_5).to_have_attribute("aria-invalid", "true")
    expect(epam_page.required_field_6).to_have_attribute("aria-invalid", "true")


def test_eight(page: Page):
    epam_page = EpamPage(page)
    epam_page.open_about()
    epam_page.logo_check()
    expect(page).to_have_url('https://www.epam.com/')


def test_nine(page: Page):
    epam_page = EpamPage(page)
    epam_page.open_about()
    epam_page.download_file()
