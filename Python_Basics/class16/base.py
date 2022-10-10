import time

from selenium import webdriver

from class16.demo1 import test_log

# log=test_log()
# from class16.demo2 import test_log2
#
# a=test_log2()

import logging.config
# ini文件调用
logging.config.fileConfig('log.ini')
a=logging.getLogger()

class BasePage:
    # driver=webdriver.Chrome()
    def __init__(self,driver):
        self.driver=driver

    def open(self,txt):
        try:
            a.info(f'访问{txt}')
            self.driver.get(txt)
        except Exception as e:
            a.error('没有访问到网址')

    def locaotr(self,name,value):
        return self.driver.find_element(name,value)

    # 想要把输入的操作记录下来日志  调用info或者error
    # 不可能每次都记录正确的，错误了 用error
    # 用日志 先拿到你封装的日志，在用info或者error调用
    # 用不用日志取决于自己  想把这个步骤记录下来，就想print
    # 登录流程
    # try:
    #   输入账号名 输入密码 登录
    #   log.info()
    # except
    #    log.error()
    def on_input(self,name,value,txt):
        try:
            a.info(f'通过{name}{value}输入{txt}')
            self.locaotr(name,value).send_keys(txt)
        except Exception as e:
            a.error('输入错误了%s'%e)

    def on_click(self,name,value):
        a.info(f'通过{name}{value}进行了点击')
        self.locaotr(name, value).click()

    def wait(self):
        time.sleep(3)

    def close(self):
        self.driver.quit()
