# 时间日期和异常处理
# yaml怎么创建读取 打开文件 yaml.load
# excel文件 工作簿 表单  循环表单数据
# csv文件 reader writter

# 学生管理系统 for if 数据类型

# 实现学生管理系统,完成对学员的增,删,改,查和退出学生管理系统。
# 输入0显示所有学员信息,1代表增加学生信息，2代表删除学生信息，3代表修改，4代表查询某一个学员学生信息，exit代表退出学生管理系统。每一个功能定义一个自定义函数。
# 输入0：显示所有学员信息
# 输入1：添加学员编号，编号,姓名，年龄
# 输入2: 根据学员姓名删除学员信息
# 输入3：修改学员姓名
# 输入4：根据名字查询学员信息
# 输入exit退出学生管理系统

# 分析学生管理系统
# 1.界面 提示
# 2.根据按钮做出响应的功能
# 有多少学员  学员的信息要保存下来  数据类型：字符串  数字   元祖 不可变的数据类型 列表 字典 可变数据类型
# '1','张三','18'
# 2,小翠,19
# 3,铁柱,20
# 用字典  键值对 关联关系的数据  散的  一个列表 班级 有多个学生
# dict1={'id':1,'name':'张三','age':18}
# dict2={'id':2,'name':'小翠','age':19}
# dict3={'id':3,'name':'铁柱','age':20}
studentInfo=[{'id':1,'name':'张三','age':18},{'id':2,'name':'小翠','age':19},{'id':3,'name':'铁柱','age':20}]


def show():
    print('-'*50)
    print('输入0:显示所有学员信息\n输入1:添加学员编号,编号姓名,年龄\n输入2:根据学员姓名删除学员信息\n输入3:修改学员姓名\n'
          '输入4:根据名字查询学员信息\n输入exit退出学生管理系统')

def show_StudentInfo():
    print('显示所有学员信息')
    for i in studentInfo:
        print(f"学生编号:{i['id']},学生姓名:{i['name']},学生年龄:{i['age']}")

# 编号,姓名,年龄  数据保存在哪  保存在字典里面 有一个学生信息  在把这个学生添加到班级中去 列表中
# 字典添加 键 值 {'id':4,'name':'王五','age':55}  列表添加值
def add_studentInfo():
    print('添加学员信息')
    new_id=int(input('请输入编号:'))
    new_name=input('请输入姓名:')
    new_age=input('请输入年龄:')
    # 如果这个学员姓名已经存在了，不让它添加了。怎么知道这个学员存不存在  循环列表
    for i in studentInfo:
        print('所有学员信息{}'.format(i))
        # 班级里面有这个编号 i['id']=1,2,3
        if i['id']==new_id:
            print('此编号以存在')
            return
    dict1={}
    dict1['id']=new_id
    dict1['name']=new_name
    dict1['age']=new_age
    studentInfo.append(dict1)
    write1(studentInfo)
    print(studentInfo)

def del_studentInfo():
    print('根据学员姓名删除学员信息')
    del_name=input('请输入要删除的学员姓名:')
    for i in studentInfo:
        if i['name']==del_name:
            studentInfo.remove(i)
            break
    else:
        print('要删除的学员不存在')
    print(studentInfo)

# ==值比较 is内存地址比较 对象
def update_studentInfo():
    print('根据学员姓名修改学员姓名')
    upd_name = input('请输入要修改的学员姓名:')
    for i in studentInfo:
        if i['name'] == upd_name:
            i['name']=input('修改后的学员姓名:')
            break
    else:
        print('要修改的学员不存在')
    print(studentInfo)

def search_studentInfo():
    print('根据名字查询学员信息')
    search_name = input('请输入要查询的学员姓名:')
    for i in studentInfo:
        if i['name'] == search_name:
            print('学员信息:学号{},姓名{},年龄{}'.format(i['id'],i['name'],i['age']))
            break
    else:
        print('要查询的学员不存在')

def write1(studentInfo):
    with open('student.txt','w',encoding='utf-8')as f:
        f.write(str(studentInfo))

while True:
    show()
    # 字符串类型 1 '1'
    num=int(input('请输入编号:'))
    if num==0:
        show_StudentInfo()
    elif num==1:
        add_studentInfo()
    elif num==2:
        del_studentInfo()
    elif num==3:
        update_studentInfo()
    elif num==4:
        search_studentInfo()
    elif num==5:
        print('输入exit退出学生管理系统')
        break
    else:
        print('输入功能序号有误')




# 输入0  atm

# 保存文件
