'''
    通过调用关键字驱动类来实现自动化测试效果
    测试用例类，调用关键字驱动类，来实现测试的业务需求。
'''
from class07_web_keys.web_keys import Keys

key = Keys('Chrome')

# 百度搜索
# key.open('http://www.baidu.com')
# key.input('id', 'kw', '虚竹关键字')
# key.click('id', 'su')
# key.sleep(5)
# key.quit()

# 注册流程
key.open('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
key.input('name', 'accounts', 'xuzhu666')
key.input('name', 'pwd', '123456')
key.click('xpath', '//button[text()="登录"]')
key.sleep(5)
key.quit()
