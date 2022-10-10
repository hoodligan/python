# 句柄与frame
'''
    新页面的访问:selenium访问新页面的时候，默认停留在老页面中，每一个页面都有一个句柄，要操作哪个页面就切换哪个句柄
        句柄的切换业务下，需要时刻记住，标签页最多保留不超过2个。一般在访问新标签页之前，要close掉旧的标签页
    内嵌窗体的元素操作:有一种场景下，你元素定位是正确的，并且再三确认过的，但是运行到这里就是找不到
        元素，也等待了，也排查了，也让虚竹看了。这时候就需要思考一下，是不是有iframe呢？
'''
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
sleep(2)
driver.maximize_window()
# driver.get('http://www.baidu.com')
# driver.find_element('id', 'kw').send_keys('虚竹')
# driver.find_element('id', 'su').click()
# driver.close()
# # 访问新页面前
# # print(driver.window_handles)
# driver.find_element('xpath', '//*[@id="1"]/div/div[1]/h3/a').click()
# sleep(1)
# print(driver.title)
# 句柄获取
# handles = driver.window_handles
# # 关闭当前标签页
# driver.close()
# # 切换标签页
# driver.switch_to.window(handles[1])
# print(driver.title)
# 访问新页面后
# print(handles)

# iframe处理
driver.get('https://music.163.com/')
driver.find_element('link text', '登录').click()
driver.find_element('link text', '选择其他登录模式').click()
driver.find_element('id', 'j-official-terms').click()
driver.find_element('partial link text', 'QQ登录').click()
sleep(1)
# 句柄获取
handles = driver.window_handles
# 关闭当前标签页
# driver.close()
# 切换标签页
driver.switch_to.window(handles[1])
# 如果元素在iframe标签中，需要先切换至iframe，再进行定位
driver.switch_to.frame('ptlogin_iframe')
driver.find_element('xpath', '//*[@id="qlogin_list"]/a[2]').click()
# 切换到默认窗体:只有切换回来以后才可以继续操作页面中iframe以外的内容
driver.switch_to.default_content()
