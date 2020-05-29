
from selenium import webdriver
import time
from lxml import etree

class Page(object):
    
    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    @property
    def tree(self):
        return etree.HTML(self.driver.page_source)

