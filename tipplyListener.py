from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

import time
# from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait
def pageReady(driver):
    while True:
        try:
            el = driver.find_element(By.CSS_SELECTOR, ".tpl-nickname")
            print("element available")
            return True
        except:
            print("Waiting till top donor info is available")
            time.sleep(3)
            


class TipplyListener:
    '''Class responsible for listening to and reacting to Tipply stream events'''
    def __init__(self, url):
        self.url = url

    def startListening(self, onCallback, offCallback):
        '''Takes callbacks that should be fired when donation occurs and when it stops being displayed'''
        ffOptions = Options()

        ffOptions.headless = True
        
        ffOptions.add_argument("—disable-gpu")
        ffOptions.add_argument("--no-sandbox")
        driver = webdriver.Firefox(options=ffOptions)

        driver.get(self.url)
        WebDriverWait(driver, timeout=10).until(pageReady)

        lastName = ""
        while True:
            el = driver.find_element(By.CSS_SELECTOR, ".tpl-nickname")
            if lastName != el.text:
                print("New donation")
                lastName = el.text
                onCallback()
                time.sleep(6)
                offCallback()

            time.sleep(1)

        print("Opened link")