from .base_page import BasePage
from selenium.webdriver.common.by import By
from Src.utils.config import Config

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        super().__init__(driver)  
        self.url = Config.LOGIN_URL  
    def load(self):
        self.driver.get(self.url)
    
    def click_login_button(self):
        self.click(*self.LOGIN_BUTTON)
        
    def login(self,username,password):
        self.send_keys(username,*self.USERNAME_INPUT)
        self.send_keys(password,*self.PASSWORD_INPUT)
        self.click_login_button()