import pytest

from playwright.sync_api import Page, expect


def test_inputbox(page: Page):

    page.goto("https://practice-automation.com/form-fields/")

    Name_Input=page.locator("#name-input")

    expect(Name_Input).to_be_visible()
    expect(Name_Input).to_be_enabled()

    Name_Input.fill("Santhosh")

    entered_value=Name_Input.input_value()

    print("Entered_value is :",entered_value)

    page.wait_for_timeout(5000)

def test_radio(page: Page):
    page.goto("https://practice-automation.com/form-fields/")

    Red_radio=page.locator("#color1")

    expect(Red_radio).to_be_visible()
    expect(Red_radio).to_be_enabled()
    expect(Red_radio).not_to_be_checked()
    Red_radio.check()
    expect(Red_radio).to_be_checked()


    page.wait_for_timeout(5000)


def test_checkboxes(page: Page):
    page.goto("https://practice-automation.com/form-fields/")

    Water_chkbox=page.get_by_label("Water")

    Water_chkbox.check()

    expect(Water_chkbox).to_be_checked()

    page.wait_for_timeout(5000)

    #2 count no of check boxes

    fav_drinks = ['Water','Milk','Coffee','Wine','Ctrl-Alt-Delight']

    checkboxes=[]

    checkboxes = [page.get_by_label(drink) for drink in fav_drinks]
    print("total number of checkboxes:", len(checkboxes))

    # 3 . select all the checkboxes and assert each check box is selected
    for checkbox in checkboxes:
         checkbox.check()
         expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)

    # 4. uncheck last 3 checkboxes
    for checkbox in checkboxes[-3:]:
         checkbox.uncheck()
         expect(checkbox).not_to_be_checked()

    page.wait_for_timeout(5000)

    # 5. Toggle checkboxes.

    # for checkbox in checkboxes:
    #     if checkbox.is_checked():
    #         checkbox.uncheck()
    #         expect(checkbox).not_to_be_checked()
    #     else:
    #         checkbox.check()
    #         expect(checkbox).to_be_checked()
    #
    # page.wait_for_timeout(5000)







