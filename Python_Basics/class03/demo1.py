# Python可变数据类型  不可变数据类型 元祖
# 回顾：
# 数字类型  整数 int  小数float 布尔类型 bool
# +-*/浮点除  //整数除 % **
# += -= *= /=
# 比较大小
# 数字常用的函数  abs 随机数 数据类型转化

# 字符串：’‘ “”  “”“
# 切片
# 字符串常用的函数 index join find split r \n \t \v 大小写的转行
# 替换 replace(旧，新)

# 作业：
# 字符串"Hey, you - what are you doing here!?"
# 分割成['Hey', 'you', 'what', 'are', 'you', 'doing', 'here']
# 分割split按照分隔符分割成一个个的字符 返回的是列表
# str="Hey, you - what are you doing here!?"
# # print(str.split(' '))
# print(str.replace(',','').replace('-','').replace('!?','').split())

# 切片的公式：str[开始值:结束值:步长]   结束值:左闭右开
# 从左到右0 1 2 3 4 5 6 7 8 9   -1右到左 -1 -2 -3 -4 -5 -6 -7
# 0 1 2 3 4 5 6 7 8 9
# [-2::1]
# str_number = "0123456789"
# # * 1. 截取从 2 ~ 5 位置 的字符串
# print(str_number[2:6])
# # * 2. 截取从 2 ~ `末尾` 的字符串
# print(str_number[2::])
# # * 3. 截取从 `开始` ~ 5 位置 的字符串
# print(str_number[:6])
# # * 4. 截取完整的字符串
# print(str_number[::])
# # * 5. 从开始位置，每隔一个字符截取字符串
# print(str_number[::2])
# # * 6. 从索引 1 开始，每隔一个取一个
# print(str_number[1::2])
# # * 7. 截取字符串末尾两个字符  1   -1
# print(str_number[-2::1])
# # * 8. 字符串的逆序（面试题）
# print(str_number[::-1])


# 元组：tuple 是用来存储一串数据的，用()标识，数据可以多个，数据类型可以任意的 字符串 数字 列表 字典
# 数据之间是用,隔开  有序的数据
# 空元组
# tup1=()
# print(tup1,type(tup1))
# 有数据 多个，用，隔开 任意的类型
# tup2=(1,1.5,'秋水',['虚竹','展昭'],{"name":"二狗"})
# print(tup2)
# 元组数据只有一个 最后加个，不加逗号会变成数据本身的类型
# tup3=(1,)
# print(tup3,type(tup3))

# 元组很多数据的 元组的数据是有序的 切片通过下标
#  -4     -3    -2    -1
#    0     1     2     3
# '秋水','虚竹','展昭',"二狗"
# tup4=('秋水','虚竹','展昭',"二狗")
# 取秋水 下标
# print(tup4[0])
# 取'虚竹','展昭'
# print(tup4[1:3])
# print(tup4[1:-1])

# 元组里面添加数据 可以吗  不可变数据类型 不能添加数据修改删除数据
# 拼接的方式可以添加数据
# id查看内存地址  查看家庭地址
# tup4=('秋水','虚竹','展昭')
# tup5=('芷若',)
# print(tup4,id(tup4))
# tup4=tup4+tup5
# print(tup4,id(tup4))
# tup4会是同一个人  不是  虽然 变量名同一个  不是同一个人 tup4 a同学  tup4 b同学
# 不可变数据类型 进行增删改 改掉了 就是另外一个人

# 删除数据  del 删除整个元祖
# tup4=('秋水','虚竹','展昭')
# del tup4
# print(tup4)
# 不可变 数字 字符串 元祖

# 可变数据类型  列表 list 字典 dict  集合set
# 列表:list有序的集合，里面有多个数据，用，号隔开，可以对数据进行增删改
# 定义:[]标识的 数据类型可以是任意的
# 创建一个空列表
# list1=[]
# print(list1,type(list1))
# 列表中有数据,数据类型任意的
# list2=[1,1.5,'秋水',['虚竹','展昭'],{"name":"二狗"},(1,2)]
# print(list2,type(list2))

# 查询列表中的数据
# list2=['秋水','虚竹','展昭']
# 查询秋水
# print(list2[0])
# # 查询 展昭虚竹
# print(list2[1:])
# 超出范围  list index out of range
# print(list2[4])

# 数据类型 操作数据 无非增删改查 不同的数据 接口 数据 字典  列表 操作获取某个

# 列表进行增删改
# 添加：append在末尾的位置添加  insert(2,元素)指定位置添加  extend在末尾添加数据
# append和extend有什么区别：append传的是一个对象，extend传的是一个个的数据
# id打印内存地址 同一个人 同一个家庭
# list2=['秋水','虚竹','展昭']
# print(list2,id(list2))
# list2.append('芷若')
# print(list2,id(list2))
# list2.insert(0,'优')
# print(list2,id(list2))
# list2.extend('a')
# print(list2)
# ['秋水','虚竹','展昭',[1,2,3]]
# list3=[1,2,3]
# list2.append(list3)
# print(list2)
# ['秋水','虚竹','展昭',[1,2,3]]
# list2.extend(list3)
# print(list2)

# 本身的意义 不用为什么
# append会比extend用的多点
# 一个班级[]  学生信息

# 修改
# list2=['秋水','虚竹','展昭']
# list2[1]='虚竹小美眉'
# print(list2)

# 删除
# pop(下标) 索引删除  remove(元素)通过元素  del删除一个或者删除整个或者删除几个
# list2=['秋水','虚竹','展昭']
# pop删掉会返回删掉的数据，括号里面不填会删除最后一个数据
# print(list2.pop())

# remove 删除之后不回返回元素的值
# print(list2.remove('虚竹'))

# del删除一个或者删除整个或者删除几个
# del list2[1]
# print(list2)

# del list2[1:]
# print(list2)

# del list2
# print(list2)

# 升序降序
# list3=['a','c','d','b']
# list4=[1,3,5,2]
# sort 升序  从小到大
# list3.sort()
# print(list3)
# list4.sort()
# print(list4)
# # reverse反转
# list3.reverse()
# print(list3)
# sort  默认不反转
# list3.sort(reverse=True)
# print(list3)

# tup1=(1,'1')
# list1=[1,'3']
# 把元组转为列表怎么转
# print(list(tup1))
# 把列表转为元组怎么转
# print(tuple(list1))

# 字典：用来存储的数据 关联关系的数据 成绩表：语文：79，数学：80，英语：60
# 姓名:秋水,年龄：18，性别：女
# 格式定义{key:value，key:value,key:value}键值对之间，隔开,字典是无序的
# 创建字典
# dict1={}
# print(dict1,type(dict1))
# 字典中有数据 键是不允许重复  键 只能是不可变数据类型
# dict2={"name":"虚竹",'age':1000,'sex':'妖'}
# print(dict2)

# 字典是无序的 通过键取到值
# dict2={"name":"虚竹",'age':1000,'sex':'妖'}
# print(dict2['age'])
# # get()取到值
# print(dict2.get('name'))

# 添加字典数据  地址  密码
# 增加一个键值对数据就行 不存在的键
# dict2={"name":"虚竹",'age':1000,'sex':'妖'}
# dict2['address']='东海龙宫'
# print(dict2)
#
# # 修改 修改存在的键
# dict2['age']=1001
# print(dict2)

# 修改多个值  旧数据更新成新数据的内容
# dict2 = {"name": "虚竹", 'age': 1000, 'sex': '妖','pwd':'123456'}
# dict3={"name": "虚竹2", 'age': 1003, 'sex': '妖','address':'东海龙宫'}
# print(dict2,id(dict2))
# dict2.update(dict3)
# print(dict2,id(dict2))
# 同一个key，值不同是更新，不同key，值相同是增加

# 查询 键 keys  值 values 键值items
# dict2={"name":"虚竹",'age':1000,'sex':'妖'}
# keys=dict2.keys()
# print(keys,type(keys))
# values=dict2.values()
# print(values,type(values))
# ims=dict2.items()
# print(ims,type(ims))

# 不能直接操作dict_keys  转成列表
# keys=dict2.keys()
# print(keys)
# print(list(keys)[1])

# values=dict2.values()
# print(values)
# print(list(values)[0])

# dict2={"name":"虚竹",'age':1000,'sex':'妖'}
# 一次性拿到所有的键，值，键值对
# for i in dict2.keys():
#     print(i)

# for i in dict2.values():
#     print(i)

# for i,j in dict2.items():
#     print(i,j)

# 创建新字典 fromkeys(键列表，值)
# {'name':'10','age':'10','sex':'10'}
# dict1={}
# list2=['name','age','sex']
# dict3=dict1.fromkeys(list2)
# print(dict3)

# 集合  1  2
# 集合：无序，特点数据是不能重复
# 定义：{}和set()进行标识
# 创建
# set1={1,2,3}
# print(set1,type(set1))
# set1=set((1,2,3))
# print(set1,type(set1))

# 空集合 不能使用{}去创建空集合
# set1={}
# set2=set()
# print(set1,type(set1))
# print(set2,type(set2))

# 特点:不能重复  自动去重
# set1={'秋水','虚竹','展昭','秋水'}
# print(set1)

# 集合是无序的  通过下标访问吗
# set1={'秋水','虚竹','展昭'}
# print(set1)

# 增加 add update
# set1.add(5)
# print(set1)
# add只能添加单一的数据
# set1.add(5,'7')
# print(set1)

# set1.update((5,6,7))
# print(set1)
# update只能添加序列的数据
# set1.update((5))
# print(set1)

# 删除
# remove(元素)  不存在报错
# pop 任意删除某个元素
# discard(指定元素删除)  不会报错
# clear清除所有
# set1.pop()
# print(set1)
# set1.remove('展昭')
# print(set1)
# set1.discard('展昭2')
# print(set1)
# set1.clear()
# print(set1)

# 交集 并集

# 数据类型 数据特点 怎么取值 作用