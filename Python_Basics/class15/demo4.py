from class15.demo3 import MySqlDB

# a=MySqlDB('127.0.0.1',3306,'root','123456','vipdb','utf8')
# b=a.get_one('select * from student3')
# print(b)

# 项目中写法 ini文件config

# 实例化对象
a=MySqlDB('db.ini','Test_db')
# 对象.方法名()
b=a.get_one('select * from student3')
print(b)

# 断点在调用的时候你打个断点  走到你封装的内部