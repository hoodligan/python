# 异常处理  异常
# 概念：
# 程序在运行时，如果程序遇到一个错误，程序就会自动停止的行为，抛出错误信息的就叫异常

# 异常处理
# 保证程序的健壮性和稳定性
# 健壮性 ：健康  小问题 自己出处理掉
# 稳定性： 让程序稳定运行

'''
try:
    要执行的代码
except:
    出现的错误
'''

# try里面放你不确定的代码
# except 如果出现了错误就执行except的代码

# 输入整数
# num=int(input('请输入整数:'))
# print(num)
# num1=3+5
# print(num1)

# try:
#     num=int(input('请输入整数:'))
#     print(num)
# except:
#     print('请输入正确的数字')
#
# num1=3+5
# print(num1)


# 处理 分报错提示
import time

'''
try:
    要执行的代码
except 错误类型：
    出现错误的处理
except 错误类型：
    出现错误的处理
'''

# 输出一个数字对于另外一个数字进行整除
# num=float(input('请输入数字:'))
# result=2/num
# print(result)
# ZeroDivisionError: float division by zero
# ValueError: could not convert string to float: 'a'

# try:
#     num = float(input('请输入数字:'))
#     result = 2 / num
#     print(result)
# except ZeroDivisionError:
#     print('请不要输入0，0不能被除')
# except ValueError:
#     print('请输入正确的数字')

# 在执行程序时，会遇到不同类型的异常，针对不同的异常做出不同的处理

'''
try:
    要执行的代码
except (错误类型1,错误类型2)：
    出现错误的处理

'''
# try:
#     num = float(input('请输入数字:'))
#     result = 2 / num
#     print(result)
# except (ZeroDivisionError,ValueError) as e:
#     print('请输入正确的数字%s'%e)

#  面试题
# 文件 ioEerro
# FileNotFoundError
# ValueError
# IndexError
# TypeError 类型错误

# 想不到那么多异常 大概预测 碰到了别的问题 怎么办 报错？
# exception 异常的父类  BaseException
# ZeroDivisionError,ValueError    exception 拿到了所有的异常 都可以去处理
# exception接受所有异常并且处理
# as e异常信息 e里面 as 取名
# 为什么会错误 e捕获到错误
# e获取异常信息
# try:
#     num = float(input('请输入数字:'))
#     result = 2 / num
#     print(result)
# except Exception as e:
#     print('请输入正确的数字%s'%e)

# 我们不知道会出现什么错误的时候 都可以用Exception捕获到异常
# 自动化

'''
try:
    要尝试的代码
except 错误类型:
    捕获错误类型
except 错误类型:
    捕获错误类型
except Exception as e:
    print(e)
else:
    没有异常才会执行的代码
finally:
    无论如何都会执行

'''
# try:
#     num = float(input('请输入数字:'))
#     result = 2 / num
#     print(result)
# except ZeroDivisionError as e:
#     # 1
#     print('不能被0整除%s'%e)
# except ValueError as e:
#     print('值错误%s'%e)
# except Exception as e:
#     # 3
#     print('所有错误%s' % e)
# else:
#     print('正常执行')
# finally:
#     print('无论有没有异常都执行')
# a

# 异常处理可以抛出去
# def demo1():
#     try:
#         num = float(input('请输入数字:'))
#         result = 2 / num
#         print(result)
#     except Exception as e:
#         print('请输入正确的数字%s'%e)
#
# print(demo1())

# def demo1():
#     num = float(input('请输入数字:'))
#     result = 2 / num
#     print(result)
#
# try:
#     print(demo1())
# except Exception as e:
#     print(e)

# 做自动中可以在函数内部 捕获异常 也可以在调用函数的时候捕获异常
# 调用函数捕获异常  代码干净点

# raise自定义异常 特定的要求就会用自定义异常
# 输入密码：
# 密码长度<8，抛出异常
# 密码>=8，返回密码的长度

# def input_password():
#     try:
#         pwd=input('请输入密码：')
#         if len(pwd)<8:
#             # print('密码小于8')
#             raise Exception(len(pwd),8)
#     except Exception as e:
#         print('密码长度不够%s'%e)
#     else:
#         print('密码输入完成')
#         return pwd
#
# pwd=input_password()
# print(pwd)

# 时间和日期  打印日志，生成测试报告 订单
# 生成日历 年历月历和日历
import calendar

# 输出3月的日历
# cal=calendar.month(2022,3)
# print(cal)

# 22年的年历
# year=calendar.calendar(2022)
# print(year)

# 时间戳：从1970年1月1日0点0分0秒时间 -现在时间秒数
# print('当前时间戳:',time.time())

# 时间元祖 元祖(年月日时分秒 一周的第几日 0-6 0是星期一一 年的第几天 夏令时)
# t=(2022,3,13,22,19,21,72,0)
# print(t)

# 时间戳转为时间元祖
# print('时间戳转为时间元祖:'time.localtime(time.time()))

# 时间元祖转为日期 time.asctime
# print('英文的日期'time.asctime(time.localtime(time.time())))

# 日期格式 百度 %Y %m %d  这个用的多点  用到了时间
# print(time.strftime('%Y/%m-%d %H:%M:%S'))