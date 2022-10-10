'''
    Unittest下的自动化测试实现:
        一个完整的流程，不同的小流程分为不同的用例去管理。这样便于维护
    DDT的使用（不要把所有的数据都直接通过@data装饰器进行传递）：
        通过装饰器形态来实现使用
        1. @data装饰器的数据驱动实现：导入相对比较简单或者固定的数据内容
        2. @unpack装饰器：将data拆解的数据进行二次拆解，便于满足单条用例执行时传入多个参数的情况
        3. @file_data()装饰器：获取yaml格式的文件内容
        4. 在setup和teardown中，不会导入ddt的任何装饰器来做数据驱动
'''
import unittest

from ddt import ddt, data, unpack, file_data

from class07_web_keys.web_keys import Keys


# 获取文件数据内容
def read_file():
    values = list()
    file = open('./data/data.txt', 'r', encoding='utf-8')
    for line in file.readlines():
        values.append(line)
    return values


# 调用ddt数据驱动，一定要在class上添加ddt的装饰器
@ddt
class UnitAuto(unittest.TestCase):
    # 前后置
    @classmethod
    def setUpClass(cls) -> None:
        cls.key = Keys('Chrome')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.key.quit()

    # def setUp(self) -> None:
    #     self.key = Keys('Chrome')

    # def tearDown(self) -> None:
    #     self.key.quit()

    # 登录测试用例
    # def test_01_login(self):
    #     self.key.open('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
    #     self.key.input('name', 'accounts', 'xuzhu666')
    #     self.key.input('name', 'pwd', '123456')
    #     self.key.click('xpath', '//button[text()="登录"]')
    #     self.assertEqual('退出1', self.key.get_text('link text', '退出'), msg='断言失败')
    #     self.key.sleep(5)

    @file_data('./data/login.yaml')
    def test_01_login(self, **kwargs):
        data = kwargs['common']
        self.key.open(data['url'])
        self.key.input(**data['accounts'], txt=kwargs['username'])
        self.key.input(**data['password'], txt=kwargs['pwd'])
        self.key.click(**data['button'])
        self.assertEqual(data['assert_text']['expected'],
                         self.key.get_text(data['assert_text']['by'], data['assert_text']['value']), msg='断言失败')
        self.key.sleep(data['sleep'])

    # 数据内容省略
    # @file_data('./data/search.yaml')
    # def test_02_search(self, **kwargs):
    #     kwargs = kwargs['search']
    #     self.key.open('http://39.98.138.157/shopxo/index.php')
    #     self.key.input('id', 'search-input', '手机')
    #     self.key.click('id', 'ai-topsearch')
    #     self.key.sleep(5)

    # 外部导入数据到测试用例中
    '''
        @data的数据驱动实现机制：
            @data('虚竹帅爆了！', '秋水不太聪明！')
            基于,进行分割，拆分成两组不同的字符串，基于拆分成多少组数据，该条用例会执行多少次
            '虚竹帅爆了！'        '秋水不太聪明！'
            把字符串从data装饰器中获取，然后作为参数传递到测试用例之中。
            @data(['虚竹帅爆了！', '秋水不太聪明！'])
            拆解后获取的是一个list，如果要对list进行二次拆分，则需要增加@unpack装饰器。
            unpack：['虚竹帅爆了！', '秋水不太聪明！']二次基于,进行拆分
                    获得'虚竹帅爆了！'与'秋水不太聪明！'两个数据
            
    '''

    # @data(['虚竹帅爆了！', '秋水太聪明了！'], ['段誉很扣', '芷若很凶'])
    # @unpack
    # def test_01(self, a, b):
    #     print('这是两个参数:{}和{}'.format(a, b))

    # data装饰器是可以调用函数的。
    # @data(*read_file())
    # def test_02(self, a):
    #     # print(a + '以及' + b)
    #     print(a)

    # @file_data('./data/demo.yaml')
    # def test_02(self, **kwargs):
    #     print(kwargs['address'])


if __name__ == '__main__':
    unittest.main()
