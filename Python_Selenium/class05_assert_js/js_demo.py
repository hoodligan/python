from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(50)

# 通过修改webdriver属性为False，一定是在访问系统之前，在启动浏览器后第一步就是运行这个。
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})
driver.set_window_size(800, 300)
driver.get('http://www.baidu.com')
'''
    document对象执行的常见函数：
        1. removeAttribute(attribute_name)   移除指定对象的指定属性
        2. setAttribute(attribute_name,value)  设置指定对象的指定属性和值
    arguments[0] 在js中可以理解为是占位符，有且只能这么写。
    滚动条操作的核心在于元素的获取，不是在于玩弄滚动条：
        window.scrollTo(x,y)    x表示横轴，横向滚动条；y表示纵轴，上下滚动条
        arguments[0].scrollIntoView()   精确定位到元素，并聚焦在页面中显示
    JS执行器在实际执行过程中，如果想要获取执行结果，便于后续的使用，就一定要在js中添加return关键字
'''

# 移除元素的属性
# js = "document.getElementById('kw').removeAttribute('name')"

# 通过占位符来实现selenium与document的关联
# el = driver.find_element('link text', '新闻')
# # 定位元素，并修改元素的文本
# js = 'arguments[0].innerHTML="虚竹新闻"'
# # 获取指定元素的文本信息
# js = 'return arguments[0].innerHTML="虚竹新闻"'  # 意思就相当于是el.text
# # 用于执行js语句的函数
# a = driver.execute_script(js, el)
# print(a)
driver.find_element('id', 'kw').send_keys('虚竹')
driver.find_element('id', 'su').click()
el = driver.find_element('link text', '下一页 >')

# 定位元素，并在页面中心显示
js = 'arguments[0].scrollIntoView()'
driver.execute_script(js, el)

# 获取元素的指定属性值。
text = el.get_attribute('href')
print(text)


