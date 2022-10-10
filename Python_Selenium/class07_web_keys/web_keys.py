'''
    关键字驱动类。
    一般在常态化中，考虑封装各类操作行为，作为关键字驱动的核心底层结构。
    以工具类的形态，便于其他的类来进行调用。
    常用的操作行为：
        1. 访问url
        2. 创建driver对象
        3. 元素定位
        4. 三类等待
        5. 输入、点击
        6. 切换iframe和句柄
        。。。。。
    封装的概念上，我们优先考虑自己用的上的内容，进行封装。
    Selenium本身类似于一家超级无敌大的商场。关键字驱动类类似于家用的工具箱，要往工具箱里添加我们需要的东西。
    在调用工具箱实现自己的自动化时，如果发现工具少了，或者缺失了，可以及时到Selenium中进行补充。
'''
import time

import SafeDriver.drivers
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from class06_options_web import chrome_options


# 构造浏览器对象，基于type_参数，构造对应的浏览器对象。
def open_browser(type_):
    '''
        getattr是python内置的四大函数之一，反射机制，用于获取指定对象的属性或者函数。
        driver = getattr(webdriver, type_)()意思就是:
        if type_ == 'Chrome':
            driver = webdriver.Chrome()
        elif type_ == 'Edge':
            driver = webdriver.Edge()
        elif.....
        因为反射本身是用来获取指定对象属性的。如果要获取的是函数，则需要在反射的后面加()
        例如：
            getattr(webdriver, type_) 表示获取webdriver的type_属性
            getattr(webdriver, type_)() 表示获取webdriver的type_函数
    '''
    try:
        if type_ == 'Chrome':
            driver = webdriver.Chrome(options=chrome_options.options())
        else:
            driver = getattr(webdriver, type_)()
    except:
        # 可以考虑通过测码提供的safedriver来实现chrome浏览器对象的生成。
        driver = SafeDriver.drivers.driver()
    return driver

    # 这种写法可以更加好地全面化满足用户的调用需求
    # browser = {'chrome': ['Chrome', 'chrome', 'cc', '谷歌'],
    #            'ie': ['ie', 'Ie', 'IE', '阿姨']}
    # if type_ in browser['chrome']:
    #     driver = webdriver.Chrome(options=chrome_options.options())
    # elif type_ in browser['ie']:
    #     driver = webdriver.Ie()
    # else:
    #     driver = webdriver.Chrome()
    # return driver


class Keys:
    # 临时driver对象
    # driver = webdriver.Chrome()

    # 构造函数
    def __init__(self, type_):
        self.driver = open_browser(type_)
        self.driver.implicitly_wait(5)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => false
                })
              """
        })

    # url的访问
    def open(self, url):
        self.driver.get(url)

    # 元素定位:一定要考虑各种不同的元素定位方法。
    def locate(self, by, value):
        return self.driver.find_element(by, value)

    # 输入
    def input(self, by, value, txt):
        self.locate(by, value).send_keys(txt)

    # 点击
    def click(self, by, value):
        self.locate(by, value).click()

    # 浏览器关闭
    def quit(self):
        self.driver.quit()

    # 显式等待
    def driver_wait(self, by, value):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locate(by, value), message='元素获取失败')

    # 强制等待
    def sleep(self, time_):
        time.sleep(int(time_))

    # 句柄的切换：为了满足有些场景下不需要close，需要考虑逻辑的处理
    def switch_handle(self, status=1):
        handles = self.driver.window_handles
        if status == 1:
            self.driver.close()
        self.driver.switch_to.window(handles[1])

    # 断言预期结果是否包含在实际结果内
    def assert_almost_equal(self, by, value, expected):
        try:
            reality = self.locate(by, value).text
            assert expected in reality, '{0}不在{1}的范围内'.format(expected, reality)
            return True
        except:
            return False

    # 文本断言
    def assert_text(self, by, value, expected):
        try:
            reality = self.locate(by, value).text
            assert expected == reality, '{0}与{1}不相等'.format(expected, reality)
            return True
        except Exception as e:
            return False
            # print('断言失败：{}'.format(e))
            # raise e

    # 获取元素文本
    def get_text(self, by, value):
        return self.locate(by, value).text


# 调试
if __name__ == '__main__':
    key = Keys('谷歌')
    key.open('http://www.baidu.com')
