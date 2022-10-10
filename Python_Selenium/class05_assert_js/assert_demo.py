# 断言
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://39.98.138.157/shopxo/index.php')
driver.find_element('link text', '登录').click()
driver.find_element('name', 'accounts').send_keys('xuzhu666')
driver.find_element('name', 'pwd').send_keys('123456')
driver.find_element('xpath', '//button[text()="登录"]').click()
# 断言部分
# 定义预期结果，并获取实际结果
expected = '退出1'
try:
    reality = driver.find_element('link text', '退出').text
    # 关键的断言关键字

except Exception as e:
    print(e)
    reality = None
assert expected == reality, '断言失败：{0}不等于{1}'.format(expected, reality)

