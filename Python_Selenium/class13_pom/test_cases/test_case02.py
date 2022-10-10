'''
   测试用例2
'''
import unittest
from time import sleep

from ddt import data, unpack, ddt
from selenium import webdriver

from class13_pom.page_object.index_page import IndexPage
from class13_pom.page_object.login_page import LoginPage


@ddt
class CaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.ip = IndexPage(cls.driver)
        cls.lp = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # @file_data('../data/login.yaml')
    @data(['xuzhu666', '123456'])
    @unpack
    def test_01_login(self, username, password):
        # driver = webdriver.Chrome()

        self.lp.login(username, password)
        sleep(3)

    def test_02_log_out(self):
        self.ip.logout()
        sleep(3)

    def test_03_search(self):
        self.ip.search('手机')
        sleep(3)


if __name__ == '__main__':
    unittest.main()
