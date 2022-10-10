'''
    等待的示例
'''
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
# 设置页面加载策略
options.page_load_strategy = 'eager'
# options.add_argument('start-maximized')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
# 去掉账号密码弹窗
prefs = dict()
prefs["credentials_enable_service"] = False
prefs['profile.password_manager_enable'] = False
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})
# driver = webdriver.Chrome()
# 隐式等待:最大等待5秒的时间。
driver.implicitly_wait(5)
time.sleep(5)
driver.get('http://39.98.138.157/shopxo/index.php')

driver.find_element('name', 'wd').send_keys('手机')
# driver.get('http://www.baidu.com')
# 显式等待，等待到kw的元素显示出来，再继续进行后续的操作。
# driver.find_element('id', 'kw').send_keys('虚竹')
# driver.find_element('id', 'su').click()
# 忽略所有的逻辑，运行到这一步就会强制等待5秒钟的时间。
# time.sleep(0.2)
# 显式等待指定元素，最大等待时间是10秒，每0.5秒执行一次，一直到元素被查找到为止，如果没找到，则显示Message的内容，抛出异常TimeoutException
el = WebDriverWait(driver, 2, 0.5).until(lambda el1: driver.find_element('xpath', '//*[@id="1"]/div/div/h3/asda'),
                                          message='显式等待失败')
temp = WebDriverWait(driver, 10, 0.5).until_not(lambda el: driver.find_element('xpath', '//*[@id="1"]/div/div/h3/a'),
                                         message='显式等待失败')

# el.click()

# print(temp)
# driver.quit()
