# 文件处理2
# 回顾：
# 匿名函数 lambda sum=lambda 参数,参数:表达式
# 推导式 [表达式 for i in range()]
# 三目运算：result1 if 判断条件 else result2
# 文件读取 打开open(路径,访问模式) 读取read 写入write  关闭 close  with open() as f:不用自己关闭
# os模块

# 文件的具体应用
# web自动化  接口自动化 读取文件里面的内容 测试数据 yaml文件,excel文件数据
# yaml文件怎么写数据 读数据
# 1.yaml文件读取数据
# 2.excel文件读取数据
# 3.txt文件读取
# 4.csv文件

# 1.txt文件读取  文件路径 相对路径 ./ ../test.txt
# f=open('./data/test.txt','r',encoding='utf-8')
# print(f.read())
# f.close()

# with open('./data/test.txt','r',encoding='utf-8')as f:
    # print(f.read())
    # print(f.readline())
    # print(f.readlines())


# yaml文件读取数据
# 创建了一个yaml文件
# 语法格式：
# 1.缩进表示层级关系  不能用tab按键 直接用空格
# 2.#表示注释
# 3.字符串不需要打引号，数字想要是字符串需要自己手动打引号
# 4.可以创建列表 []  -表示列表
# 5.可以创建字典{key:value}  :表示字典
# yaml中的数据要空格

# 1.安装yaml
# 1.cmd输入pip install pyyaml 检测 pip list
# 2.setting里面安装
# 读取yaml文件里面数据

import yaml

# 打开yaml
# f=open('./data/dict1.yaml','r',encoding='utf-8')
# # 读取加载yaml文件  5.1以后要用 Loader=yaml.FullLoader 读取更加安全
# data=yaml.load(f,Loader=yaml.FullLoader)
# print(type(data),data)
# f.close()

# with open('./data/dict1.yaml','r',encoding='utf-8')as f1:
#     data=yaml.load(f1,Loader=yaml.FullLoader)
#     print(data)
    # data是拿到所有数据  秋水 字典怎么取值  拿到键 就拿到值
    # print(data['person'])
    # print(data['person']['name'])
    # print(data['address'])

# 问题：怎么拿到秋水这个值
# {'code':200,{'name':admin,'sex':'女'},address:'changsha','token':'xxxxx'}

# 读取yaml中列表的数据
# 1.导入yaml
# 2.打开yaml文件
# 3.加载yaml文件数据
# 4.打印yaml文件内容

# with open('./data/list_yaml.yaml','r',encoding='utf-8') as f:
#     data=yaml.load(f,Loader=yaml.FullLoader)
#     print(data)
#     # 想要拿到虚竹这个值 怎么拿 列表怎么取值  拿到小狗这个值怎么拿
#     print(data[1][1])

# 列表嵌套字典
# [{'id':1,'name':'小翠','age':18},{'id':2,'name':'小花','age':19}]

# with open('./data/listdict_yaml.yaml','r',encoding='utf-8') as f:
#     data=yaml.load(f,Loader=yaml.FullLoader)
#     print(data)