from selenium.webdriver.common.by import By

from utils import DriverTool


class BasePage():
    def __init__(self):
        self.driver=DriverTool().get_driver()
        self.driver.implicitly_wait(10)
    def find_element(self,element):

        return self.driver.find_element(element[0],element[1])
