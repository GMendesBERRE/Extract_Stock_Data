from Pages.YahooLandingPage import YahooLandingPage
from selenium import webdriver

browser = webdriver.Chrome()

yLandingPage = YahooLandingPage(driver=browser)
yLandingPage.go()

yLandingPage.search_input.type("ITSA4.SA")
yLandingPage.search.click()



print("Finished execution")