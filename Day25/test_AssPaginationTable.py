from playwright.sync_api import expect,Page
import pytest
import re

def test_AssPaginationTable(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    pages = page.locator("#pagination a")
    total_pages=pages.count()
    assert total_pages==4

    #Locate the product table
    table = page.locator("#productTable")

    rows = table.locator("tr")
    rows_count = rows.count()

    data_rows= table.locator("tbody tr")
    data_rows_count= data_rows.count()

    print("The number of rows in the table including Header:",rows_count)

    print("The number of rows in the table elxcluding Header:", data_rows_count)

    columns = table.locator("th")
    columns_count = columns.count()

    print("The number of columns in the table including Header:",columns_count)


    All_row_datas = data_rows.all()

    for p in range(total_pages):
        pages.nth(p).click()
        for row in All_row_datas:
            row_data = row.locator("td").all_inner_texts()
            print(row_data)

            check_box= row.locator("td").nth(3).locator('input[type="checkbox"]')

            check_box.click()
            page.wait_for_timeout(3000)

        page.wait_for_timeout(2000)




















