import time

import os

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from utils import tap_secret, my_swipe


class Test_Eteams():
    def setup_class(self):
        desired_caps=dict()
        desired_caps['platformName']='android'
        desired_caps['platformVersion']='5.1'
        desired_caps['deviceName']='85GBCMA2278K'
        desired_caps['appPackage']='com.meizu.flyme.launcher'
        desired_caps['appActivity']='.Launcher'
        desired_caps['unicodeKeyboard']=True
        desired_caps['resetKeyboard']=True
        desired_caps['noReset']=True
        desired_caps['automationName']='Uiautomator2'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(60)
    @pytest.mark.parametrize("datas",[[(820, 1253), (528, 724), (534, 1478), (822, 973), (243, 724), (538, 722)]])
    def test_01(self,datas):
        self.driver.press_keycode(26)
        time.sleep(2)
        self.driver.press_keycode(3)
        my_swipe(self.driver)
        time.sleep(2)

        time.sleep(2)
        # datas = [(820, 1253), (528, 724), (534, 1478), (822, 973), (243, 724), (538, 722)]
        for data in datas:
            tap_secret(data,self.driver)

        # driver.start_activity('com.meizu.flyme.launcher','.Launche')
        print(self.driver.get_window_size())
        time.sleep(5)
        # driver.press_keycode()
        self.driver.implicitly_wait(10)
#         # driver.find_element_by_id("com.weaver.teams:id/et_loginname").send_keys("15156458")
#         self.driver.start_activity('com.meizu.media.gallery','.GalleryActivity')
# # TouchAction(driver).tap(x=141,y=151).perform()
#         time.sleep(2)
#         self.driver.find_element_by_xpath('//*[@bounds="[48,329][288,569]"]').click()
#         time.sleep(2)
#         self.driver.get_screenshot_as_file(os.getcwd()+os.sep+'screen.png')
        self.driver.set_network_connection(6)
        self.driver.start_activity('com.weaver.teams', '.activity.BootandLoginActivity')
        # self.driver.find_element_by_id('com.weaver.teams:id/et_loginname').send_keys('15926413939')
        # self.driver.find_element_by_id('com.weaver.teams:id/et_loginpwd').send_keys('jllsmxy19920612')
        # self.driver.find_element_by_id('com.weaver.teams:id/btn_eteams_login').click()
        # self.driver.find_element_by_xpath('//*[@bounds="[510,1560][570,1620]"]').click()
        # self.driver.find_element_by_xpath('//*[@text="进入 eteams"]').click()
        # self.driver.find_element_by_xpath('//*[@text="不再显示"]').click()
        # self.driver.find_element_by_xpath('//*[@text="忽略"]').click()
    def teardown(self):
        self.driver.quit()