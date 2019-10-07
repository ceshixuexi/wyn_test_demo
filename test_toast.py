from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def find_toast(driver, message):
    message = '//*[contains(@text,"'+message+'")]'
    element=WebDriverWait(driver,10,1).until(lambda x:x.find_element(By.XPATH,message))
    print(element.text)
    return element.text
desired_caps = dict()
desired_caps['platformName'] = 'android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '85GBCMA2278K'
desired_caps['appPackage'] = 'com.estrongs.android.pop'
desired_caps['appActivity'] = '.view.FileExplorerActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['automationName'] = 'Uiautomator2'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.press_keycode(4)
driver.implicitly_wait(60)
find_toast(driver,'再按')