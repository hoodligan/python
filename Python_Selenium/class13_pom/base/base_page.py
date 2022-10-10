'''
    基类：用于POM中的工具类，便于页面对象类的调用
'''
import time

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 临时driver对象
    # driver = webdriver.Chrome()

    # 构造函数:通过driver对象，将不同的页面对象串联起来
    url = 'http://39.98.138.157/shopxo/'

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => false
                })
              """
        })

    # url的访问
    def _open(self, url):
        self.driver.get(url)

    # 元素定位:一定要考虑各种不同的元素定位方法。
    def locate(self, by, value):
        return self.driver.find_element(by, value)

    # 输入
    def input(self, by, value, txt):
        el = self.locate(by, value)
        el.clear()
        el.send_keys(txt)

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
