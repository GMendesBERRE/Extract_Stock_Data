from Pages.Page import  Page
from Elements.InputElement import InputElement
from Elements.ButtonElement import ButtonElement
from Elements.Locator import  Locator
from Stock.Stock import Stock
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree

class YahooStockPage(Page):
        
    @property
    def financials_button(self):
        locator = Locator(By.XPATH, '//li[@data-test="FINANCIALS"]')
        return ButtonElement(driver=self.driver, locator=locator)

    @property
    def stock_data(self):
        # <div class="D(tbr) fi-row Bgc($hoverBgColor):h" data-reactid="71">
        locator = ".//div[@class='D(tbr) fi-row Bgc($hoverBgColor):h']"
        # Wait until the URL changes to make sure we are getting the rigth HTML
        statements = self.tree.findall(locator)

        dict_statements = {}
        for statement in statements:
            name_statement = statement.find(
                ".//div[@class='D(tbc) Ta(start) Pend(15px)--mv2 Pend(10px) Bxz(bb) Py(8px) Bdends(s) Bdbs(s) Bdstarts(s) Bdstartw(1px) Bdbw(1px) Bdendw(1px) Bdc($seperatorColor) Pos(st) Start(0) Bgc($lv2BgColor) fi-row:h_Bgc($hoverBgColor) Pstart(15px)--mv2 Pstart(10px)']/div[@class='D(ib) Va(m) Ell Mt(-3px) W(215px)--mv2 W(200px) undefined']"
                ).get('title')
            value_statement = statement.findall(
                ".//div[@class='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(140px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)']"
                )[0].text

            print("Name: " + name_statement + " value: " + value_statement)
            dict_statements[name_statement] = value_statement

        return dict_statements

    @property
    def price(self):
        pass

    

