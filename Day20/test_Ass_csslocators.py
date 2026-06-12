
from playwright.sync_api import Page, expect

def test_verify_css_locators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    logo= page.locator("[alt='Tricentis Demo Web Shop']")

    expect(logo).to_be_visible()


    #Capture all the computer related products and verify the count . Count should be 4

    products=page.locator("h2>a[href*='computer']")
    print("Products count:", products.count())
    expect(products).to_have_count(4)


    #print first product

    #print("First Product:", products.first.text_content())

    print("First Product:", products.first.inner_text())

    # print last product

    print("First Product:", products.last.text_content())

    #print nth product

    print("Second product", products.nth(1).text_content())

    #Print titles of all the all products  (Tip: all_text_contents())


    product_titles = products.all_text_contents()

    print("Titles of the captured products are:",product_titles)

    for pt in product_titles:
        print("Title:", pt)

    footer_products = page.locator("div>h3")


    print("The first footer product:",footer_products.first.text_content())

    print("The last footer product", footer_products.last.text_content())

    print("The second footer product", footer_products.nth(2).text_content())









