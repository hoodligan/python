# 文件处理和os模块
# 回顾一下：函数
# 结构：
'''
def 函数名(参数，参数):
    逻辑
    return
调用：函数名(参数，参数)

参数：位置参数 关键字参数 默认参数 不定长传参 * **
*和**：可以接受多个参数  *接受参数接受未命名的参数 1,2,3,4,5，打包成一个元祖;
**接受参数接受命名的参数 name='小明',age=18,打包成字典

*和**解包：*把一个元祖解包成多个值
**把一个字典解包成name='小明',age=18

作业：下下节课

'''

# 匿名函数：lambda 表达式  lambda的主体是一个表达式，不是一个代码快
# 语法：lambda 参数,参数:表达式，逻辑功能
# 冒号前面的是参数
#  匿名函数不需要返回，它本身的结果就是返回值

# 求和 用普通
# def sum(a,b):
#     c=a+b
#     return c
# z=sum(2,6)
# print(z)
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
# num=lambda a,b:a+b
# print(num(2,9))

# 匿名函数只会完成基本的简单功能
# 普通函数完成复杂功能

# 使用  函数名()
# c=lambda :True
# print(c())
#
# def c():
#     return True
# c()

# 推导式 可以循环数据
# 推导式语法： [表达式 for xx in range()]
# 创建0-100的整数的列表
# list1=[i for i in range(101)]
# print(list1)

# list1=[]
# for i in range(101):
#     print(i+1)
#     list1.append(i)
# print(list1)

# list1=[i+1 for i in range(101)]
# print(list1)

# 创建字典：{key:value for i in range()}
# dict1={}
# for i in range(0,6):
#     # print(i)
#     dict1[i]=i*5
# print(dict1)

# dict1[0]=0
# dict1[1]=5
# dict1[2]=10
# dict1[3]=15
# dict1[4]=40
# 字典赋值：dict1={0:0,1:5,2:10}  没有重复的键  添加值
# dict['name']='xiaomin'
# dict{'name':'xiaoming'}

# {0:0,1:5,2:10,3:15}

# 推导式去创建字典
# dict1={i:i*5 for i in range(0,6)}
# print(dict1)

# 列表里面嵌套字典[{key:value} for i in range()]
# list1=[{i:i*5} for i in range(0,6)]
# print(list1)
#
# # 课后作业：用普通的for循环怎么表述
# list1=[]
# for i in range(0,6):
#     dict1={}
#     dict1[i]=i*5
#     # print(dict1)
#     list1.append(dict1)
# print(list1)

# if语句的三目运算  if的简写：
# 格式：result1 if 条件  else result2
# if 条件：
#     满足条件的事情
# else:
#     条件不满足的事情

# 两个数字判断 如果数字1大于数字数字2 大于数字1大，否则打印数字2大
# x=1
# y=2
# if x>y:
#     print('数字1大')
# else:
#     print('数字2大')

# print('数字1大') if x>y else print('数字2大')

# 匿名函数 推导式 for  三目运算

# 文件处理：
# 文件：音频，视频，照片，html
# 文件基本操作 打开文件  读取文件数据，写入文件数据 关闭文件数据
# 作用:为了方便管理数据 存储数据  下次可以直接使用

# 文件基本操作
# 打开 open(文件路径,访问模式)
# 读取 read
# 写入 write
# 关闭 close

# 打开test1.txt文件 写入数据  w  乱码 utf-8
# 打开
# f=open('test2.txt','w',encoding='utf-8')
# # 写入数据
# f.write('哈喽你好')
# f.close()

# f=open('test3.txt','r',encoding='utf-8')
# # 写入数据
# print(f.read())
# f.close()

# f=open('test2.txt','a',encoding='utf-8')
# # 写入数据
# f.write('你真好玩')
# f.close()

# f=open('test2.txt','w',encoding='utf-8')
# # 写入数据
# f.write('你是来开玩笑的吧')
# f.close()

# w是写入，没有文件创建文件写入内容  w会覆盖原有的内容
# r是读取，没有文件不会创建文件读取
# a是追加，没有文件创建文件追加内容


# 文件路径 open(文件路径,访问模式)
# 绝对路径:详细地址
# 相对路径:运行文件 相对于你的路径

# ./当前目录 运行文件在根目录 你要找文件夹的内容  找到class06房间里面的test1.txt 怎么找 相对路径
# f=open('./class06/test1.txt','r')
# print(f.read())
# f.close()

# .上一级./上级目录 运行文件在文件夹里面 我要找class05文件夹里面的test1.txt
# f=open('../class05/test1.txt','r')
# print(f.read())
# f.close()

# 注意：你的运行文件在哪

# 绝对路径:详细地址  \t解决
# f=open(r'D:\cmVip\CmVip0224\class06\test1.txt','r')
# print(f.read())
# f.close()

# 文件路径 open(文件路径,访问模式)
# 相对路径 绝对路径 访问模式 r w a  r+ w+ a+
#  r+读取可以写
# f=open('test1.txt','r+',encoding='utf-8')
# # print(f.read())
# # tell指针位置 0最前面
# print(f.tell())
# # 指针放到最后，偏移指针位置seek seek(字节数，指针位置)0开头 1当前位置 2结尾位置
# f.seek(0,0)
# print(f.tell())
# f.write('你好，妈妈咪呀')
# f.close()

# w是会覆盖掉
# f=open('test1.txt','w+',encoding='utf-8')
# # print(f.tell())
# f.seek(0,2)
# f.write('你是来搞笑的吗')
# f.close()

# f = open('test1.txt', 'a+', encoding='utf-8')
# print(f.tell())
# f.seek(0,0)
# f.write('我是来追加的')
# f.close()

# rb wb ab二进制文件
# 二进制文件：不能用txt打开
# 文本文件：能用txt打开

# 读取操作
# read() 读取整个文件
# readline()：读取一行
# readlines():读取所有的放在列表中
# 读取某一行的内容

# f=open('test1.txt', 'r', encoding='utf-8')
# # print(f.read())
# # print(f.readline())
# # print(f.readlines())
# print(f.readlines()[1])
# f.close()

# 读取文件的方式
# with open(路径,访问模式) as 变量名:
#   代码块

# with open('test1.txt', 'r', encoding='utf-8')as f:
#     print(f.read())

# z这个方式不用关闭

# 文件路径和读取文件的操作  读取yaml文件

# 文件和文件夹的操作
# os模块：提供了处理文件和文件目录的操作
import os

# 创建一个文件夹 w文件路径
# file=r'D:\cmVip\CmVip0224\class06\cc'
# os.mkdir(file)

# 删除文件夹
# os.rmdir(file)

# 非空文件夹
# import shutil
# shutil.rmtree(file)

# 文件重命名
# os.rename('test1.txt','test55.txt')

# 判断是文件夹
# print(os.path.isdir(file))
# 判断是文件
# print(os.path.isfile(file))

# 获取文件路径
# 当前文件夹绝对路径  D:\cmVip\CmVip0224\class06
# print(os.getcwd())
# 文件绝对路径  D:\cmVip\CmVip0224\class06\demo1.py
# print(os.path.abspath(__file__))
# D:/cmVip/CmVip0224/class06/demo1.py
# print(__file__)

# 当前路径的父路径 D:\cmVip\CmVip0224\class06
# print(os.path.dirname(os.path.abspath(__file__)))
# 数据库  绝对路径  config/conf.ini
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# D:\cmVip\CmVip0224\config
# a=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'config')
# # print(a)
# print(a+'\conf.ini')
# print(a+'\info.yaml')


# 作业：把学生管理系统的信息  添加信息保存到文件里面