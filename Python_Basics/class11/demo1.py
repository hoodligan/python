# 装饰器
# 上节课：
# 继承（单继承，多继承）语法： 类名(父类) 继承 继承父类的属性和方法
# 多态：同一个方法传入不同的对象会有不同的形态 飞  天鹅 鸡 麻雀
# 类方法 实例方法 静态方法：
# 实例方法 类中的函数带有self
# 类方法：需要用到@classmethod装饰，参数命名cls
# 静态方法：需要用到@staticmethod装饰,参数没有self也没有cls  参数

# class Stu:
#     school='测码课堂'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     # 实例方法
#     def play_ball(self):
#         print(f'{self.name}打篮球')
#
#     # 类方法
#     @classmethod
#     def sport(cls):
#         print(f'{cls.school}的同学都喜欢打羽毛球')
#
#     # 静态方法内部里面没有用到类相关的内容，可以把这个函数定位静态方法
#     # 定义成静态方法可以不用对象.方法名。可以类.方法名
#     # 静态方法要求，你想要把你的普通方法定义成静态方法，要求你的这个方法，不要去引用到外部的东西
#     @staticmethod
#     def clean():
#         print('打扫卫生')
# stu1=Stu('cxk',18)
# stu1.play_ball()
# Stu.play_ball(stu1)

# stu1=Stu('cxk',18)
# stu1.sport()
# Stu.sport()

# Stu.clean()
# 实例方法：对象名.方法名()  类.方法名(对象名)
# 类方法：对象名.方法名()   类.方法名  你的整个类都可以拥有的一个方法，可以设计成类方法
# 静态方法：对象名.方法名()  类.方法名  不会访问类的任何属性或其他方法，可以设计成静态方法

# 装饰器：给已有的函数增加额外的功能，它的本质是一个闭包函数
# 闭包函数：
# 函数，函数调用完之后，内部定义的变量直接销毁了，但是有时候我们需要保存函数内的这个变量
# 在这个变量进行一些其他操作，比如求和
# 闭包：
# 形成条件
# 1.实现函数嵌套
# 2.内部函数使用外部函数的变量
# 3.外部函数返回内部函数名字，不要加括号

# 简单写个闭包
# def test01(a):
#     b=1
#     def test02():
#         print(a,b)
#     return test02
#
# # a=test02
# a=test01(6)
# # test02()
# a()
# print里面会返回什么  6,1
# 步骤：是怎么运行的？
# 函数是从上到下执行，只要在函数调用 也就是 函数名()才会执行到函数内部
# 不会走到test02    test02()才会执行到test02函数内部

# retrun 返回 test02   test02给谁？ test01

# 定义两个数字相加求和
# def outer(num1):
#     print(num1)
#     def inner(num2):
#         result=num1+num2
#         print(result)
#     return inner
#
# c=outer(5)
# c(9)

# print之后
# 1.outer(5)先走入到outer(num1)函数内部，num1就是5，打印出来的也是5、
# 接下来不会走入到inner(num2)函数内部。返回inner给到outer(5)，所以outer(5)就是inner.
# c=inner   c(9)就相当于 inner(9) 触发了函数条件，打印出来的就是14

# result=num1+num2  num1+=num2 可以吗？ 可以1 不可以2

# def outer(num1):
#     print(num1)
#     def inner(num2):
#         result=num1+num2
#         # print(result)
#         return result
#     return inner
# # inner只是一个名 没加()
#
# # 不是固定写法  c是变量名随便取  c就是为了取 inner
# a=outer(5)
# c=a(9)
# print(c)

# 函数从上到下执行，只有 函数名(参数) 的时候才会执行
# 打印print(5)
# def inner(num2):
#     result = num1 + num2
#     print(result)
# 没有触发条件 inner(num2)
# 返回inner  a就是inner  a(9)==inner(9)


# result=num1+num2  num1+=num2 可以吗？ 可以1 不可以2

# def outer(num1):
#     print(num1)
#     def inner(num2):
#         nonlocal num1
#         num1+=num2
#         print(num1)
#     return inner
# d=outer(5)
# d(8)
# 定义一下num1编程global
# 不用global定义修改值用于不同函数  这里用nonlocal：作用对象是外层的变量，就是用在闭包里面

# 普及知识点：局部变量
# 局部变量：定义在函数内部
# 全局变量：定义在函数外部
# 全局变量
# num1=100
# def test01():
#     # 局部变量
#     num2=3
#     # 局部里面不能直接修改外部变量
#     # 在函数内部修改全局变量的值 用到global
#     global num1
#     num1+=num2
#     print(num1)
# test01()

# 闭包的作用，变量不会污染全局变量，不会因为外部函数调用而销毁掉

# 装饰器：就是给已有的函数增加额外的功能
# 特点：
# 不需要修改原有的代码，就能增加函数额外的功能
# 不用修改调用方式，就能增加函数额外的功能

# 发表评论 检查有没有登录 检查一下我有没有登录 没有登录 登录一下
# 闭包
# check(comment)
# def check(fc):
#     print('装饰器函数执行')
#     def inner():
#         print('请先登录')
#         fc()
#     return inner
#
# # check(comment)
# @check
# def comment():
#     print('发表评论')
#
# # 调用方式更改了
# # a=check(comment)
# # a()
#
# # 装饰器的语法糖改一下  @额外功能的函数  inner()
# comment()


# @check装饰器，怎么去运行的？@check相当于代理，
# 现在要运行comment()找代理人先预约走入到
# 1.先打印 print('装饰器函数执行')
# 不会走入到inner函数内部，没有被调用。返回inner 这个inner返回给谁
# inner返回给秘书inner=comment()
# 2.print('请先登录')
# 3.fc() fc是comment  comment()


# 练习题目：现在有个函数，想要知道这个函数执行了多久时间
import time


# def decorate(fc):
#     def inner():
#         # 获得当前的时间
#         print(time.strftime('%Y-%m-%d %H:%M:%S'))
#         # 当前时间的时间戳 秒数
#         t_starttime=time.time()
#         b=fc()
#         print(b)
#         #结束时间的时间戳
#         t_endtime=time.time()
#         print(time.strftime('%Y-%m-%d %H:%M:%S'))
#         # 结束时间-开始时间秒数=剩余秒数
#         print('总共花了%.5f'%(t_endtime-t_starttime))
#         return 5
#     return inner
#
#
# # decorate(test_01)
# @decorate
# def test_01():
#     time.sleep(2)
#     print('函数在执行中')
#     return 8
#
# c=test_01()
# print(c)

# 迭代器 自定义迭代器里面 iter 还有一个next
# 数据类型：字符串 列表 元祖 集合字典 是不是可以用for循环拿到里面的数据类型
# for里面是怎么运行  台前看不到
# 特殊方法__iter__() 返回一个迭代器对象，迭代器对象里面在用__next__()把里面的数据拿出来
# 多拿了一个，报错 StopIteration 异常
# a=[1,2,3,4]
# b=(1,2,3)
# # print(a.__iter__())
# # print(b.__iter__())
# iterA=a.__iter__()
# print(iterA.__next__())
# print(iterA.__next__())
# print(iterA.__next__())
# print(iterA.__next__())
# print(iterA.__next__())


# 生成器也就是一个特殊的迭代器，使用yield的函数就被称为生成器，不是一个普通的函数了
# def gen():
#     yield
# print(gen())

# 第一种用yield 生成器
# 5
# def gen(n):
#     # 0,1,2,3,4
#     for i in range(n):
#         # 每次遇到yield时候函数暂停并报错当前的运行信息
#         yield i*i
# # 不会直接进入gen(5)生成器内部，需要循环或者next才会进入到生成器函数内部
# x=gen(5)
# for i in x:
#     print(i)
# lst = [1,3,4,5,6]
# # lst = [1,2,5,6,7]
# for i in lst:
#     print(list(i))
# #     if i in lst1:
# #         print(i)
#
# 最外层的循环会先运行  [1,3,4,5,6]
# lst = [1,3,4,5,6]
# l = (i for i in lst if i in lst)
# lst = [1,2,5,6,7]
# # for i in l:
# print(list(l))

# 打印出来的值是什么？
# 0

# 推导式外层()用也表示生成器
# gen=(i*i for i in range(5))
# print(gen)
# for i in gen:
#     print(i)

# send方法实现生成器内部进行数据交互
# close关闭生成器


