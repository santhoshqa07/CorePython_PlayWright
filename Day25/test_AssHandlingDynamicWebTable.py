from playwright.sync_api import expect,Page
import pytest
import re

def test_AssHandlindDynamicWebTable(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    table=page.locator("#taskTable")
    expect(table).to_be_visible()

    rows_count = table.locator('tr')
    expect(rows_count).to_have_count(5)

    #row_count = rows.count()
    #print("Number of rows in a table:", row_count)
    rows = table.locator('#rows tr').all()
    cpu_load = ""
    Memory_usage = ""
    Network_Speed = ""
    Disk_space = ""

    for row in rows:
        browser = row.locator('td').nth('0').inner_text()
        if browser == 'Chrome':
            cpu_load = row.locator("td:has-text('%')").inner_text()
            print("CPU Load of chrome:", cpu_load)
            break

    expect(page.locator('.chrome-cpu')).to_contain_text(cpu_load)

    for row in rows:
        browser = row.locator('td').nth('0').inner_text()
        if browser == 'Chrome':
            Network_Speed = row.locator("td:has-text('Mbps')").inner_text()
            print("Network speed of chrome:", Network_Speed)
            break

    expect(page.locator('.chrome-network')).to_contain_text(Network_Speed)



    #Loop to display memory Usage value for the Firefox process
    # Loop to display Disk Space value for the Firefox process

    for row in rows:
        browser = row.locator('td').nth('0').inner_text()

        if browser == 'Firefox':
            cells= row.locator('td').all_inner_texts()

            for cell in cells:
                if cell.endswith("MB"):
                    Memory_usage = cell
                    print("Memory usage of firefox:", Memory_usage)
                if "MB/s" in cell:
                    Disk_space = cell
                    print("Disk space of firefox:", Disk_space)
            break
    expect(page.locator('.firefox-memory')).to_contain_text(Memory_usage)

    expect(page.locator('.firefox-disk')).to_contain_text(Disk_space)




    # for row in rows:
    #     browser = row.locator('td').nth('0').inner_text()
    #     if browser == 'Firefox':
    #         Disk_space = row.locator("td:has-text('MB/s')").inner_text()
    #         print("Disk space of firefox:", Disk_space)
    #         break




