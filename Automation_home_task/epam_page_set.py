import re
import os


class EpamPage:

    def __init__(self, page):
        self.page = page
        self.location_list = self.page.locator('.location-selector__list')
        self.header = self.page.locator('.header-ui-23')
        self.language_button = self.page.locator('.location-selector__button-language')
        self.header_light = '#fbfafa'
        self.header_dark = '#060606'
        self.country = 'Україна'
        self.policies_values = ('INVESTORS\nOPEN SOURCE\nPRIVACY POLICY\nCOOKIE POLICY\nAPPLICANT'
                                ' PRIVACY NOTICE\nWEB ACCESSIBILITY')
        self.policies = self.page.locator('.policies-links-wrapper')
        self.our_locations = self.page.locator('.tabs-23__ul')
        self.locations = 'AMERICAS\nEMEA\nAPAC'
        self.americas_locations = 'CANADA'
        self.emea_locations = 'ARMENIA'
        self.apac_locations = 'AUSTRALIA'
        self.results_counter = self.page.locator('.search-results__counter')
        self.counter = re.compile(r'\d+ RESULTS FOR "AI"')
        self.file_name = "EPAM_Corporate_Overview_Q3_october.pdf"
        self.required_field_1 = self.page.locator('input[name="user_first_name"]')
        self.required_field_2 = self.page.locator('input[name="user_last_name"]')
        self.required_field_3 = self.page.locator('input[name="user_email"]')
        self.required_field_4 = self.page.locator('input[name="user_phone"]')
        self.required_field_5 = self.page.locator('span.select2-selection[aria-expanded="false"]'
                                                  '[aria-labelledby$="how_hear_about-container"]')
        self.required_field_6 = self.page.locator('input[name="gdprConsent"]')

    def open_epam_com(self):
        self.page.goto("https://www.epam.com/")

    def open_about_page(self):
        self.page.goto("https://www.epam.com/about")

    def click_careers(self):
        careers_link = self.page.locator('.top-navigation__item-text a[href="/careers"]')
        careers_link.click()

    def click_location_dropdown(self):
        locations_dropdown = self.page.locator('.selection')
        locations_dropdown.click()

    def click_ukraine_option(self):
        ukraine_option = self.page.locator('.select2-results__group').get_by_text("Ukraine")
        ukraine_option.click()

    def click_lviv_option(self):
        lviv_option = self.page.locator('.select2-results__options').get_by_text("Lviv")
        lviv_option.click()

    def click_find_button(self):
        find_button = self.page.locator('.small-button-text').get_by_text("Find")
        find_button.click()

    def click_theme_switcher(self):
        find_button = self.page.locator('.header__content > section > .theme-switcher > .switch')
        find_button.click()

    def click_language_button(self):
        find_button = self.page.get_by_role("button", name="Global (EN)")
        find_button.click()

    def click_language_label(self):
        find_button = self.page.locator('.location-selector__item a[href="https://careers.epam.ua"]')
        find_button.click()

    def click_americas(self):
        find_button = self.page.locator('.tabs-23__link').get_by_text("AMERICAS")
        find_button.click()

    def click_emea(self):
        find_button = self.page.locator('.tabs-23__link').get_by_text("EMEA")
        find_button.click()

    def click_apac(self):
        find_button = self.page.locator('.tabs-23__link').get_by_text("APAC")
        find_button.click()

    def search(self):
        search_icon = self.page.locator('.search-icon')
        search_icon.click()
        search_field = self.page.locator('#new_form_search')
        search_field.click()
        search_field.fill('AI')
        find_button = self.page.locator('.custom-button')
        find_button.click()

    def open_contacts(self):
        self.page.goto("https://www.epam.com/about/who-we-are/contact")

    def check_fields(self):
        submit_button = self.page.locator('.button-ui')
        submit_button.click()

    def open_about(self):
        self.page.goto("https://www.epam.com/about")

    def logo_check(self):
        logo = self.page.locator('a.header__logo-container.desktop-logo')
        logo.click()

    def download_file(self):
        with self.page.expect_download() as download_info:
            self.page.locator('span.button__content.button__content--desktop').get_by_text("DOWNLOAD").click()
        download = download_info.value
        self.page.wait_for_timeout(5000)
        wd = os.getcwd()
        download_path = os.path.join(wd, "Downloads/")
        download.save_as(download_path + download.suggested_filename)
        self.page.wait_for_timeout(5000)
        assert download.suggested_filename == "EPAM_Corporate_Overview_Q3_october.pdf"
