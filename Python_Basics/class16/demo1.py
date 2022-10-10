# 日志：日记  记录作用
# 日志作用：系统运行信息

# 学习日志：
# 几个组件：
# loggers:日志器 程序的入口 别的文件想要调用就用日志器
# handlers处理器：日志信息 输出到你想要的位置 控制台处理器 文本文件处理器
# formatter格式器：处理日志格式 格式比较好看
# filter过滤器

# 日志级别：
# 1.debug级别：调试级别  1  10
# 2.info级别：正常级别  2   20
# 3.warning警告：有问题但不影响程序运行  3  30
# 4.error级别：错误的  4   40
# 5.critical:严重的 程序崩溃   5  50

# 输出日志信息
import logging
def test_log():
    # 设置日志级别  默认级别 warning警告
    fmt='%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s'
    logging.basicConfig(level=logging.INFO,format=fmt,filename='log.txt')
    return logging





# log=test_log()
# log.info('aaaaaa')


# 打印日志信息  日志写死的
# try..except  你用info调用的日志信息就是打印正常的日志信息
# 你用error调用的日志信息就是错误的日志信息
# logging.debug('调试的日志信息')
# logging.info('正常日志信息')
# logging.warning('警告的日志信息')
# logging.error('错误的日志信息')
# logging.critical('严重的日志信息')

# 日志信息很像print，
# 用日志信息可以自己设置格式，可以保存到文本文件
# 什么时间生成的日志  在哪个文件生成的日志 在哪个函数生成的日志


# basicConfig 生成日志文件很简单
# 有缺点：控制台，日志信息保存在文件中后，会显示在文本里面控制台里面就没有。不会同时存在
# 中文会乱码,需要到basicConfig底层去修改utf-8
# 没怎么用，自己封装下日志
