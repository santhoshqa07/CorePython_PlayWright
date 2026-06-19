import pytest
from playwright.sync_api import sync_playwright, expect, Page


def test_single_select_dropdown(page: Page):
    page.goto("https://bstackdemo.com/")

    #1 Locate and Verify Dropdown, Assert that it is visible and enabled.
    orderBy_dropdown=page.locator(".sort>select")
    expect(orderBy_dropdown).to_be_visible()
    expect(orderBy_dropdown).to_be_enabled()

    #2 Sort Products, Select the "Lowest to highest" option from the dropdown.

    orderBy_dropdown.select_option(value="lowestprice")

    page.wait_for_timeout(5000)

    #3 Extract Product Data

    product_data=page.locator(".shelf-item>P").all_text_contents()

    prices= page.locator(".val>b").all_text_contents()

    print("product_data",product_data)
    print("prices",prices)

    #Print Products and Prices
    # for k,i in zip(product_data,prices):
    #     print("The title is ", k, "and the price is ", i)

    for i in range(len(product_data)):
        print(f"{product_data[i]} : {prices[i]}")


    print(f"The highest price is : {product_data[-1]}:{prices[-1]}")
    print(f"The lowest price is: {product_data[0]}:{prices[0]}")

