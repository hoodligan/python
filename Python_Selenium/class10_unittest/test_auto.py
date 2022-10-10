'''
    Unittest下的自动化测试实现:
        一个完整的流程，不同的小流程分为不同的用例去管理。这样便于维护

'''
import unittest

from class07_web_keys.web_keys import Keys


class UnitAuto(unittest.TestCase):

    # 前后置
    @classmethod
    def setUpClass(cls) -> None:
        cls.key = Keys('Chrome')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.key.quit()

    def setUp(self) -> None:
        # self.key = Keys('Chrome')
        self.accounts = 'xuzhu666'

    def tearDown(self) -> None:
        self.key.quit()

    # 登录测试用例
    def test_01_login(self):
        # key =
        self.key.open('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
        self.key.input('name', 'accounts', 'xuzhu666')
        self.key.input('name', 'pwd', '123456')
        self.key.click('xpath', '//button[text()="登录"]')
        # self.assertEqual() 类似于 assert a == b , msg
        # self.assertTrue(self.key.assert_text('link text', '退出', '退出1'), msg='断言失败')
        self.assertEqual('退出1', self.key.get_text('link text', '退出'), msg='断言失败')
        self.key.sleep(5)
        # self.key.quit()

    # def test_02_search(self):
    #     # key = Keys('Chrome')
    #     self.key.open('http://39.98.138.157/shopxo/index.php')
    #     self.key.input('id', 'search-input', '手机')
    #     self.key.click('id', 'ai-topsearch')
    #     self.key.sleep(5)
    #     # key.quit()


if __name__ == '__main__':
    unittest.main()
