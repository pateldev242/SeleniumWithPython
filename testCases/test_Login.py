import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_CommonInfoFile(self,setup):
        self.logger.info("TC01")
        print(self.baseURL)
    def test_homePageTitle(self,setup):
        self.logger.info("TC02 started")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("TC02 Passed")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Dev Patel\\PycharmProjects\\pythonWithSelenium\\Screenshots\\"+"test_homepageTitle.png")
            self.logger.info("TC02 failed")
            assert False
        self.driver.close()
        self.logger.info("TC02 Completed")


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        time.sleep(1)
        self.lp.setUserName(self.username)
        time.sleep(1)
        self.lp.setPassword(self.password)
        time.sleep(1)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/"+"test_login.png")
            assert False
        self.driver.close()
