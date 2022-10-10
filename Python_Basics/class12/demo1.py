# python常见的几种算法   面试的时候

# 1.算法：冒泡排序 是一种简单的排序
# 怎么排序？相邻的一个一个比较  8 6 5 4 2   6 8 5 4 2  6 5 8 4 2  6 5 4 8 2  6 5 4 2 8
# 算法简介：
# 1.比较相邻的元素  前一个比后一个大(小)调换位置
# 2.针对出来的最后一个元素重复上面的步骤

# 题目：列表数据[9,8,4,5,2,1,3,7,6] 进行排序 从小到大排序
# list1=[9,8,4,5,2,1,3,7,6]
# # 这个列表里面有多少数据
# len1=len(list1)
# # print(len1)
# # 循环：总共循环多少次？ 8次  1

# for i in range(1,len1):
#     # print(i)
#     # 需要一次一次的比较  第一次循环：9要循环8次
#     # 9-1=8   1,8 循环7次  len1  1,9 可以1 不可以2
#     # 第二次循环：9-2+1  循环7
#     for j in range(1,len1-i+1):
#         # 判断 第一个数>第二个数 交换2个数的位置
#         if list1[j-1]>list1[j]:
#             list1[j-1],list1[j]=list1[j],list1[j-1]
# print(list1)

# 第一个循环控制次数 总共要循环8次 教练第一次
# 第二个循环 真正的一个学员去进行比较  这个9要去比较 要比较8次  1，len1-i+1  1,9 左闭右开的区间 循环8次
# 第一个数字要循环8次
# j=1 list[j-1]  list[0]>list[1]  9>8 替换 列表[8,9,4,5,2,1,3,7,6]
# j=2 list[j-1]  list[1]>list[2]  9>4 替换 列表[8,4,9,5,2,1,3,7,6]
# j=3 list[j-1]  list[2]>list[3]  9>5 替换 列表[8,4,5,9,2,1,3,7,6]
# j=4 list[j-1]  list[3]>list[4]  9>2 替换 列表[8,4,5,2,9,1,3,7,6]
# j=5 list[j-1]  list[4]>list[5]  9>1 替换 列表[8,4,5,2,1,9,3,7,6]
# j=6 list[j-1]  list[5]>list[6]  9>3 替换 列表[8,4,5,2,1,3,9,7,6]
# j=7 list[j-1]  list[6]>list[7]  9>7 替换 列表[8,4,5,2,1,3,7,9,6]
# j=8 list[j-1]  list[7]>list[8]  9>6 替换 列表[8,4,5,2,1,3,7,6,9]
# 教练在叫第二次 i=2
# 第二个数字要循环7次 len1-i+1  9-2+1=8  1,8 左闭右开 只循环7次
# [8,4,5,2,1,3,7,6,9]
# j=1  list[j-1]  list[0]>list[1]  8>4 替换[4,8,5,2,1,3,7,6,9]
# j=2  list[j-1]  list[1]>list[2]  8>5 替换[4,5,8,2,1,3,7,6,9]
# j=3  list[j-1]  list[2]>list[3]  8>2 替换[4,5,2,8,1,3,7,6,9]
# j=4  list[j-1]  list[3]>list[4]  8>1 替换[4,5,2,1,8,3,7,6,9]
# j=5  list[j-1]  list[4]>list[5]  8>3 替换[4,5,2,1,3,8,7,6,9]
# j=6  list[j-1]  list[5]>list[6]  8>7 替换[4,5,2,1,3,7,8,6,9]
# j=7  list[j-1]  list[6]>list[7]  8>6 替换[4,5,2,1,3,7,6,8,9]
# 1.总共要循环8次 教练  学员9个人 排下名词
# 教练叫第一次：9个学员中的某一个学员站出来 分别去挑战 厉害的人 ，就把9放在最后
# 教练叫第二次：8个学员中的某一个学员站出来，去挑战




# 选择排序：
# 原理：在一组数据中从最开始找最大(小)的元素，放在排序的起始位置
# 从大到小
# list1=[6,8,4,5,2,1,3,7,9]
# # [6,8,4,5,2,1,3,7,9]
# # 最大值的下标 0
# max_index=0
# # 循环8次  0开始 9 8
# for i in range(0,len(list1)-1):
#     for j in range(i+1,len(list1)):
#         if list1[j]>list1[max_index]:
#             max_index=j
#     list1[i],list1[max_index]=list1[max_index],list1[i]
#     max_index=i+1
# print(list1)

#第一次循环 # i=0
# j=1
# list1[1]>list1[0]  8>6 进入判断 j=1   max_index=1
# list1[2]>list1[1] 4>8 不大于 不走入循环
# list1[3]>list1[1] 5>8 不大于
# list1[4]>list1[1] 2>8 不大于
# list1[5]>list1[1] 1>8 不大于
# list1[6]>list1[1] 3>8 不大于
# list1[7]>list1[1] 7>8 不大于

# list1[9]>list1[8]
# [9, 8, 4, 5, 2, 1, 3, 7, 6]
# max_index=1
# j=2
# list1[2]>list1[1] 4>8 不大于 不替换
# list1[3]>list1[1] 5>8 不大于 不替换
# list1[4]>list1[1] 2>8 不大于 不替换
# list1[5]>list1[1] 1>8 不大于 不替换
# list1[6]>list1[1] 3>8 不大于 不替换
# list1[7]>list1[1] 7>8 不大于 不替换
# list1[8]>list1[1] 6>8 不大于 不替换
# [9, 8, 4, 5, 2, 1, 3, 7, 6]
# max_index=4
# j=3

# 递归：递给你拿回来
# 生活中递归：小时候传纸条 第一排传纸条传到最后的那个妹子  妹子手里 妹子给你回消息 传回来
# 递归有出口  有个结束的点  没有结束的点 造成死循环

# 编程中的递归：一种特殊函数，自己调用自己
# 递归的特点：一定要有出口，满足条件不执行返回执行本身
# 算法：计算1+2+3。。。+1000的题目
# def sum_number(num):
#     # print(num)
#     if num==1:
#         return 1
#     temp=sum_number(num-1)
#     return temp+num
# a=sum_number(100)
# print(a)

# 方法栈：方法是先进后出
# num=3 sum_number(3)   返回 3+3=6
# num=2 sum_number(3-1)  返回 3=1+2
# sum_number(2-1)  temp= 1
# 1.方法都没有返回。就是没有执行完毕，压栈了
# 2.直到sum_number(2-1)有返回值了，依次出展，最后返回sum_number(3)

# 树结构

# 摆放家具
# # 需求：
# # 1）房子有户型，总面积和家具名称列表
# # ?? ?新房子没有任何的家具
# # 2）家具有名字和占地面积，其中
# # ?? ?床：占4平米
# # ?? ?衣柜：占2平面
# # ?? ?餐桌：占1.5平米
# # 3）将以上三件家具添加到房子中
# # 4）打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

class House:
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area
        # 没有家具用list装起来
        self.jiaju_list=[]
        # 剩余面积
        self.free_area=area

    # 添加家具的方法  家具对象
    def add_jiaju(self,jiajuyo):
        # 家具面积>房子剩余面积 就不让它加进去  否则就可以加进去并且把房子面积-下来
        if jiajuyo.use_area>self.free_area:
            print('%s家具添加不进去了'%jiajuyo.name)
        else:
            self.jiaju_list.append(jiajuyo.name)
            self.free_area-=jiajuyo.use_area

    def __str__(self):
        return f'户型{self.house_type}总面积{self.area},剩余面积{self.free_area},家具有{self.jiaju_list}'

class jiaju:
    def __init__(self,name,use_area):
        self.name=name
        self.use_area=use_area

    def __str__(self):
        return f'我添加了{self.name},占地{self.use_area}'

bed=jiaju('床',4)
yigui=jiaju('衣柜',2)
canzhuo=jiaju('餐桌',8)
print(bed)
print(yigui)
print(canzhuo)

house=House('三室两厅',10)
house.add_jiaju(bed)
house.add_jiaju(yigui)
house.add_jiaju(canzhuo)
print(house)