# 函数和模块
# 回顾：1.if和循环
# 1. for 题目 计算0+1+2+3+4+5+6+7.......+100相加的和等于多少
# i=0
# sum=0
# while i<=100:
#     print(i)
#     sum=sum+i
#     print('0,100的和',sum)
#     i+=1

# sum=0
# for i in range(0,101):
#     print(i)
#     sum=sum+i
#     print('0,100的和', sum)

'''
2、"在一个月黑风高的夜晚，一个小男生用自己的零花钱给小女生买了一束鲜花，小女生问小男生鲜花的数量:“这花多少束?”，" \
"通过键盘输入小男孩回答的鲜花的束数，数量不一样小女生的反应也不一样。如果鲜花数大于等于9999，" \
"打印："小女生直接晕了过去",如果在1000(包含)-9999(不包含)，打印："明天就结婚",如果在100(包含)" \
"-1000(不包含)，打印："拉拉手意思意思，有空再约！",否则：打印："你是个好人"
'''
# 判断鲜花数
# 通过键盘输入鲜花的束数
# if 大于等于9999  打印："小女生直接晕了过去"
# 如果在1000(包含)-9999(不包含)  打印："明天就结婚"
# 如果在100(包含)" \"-1000(不包含)，打印："拉拉手意思意思，有空再约！"
# 否则：打印："你是个好人"
# num=int(input('请输入鲜花数量：'))
# if num>=9999:
#     print("小女生直接晕了过去")
# elif num>=1000 and num<9999:
#     print("明天就结婚")
# elif num>=100 and num<1000:
#     print('拉拉手意思意思，有空再约！')
# else:
#     print('你是个好人')

# 8、python实现石头剪刀布的游戏。
# 1.从控制台输入要输出的拳 - -石头（1）剪刀2、布3
# 2.电脑随机出拳 - -假定电脑只会出石头
# 3.
# 比较胜负

# 1.玩家在控制台中输入- -石头（1）剪刀2、布3
# 2.电脑随机出拳
# 3.比较胜负

# import random
# # 玩家
# play=int(input('请输入玩家要输出的拳- -石头（1）剪刀2、布3:'))
# # 电脑
# computer=random.randint(1,3)
# # 打印玩家输出的什么，电脑输出的什么
# print(f'玩家输出的是{play},电脑输出的是{computer}')
# # 比较胜负
# # 3种情况
# # 玩家赢：玩家石头--电脑剪刀   玩家剪刀--电脑布   玩家出布--电脑石头
# # 电脑赢：电脑石头--玩家剪刀   电脑剪刀--玩家布    电脑出布--玩家石头
# # 平局：玩家石头--石头
# # 玩家赢
# # if (play==1 and computer==2) or (play==2 and computer==3) or (play==3 and computer==1):
# #     print('玩家赢了')
# # elif (computer==1 and play==2) or (computer==2 and play==3) or computer==3 and play==1:
# #     print('电脑赢了')
# # else:
# #     print('平局')
#
# if (play==1 and computer==2) or (play==2 and computer==3) or (play==3 and computer==1):
#     print('玩家赢了')
# elif computer==play:
#     print('平局')
# else:
#     print('电脑赢')

# 任意的输入10个数字，按从大到小排序  冒泡排序 选择排序
# import random
# i=1
# list1=[]
# while i<=10:
#     a=random.randint(1,10)
#     # print(a)
#     list1.append(a)
#     i+=1
# list1.sort(reverse=True)
# print(list1)

# 函数和模块
# 函数：函数是把一个功能或者一个常用的代码，封装起来，封装成一个独立的模块，后面直接去使用函数名
# 使用步骤：
# 1.封装函数  常用的代码 封装成一个独立模块
# 2.调用函数  享受封装后的效果
# 作用：提高代码效率

# 语法
# def 函数名():
#     逻辑
# 调用   函数名()

# demo1.py文件里面输入 编号，姓名，年龄在控制台，在demo2.py文件，输入编号，姓名，年龄在控制台
# 封装 函数
# def info():
#     id=input('请输入编号:')
#     name=input('请输入姓名:')
#     age=input('请输入年龄:')
#     print('我的编号是{},姓名{},年龄{}'.format(id,name,age))

# 题目：实现两个数字相加  11 12  1 2  5 6
# def sum():
#     a=11
#     b=12
#     c=a+b
#     print(c)
#
# sum()

# 参数  函数带参数
# 形参  3 none
# def sum(a,b):
#     c=a+b
#     print(c)
#
# # 一定要传两个参数
# # 实参
# a=sum(1,2)
# print(a)

# 就需要return
# a想要把3拿出来，后面进行的运算  3 3
# def sum(a,b):
#     c=a+b
#     print(c)
#     return c
#
# a=sum(11,25)
# print(a)
# 拿到c之后在进行运算
# 不需要返回


# 返回是把结果返回给调用者。先调用函数执行运算，把结果返回给调用者

# print和return有什么区别
# print只是把结果打印在控制台，return把结果给到调用者，调用可以接受保存在变量里面

# 接口自动化  登录 拿到token值  token值返回出去  别的函数使用token
# retrun要不要  取决于自己

'''
def 函数名(参数，参数):
    逻辑
    return 
    
使用： 函数名(参数，参数)   
'''
# 空函数  pass 实际的作用  作用：写下个函数的逻辑时不让你报错
# 一个流程 登录 下单 支付
# def login():
#     pass
#
# def order():
#     print('下单')

# 函数 参数 写法
# 位置参数，关键字参数，默认参数，不定长参数
# 位置参数：实参的顺序，个数要和形参对应
# def sum(a,b):
#     return a+b
# z=sum(66,55)
# print(z)

# name=18,age='秋水'
# def person(name,age):
#     return '我是%s,年龄%s'%(name,age)
# p=person('秋水',18)
# print(p)

# 关键字参数，先定义形参，实参可以顺序不同，但是实参前面需要加上参数名称
# def person(name,age):
#     return '我是%s,年龄%s' % (name, age)
# d=person(age='虚竹',name='18')
# print(d)

# 默认参数 给形参加个实际的数据，加了数据之后，实参就不用给数据。实参给了数据，以实参数据为准
# def person(name,age=18):
#     return '我是%s,年龄%s' % (name, age)
# p=person('秋水',88)
# print(p)

# 一个函数里面又有默认参数，又有位置参数 怎么办
# 位置和默认参数同时存在，位置参数必须在默认参数前
# def person(name,age,sex='女'):
#     return '我是%s,年龄%s,性别%s' % (name, age,sex)
# p=person('秋水',88,'15')
# print(p)

# 不定长传参
# 不知道有多少个参数，在参数前面加个*或者**
# 加一个*，把传进来的值，放在元祖中
# 加两个** 把传进来的值，放在字典中

# *可以传多个值，后面的形参名，可以任意取名字，不建议换名字 args
# def person(args):
#     print(args)
# person('小米','华为','魅族')

# def person(*args):
#     print(args)
# person('小米','华为','魅族')

# 加两个 ** 把传进来的值，放在字典中
# *可以传多个值，后面的形参名，可以任意取名字，不建议换名字 kwargs
# 命名
# def person(**kwargs):
#     print(kwargs)
# person(name='秋水',age='18',sex='女')

# 一个函数里面又存在* ，又存在**
# *args放在**kwargs前面
# def person(*args,**kwargs):
#     print(args)
#     print(kwargs)
# person('小米','华为','魅族','a',1,name='秋水',age='18',sex='女')

# *可以接受多个值，接受后的值存在元祖中
# **可以接受多个值，接受后的值存在字典中

# 解包 pom
# username=('id','kw')
# pwssword=('name','su')
# # driver.find_element_by_id('su')
# def loctor(loc):
#     driver.find_element(*loc)


# *能解包元祖
# def person(loc):
#     print(*loc)
#     # print(loc)
# person(('id','kw'))

# loc 能不能接受 ('id','kw') 一个元祖 一个数据
# 一个数据，解包解开  解成2个数据 *

# **能够解包字典  为什么不能直接print(**loc)  print函数
#
# def person(loc):
#     print(**loc)
# person({'name':'秋水','age':'18'})
# name='秋水'，age=18


# loc相当于接受到{'name':'秋水','age':'18'}
# print  **loc  name='秋水'，age=18
# print是一个函数
# def print(self, *args, sep=' ', end='\n', file=None):
#     print('aaa')
# print(name='秋水',age=18)


# 函数嵌套
# 函数里面嵌套函数 一个test1函数 一个test2函数
# 函数 从上到下执行 只有函数调用的时候才是真正的执行
# 要调用函数才会执行
# def test01():
#     print('*'*50)
#     print('test1')
#
# def test02():
#     print('*'*50)
#     print('test2')
#     test01()
#     print('-'*50)
#
# test02()

# 结果是怎样的？
# *******
# test1
# *******
# test2
# ------


# print('*' * 50)
# print('test2')
# print('*'*50)
# print('test1')
# print('-'*50)


# *******
# test2
# *******
# test1
# ------


# 函数
'''
def 函数名(参数，参数):
    逻辑  
变量=函数名(参数，参数)

# 参数:位置参数：形参实参一一对应
# 关键字参数：实参前面给个具体的参数命名和参数数据
# 默认参数：形参里面默认给了个数据，实参可以不给数据
# 不定长传参：* 接受多个，转成元祖  ** 接受多个  转成字典
# *接受元祖后，可以解成一个个的数据   ** 接受字典后，可以解成一个个的命名数据
# return返回值：你要不要返回  

# web自动化  尝试理解一下base文件里面的封装  写一下
'''

# 封装之后，不能直接使用，一定要调用才行  demo1.py文件没有注释
# demo1.py文件运行了一次  一次
# 用main 入口函数 可以自己运行函数，还不会被别的文件调用到
# if __name__ == '__main__':
#     info()


