from class13_pom.base.base_page import BasePage


class IndexPageElement(BasePage):
    # url
    url = BasePage.url

    # 核心元素
    exit_ = ('link text', '退出')

    input_ = ('id', 'search-input')
    button = ('id', 'ai-topsearch')