import re

from playwright.sync_api import Page, expect, Locator, sync_playwright

from epam_page_set import EpamPage


def test_search_lviv_location(page: Page):
    epam_page_set = EpamPage(page)
    epam_page_set.open_epam_com()  #Open Epam.com page

    expect(page).to_have_title(re.compile("^EPAM"))  # check if page have title EPAM

    epam_page_set.click_careers()  # Moving to Careers page

    expect(page).to_have_title(re.compile('EPAM Careers$'))  # check if page have title EPAM Careers

    epam_page_set.click_location_dropdown()  # Clicking on Location dropdoun

    expect(page.locator('.select2-results')).to_contain_text(re.compile('Ukraine'))  # check if Ukraine option is in the list

    epam_page_set.click_ukraine_option()  # click Ukraine option

    expect(page.locator('li[aria-label="Ukraine"]')).to_contain_text('Lviv')  # check if Ukraine option is in the list

    epam_page_set.click_lviv_option()  # click Lviv option

    expect(page.locator('.select2-selection__rendered')).to_contain_text('Lviv')  # Check if Lviv is populated into the field

    epam_page_set.click_find_button()  # Click find button

    expect(page.locator('.search-result__heading-23')).to_contain_text(re.compile(r"We found \d\d job openings for you")) # Check if page contain the text. Will fail if page doesn't contain page.






#  1) Check the title is correct
#  Steps
#Open EPAM.com
#Compare the title
#The title should be equal "'EPAM | Software Engineering & Product Development Services'"

def TestOne(page: Page):
    epam_page_set = EpamPage(page)
    epam_page_set.open_epam_com()  # Open Epam.com page
    expect(page).to_have_title(re.compile("'EPAM | Software Engineering & Product Development Services'"))  # check if page have title 'EPAM | Software Engineering & Product Development Services'



# 2) Check the ability to switch Light / Dark mode
# Steps
# Open EPAM.com
# Switch the toggle for theme to opposite state
# Expected: the theme should be changed to opposite

class TestTwo:

# 3) Check that allow to change language to UA
# Steps
# Open EPAM.com
# Switch the site's language to Ukraine
# Expected: The site's context should be changed to UA

class TestThree:

# 4) Check the policies list
#Steps
#Open EPAM.com
#Go to the bottom of the page
#Check the policies list
#Expected: The policies list should include the following items:
#INVESTORS
#COOKIE POLICY
#OPEN SOURCE
#APPLICANT PRIVACY NOTICE
#PRIVACY POLICY
#WEB ACCESSIBILITY

class TestFour:

#5) Check that allow to switch location list by region
#Steps
#Open EPAM.com
#Go to Our Locations part
#Check that 3 regions are presented [AMERICAS, EMEA, APAC] and allows to switch the region's locations list

class TestFive:

#6) Check the search function
#Steps
#Open EPAM.com
#Open search field and submit request "AI"
#Expected:  the site should show the search result

class TestSix:

#7)  Chack form's fields validation
#Steps
#Open https://www.epam.com/about/who-we-are/contact
#Check validation for required fields
#Expected: Required fields

class TestSeven:

#8) Check tha the Company logo on the header lead to the main page
#Steps
#Open https://www.epam.com/about
#Click on the company logon on the header
#Expected: https://www.epam.com/ page should be opened

class TestEight:

#9) Check that allows to download report
#Steps
#Open https://www.epam.com/about
#Download EPAM Corporate Overview 2023 report on "EPAM at
#a Glance" block
#Expected: The files should be downloaded and have corect name and extension

class TestNine:
