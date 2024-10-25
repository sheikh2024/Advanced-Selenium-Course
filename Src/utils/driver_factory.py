from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

class DriverFactory:
    @staticmethod
    def create_driver():
        chrome_options=Options()
        chrome_options.add_argument("--start-fullscreen")
        chrome_service=ChromeService()
        
        driver=webdriver.Chrome(service=chrome_service,options=chrome_options)
        return driver
        