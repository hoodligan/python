# 面向对象
# 万物皆对象
# 封装代码的方法，封装更先进
# 面向对象，从面向过程的基础发展过来的，比面向过程更具有灵活性和扩展性
# 面向过程，面向对象编程解决问题的一种方式 ，都是指对同一个问题的不同解决方式

# 把大象装进冰箱步骤？3步
# 1.打开冰箱门
# 2.把大象装进冰箱
# 3.关闭冰箱门

# 学生管理系统面向过程，添加修改删除查询工具独立封装成一个个的函数，最后使用有顺序的去调用不同的函数
# 日常思维去做
# 面向过程思维：
# 2.把大象装进冰箱
# 3.关闭冰箱门
# 1.打开冰箱门
# 使用的时候 1.打开冰箱门  2.把大象装进冰箱  3.关闭冰箱门
# 流水线思维  web自动化公开课  线性代码 实现百度搜索
# 1.打开谷歌浏览器  2.访问百度  3.找到输入框输入搜索内容  4.找到搜索按钮进行点击
# 面向过程：注重过程

# 面向对象：创建一个对象  把要做的事情交给这个对象去做
# 创建一个对象
# 冰箱对象
# 冰箱有打开门的方法
# 冰箱有装东西的方法(大象，零食，饮料)
# 冰箱有关闭的方法

# 编程解决问题的方案
# 面向对象：侧重的谁来做
# 面向过程：一套流水线，从头到尾一套流程有顺序的去解决问题

# 面向对象，面向过程 方式更好：学习的思维 简单代码 不复杂的流程 面向过程做 元素定位（追踪报错）
# 1.打开谷歌，2.访问登录页，3，找到输入框输入用户，密码点击登录，搜索手机，手机添加到购物车
# 复杂的流程 面向对象的思维去做
# 面向对象pom页面对象：
# 登录一个页面对象 登录页对象 找用户名输入框 找密码输入框 找登录按钮 登录的整个流程 加了个流程 验证码
# 添加到购物车页  找颜色 找数量

# 有几个学生，第一个学生：
# 小李 年龄18岁，性别女，会打游戏，会打羽毛球
# 小明，年龄20岁，性别男，会吃鸡，会打篮球
# 弯弯，年龄60岁，性别女，会做饭，会织毛衣
# 面向过程去写：
# 定义一个小李学生年龄18岁，性别女，会打游戏，会打羽毛球 函数信息
# 定义一个小明，年龄20岁，性别男，会吃鸡，会打篮球 函数信息
# 定义一个弯弯，年龄60岁，性别女，会做饭，会织毛衣  函数信息
# 获得小李的信息
# 调用小李的函数就行
# 小明的函数

# 面向对象去写？
# 学生对象
# 学生模板：名字，年龄，性别  会打游戏  会打羽毛球  会吃鸡  会打篮球  会做饭  会织毛衣
# 创建('小李',18,女) 会打游戏  会打羽毛球
# ('弯弯',60,女) 会做饭  会织毛衣
# 创建多少个学生 给他多少学生  学生有多少技能多少技能

# 面向对象：了解到两个名称
# 类：具有共同特征或者相同行为的事物的一个统称
# 鸟类：
# 特征：有翅膀，有两只脚，有一双眼睛，心脏为四室，体温恒温
# 行为：会飞，会吃虫子
# 特征被称为：属性
# 行为称为：方法

# 类是抽象,不能指具体的事物，就是一个总的模板
# 对象：具体的某一个东西  具体的楼下阿姨家的鹦鹉，隔壁小王家的麻雀  不同具体的对象

# 定义类
'''
class 类名:
    类属性
    类方法
    def 方法1(self):
        pass

    def 方法2(self):
        pass

类属性：事物的特征
类方法：事物具有的行为
类名:第一个首字母大写
'''

# 游戏，游戏中有几只猫，都是20kg，颜色都是白色，所有我有几只20斤的白猫，一只白猫会抓老鼠
# 一只白猫会吃鱼，一只白猫会吃鱼又会抓老鼠又会打洞。
# 写？面向过程？定义3只猫
# 面向对象。创建一个模板 也就是类
# class Cat:
#     cat_color='白色'
#     cat_weight=40
#
#     def catch(self):
#         print('小白猫抓老鼠')
#
#     def eat(self):
#         print('小白猫爱吃鱼')
#
#     def cave(self):
#         print('小白猫会打洞')

# 白猫类的所有特征

# 类不能够直接使用

# 创建具体的对象  也就是实例化对象 对象名=类()  对象名.方法名 对象名.属性
# tom小白猫
# tom1=Cat()
# tom1.catch()
# # 创建出来一只具体的会抓老鼠的猫
# print('-'*50)
# tom2=Cat()
# tom2.eat()
# # 创建出来一只具体的会吃鱼的猫
# print('-'*50)
# tom3=Cat()
# tom3.eat()
# tom3.catch()
# tom3.cave()
# # 创建出来一只具体的会吃鱼会抓老鼠会打洞的猫
#
# # 这是是3只猫 不确定是不是三只猫 检测是不是三只猫？id检测
# print(tom1,id(tom1))
# print(tom2,id(tom2))
# print(tom3,id(tom3))

# class Cat:
#     def __init__(self,color,weight):
#         self.cat_color=color
#         self.cat_weight=weight
#
#     def catch(self):
#         print(f'{self}小{self.cat_color}猫抓老鼠')
#
#     def eat(self):
#         print('小白猫爱吃鱼')
#
#     def cave(self):
#         print('小白猫会打洞')
#
# # self  不知道 断点看看  self像是对象地址  self好像就是对象
# # 创建了一个对象，self就能区分你是哪个对象
# # self 代表你自己 对象本身
# tom1=Cat('小翠',20)
# tom1.catch()
# # # 创建出来一只具体的会抓老鼠的猫
# print('-'*50)
# tom2=Cat('小花',30)
# tom2.eat()
# tom2.catch()
# # 创建出来一只具体的会吃鱼的猫
# print('-'*50)
# tom3=Cat()
# tom3.eat()
# tom3.catch()
# tom3.cave()

# 猫都是白色的，能不能搞特殊，有一只猫长着变异 黑白猫
# 改变猫的属性
# tom1=Cat()
# tom1.cat_color='黑白'
# tom1.catch()
#
# tom2=Cat()
# tom2.catch()


# 创建每一只猫，体重，颜色，给猫取个名字都自己去改变
# 用init初始化函数  作用 只要创建类对象，就会执行这个init


# name是翠花 weight 20  color 黑白灰

# class Cat:
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls)
#     def __init__(self,name,weight,color):
#         # 翠花赋值给self.name 所以self.name是翠花。然后self是代表对象本身。所以tom1.name 翠花
#         self.name=name
#         self.weight=weight
#         self.color=color
#
#     def catch(self):
#         print(f'{self}小{self.color}猫抓老鼠')
#
#     def eat(self):
#         print('小白猫爱吃鱼')
#
#     def cave(self):
#         print('小白猫会打洞')
#
#     def __str__(self):
#         return f'这是一个对象的描述信息:{self.name}{self.color}猫的悲伤故事'
#
#     def __del__(self):
#         print(f'{self.name}小猫挂了')
# # tom1就是self
# # tom1=Cat('翠花','20','黑白灰')
# # # print('名字为{}的小{}猫的故事'.format(tom1.name,tom1.color))
# # tom1.catch()
# #
# # tom2=Cat('月下','20','月下猫')
# # print('名字为{}的小{}猫的故事'.format(tom2.name,tom2.color))
#
# tom1=Cat('翠花','20','黑白灰')
# print(tom1)
# 想要tom1打印出来的是我自己自定义的内容

# 在项目中什么时候会用到init函数  创建一个对象，用到对象里面的内容。之前我一定要干啥
# 一定要干的事情就写在init里面
# 数据库配置  数据库的链接

# 魔法
# 用init初始化函数  作用 只要创建类对象，就会执行这个init
# __str__对象描述方法，只要定义了__str__方法，对象就会打印这个方法中return
# __del__销毁对象，不管写不写这个del函数，都会销毁
# __new__ 创建类的对象

# 题目：去银行存取钱
# 二狗 银行账号123456789 余额500，想要存钱200
# 虚竹 银行账号23456789 余额5，想要取钱100
# 秋水 银行账号3456789 余额5亿，想要存钱1亿
# 剩下的逻辑
# 二狗存钱,存了之后账号里面的钱没增加
# 虚竹取钱,取了超过他的余额他还有钱

# class Bank:
#     def __init__(self,username,card_no,balance):
#         self.username=username
#         self.card_no=card_no
#         self.balance=balance
#
#     # 存钱
#     def deposit(self,amount):
#         print('{}你是来存钱的，存{}'.format(self.username,amount))
#
#     # 取钱
#     def withdrawal(self,amount):
#         print('{}你是来取钱的，取{}'.format(self.username,amount))
#
#     def __str__(self):
#         return f'我是{self.username},我的账户{self.card_no},我的余额{self.balance}'
#
#
# ergou=Bank('二狗','123456789','500')
# ergou.deposit(200)
# print(ergou)
# xuzhu=Bank('虚竹','123456789','5')
# xuzhu.withdrawal(100)
# print(xuzhu)

# 剩下的逻辑
# 二狗存钱,存了之后账号里面的钱没增加
# 虚竹取钱,取了超过他的余额他还有钱

# 面向对象
# 类和对象  创建类  实例化对象才能去使用
# self代表的是自己的
# init函数 del str