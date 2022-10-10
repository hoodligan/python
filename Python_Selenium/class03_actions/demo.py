from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://1.12.218.8/fsmarket/')
driver.implicitly_wait(5)
driver.find_element('link text', '会员注册').click()
