import unittest

from page.login_page import LoginProxy
from utils import DriverTool


class TestLogin(unittest.TestCase):
    def setUp(self):
        # self.driver=DriverTool().get_driver()
        self.login_proxy=LoginProxy()
    def test01_login(self):
        self.login_proxy.login('15926413939')

if __name__ == '__main__':
    unittest.main()