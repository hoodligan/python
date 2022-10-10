'''
    三种弹窗的处理方式
'''

from selenium import webdriver

driver = webdriver.Chrome()

# 切换到弹窗
alert = driver.switch_to.alert
# 确认
alert.accept()
# 取消
alert.dismiss()
# 输入文本
alert.send_keys('输入的文本')
# 获取alert弹窗中的文本信息
text = alert.text

