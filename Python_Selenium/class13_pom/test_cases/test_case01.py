'''
    POM的测试用例
'''
import unittest
from time import sleep

from ddt import ddt, file_data, data, unpack
from selenium import webdriver

from class13_pom.page_object.login_page import LoginPage
from class13_pom.page_object.phone_page import PhonePage


@ddt
class CaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    # @file_data('../data/login.yaml')
    @data(['xuzhu666', '123456'])
    @unpack
    def test_01_login(self, username, password):
        # driver = webdriver.Chrome()
        lp = LoginPage(self.driver)
        lp.login(username, password)
        # sleep(3)

    # 添加购物车
    @file_data('../data/phone.yaml')
    def test_02_add(self, num):
        pp = PhonePage(self.driver)
        pp.add(num)
        sleep(3)


if __name__ == '__main__':
    unittest.main()
