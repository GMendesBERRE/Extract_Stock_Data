from Pages.Page import  Page
from Elements.InputElement import InputElement
from Elements.ButtonElement import ButtonElement
from Elements.Locator import  Locator
from selenium.webdriver.common.by import By

class YahooLandingPage(Page):

    url = "https://finance.yahoo.com/"

    @property
    def search_input(self):
        locator = Locator(By.ID, 'yfin-usr-qry')
        return InputElement(driver=self.driver, locator=locator)

    @property
    def search(self):
        locator = Locator(By.ID, 'header-desktop-search-button')
        return ButtonElement(driver=self.driver, locator=locator)

        