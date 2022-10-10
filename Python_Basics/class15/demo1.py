# 用python连接数据
# 1.连接数据库
# 2.操作数据库  创建游标  用游标  执行sql语句  获得结果
# 3.关闭数据库

# pymysql安装方式 pip isntall pymysql
# 1.导包
import pymysql


# 1.连接数据库  查询
con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='vipdb',charset='utf8')
# print(con)
# 2.操作数据库 创建游标
cur=con.cursor()
# 写sql
sql='select * from student3'
# 执行sql
cur.execute(sql)
# 查询几条数据fetchmany(指定数据)  查询所有数据fetchall 查询一条数据fetchone
reslut=cur.fetchmany(3)
print(reslut)

# 增加 修改 删除
con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='vipdb', charset='utf8')
cur=con.cursor()
# sql='delete from student3 where id=8'
sql1='insert into student3(id,name) values(8,"aaa")'
cur.execute(sql1)
cur.execute('commit')

# 别的地方 不会重新写  用哪部分改一下  封装 函数