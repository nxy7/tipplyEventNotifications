from selenium import webdriver
import time
# from webdriver_manager.chrome import ChromeDriverManager

class TipplyListener:
    '''Class responsible for listening to and reacting to Tipply stream events'''
    def __init__(self, url):
        self.url = url

    def startListening(self, onCallback, offCallback):
        '''Takes callbacks that should be fired when donation occurs and when it stops being displayed'''
        driver = webdriver.Chrome()

        driver.get("https://google.com")


        while True:
            time.sleep(1)
        print("Opened link")