'''
selenium4中新增的有用的操作行为：针对于浏览器与标签页的
'''
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
sleep(3)
# 自动生成新的标签页，并切换过去
# driver.switch_to.new_window('tab')
# 自动生成新的浏览器，并切换过去
driver.switch_to.new_window('window')
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[0])
driver.get('http://www.baidu.com')
