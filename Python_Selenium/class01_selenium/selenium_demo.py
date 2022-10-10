'''
    Selenium部署后的第一次应用：jd搜索
    养成一个正常的思维逻辑：
        电脑很蠢，代码也很蠢，他们不知道你心里所想的任何事情，只知道代码写了什么就执行什么。
    业务逻辑是人定的，对于程序而言，没有任何所谓的业务逻辑，只有代码。
'''
from time import sleep

from selenium import webdriver
# from selenium.webdriver.common.by import By


# 创建一个浏览器驱动，基于驱动来启动浏览器的，创建时，通过session来管理浏览器
driver = webdriver.Chrome()

# 访问JD的url：get函数要求输入的url必须是完整的内容。http://的前缀是不可以取消掉的。
driver.get('http://www.jd.com')

# 在输入框输入你想要输入的搜索内容
# 找到输入框，不要用find_element_by_*函数去定位元素。
el = driver.find_element("id", 'key')
# 对输入框进行输入
el.send_keys('虚竹')
# 找到搜索按钮，进行点击
el1 = driver.find_element('xpath', '//button[@aria-label="搜索"]')
el1.click()

# 等待3秒
sleep(3)

# 浏览器退出
driver.quit()
