
import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_Flipkart(page: Page):

    #1. Open the Flipkart Website.
    page.goto("https://www.flipkart.com/")

    #2. Locate the search box and type the search query
    search_area=page.locator("input[name='q']:not([readonly])")

    search_area.click()

    search_area.press_sequentially("smart")

    #page.pause()

    #3 Suggestions

    Suggestions= page.locator(".POIDhv span")

    print("The suggestions displayed after entering the text smart", Suggestions.count())



    page.wait_for_timeout(10000)







