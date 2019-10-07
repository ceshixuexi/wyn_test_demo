import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class DriverTool():
    def get_driver(self):
        desired_caps=dict()
        desired_caps['platformName']='android'
        desired_caps['platformVersion']='5.1'
        desired_caps['deviceName']='85GBCMA2278K'
        desired_caps['appPackage']='com.weaver.teams'
        desired_caps['appActivity']='.activity.BootandLoginActivity'
        desired_caps['unicodeKeyboard']=True
        desired_caps['resetKeyboard']=True
        desired_caps['noReset']=True
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        return self.driver
    def quit_driver(self):
        time.sleep(3)
        self.driver.quit()

def  tap_secret(element,driver):   #输入密码

    TouchAction(driver).tap(x=element[0], y=element[1]).perform()
    print(element[0], element[1])
def my_swipe(driver):
    driver.swipe(100, 1000, 100, 100)
def find_toast(driver, message):  #定义toast用于断言
    message = '//*[contains(@text,"'+message+'")]'
    element=WebDriverWait(driver,10,1).until(lambda x:x.find_element(By.XPATH,message))
    return element.text
