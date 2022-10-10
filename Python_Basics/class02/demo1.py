# Python不可变数据类型
# 回顾：1.python简介
# 2.python安装 pycharm安装
# 3.print打印  变量  输入  模块

# name='翠花'
# age=18
# sex='女'
# height=1.65
# weight=55
# print(name,age,sex,height,weight)
# 打印出自己想要的格式
# 字符串格式化 3种写法 我的名字叫xx，年龄xx岁，性别xx，身高xx，体重xx  关键字  用
# print('我的名字叫{}，年龄{}岁，性别{}，身高{}，体重{}'.format(name,age,sex,height,weight))
# # 不想按顺序  下标  生活1开始  编程0开始
# print('我的名字叫{1}，年龄{0}岁，性别{2}，身高{3}，体重{4}'.format(age,name,sex,height,weight))
# 传数据%s 字符串   %s 字符串  %d传数字
# print('我的名字叫%s，年龄%d岁，性别%s，身高%s，体重%s'%(name,age,sex,height,weight))
# f-string
# print(f'我的名字叫{name}，年龄{age}岁，性别{sex}，身高{height}，体重{weight}')
# 用的比较多  用哪个 你们自己开心

# name=input('请输入你的姓名：')
# print(name)

# Python不可变数据类型
# 不可变数据类型：字符串  数字 元组
# 可变数据类型：列表 字典 集合

# 数字:
# 小数float 1.5  1.2
# 整数 int 1 2 3 4
# 布尔类型 bool True 1  False 0

# # 数据类型是什么  type(变量名) 打印数据类型
# inta=1
# print(inta,type(inta))

# floatb=2.5
# print(floatb,type(floatb))

# boolTrue=True
# print(boolTrue,type(boolTrue))

# 判断True是不是1
# 1 返回  真  不相等 false  ==相等  =赋值
# print(True==1)
# print(True==0)
# print(False==0)

# 数字  数字运算+ - */  比较大小
# a1=10
# b1=8
# + -* /浮点除 //整数除  %取余数  **乘方
# print(a1+b1)
# print(a1-b1)
# print(a1*b1)
# print(a1/b1)
# print(a1//b1)
# print(a1%b1)
# print(a1**b1)
# print(2**4)

# 比较大小  == != >= <= > <  返回 真假
# a1=10
# b1=8
# print(a1>b1)
# print(a1<b1)
# print(a1<=b1)
# print(a1>=b1)
# print(a1!=b1)
# print(a1+b1==a1-b1)

# 赋值运算符 += -= *= /=
# a1=10
# b1=8
# a1=a1+b1 1.先运算   2.在赋值
# a1+=b1
# print(a1)
# # a1=a1-b1  1.先运算 a1=18-8   2.在赋值  变量的值 可变的
# a1-=b1
# print(a1)

# 数据类型可以进行转化的  int float  记住
# a1=10
# b1=8.2
# # print(float(a1),type(float(a1)))
# print(int(b1),type(int(b1)))
# 10是整数类型 ，想要改成小数类型 float(变量名)
# 8.2是float类型 ，想要改成整数类型 int(变量名)

# 常用的用法  大概知道有这么个东西，用到百度
# 绝对值 abs()
# abs1=-1
# print(abs1,abs(abs1))

# 向上取整ceil  向下取整floor
# 1.导包 math
# import math
# a1=2.3
# print(math.ceil(a1))
# print(math.floor(a1))

# 随机数 random  random.random()
# 1.导包
# import random
# random.random()  0-1随便出
# print(random.random())
# 指定范围输出数字
# print(random.randint(1,20))

# 数字类型：
# 1.整数 小数 布尔类型  int  float boole
# 2.加减乘除 + - * / %  比较大小 == >= <= != 赋值运算 += -= *= /=
# 3.常用函数 abs floor ceil 随机数
# 不用死记  转型 知道

# 字符串
# 中文 a b c d 你好  hello   1 2 3 4 5
# 只要是双引号 或者单引号 或者三引号 括起来的都是字符串  三引号 换行
# str1=1
# str2='1'
# str3="23"
# str4="""你好"""
# print(str1,type(str1))
# print(str2,type(str2))
# print(str3,type(str3))
# print(str4,type(str4))

# 难点 字符串的切片  面试中
# 字符串  test123456hello  取出123456
# 列表 1=['秋水','虚竹'，'展昭']  t=(a,b,1)
# 作用：把一个大的字符串切成小的字符串
# 语法：str[开始值:结束值:步长] 0开始  结束值：左闭右开  1，2，3，4，5，6   0-5  0-6
# 步长：决定方向 1从左往右取  -1 从右往左取  默认 1    间隔数

# 0  1   2  3   4   5  6  7  8   9  10  11  12  13 14
# t  e   s  t    1  2  3  4   5  6  h   e   l   l   o
#                                    -5  -4 -3   -2  -1
# str2='test123456hello'
# 取出123456
# print(str2[4:10])
# print(str2[4:10:1])

# 取出hello  从右往左走   默认 1 从左往右走
# print(str2[-1:-6])
# olleh
# print(str2[-1:-6:-1])
# print(str2[10:15])
# print(str2[10:])
# print(str2[-5:])
# print(str2[-5:15])

# 隔一个取一个
# print(str2[::3])

# 反转  0lleh
# print(str2[::-1])

# 字符串中的运算符  拼接+  *复制
# name='cc'
# age='18'
# print('你的名字叫'+name,'年龄'+age)
# # *复制
# print(age*3)

# 常用函数
# join连接 元组，列表字符串的元素连接成一个新的字符串
# 分割符.join(数据)
# l=['my','name','is','qiushui']
# print(' '.join(l))
# print('-'.join(l))

# split:把字符中的数据通过指定的分割符号拆成一个个的，返回列表
# str2.split(分割符，分割几次)
# str2='www.baidu.com.cn'
# print(str2.split('.'))
# print(str2.split('.',2))
# print(str2.split('.',1))

# 查找 find  index  字符中包含这个字符串没有
# find在里面返回索引  不在里面就会返回-1  下标
# index在里面返回索引  不在里面就会报错
# name='my name is qiushui'
# str2='is'
# # print(name.find(str2))
#
# print(name.index(str2))
# \n换行 \t tab键
# print('你好\n我是秋水')
# print('\t你好我是秋水')

# 设置路径 设置r 或者用\\
# url=r'D:\\vcmVip\\CmVip0224\\nclass02\\demo1.py'
# print(url)

# 判断
# str1='post get'
# # 大写
# print(str1.upper())
# # 小写
# print(str1.lower())
# # 首字母大写
# print(str1.capitalize())
# # 首字母每个都是大写
# print(str1.title())
# # 判断是不是大写
# print(str1.isupper())
# print(str1.islower())

# 知识点 用的