from Pages.YahooLandingPage import YahooLandingPage
from selenium import webdriver

browser = webdriver.Chrome()

yLandingPage = YahooLandingPage(driver=browser)
yLandingPage.go()

