'''
    手机商品详情页
'''
from selenium import webdriver

from class13_pom.base.base_page import BasePage


class PhonePage(BasePage):
    # url
    url = BasePage.url + 'index.php?s=/index/goods/index/id/2.html'

    # 核心元素
    suite = ('xpath', '//li[@data-value="套餐一"]')
    color = ('xpath', '//li[@data-value="金色"]')
    memory = ('xpath', '//li[@data-value="64G"]')
    number = ('xpath', '//input[@id="text_box"]')
    button = ('xpath', '//button[@title="加入购物车"]')

    # 添加购物车业务流程
    def add(self, num):
        self._open(self.url)
        self.click(*self.suite)
        self.sleep(1)
        self.click(*self.color)
        self.sleep(1)
        self.click(*self.memory)
        self.input(*self.number, txt=num)
        self.click(*self.button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    pp = PhonePage(driver)
    pp.add(3)
