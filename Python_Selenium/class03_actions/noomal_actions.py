# 常规元素操作行为：selenium本身就是用于模拟人的操作行为，遇到不知道怎么处理的，参考人类的使用习惯
from time import sleep

from selenium import webdriver

# chrome浏览器配置
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
# options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
sleep(3)
# 窗体最大化：不要用。在selenium2开始就存有一个bug，调用窗体最大化时会造成driver的超时异常
# driver.maximize_window()
# 设置窗体大小尺寸
# driver.set_window_size(200, 1000)
# 访问url以及文件
# driver.get('http://39.98.138.157/shopxo/index.php')
driver.get('https://www.baidu.com/')

# 窗体最小化：不实用，不如不用
# driver.minimize_window()
# 浏览器操作，前进后退以及刷新
# driver.forward()
# driver.back()
# driver.refresh()
# 获取title:用于在调试的时候可以判断一下。仅此而已，不代表可以用于断言
# print(driver.title)
# 元素定位
# driver.find_element()   # 定位单个元素，如果同时有多个元素满足条件，定位第一个发现的元素并返回
# driver.find_elements()  # 定位符合条件的所有元素，最终以list的格式返回。如果要操作其中的元素，需要通过下标
# 获取到元素之后的操作行为
# 输入操作
# driver.find_element('name', 'wd').send_keys('虚竹')
# 文件上传:如果在系统操作中遇到文件上传的操作，如果是input标签则可以通过sendkeys直接操作，非input标签，弄死开发，或者用autoIT去解决
# driver.find_element('xpath', '//span[@class="soutu-btn"]').click()
# driver.find_element('xpath', '//input[@value="上传图片"]').send_keys(r'D:\测码\头像\1.jpg')
# 点击：如果有点击的需求，统一通过click()来实现
# driver.find_element().click()
# 操作下拉列表框
# 1. 悬停在设置元素上:悬停操作时，鼠标不要在driver的浏览器中进行移动。
ActionChains(driver).move_to_element(driver.find_element('xpath', '//span[text()="设置"]')).perform()
# 2. 点击高级搜索
driver.find_element('link text', '高级搜索').click()

'''
    下拉列表框分为以下三种：
        1. 基于input标签实现的下拉列表框
        2. 基于Select标签实现的
        3. 基于其他标签实现的
'''

# 常见的下拉列表框操作一：其他标签
sleep(1)
driver.find_element('xpath', '//span[text()="全部时间"]').click()
driver.find_element('xpath', '//p[text()="最近一月"]').click()
# 常见的下拉列表框操作二：input标签（一般input下拉列表框是具有只读属性，无法直接通过send_keys输入，输入前需要remove只读属性，此方法如果无效，则使用两次click解决）
# driver.find_element('xpath', '//input[text()="全部时间"]').send_keys("最近一月")
# Select标签下拉列表框：如果你的系统有这个东西，也就意味着他比你的工作年限还要长的多，最初的下拉列表框
# select = Select(driver.find_element('id', 'cityId'))
# # 选择值
# # 通过下标选择
# select.select_by_index(5)
# # 通过value选择
# select.select_by_value('12')
# # 通过文本选择
# select.select_by_visible_text('成都')
# 退出浏览器，需要把后端进程一同关闭
# driver.close()
driver.quit()
