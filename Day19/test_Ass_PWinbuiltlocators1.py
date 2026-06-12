from playwright.sync_api import Page, expect

def test_Ass_PWinbuiltlocators(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(10000)

    print("Title:", page.title())
    print("URL:", page.url)

    #1) Passing user name, passwords, click on login & verify the dashboard

    page.get_by_role("textbox", name="username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(10000)
    expect(page.get_by_role("heading",name="Dashboard")).to_be_visible()



