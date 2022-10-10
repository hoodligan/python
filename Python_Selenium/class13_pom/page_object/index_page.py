'''
    首页页面对象
'''
from class13_pom.base.base_page import BasePage


class IndexPage(BasePage):
    # url
    url = BasePage.url

    # 核心元素
    exit_ = ('link text', '退出')

    input_ = ('id', 'search-input')
    button = ('id', 'ai-topsearch')

    # 登出
    def logout(self):
        self._open(self.url)
        self.click(*self.exit_)

    # 商品搜索
    def search(self, txt):
        self._open(self.url)
        self.input(*self.input_, txt=txt)
        self.click(*self.button)
