import time

from selenium import webdriver
# 在有一个不用你们封装的日志  直接拿来用的日志
# luckylog
# 1.导包
# 2.给一个路径  日志信息放在哪个文件的路径
# 3.把哪些信息保存在luckylog.txt文件里面
# 4.设置错误的路径

# 安装 pip install lucklog
from luckylog.luckylog import Logger,logger
from luckylog import luckylog
# 正确的日志信息
luckylog.path='logSuccess.txt'
luckylog.module='success'
# 错误的日志
luckylog.debug_file='logError.txt'
# 想要日志信息更加详细
luckylog.Debug=True

class BasePage:
    # driver=webdriver.Chrome()
    def __init__(self,driver):
        self.driver=driver

    @logger(success='成功打开网址',fail='失败网址')
    def open(self,txt):
        self.driver.get(txt)

    def locaotr(self,name,value):
        return self.driver.find_element(name,value)

    @logger(success='成功输入内容',fail='失败输入内容')
    def on_input(self,name,value,txt):
        self.locaotr(name,value).send_keys(txt)

    @logger(success='成功点击', fail='失败点击')
    def on_click(self,name,value):
        self.locaotr(name, value).click()

    def wait(self):
        time.sleep(3)

    def close(self):
        self.driver.quit()

