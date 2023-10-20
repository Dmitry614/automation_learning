import re


class EpamPage:

    def __init__(self, page):
        self.page = page

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
