# csv文件 叫逗号分割值文件 也可以叫字符分割符文件
# 内容，隔开

# 怎么操作csv文件
# 1.打开文件
# 2.读取 用的是csv.reader() 返回的是一个csv.reader的对象，可迭代的对象
# 我们对象进行遍历，输出每一行，每一列

import csv
f=open('./data/data.csv','r',encoding='utf-8')
# a=csv.reader(f)
# print(type(a))
# print(type(f))
for i in f:
    print(i)

# with open('./data/data.csv','r',encoding='utf-8')as f:
#     a = csv.reader(f)
#     print(a)
#     # for i in a:
#     #     print(i)
#     #     print(i[1])
#     # 某一行的数据 转成list
#     result=list(a)
#     print(result)
#     print(result[1])


# 写入write
# stu1=[1,'秋水',18,'女']
# stu2=[2,'虚竹',108,'妖']
# out=open('./data/data.csv','a',encoding='utf-8',newline='')
# write=csv.writer(out)
# write.writerow(stu1)
# write.writerow(stu2)

# data=[('测试1,','测试2'),
# ('测试2,','测试2'),
# ('测试3,','测试2'),
# ('测试4,','测试2'),
# ('测试5,','测试2')]
# f1=open('./data/data.csv','a',encoding='utf-8',newline='')
# out=csv.writer(f1)
# for i in data:
#     out.writerow(i)
# f1.close()
