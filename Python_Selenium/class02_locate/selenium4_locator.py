'''
    相对定位器进行元素定位，在selenium4 中所新增的内容
    基于人的方向来对元素进行定位，只需要定位一个元素，就可以把这个元素周围的所有元素都定位到。
    实际使用中，会出现定位不准确
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# 核心元素
el = driver.find_element('id', 'kw')
# 上
a = driver.find_elements(locate_with(By.TAG_NAME, 'div').above(el))
# 下
b = driver.find_elements(locate_with(By.TAG_NAME, 'div').below(el))
# 左
l = driver.find_elements(locate_with(By.TAG_NAME, 'div').to_left_of(el))
# 右
r = driver.find_elements(locate_with(By.TAG_NAME, 'div').to_right_of(el))
# 附近
n = driver.find_elements(locate_with(By.TAG_NAME, 'div').near(el))
print(a)
print(b)
print(l)
print(r)
print(n)
