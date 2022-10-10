'''
    通过这个demo了解Driver的运行底层逻辑
'''
from selenium.webdriver.chrome.webdriver import WebDriver

# driver = webdriver.Chrome()
driver = WebDriver(executable_path="chromedriver")

# driver.get('http://www.jd.com')
driver.execute('get', {'url': 'http://www.jd.com'})

# 找到输入框，不要用find_element_by_*函数去定位元素。
# el = driver.find_element("id", 'key')
# # 对输入框进行输入
# el.send_keys('虚竹')
el = driver.execute("findElement", {
    'using': "css selector",
    'value': '[id="key"]'
})['value']
# print(el)
el._execute("sendKeysToElement", {
    'text': "虚竹的driver",
    'value': ""})
# 找到搜索按钮，进行点击
# el1 = driver.find_element('xpath', '//button[@aria-label="搜索"]')
# el1.click()
el1 = driver.execute("findElement", {
    'using': "xpath",
    'value': '//button[@aria-label="搜索"]'
})['value']
el1._execute("clickElement")
