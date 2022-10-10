# 面向对象
# 上节课：创建类 怎么创建对象 self 怎么获得对象属性 对象方法
# 魔法方法 init del str
# 作业：
# 1.# 减肥成长记  类和对象
# 小明 体重 160斤
# 1.小明每次跑步 会减肥0.5斤
# 2.每次吃东西 体重会增加1斤

# 名字  星辰  寒灯
# class Person:
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight
#
#     # 减肥给个次数
#     def run(self,num):
#         print('%s爱跑步，跑步减肥，减0.5斤'%(self.name))
#         self.weight=self.weight-0.5*num
#
#     # 吃东西时，给个次数  不确定  5
#     def eat(self,num):
#         print('%s爱吃东西，一吃就胖，一胖就胖1斤'%(self.name))
#         self.weight=self.weight+1*num
#
#     def __str__(self):
#         return "我的名字叫%s,体重%.2f斤"%(self.name,self.weight)
#
# # 创建对象 对象名=类名()  对象名.方法名()
# x=Person('星辰',80)
# # print(x)
# # 吃东西 吃的方法  每次吃东西 体重会增加1斤  原来的体重上面要加上一斤
# x.eat(2)
# print(x)
# x.run(3)
# print(x)
# # x.run()
# # print(x)

# 星辰一天吃3顿，3顿都没有运动  10顿

# 题目：去银行存取钱
# 二狗 银行账号123456789 余额500，想要存钱200
# 虚竹 银行账号23456789 余额5，想要取钱100
# 秋水 银行账号3456789 余额5亿，想要存钱1亿
# 剩下的逻辑
# 二狗存钱,存了之后账号里面的钱没增加
# 虚竹取钱,取了超过他的余额他还有钱
#
# class Bank:
#     def __init__(self,username,card_no,balance):
#         self.username=username
#         self.card_no=card_no
#         self.balance=balance
#
#     # 存钱
#     def deposit(self,amount):
#         print('{}你是来存钱的，存{}'.format(self.username,amount))
#         self.balance=self.balance+amount
#
#     # 取钱
#     def withdrawal(self,amount):
#         print('{}你是来取钱的，取{}'.format(self.username,amount))
#         if self.balance>=amount:
#             self.balance=self.balance-amount
#         else:
#             print('想钱想疯了,快走')
#
#     def __str__(self):
#         return f'我是{self.username},我的账户{self.card_no},我的余额{self.balance}'
#
# # 原本500 存了200之后  余额是没有坑
# # ergou=Bank('二狗','123456789',500)
# # ergou.deposit(200)
# # print(ergou)
# # 原本账号5块钱 想取100块 没门 提示  判断 账户余额大于等于取钱余额 让你取.记得把账号里面减掉
# # 否则想钱想疯了
# xuzhu=Bank('虚竹','123456789',5)
# xuzhu.withdrawal(5)
# print(xuzhu)

# 面向对象三个特征：封装，继承，多态
# 封装在一个类中 用的时候 实例化 对象名=类() 方法 属性

# 继承：顾名思义 拿来吧你 依法接受
# 生活中：子女继承父母的基因 子女继承父母的财产
# 面向对象中：子类继承父类的属性和方法  儿子 父亲有钱
# 单继承 多继承
# 作用：实现代码的重用，相同的代码不需要重复编写


# 两个类
# 动物类：吃 睡
# 狗类：吃 睡 跑 叫
# 封装 写 动物类  狗类 动物类 吃睡  狗类  吃 睡 跑 叫
# 继承的语法 类名(继承的类)

# class Animal:
#     def eat(self):
#         print('动物有吃的方法')
#
#     def sleep(self):
#         print('动物有睡的方法')
#
# #不写吃和睡  继承
# class Dog(Animal):
#     def run(self):
#         print('动物有跑的方法')
#
#     def bark(self):
#         print('动物有叫的方法')
#
# # 可以 正常逻辑 点出吃和睡
# ergou=Dog()
# ergou.eat()
# ergou.sleep()
# ergou.run()
# ergou.bark()

# 继承可以直接享用父类的方法，不需要再次开发
# 子类按照自己的需求，封装自己的方法

# 扩展专业术语：
# Dog类是Animal类的  子类 Animal类是Dog类的  父类  Dog类从Animal类进行 继承
# Dog类是Animal类的 派生类  Animal类是Dog类的  基类   Dog类从Animal类进行 派生

# 狗类下面可以还有子类吗？可以有子类
# 继承可以一直继承下去
# A-B-C-D d具有所有的父类的特征 单继承
class Animal:
    def eat(self):
        print('动物有吃的方法')
    def sleep(self):
        print('动物有睡的方法')

#不写吃和睡  继承
class Dog(Animal):
    def run(self):
        print('动物有跑的方法')

    def bark(self):
        print('动物有叫的方法')

class GodDog(Dog):
    def fly(self):
        print('啸天狗会飞')

class CommonDog(Dog):
    def catch(self):
        print('会抓老鼠')

# 哮天犬具有了所有父类的特征
# xtq=GodDog()
# xtq.sleep()
# xtq.run()
# xtq.bark()
# xtq.fly()

# 问题：定义一个普通狗继承狗类 普通狗会有哪些方法？
# 除了会飞都有
# 没有会飞是为什么？没有继承   Dog类 2个儿子  1个儿子 天狗  1个儿子 普通狗
# pt=CommonDog()
# pt.run()
# pt.sleep()

# 能拥有两个爸爸吗？ 多继承 有一个爸爸 有一个妈妈
# 可以多继承，子类可以拥有多个父类 ，并且具有父类所有的属性和方法
# 多继承  类名(父类,父类)
# class A:
#     def demoA(self):
#         print('这是父类A的方法')
#
# class B:
#     def demoB(self):
#         print('这是父类B的方法')
#
# class C(A,B):
#     def demoC(self):
#         print('这是儿子C的方法')
# c=C()
# c.demoA()
# c.demoB()
# c.demoA()

# 项目中不会使用多继承
# 如果说用了多继承  那我会以哪个为主
# 你爸爸会缝衣服，你妈妈也会缝衣服  想要继承缝衣服 先继承你爸爸缝衣服的技术 还是你妈妈

# 我现在想学蛋糕技术，一个是拜人家为师，学习人家祖传秘方
# # 另外一个 去培训学校培训蛋糕技术
# class Master:
#     def __init__(self):
#         self.peifang='师傅的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}技术，学习蛋糕')
#
# class School:
#     def __init__(self):
#         self.peifang='学校的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}技术，学习蛋糕')
#
# class Tudi(Master,School):
#     pass

# 是以哪个配方为主  师傅 就近
# xiaxia=Tudi()
# xiaxia.make_cake()

# 结论：一个类继承多个父类会优先继承第一个类的数学和方法

# 随着时间的流逝，徒弟蛋糕就学会了。自己创新了一个蛋糕技术。徒弟他也有制作蛋糕的方法了
# class Master:
#     def __init__(self):
#         self.peifang='师傅的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}技术，学习蛋糕')
#
# class School:
#     def __init__(self):
#         self.peifang='学校的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}技术，学习蛋糕')
#
# class Tudi(Master,School):
#     def __init__(self):
#         self.peifang='自己的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}技术，学习蛋糕')
#
# xiaxia=Tudi()
# xiaxia.make_cake()

# 结论：子类和父类拥有同名的方法和属性，会覆盖父类的方法和属性

# 剧情继续发展，徒弟学出来之后，自己开了一个店，结合三个口味推出了
# 师傅的配方拿出来，学校的配方拿出来  自己创建的配方拿出来 整出3个口味
# super()拿的是父类  拿到父类的属性和方法

# class Master:
#     def __init__(self):
#         self.peifang='师傅的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}技术，学习蛋糕')
# class School(Master):
#     def __init__(self):
#         self.peifang='学校的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}技术，学习蛋糕')
#         super().__init__()
#         super().make_cake()
#
# class Tudi(School):
#     def __init__(self):
#         self.peifang='自己的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}技术，学习蛋糕')
#         super().__init__()
#         super().make_cake()
#
#
# xiaxia=Tudi()
# xiaxia.make_cake()

# 多态：不明显  不需要继承
# 指的是同一类型的事物，有不同的形态
# 传入不同的对象，产生不同的结果  动物都会吃 吃的东西不一样
# 猪吃饭，猫吃猫粮，狗吃狗粮，动物都有吃的方法 ，干脆创建吃的方法
# 创建好的对象使用吃的方法 猪吃  猫吃 狗吃  吃的方法 不同的形态

# class Pig:
#     def eat(self):
#         print('猪吃饭')
# class Cat:
#     def eat(self):
#         print('猫吃猫粮')
# class Dog:
#     def eat(self):
#         print('狗吃狗粮')
#
# # 传入不同对象
# def eat(a):
#     a.eat()
#
# p=Pig()
# c=Cat()
# d=Dog()
#
# eat(p)
# eat(c)
# eat(d)

# 调用不同类对象的相同方法名，产生不同的结果

# 往方法里面传入一个类对象
class Dog:
    def __init__(self,name):
        self.name=name
    def work(self):
        print('看守家门')
class BigDog(Dog):
    def work(self):
        print('抓小偷')
class SmartDog(Dog):
    def work(self):
        print('缉毒')

class Person:
    def with_dog(self,obj):
        print('警员和%s一起去--'%(obj.name))
        obj.work()

xiaoqi=BigDog('神犬小七')
erha=SmartDog('二哈')

p=Person()
p.with_dog(erha)

# 调用不同类对象的相同方法名，产生不同的结果

# 方法里面可以传入对象进去