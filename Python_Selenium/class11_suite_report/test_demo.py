'''
    Skip装饰器的使用：
        skip表示无条件直接跳过
        skipIf表示表达式成立，则跳过，不成立则继续执行
        skipUnless与skipIf相反
        expectedFailure 默认用例执行会失败，并将其忽略。
        UnitTest下的杂技套装。
'''
import unittest


class Demo(unittest.TestCase):

    @unittest.skip('无条件跳过该条用例执行')
    def test_01(self):
        print(1)

    # @unittest.skipIf(1 == 2, '这是If的理由')
    def test_02(self):
        print(2)

    # @unittest.skipUnless(1 == 2, '这是Unless的理由')
    def test_03(self):
        print(3 / 0)

    @unittest.expectedFailure
    def test_04(self):
        print(4)
        # self.assertEqual(1, 2, msg='断言失败')

# if __name__ == '__main__':
#     unittest.main()
