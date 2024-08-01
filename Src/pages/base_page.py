from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    
    def __init__(self,driver:WebDriver) :
        self.driver=driver
        self.wait=WebDriverWait(driver,30,1,
                                ignored_exceptions=[TimeoutException])
    
    def find_element(self,*locator):
        return self.wait.until(EC.visibility_of_element_located(locator))