
import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_Flipkart(page: Page):

    #1. Open the Flipkart Website.
    page.goto("https://www.flipkart.com/")

    #2. Locate the search box and type the search query
    search_area=page.locator("input[name='q']:not([readonly])")

    page.wait_for_timeout(10000)

    search_area.click()

    search_area.press_sequentially("smart")

    page.wait_for_timeout(5000)

    # Step 3: Locate all suggestions
    options = page.locator("ul > li")
    count = options.count()
    print("Number of suggested options:", count)

    page.wait_for_timeout(5000)
    # Assertion: Expect at least 1 suggestion
    expect(options).to_have_count(count)

    # Step 4: Print the 5th option (index starts from 0)
    if count > 5:
        print("5th option:", options.nth(4).inner_text())

    print("Printing all auto suggestions...")
    for i in range(count):
        print(options.nth(i).text_content())

    # Step 5: Select "smartphone" if it appears
    for i in range(count):
        text = options.nth(i).inner_text()
        if text.strip().lower() == "smartphone":
            options.nth(i).click()
            break

    page.wait_for_timeout(3000)
















