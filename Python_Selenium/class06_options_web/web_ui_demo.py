'''
    实现登录，搜索商品，将商品添加购物车，并进行断言
    在实现整个自动化流程的时候，可以去思考如何简化你的操作步骤，注意，核心的业务流程不应该省略的就不要省略
    在测试执行的时候，流程的每一个步骤是你们已经提前知道了的。
'''
from time import sleep

from selenium import webdriver

# 创建driver对象
from selenium.webdriver.support.wait import WebDriverWait

from class06_options_web import chrome_options

driver = webdriver.Chrome(options=chrome_options.options())
# driver = webdriver.Chrome(options=None)
sleep(3)
# 窗体最大化
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(5)
# # 访问URL
# driver.get('http://39.98.138.157/shopxo/index.php')
# # 登录页跳转
# driver.find_element('link text', '登录').click()

# 直接访问到登录URL
driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')

# 输入账号密码，进行登录
driver.find_element('name', 'accounts').send_keys('xuzhu666')
driver.find_element('name', 'pwd').send_keys('123456')
driver.find_element('xpath', '//button[text()="登录"]').click()

# 基于显式等待，做一个简单的校验
WebDriverWait(driver, 10, 0.5).until(lambda el: driver.find_element('link text', '退出'), message='元素获取失败')

# 简化操作步骤
# driver.switch_to.new_window('tab')
driver.get('http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/2.html')
# print('登录成功')
# 商品搜索
# 手机商品
# driver.find_element('id', 'search-input').send_keys('手机')
# driver.find_element('id', 'ai-topsearch').click()
#
# # 进入指定商品详情页
# driver.find_element('partial link text', 'iPhone').click()
# # print(driver.find_element('xpath',
# #                           '//a[@href="http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/2.html"]').text)
# # 切换句柄
# sleep(1)
# handles = driver.window_handles
# driver.close()
# driver.switch_to.window(handles[1])
#
# # 校验页面是否切换成功
# WebDriverWait(driver, 10, 0.5).until(lambda el: driver.find_element('xpath', '//h1[contains(text(),"iPhone")]'),
#                                      message='元素获取失败')

# 添加商品属性
driver.find_element('xpath', '//li[@data-value="套餐一"]').click()
sleep(1)
driver.find_element('xpath', '//li[@data-value="金色"]').click()
sleep(1)
driver.find_element('xpath', '//li[@data-value="32G"]').click()

# 输入购买数量
el = driver.find_element('id', 'text_box')
el.clear()
el.send_keys(20)

# 加入购物车
driver.find_element('xpath', '//button[@title="加入购物车"]').click()

# 获取加入成功文本进行断言
text = WebDriverWait(driver, 10, 0.5).until(lambda el: driver.find_element('xpath', '//p[text()="加入成功"]'),
                                            message='元素获取失败').text
assert '加入成功' == text, '预期结果与{}不一致'.format(text)
# 资源释放。关闭浏览器
driver.quit()
