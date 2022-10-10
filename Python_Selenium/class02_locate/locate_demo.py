'''
    八种元素定位法则：
        Id,Name,Link text,Partial Link Text,Tag Name,Class Name,Xpath,Css Selector
    xpath与cssSelector在速度的区别上大概就是10ms左右
    自动化领域下，正确率和稳定性永远排在第一位。
'''
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

# ID定位:在元素具备有ID的属性时，可以通过ID去进行定位。ID就相当于身份证号码。一般而言是不会重复的。
# driver.find_element('id', 'su')
# Name定位:在元素具备有Name属性时，通过Name属性去定位。重复的概率相对而言还是可能存在的。类似于身份证上的名字
# driver.find_element('name', 'rn')
# Link Text:针对于a标签来实现的定位,定位条件是a标签的text内容
# driver.find_element('link text', '新闻').click()
# Partial Link Text: 针对于A标签来实现的定位，是基于a标签的text内容进行模糊查找。类似于sql中的like
# 如果定位的元素有多个，则默认返回第一个定位到的元素。
# els = driver.find_element('partial link text', '使用百度')
# for el in els:
#     print(el.text)
# print(els.text)
# TagName定位：测试用不上，一般是在爬虫的时候应用，基于标签名称来进行元素定位
# els = driver.find_elements('tag name', 'input')
# print(len(els))
# ClassName定位，基于元素的class属性去进行定位，不推荐使用，如果class值只有一个，可以考虑使用，但是要避免重复
# el = driver.find_element('class name', 'bg s_ipt_wr new-pmd quickdelete-wrap ipthover')
# print(el.get_attribute('class'))
# CSS Selector元素定位：万金油型的元素定位。原理就是基于css样式来对元素进行定位。也是传说中定位最快的方法。
# driver.find_element('css selector', '#kw').send_keys('#kw')
# Xpath元素定位：虚竹个人推荐常用款，定位界的万金油，原理是基于html结构来对元素进行定位，类似于操作系统下的文件管理系统
# 绝对路径：不到穷途末路之时，不要使用这个定位方法
# /html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input
# 相对路径：元素的查询功能，通过右键copy，copy xpath获取元素的相对路径（此方法不推荐），一般都是通过手写xpath的形式
# //*[@id="kw"]
driver.find_element('xpath', '//*[@id="su"]')
