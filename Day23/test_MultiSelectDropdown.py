
import pytest
from playwright.sync_api import sync_playwright, expect, Page


def test_multi_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

   # select multiple options from the dropdown - 3 ways

    #page.locator("#colors").select_option(["Red","Blue","Green"])   # by label
    Choose_colors=page.locator("#colors")
    # by label
    Choose_colors.select_option(label=["Red", "Blue", "Green"])

    Choose_colors.scroll_into_view_if_needed()


    #page.locator("#colors").select_option(value=["red","white","green"])  # by values
    #page.locator("#colors").select_option(index=[4,2])  # by index


    drowpdown_options=page.locator("#colors>option")
    #drowpdown_options.scroll_into_view_if_needed()
    expect(drowpdown_options).to_have_count(7)

    print("The total options available in dropdown are:", drowpdown_options.count())


    page.wait_for_timeout(5000)


