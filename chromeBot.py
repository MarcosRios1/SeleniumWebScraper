import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class chromeBot:

    def __init__(self):
        pass

    def search_url(self, url):
        driver = webdriver.Chrome('/Users/Marcos/dev/chromedriver')
        driver.get(url)
        time.sleep(1)
        return driver

    def send_search(self, driver, search):
        element = driver.find_element_by_id('gh-ac')
        element.send_keys(search)
        element.send_keys(Keys.RETURN)
        time.sleep(5)
