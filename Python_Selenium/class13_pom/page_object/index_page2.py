'''
    提取分层版本IndexPage
'''
from class13_pom.base.base_page import BasePage
from class13_pom.page_object.index_page_element import IndexPageElement
from class13_pom.page_object.page_element import PageElement


class IndexPage(BasePage, IndexPageElement,PageElement):

    # 登出
    def logout(self):
        self._open(self.index_url)
        self.click(*self.exit_)

    # 商品搜索
    def search(self, txt):
        self._open(self.url)
        self.input(*self.input_, txt=txt)
        self.click(*self.button)
