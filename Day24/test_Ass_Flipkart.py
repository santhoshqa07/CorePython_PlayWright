
import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_Flipkart(page: Page):

    #1. Open the Flipkart Website.
    page.goto("https://www.flipkart.com/")

    #2. Locate the search box and type the search query
    page.locator("input[name='q']:not([readonly])").fill("smart")

    page.wait_for_timeout(5000)







