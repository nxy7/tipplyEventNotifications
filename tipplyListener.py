from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
# from webdriver_manager.chrome import ChromeDriverManager

class TipplyListener:
    '''Class responsible for listening to and reacting to Tipply stream events'''
    def __init__(self, url):
        self.url = url

    def startListening(self, onCallback, offCallback):
        '''Takes callbacks that should be fired when donation occurs and when it stops being displayed'''
        chromeOptions = Options()

        chromeOptions.headless = True
        
        chromeOptions.add_argument("—disable-gpu")
        chromeOptions.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=chromeOptions)

        driver.get(self.url)

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