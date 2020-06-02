from Pages.Page import  Page
from Elements.Element import Element
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
    def stock_data_table(self):
        locator = Locator(By.XPATH, '//div[@class="M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"]')
        return Element(driver=self.driver, locator=locator)

    @property
    def stock_data(self):

        #Wait until the table is visible
        self.stock_data_table.wait_visible()

        # <div class="D(tbr) fi-row Bgc($hoverBgColor):h" data-reactid="71">
        locator = ".//div[@class='D(tbr) fi-row Bgc($hoverBgColor):h']"
        # Wait until the URL changes to make sure we are getting the rigth HTML
        statements = self.tree.findall(locator)


        dict_statements = {}
        for statement in statements:
            # <span class="Va(m)" data-reactid="75">Total Revenue</span>
            name_statement = statement.findtext(".//div/div/span")

            # <div class="Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(140px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)" data-test="fin-col" data-reactid="77">
            value_element = statement.find(
                        ".//div[@class='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(140px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)']"
                        )
            if len(value_element)==0:
                value_statement = value_element.text
            else:
                # <span data-reactid="78">
                value_statement = value_element.findtext(".//span")

            dict_statements[name_statement] = value_statement

        return dict_statements

    @property
    def price(self):
        pass

    

