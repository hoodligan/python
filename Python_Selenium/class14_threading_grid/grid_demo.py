'''
    访问selenium grid体系
'''
from time import sleep

from selenium import webdriver

# 创建remote对象
driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub')
# a业务，b业务，c业务，用不同的driver对象执行不同的业务不就可以了？
driver.get('http://www.baidu.com')
sleep(5)
driver.quit()
