from selenium.webdriver.common.by import By

from base.base import BasePage
from utils import DriverTool


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.phone_number = (By.ID,'com.weaver.teams:id/et_loginname')
    def find_phone_number(self):
        return self.find_element(self.phone_number)

class HandlePage():
    def __init__(self):
        self.login_page = LoginPage()
    def send_phone_number(self,phone_number):
        self.login_page.find_phone_number().send_keys(phone_number)

class LoginProxy():
    def __init__(self):
        self.handle_page = HandlePage()


    def login(self,phone_number):
        self.handle_page.send_phone_number(phone_number)
