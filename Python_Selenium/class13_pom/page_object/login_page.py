'''
    登录页：实现商城的登录行为。
'''
from selenium import webdriver

from class13_pom.base.base_page import BasePage


# Python版本的登录页
class LoginPage(BasePage):
    # 页面URL
    url = BasePage.url + 'index.php?s=/index/user/logininfo.html'
    # 核心元素:与业务流程有关的元素
    accounts = ('name', 'accounts')
    pwd = ('name', 'pwd')
    button = ('xpath', '//button[text()="登录"]')

    # button = {
    #     'by': 'xpath',
    #     'value': '//button[text()="登录"]'
    # }

    # 业务流程
    def login(self, username, password):
        self._open(self.url)
        self.input(*self.accounts, txt=username)
        self.input(*self.pwd, txt=password)
        self.click(*self.button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login('xuzhu666', '123456')
