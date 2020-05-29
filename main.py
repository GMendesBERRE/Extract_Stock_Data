from Pages.YahooLandingPage import YahooLandingPage
from Pages.YahooStockPage import YahooStockPage
from selenium import webdriver

# Opening a browser
browser = webdriver.Chrome()

# Going to yahoo landing page
yLandingPage = YahooLandingPage(driver=browser)
yLandingPage.go()

# Looking for the stock
yLandingPage.search_input.type("ITSA4.SA")
yLandingPage.search.click()

# Getting Stock data
yStockPage = YahooStockPage(driver=browser)
yStockPage.financials_button.click()
data = yStockPage.stock_data

print(data)

print("Finished execution")