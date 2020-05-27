from Elements.Locator import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Element(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

