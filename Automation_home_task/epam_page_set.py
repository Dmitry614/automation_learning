import re
import os
import random
import pytest

from playwright.sync_api import Page, expect, Locator, sync_playwright


class EpamPage:


    @pytest.fixture(params=["chromium", "firefox"])
    def browser(request):
        browser_type = request.param
        with sync_playwright() as p:
            browser = p[browser_type].launch()
            yield browser
            browser.close()

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
        self.choosed_value = self.page.locator('.tabs-23__link')

    def open_epam_com(self):
        self.page.goto("https://www.epam.com/")

    def check_title(self):
        self.open_epam_com()
        expect(self.page).to_have_title(
            "EPAM | Software Engineering & Product Development Services")

    def check_theme_switcher(self):
        theme_switcher = self.page.locator('.header__content > section > .theme-switcher > .switch')
        theme_switcher.click()
        expect(self.header).to_have_css("--header-background-color", self.header_light)
        theme_switcher.click()
        expect(self.header).to_have_css("--header-background-color", self.header_dark)

    def click_language_button(self):
        find_button = self.page.get_by_role("button", name="Global (EN)")
        find_button.click()
        expect(self.location_list).to_contain_text(self.country)

    def check_language_label(self):
        find_button = self.page.locator('.location-selector__item a[href="https://careers.epam.ua"]')
        find_button.click()
        expect(self.page).to_have_title('EPAM Ukraine - найбільша ІТ-компанія в Україні | Вакансії ')

    def check_regions(self):
        apac_button = self.page.locator('.tabs-23__link').get_by_text("APAC")
        emea_button = self.page.locator('.tabs-23__link').get_by_text("EMEA")
        americas_button = self.page.locator('.tabs-23__link').get_by_text("AMERICAS")
        expect(self.our_locations).to_contain_text(self.locations)
        emea_button.click()
        expect(self.choosed_value.get_by_text("EMEA")).to_have_attribute("aria-selected", "true")
        apac_button.click()
        expect(self.choosed_value.get_by_text("APAC")).to_have_attribute("aria-selected", "true")
        americas_button.click()
        expect(self.choosed_value.get_by_text("AMERICAS")).to_have_attribute("aria-selected", "true")

    def check_policies(self):
        self.open_epam_com()
        expect(self.policies).to_contain_text(self.policies_values)

    def check_search(self):
        self.open_epam_com()
        search_icon = self.page.locator('.search-icon')
        search_icon.click()
        search_field = self.page.locator('#new_form_search')
        search_field.click()
        search_field.fill('AI')
        find_button = self.page.locator('.custom-button')
        find_button.click()
        expect(self.results_counter).to_contain_text(re.compile(r'\d+ results for "AI"'))

    def open_contacts(self):
        self.page.goto("https://www.epam.com/about/who-we-are/contact")

    def check_fields(self):
        submit_button = self.page.locator('.button-ui')
        submit_button.click()
        expect(self.required_field_1).to_have_attribute("aria-invalid", "true")
        expect(self.required_field_2).to_have_attribute("aria-invalid", "true")
        expect(self.required_field_3).to_have_attribute("aria-invalid", "true")
        expect(self.required_field_4).to_have_attribute("aria-invalid", "true")
        expect(self.required_field_5).to_have_attribute("aria-invalid", "true")
        expect(self.required_field_6).to_have_attribute("aria-invalid", "true")

    def open_about(self):
        self.page.goto("https://www.epam.com/about")

    def logo_check(self):
        logo = self.page.locator('a.header__logo-container.desktop-logo')
        logo.click()
        expect(self.page).to_have_url('https://www.epam.com/')

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


class DemoWebshop:

    def __init__(self, page):
        self.page = page
        random_number = random.randint(1, 1000)
        self.user_name_1 = "Name" + str(random_number)
        self.user_name_2 = "Surname" + str(random_number)
        self.user_email = "pythtestlearn" + "+" + str(random_number) + "@mailinator.com"
        self.pswd = "QAtestpswd"
        self.computers = self.page.locator('.sub-category-grid')
        self.computers_values = 'Desktops\nNotebooks\nAccessories'
        self.customer_info = self.page.locator('.header-links a[href="/customer/info"]')
        self.sort_dropdown = self.page.locator('#products-orderby')
        self.sort_selected_option = self.page.locator('#products-orderby option[selected="selected"]')
        self.pagesize_dropdown = self.page.locator('#products-pagesize')
        self.pagesize_selected_option = self.page.locator('#products-pagesize option[selected="selected"]')
        self.bar_notification = self.page.locator('#bar-notification p[class="content"]')
        self.shopping_cart = self.page.locator('#topcartlink a[href="/cart"]')

    def open_site(self):
            self.page.goto("https://demowebshop.tricentis.com/")

    def verify_registration(self):
        registration_link = self.page.locator(".ico-register")
        registration_link.click()
        gender_checkbox = self.page.locator('#gender-male')
        gender_checkbox.click()
        first_name = self.page.locator('input#FirstName')
        first_name.fill(self.user_name_1)
        last_name = self.page.locator('input#LastName')
        last_name.fill(self.user_name_2)
        email = self.page.locator('input#Email')
        email.fill(self.user_email)
        password = self.page.locator('input#Password')
        password.fill(self.pswd)
        confirm_password = self.page.locator('input#ConfirmPassword')
        confirm_password.fill(self.pswd)
        register_btn = self.page.locator('input#register-button')
        register_btn.click()
        expect(self.page.locator('.result')).to_contain_text("Your registration completed")
        self.page.wait_for_timeout(3000)
        log_out_link = self.page.locator(".ico-logout")
        log_out_link.click()

    def verify_login(self):
        log_in_link = self.page.locator(".ico-login")
        log_in_link.click()
        email = self.page.locator('input#Email')
        email.fill(self.user_email)
        password = self.page.locator('input#Password')
        password.fill(self.pswd)
        rmb_me_checkbox = self.page.locator('#RememberMe')
        rmb_me_checkbox.click()
        log_in_btn = self.page.locator('.button-1.login-button')
        log_in_btn.click()
        self.page.wait_for_timeout(3000)
        expect(self.customer_info).to_contain_text(self.user_email)

    def verify_sub_categories(self):
        self.page.goto("https://demowebshop.tricentis.com/computers")
        expect(self.computers).to_contain_text(self.computers_values)

    def verify_sort_by(self):
        self.page.goto("https://demowebshop.tricentis.com/desktops")
        self.sort_dropdown.select_option(index=0)
        self.page.wait_for_timeout(5000)
        expect(self.sort_selected_option).to_contain_text("Position")
        self.sort_dropdown.select_option(index=1)
        self.page.wait_for_timeout(5000)
        expect(self.sort_selected_option).to_contain_text("Name: A to Z")
        self.sort_dropdown.select_option(index=2)
        self.page.wait_for_timeout(5000)
        expect(self.sort_selected_option).to_contain_text("Name: Z to A")
        self.sort_dropdown.select_option(index=3)
        self.page.wait_for_timeout(5000)
        expect(self.sort_selected_option).to_contain_text("Price: Low to High")
        self.sort_dropdown.select_option(index=4)
        self.page.wait_for_timeout(5000)
        expect(self.sort_selected_option).to_contain_text("Price: High to Low")
        self.sort_dropdown.select_option(index=5)
        self.page.wait_for_timeout(5000)
        expect(self.sort_selected_option).to_contain_text("Created on")

    def verify_display_on_page(self):
        self.pagesize_dropdown.select_option('4')
        self.page.wait_for_timeout(5000)
        expect(self.pagesize_selected_option).to_contain_text("4")
        self.pagesize_dropdown.select_option('8')
        self.page.wait_for_timeout(5000)
        expect(self.pagesize_selected_option).to_contain_text("8")
        self.pagesize_dropdown.select_option('12')
        self.page.wait_for_timeout(5000)
        expect(self.pagesize_selected_option).to_contain_text("12")

    def verify_add_to_wishlist(self):
        self.page.goto("https://demowebshop.tricentis.com/album-3")
        add_to_wishlist_button = self.page.locator('input[value="Add to wishlist"]')
        add_to_wishlist_button.click()
        expect(self.bar_notification).to_contain_text("The product has been added to your wishlist ")

    def verify_cart(self):
        self.page.goto("https://demowebshop.tricentis.com/album-3")
        add_to_cart = self.page.locator('.add-to-cart input[value="Add to cart"]')
        add_to_cart.click()
        expect(self.bar_notification).to_contain_text("The product has been added to your shopping cart ")
        self.shopping_cart.click()
        checkbox = self.page.locator('input[name="removefromcart"]')
        checkbox.click()
        update_cart_button = self.page.locator('input[name="updatecart"]')
        update_cart_button.click()
        expect(self.page.locator('.order-summary-content')).to_contain_text("Your Shopping Cart is empty! ")

    def verify_checkout(self):
        self.page.goto("https://demowebshop.tricentis.com/album-3")
        add_to_cart = self.page.locator('.add-to-cart input[value="Add to cart"]')
        add_to_cart.click()
        expect(self.bar_notification).to_contain_text("The product has been added to your shopping cart ")
        self.shopping_cart.click()
        termsofservice = self.page.locator('input#termsofservice')
        termsofservice.click()
        checkout = self.page.locator('button#checkout')
        checkout.click()
        asguest = self.page.locator('input[value="Checkout as Guest"]')
        asguest.click()
        first_name = self.page.locator('input[name="BillingNewAddress.FirstName"]')
        first_name.fill(self.user_name_1)
        last_name = self.page.locator('input[name="BillingNewAddress.LastName"]')
        last_name.fill(self.user_name_2)
        email = self.page.locator('input[name="BillingNewAddress.Email"]')
        email.fill(self.user_email)
        country = self.page.locator('select[name="BillingNewAddress.CountryId"]')
        country.select_option('United States')
        city = self.page.locator('input[name="BillingNewAddress.City"]')
        city.fill("City")
        address = self.page.locator('input[name="BillingNewAddress.Address1"]')
        address.fill("Address")
        zip_code = self.page.locator('input[name="BillingNewAddress.ZipPostalCode"]')
        zip_code.fill("0101ZA")
        phone = self.page.locator('input[name="BillingNewAddress.PhoneNumber"]')
        phone.fill("080077711")
        next_1 = self.page.locator('#billing-buttons-container input[title="Continue"]')
        next_1.click()
        card = self.page.locator('#paymentmethod_0')
        card.click()
        next_2 = self.page.locator('#payment-method-buttons-container input[value="Continue"]')
        next_2.click()
        next_3 = self.page.locator('#payment-info-buttons-container input[value="Continue"]')
        next_3.click()
        confirm = self.page.locator('#confirm-order-buttons-container input[value="Confirm"]')
        confirm.click()
        expect(self.page.locator('.section.order-completed')).to_contain_text("Your order has been successfully processed!")









