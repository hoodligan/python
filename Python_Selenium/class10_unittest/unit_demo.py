'''
    Unittest的应用规则：
        1. 是Python默认自带的库。不需要安装了。直接导入就可以。
        2. 调用时一定要通过继承UnitTest.TestCase类来实现
        3. UnitTest四大组件：
            前后置条件：setup和teardown，分为class级和Function级
                        不会把测试数据的初始化放到前置函数之中
                        一个class中只能存在class级和Function级各一套
                        如果考虑多用例间缓存数据共用的场景，使用setupclass，否则使用setup进行前置设置
            测试用例：所有的测试用例都是基于test开头的函数，用例运行顺序是固定的，基于ascii来进行排序，再执行
                    0-9，A-Z，a-z的顺序，建议在编写用例的时候，进行编号排序
                    不加test开头的函数，都是普通的函数，需要被调用才可以生效。
                    UnitTest下支持单用例的执行，但是虚竹不推荐使用。因为容易因为用例关联逻辑报错
            断言：在UnitTest下，只要代码没有报错，就认为是通过的。
                通过self.assert*字样来进行调用
        4. UnitTest要启动运行，一定是在main函数中用unittest.main()启动
        5. UnitTest控制台的打印有点莫名其妙，不要太过于去在意控制台的输出顺序
        6. 测试用例在设计的时候一定要考虑到用例间的关联性要尽可能低。让每一个用例尽可能是独立化存在的
'''

import unittest


# class UnitDemo02(unittest.TestCase):
#     # 前置条件：可以理解为是class在执行之初，先执行的初始化行为(类级别) 只执行一次
#     @classmethod
#     def setUpClass(cls) -> None:
#         print('这是setupclass02')
#         cls.a = '虚竹'
#
#     # 后置条件：可以理解为是class在执行结束时，最后执行的收尾（类级别）只执行一次
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print('这是teardownclass02')
#
#     # 前置条件：可以理解为是每一个测试用例在执行前的初始化行为。(用例级别)
#     def setUp(self) -> None:
#         print('这是前置条件')
#
#     # 后置条件：可以理解为是每一个用例在执行结束之后的收尾。(用例级别)
#     def tearDown(self) -> None:
#         print('这是后置条件')
#
#     # 测试用例1
#     def test_01_a(self):
#         print('这是a')
#         # print(self.a)
#         # 修改cls.a的值
#         # 类名.属性修改，可以修改元素的值，对全局生效
#         # UnitDemo.a='钟灵'
#         # self.属性修改，可以在函数内修改，对全局无效
#         # self.a = '钟灵'
#         print(self.a)
#
#     # 测试用例2
#     def test_02_A(self):
#         print('这是A')
#         # print(self.a)
#
#     def test_03_1(self):
#         print('这是1')


# 这个是第二个class对象
class UnitDemo(unittest.TestCase):
    # 前置条件：可以理解为是class在执行之初，先执行的初始化行为(类级别) 只执行一次
    @classmethod
    def setUpClass(cls) -> None:
        print('这是setupclass')
        cls.a = '虚竹02'

    # 后置条件：可以理解为是class在执行结束时，最后执行的收尾（类级别）只执行一次
    @classmethod
    def tearDownClass(cls) -> None:
        print('这是teardownclass')

    # def test_01(self):
    #     a = 3.1415926123456789
    #     b = 3.141592612345678
    #     self.assertAlmostEqual(a, b, msg='不对')
    #     self.assertEqual(a, b, msg='不对')

    def test_02(self):
        c = 10
        print('这是02')
        UnitDemo.a = c
        # return c

    def test_03(self):
        # print(self.test_02())
        print(self.a)


# 如果不用test开头，则为普通函数
# def func(self, a, b):
#     print('这是func函数')
#     return a + b


# unittest的启动
if __name__ == '__main__':
    unittest.main()
