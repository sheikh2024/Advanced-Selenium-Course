from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from Src.utils.config  import Config


class BasePage:
    
    def __init__(self,driver:WebDriver) :
        self.driver=driver
        self.wait=WebDriverWait(driver, Config.WAIT_TIME ,1,
                                ignored_exceptions=[TimeoutException])
    
    def find_element(self,*locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click(self,*locator):
        element =self.find_element(*locator)
        element.click()
        
    def send_keys(self,text,*locator):
        element=self.find_element(*locator)
        element.send_keys(text)
        
    def get_current_url(self):
        return self.driver.current_url