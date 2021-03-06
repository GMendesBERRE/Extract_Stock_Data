from Pages.YahooLandingPage import YahooLandingPage
from Pages.YahooStockPage import YahooStockPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Opening a browser
options = Options()
options.headless = True
browser = webdriver.Chrome(chrome_options=options)

# Going to yahoo landing page
yLandingPage = YahooLandingPage(driver=browser)
yLandingPage.go()

# Looking for the stock
yLandingPage.search_input.type("PETR4.SA")
yLandingPage.search.click()

# Getting Stock data
yStockPage = YahooStockPage(driver=browser)
yStockPage.financials_button.click()
data = yStockPage.stock_data

browser.quit()

print(data)
