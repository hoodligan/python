# 日志器封装
# 组件
# 学习日志：
# 几个组件：
# loggers:日志器 程序的入口 别的文件想要调用就用日志器
# handlers处理器：日志信息 输出到你想要的位置 控制台处理器 文本文件处理器
# formatter格式器：处理日志格式 格式比较好看
# filter过滤器

# 两种封装 一个是basicConfig,一个是自己封装的
# 意思：使日志信息 格式是我们想要的，日志能保存在控制台 能保存在文本文件
import logging

def test_log2():
    # 创建日志器  这个日志器就写入了日志信息
    logger=logging.getLogger()
    # 显示日志信息全面 设置日志级别
    logger.setLevel(logging.INFO)
    # 日志信息显示在控制台  你不加这句话
    if not logger.handlers:
        # 需要控制台处理器
        sh=logging.StreamHandler()
        # 日志信息放入控制台中
        logger.addHandler(sh)

        # 保存在文件中 文件处理器
        fh=logging.FileHandler('log1.txt',encoding='utf-8')
        # 把日志信息添加到文件中去
        logger.addHandler(fh)

        # 日志比较丑，设置格式  创建格式器
        fmt = '%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s'
        formater1=logging.Formatter(fmt)

        # 给谁加格式
        # 给控制台加格式  控制台是哪个单词？
        sh.setFormatter(formater1)
        fh.setFormatter(formater1)
    return logger


# 封装日志 有三种方式 1.baseConfig  2.自定义函数封装  3.ini文件
# 使用的话 拿到封装文件.info()或者拿到封装文件.error()
# 重要 重要 项目 加上日志  不重要 封装一次 后续只要使用即可
# 我们还是要会

# 这种方式用的多








# 要用的时候才调用info 封装一下

# logger.debug('调试的日志信息')
# logger.info('正常日志信息')
# logger.warning('警告的日志信息')
# logger.error('错误的日志信息')
# logger.critical('严重的日志信息')