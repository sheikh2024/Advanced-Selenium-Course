import pytest
from selenium import webdriver
from Src.utils.driver_factory import DriverFactory
from Src.pages.login_page import LoginPage
from Src.utils.config import Config


@pytest.fixture(scope="module")
def driver():
    driver=DriverFactory.create_driver()
    yield driver
    driver.quit()
    
@pytest.fixture
def login_page(driver):
 return LoginPage(driver)




def test_login_with_valid_crendential(login_page,driver):
    login_page.load()
    login_page.login(Config.VALID_USERNAME,Config.VALID_PASSWORD)
    assert driver.current_url == Config.MINE_URL
    
    
def test_login_with_wrong_username(login_page,driver):
    login_page.load()
    login_page.login(Config.INVALID_USERNAME,Config.VALID_PASSWORD)
    assert driver.current_url == Config.LOGIN_URL
    
def test_login_with_wrong_password(login_page,driver):
    login_page.load()
    login_page.login(Config.VALID_USERNAME,Config.INVALID_PASSWORD)
    assert driver.current_url == Config.LOGIN_URL
    
def test_login_with_invalid_crendential(login_page,driver):
    login_page.load()
    login_page.login(Config.INVALID_USERNAME,Config.INVALID_PASSWORD)
    assert driver.current_url == Config.LOGIN_URL