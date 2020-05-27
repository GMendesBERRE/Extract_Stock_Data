from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import time

class Page(object):
    
    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        #t = time.time()
        #self.driver.set_page_load_timeout(10)

        #try:
        #    self.driver.get(self.url)
        #except TimeoutException:
        #    self.driver.execute_script("window.stop();")

        #print('Time consumed to load page:', time.time() - t)

        self.driver.get(self.url)

