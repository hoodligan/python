# 条件判断和循环语句  上节课知识点 字典的删除
# 回顾一下：不可变数据类型
# 元祖  列表  字典  集合
# 元祖：用（）标识，可以多个数据，逗号，隔开，任意数据类型，有序的集合，不能进行增删改
# 列表：是有序的集合，查到。用[]标识的，数据是任意类型，增删改
# 字典：{key:value}存储的数据，关联关系，无序的，通过键，拿值
# 删除 del[删除键]或删除整个 pop指定键删除  popitem()删除最后一个  clear()清空字典
# dict1={'name':'星辰','age':18,'sex':'女'}
# del dict1['name']
# print(dict1)
# del dict1
# print(dict1)
# dict1.pop('age')
# print(dict1)
# dict1.popitem()
# print(dict1)
# dict1.clear()
# print(dict1)
# 集合：特点：去重复 {}或者set()进行标识

# 1、定义一个列表[1, 2, 3]，并将列表中的头尾两个元素对调。对调后为[3, 2, 1]
# list1=[1, 2, 3]
# print(list1[::-1])

# list1[0],list1[2]=list1[2],list1[0]
# print(list1)

# list1[3,2,1]
# a=1   3
# a=list1[0]
# list1[0]=list1[2]
# list1[2]=a
# print(list1)

# 2、对列表[10, 11, 12, 13, 14, 15]翻转，调整后为[15, 14, 13, 12, 11, 10]
# list1=[10, 11, 12, 13, 14, 15]
# list1.reverse()
# print(list1)
# 不能直接打印list1.reverse() 是没有返回

# 3、将列表数据[ 1, 6, 3, 5, 3, 4 ]转换为元组
# list1=[ 1, 6, 3, 5, 3, 4 ]
# print(tuple(list1))

# 4、循环打印出字典{'name':'aming','age':18,'school':'cema'}中的所有键和值
# dict1={'name':'aming','age':18,'school':'cema'}
# for x,y in dict1.items():
#     print(x,y)

# 5、在控制台输入学员编号，姓名，年龄，保存在字典里面  {}  1  aa 22  字典新增数据  直接给字典加不存在的键和值
# new_id=input('请输入学员编号:')
# new_name=input('请输入学员姓名:')
# new_age=input('请输入学员年龄:')
# dict1={}
# dict1['id']=new_id
# dict1['name']=new_name
# dict1['age']=new_age
# print(dict1)



# 条件判断和循环语句
# 回顾：
# 运算符
# 1.算术运算符：+ - * /
# 2.比较运算符：== >= <=  !=
# 3.赋值运算符:+= -= *= /=
# 逻辑运算符： and or not   两个表达式去做判断 1+1=2 and 1+1=3
# and两个表达式同时都为真的时候 返回真 True 1 一个表达为真一个表达式为假 返回假 False 2
# False
# print(1==1 and 1==2)
# True
# print(1==1 and 1!=2)

# or 两个表示有一个为真就为真
# True
# print(1==1 or 1==2)
# # True
# print(1!=1 or 1!=2)
# print(1==2 or 1==3)

# not  非
# a=1
# b=2
# # False
# print(not a==b)

# 成员运算符：in not in  in在。。里面  一个字符串python  一个字符a 问 a在不在python里面
# 大列表 有没有我想要的数据
# 身份运算符：is not is 判断同一个对象 a 和b a=4  b=4 id内存地址  值是不是相等==
# 对象 is  值相等 ==

# 条件判断和循环语句
# 判断：如果你考试得了100分，游乐场，否则：打你屁股
# if语句
# 语法：
'''
if 条件：
    做条件满足的事情
else:
    不满足的事情
'''
# 案例：如果年龄达到18岁，允许你进入网吧，否则回去睡觉
# 不知道年龄多少岁
# age=17
# if age>=18:
#     print('允许你进入网吧')
# else:
#     print('回去睡觉')

# 升级一下 ，年龄在控制台自己输入，如果年龄达到18岁，允许你进入网吧，否则回去睡觉
# 字符串和数字能进行对比 '秋水'>=1  ’虚竹‘>=5
# 数字 的类型age 转化类型 强转
# age=int(input('请输入你的年龄:'))
# age=input('请输入你的年龄:')
# print(int(age),type(int(age)))
# if int(age)>=18:
#     print('允许你进入网吧')
# else:
#     print('回去睡觉')

# 题目：找出列表中list1=[1,'2','熊猫',(1,2,'a')] 有没有a字符，没有打出 ’我不在‘，有的话打印出’我在‘
# list1=[1,'2','熊猫',(1,2,'a')]
# if '熊猫' in list1:
#     print('我在')
# else:
#     print('我不在')

# 多重if:多个判断
# 如果你的名字叫虚竹，就打一顿，如果你的名字叫二狗，让你旺旺两声，如果你的名字叫铁柱，就把翠花嫁给你，否则你就单身
'''
if 条件：
    满足的事情
elif 条件:
    满足的事情
elif 条件：
    满足的事情
elif 条件：
    满足的事情
else:
    不满足的事情
'''
# 判断成绩 如果你的成绩大于90分，你是最棒的，如果你的成绩大于80分，你是棒棒的，如果你的成绩大于70分，你是优秀的
# 否则，加油
# grade=90
# if grade>=90:
#     print('你是最棒的')
# elif grade>=80:
#     print('你是棒棒的')
# elif grade>=70:
#     print('你是优秀的')
# else:
#     print('加油，好自为之')

# 如果你的成绩大于90分 成绩A 如果你的成绩在大于80分，小于90分，成绩B  如果你的成绩大于70分，小于80，成绩c
# 否则 加油，好自为之
# grade=int(input('请输入成绩：'))
# if grade>=90:
#     print('成绩A')
# elif grade>=80 and grade<90:
#     print('成绩B')
# elif grade>=70 and grade<80:
#     print('成绩C')
# else:
#     print('加油，好自为之')

# 嵌套if,满足了第一条件，才有第二条件
# 相亲：相亲 有没有车，有没有房 ，有的话，进入到第二条件（你长的帅不帅，长的帅，会不会做饭，考虑，条件：你会不会做家务
# 会。长得不帅，走。）
# 没有，滚吧你
# 1.有车有房 2.你长的帅不帅 3.会不会做饭 4.会不会做家务 走吧 否则 滚了
'''
if 条件：
    if 条件：
        满足的条件
    elif 条件：
        满足的条件
    elif 条件：
        满足的条件
    else:
        不满足的条件   
else:
    不满足条件
'''
# 题目：要求
# 考试：你妈的最低要求70分，没满足70分，跪搓衣板。如果你成绩在80分以上，游乐场，吃棒棒糖
# grade=int(input('请输入你的成绩：'))
# if grade>=70:
#     if grade>=80:
#         print('游乐场')
#     else:
#         print('吃棒棒糖')
# else:
#     print('跪搓衣板')

# 循环：
# 重复执行  while for
'''
while 条件：
    循环内容
'''
# 打印5次hello world
# print('hello world')
# 变量 记住  死循环
# 计算 加1
# hello world  i=1
# hello world  i=2
# hello world  i=3
# hello world i=4
# hello world  i=5
# hello world i=6
# i=0
# while i<5:
#     print('hello world')
#     i=i+1

# 题目：计算0+1+2+3+4+5+。。。。。+100相加的和等于多少？0+1=1  1+2=3  3+3=6 6+4=5
# 1.输出0到100的数
# 求和
# 第一次循环：i=0 sum=0 sum=0+0  sum=0 i=1
# 第二次循环：i=1 sum=0 sum=0+1  sum=1 i=2
# 第三次循环：i=2 sum=1 sum=1+2  sum=3 i=3
# 第四次循环：i=3 sum=3 sum=3+3  sum=6 i=4
# i=0
# sum=0
# while i<=100:
#     print(i)
#     sum=sum+i
#     i=i+1
#     print('0,100的和',sum)

# 循环中的break和continue 退出循环
# break:条件满足的时候，退出循环，退出的整个循环
# continue:当条件满足的时候，退出循环，本次循环

# 打印0-10的数字，循环到3的时候，退出循环
# 第一次循环：i=0  0 i=1
# 第二次循环：i=1  1  i=2
# 第三次循环：i=2  2  i=3
# 第四次循环：i=3  3
# i=0
# while i<=10:
#     print(i)
#     if i==3:
#         break
#     i=i+1

# continue本次循环
# 打印0-10的数字，循环到3的时候，退出循环
# 第一次循环：i=0  0 i=1
# 第二次循环：i=1  1  i=2
# 第三次循环：i=2  2  i=3
# 第四次循环：i=3  3  退出本次循环
# i=3
# i=0
# while i<=10:
#     print(i)
#     if i==3:
#         i=i+1
#         continue
#     i+=1

# 循环嵌套 循环中嵌套循环
# 题目：
'''
*
**
***
****
*****
'''
# 5行
# 行数和星星数是一致的
# 第一次循环：一个      *
# 第二次循环：# row 2  *  *
# 第三次循环：# row 3  * * *
# 第四次循环：# row 4  * * * *
# 第五次循环：
# row=1
# # 2  3  4
# while row<=5:
#     col=1
#     # 2 3 4
#     while col<row:
#         print('*',end='')
#         col+=1
#     print('*')
#     row+=1

# while循环后面加else,循环完了会执行else的代码，如果循环中间停止了，不会打印else
'''
while 条件：
    循环语句
else:
    语句
'''
# i=1
# while i<=5:
#     print('hello world')
#     # if i==3:
#     #     break
#     i+=1
# else:
#     print('循环结束')

# for循环
'''
for 变量名 in 区间/列表:
    循环体
'''
# 循环5次hello world
# range 0开始 0,1，2 ，3 ，4  左闭右开区间
# for i in range(5):
#     print('hello world')

# for i in range(0,5):
#     print('hello world')

# 循环列表
# list1=['小米','华为','魅族']
# for i in list1:
#     print(i)

# 循环字典  字符串 +拼接  数字+
dict1={'name':'秋水','age':'18','sex':'女'}
for i in dict1:
    print(i+':'+dict1[i])