from class16.base1 import BasePage
from selenium import webdriver

a=BasePage(webdriver.Chrome())
a.open('http://www.baidu.com')
a.on_input('id2','kw','秋水')
a.wait()
a.on_click('id','su')
a.wait()
a.close()


# 小的项目  记录每一步操作日志去记录

# 用  日志怎么用？
# 日志信息  记录每一步操作
# 打开了浏览器
# 访问了百度
# 输入了秋水
# 点击了搜索按钮
# 等待
# 用日志信息 就跟用print一样