# 创建driver对象
from time import sleep

from selenium import webdriver

from class06_options_web import chrome_options


if __name__ == '__main__':
    driver = webdriver.Chrome(options=chrome_options.options())
    # driver = webdriver.Chrome(options=None)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => false
        })
      """
    })
    driver.get('http://www.baidu.com')
    # driver.get('http://www.iqiyi.com')
    # sleep(3)
    # print(driver.title)
    # driver.find_element('id', 'kw').send_keys('秋水无头')
    # driver.find_element('id', 'su').click()
    sleep(5)
    print(driver.title)
    driver.quit()
