from playwright.sync_api import Page, expect
import pytest

def test_FlightBooking(page:Page):
    page.goto("https://blazedemo.com/")

    departure_city = page.locator("[name='fromPort']")

    #Select Departure
    departure_city.select_option(value="Boston")

    page.wait_for_timeout(3000)

    destination_city = page.locator("[name='toPort']")

    # Select Destination
    destination_city.select_option(value="London")

    #page.wait_for_timeout(3000)

    #Click on FIndFlights Button

    Find_flightsBtn = page.locator("[value='Find Flights']")

    Find_flightsBtn.click()

    #page.wait_for_timeout(3000)

    #Locate the results table and extract the flight prices
    results_table = page.locator(".table")

    data_rows = results_table.locator("tbody tr")

    print("The total number of available flights are:", data_rows.count())

    All_data_rows    = data_rows.all()

    price_list = []

    for row in All_data_rows:

        price= row.locator("td").nth(5).inner_text()
        price_list.append(price)


    print("The price of all flights are:", price_list)

    numeric_prices = [float(price.replace('$', '')) for price in price_list]

    print(type(numeric_prices))

    print(numeric_prices)

    #Find the lowest price

    lowest_price = min(numeric_prices)

    print(lowest_price)

    for row in All_data_rows:
        current_price= float(row.locator("td").nth(5).inner_text().replace('$', ''))

        if current_price == lowest_price:
            print("The cheapest flight was found at price:", current_price)

            page.wait_for_timeout(3000)

            row.locator("[value='Choose This Flight']").click()
            break
            #Filling forms

    Name = page.get_by_placeholder("First Last")
    Name.fill("John")

    Address = page.get_by_placeholder("123 Main St.")
    Address.fill("1403 American Beauty Ln")

    City = page.get_by_placeholder("Anytown")
    City.fill("Columbus")

    State = page.get_by_placeholder("State")
    State.fill("OH")

    ZipCode = page.get_by_placeholder("12345")
    ZipCode.fill("43240")

    CardType = page.locator("#cardType").select_option(value="Visa")

    Card_No = page.locator("#creditCardNumber")
    Card_No.fill("6789 0673 4523 1267")

    Month = page.locator("#creditCardMonth")
    Month.fill("12")

    Year = page.locator("#creditCardYear")
    Year.fill("2020")

    Name_on_card = page.locator("#nameOnCard")
    Name_on_card.fill("John Canedy")

    Check_rememberme = page.locator("#rememberMe")
    Check_rememberme.check()

    purchaseFlight_btn = page.locator("[value='Purchase Flight']")
    purchaseFlight_btn.click()





    success_text = page.locator('h1:has-text("Thank you for your purchase today!")')

    print("The success message is:", success_text.inner_text())

    page.wait_for_timeout(3000)















            


























