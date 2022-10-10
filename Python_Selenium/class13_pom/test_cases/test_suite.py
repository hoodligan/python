'''
    封装获取用例的套件函数
'''
import threading
import unittest


def get_suite():
    path = './'
    discover = unittest.defaultTestLoader.discover(start_dir=path, pattern='test*.py')
    return discover


# 运行器运行套件函数
def runner(suite):
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    suites = get_suite()
    th = []
    for suite in suites:
        th.append(threading.Thread(target=runner, args=[suite]))
    for t in th:
        t.start()
