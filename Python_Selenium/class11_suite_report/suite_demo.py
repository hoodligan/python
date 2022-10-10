'''
    Suite测试套件，专门用于管理所有的测试用例类。可以理解为是用例的List，物理形态下就是一个文件夹的概念。
    套件的使用，一定是重新建立一个py文件进行调用，如果在UnitTest类下通过main函数调用则不会生效。
    unittest.TestSuite类来进行使用
    suite的运行一定是基于运行器来运行的。
    套件中运行的测试用例，是基于添加的顺序来进行执行的，与UnitTest的用例排序没有关系
    HTMLTestRunner测试报告：本质意义而言，其实就是一个运行器。
        环境部署：直接下载py文件，放到python安装路径下的Lib文件夹中就可以了。不要通过pip安装
        网上下载的默认是只支持2.7版本及以下的。如果要支持到3以上版本，需要修改源码。
        修改py文件的源码：
            第94行，将import StringIO修改成import io
            第539行，将self.outputBuffer = StringIO.StringIO()修改成 self.outputBuffer = io.StringIO()
            第642行，将if not rmap.has_key(cls):修改成if not cls in rmap:
            第766行，将uo = o.decode('latin-1')修改成uo = e
            第772行，将ue = e.decode('latin-1')修改成ue = e
            第631行，将print >> sys.stderr, '\nTime Elapsed: %s' %  (self.stopTime-self.startTime)修改成print(sys.stderr, '\nTime  Elapsed: %s' % (self.stopTime-self.startTime))

        UnitTest下所有的测试用例用test开头。所有的测试用例文件，也需要以test开头
'''
import os
import unittest
# from HTMLTestRunner import HTMLTestRunner
from HTMLTestReportCN import HTMLTestRunner
# 创建测试套件
from class10_unittest import test_demo
from class10_unittest.test_demo import UnitDemo, UnitDemo02
from class11_suite_report.test_demo import Demo

# suite = unittest.TestSuite()
# 在套件中添加测试用例
# 基于用例的名称来添加单个测试用例
# suite.addTest(UnitDemo('test_02'))
# suite.addTest(Demo('test_03'))
# 批量添加用例
# 基于用例名称进行添加，以list形式
# cases = [Demo('test_01'), UnitDemo('test_03')]
# suite.addTests(cases)
# 通过添加一个完整的class进入套件
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Demo))
# 基于文件名称来进行添加:添加的是当前路径下的py文件，否则会报错
# cases = [unittest.TestLoader().loadTestsFromName('unit_demo.UnitDemo')]
# suite.addTests(cases)
# names = ['unit_demo.UnitDemo', 'unit_demo.UnitDemo02']  # py文件的名称+class的名称
# suite.addTests(unittest.TestLoader().loadTestsFromNames(names))
# 批量添加测试用例，在持续集成中比较好用。批量化管理测试用例也很好用
# 定义用例的获取路径
path = '../'
discover = unittest.defaultTestLoader.discover(start_dir=path, pattern='test*.py')
# 通过运行器来运行套件
# run = unittest.TextTestRunner(verbosity=2)  # verbosity 参数表示显示的控制台信息详细度，分为0，1，2三级
# # run.run(suite)
# run.run(discover)

# HTMLTestRunner生成测试报告
# 配置测试报告的相关内容
report_dir = './report/'  # 保存路径
report_title = '虚竹的测试报告'  # 报告名称
report_description = '这是测试报告中的描述部分'  # 测试报告描述
report_file = report_dir + 'report1.html'  # 测试报告的文件：建议测试报告的名称以时间戳的形式进行命名
# 测试执行者
report_tester = '小别扇'
# 保存报告的路径是否存在，不存在则创建一个
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

# 生成测试报告,其实就是写入一个文件内容
with open(report_file, 'wb') as file:
    runner = HTMLTestRunner(stream=file, title=report_title,
                            description=report_description, verbosity=2, tester=report_tester)
    runner.run(discover)
