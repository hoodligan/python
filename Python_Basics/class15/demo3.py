import pymysql
import configparser

class MySqlDB:
    # 获取配置文件里面的数据 MySqlDB('db.ini','Test_db')  MySqlDB('db.ini','zs_db')
    # 封装这个部分
    # 类的作用：模板 后面可以实例化使用
    # init:连接了数据库  创建了游标  为什么init数据库  创建了游标：只要用到查询语句  修改语句
    # 读取配置文件里面的数据，在放到连接中连接数据库
    def __init__(self,configpath,db):
        config=configparser.ConfigParser()
        config.read(configpath)
        # 读取文件数据
        host=config[db]['host']
        port=int(config[db]['port'])
        user=config[db]['user']
        password=config[db]['password']
        database=config[db]['database']
        charset=config[db]['charset']
        self.con=pymysql.connect(host=host, port=port, user=user, password=password, database=database,
                                  charset=charset)
        self.cur = self.con.cursor()

    # 连接部分写在初始化函数里面
    # 初始化的作用是什么：调用就连接
    # 实例化类，里面进入到init初始化函数  a=MySqlDB('127.0.0.1',3306,'root','123456','vipdb','utf8')
    # 调用的时候传ip地址，端口号这类
    # def __init__(self,host,port,username,password,db,charset):
    #     try:
    #         self.con = pymysql.connect(host=host, port=port, user=username, password=password, database=db,
    #                               charset=charset)
    #     except Exception as  e:
    #         print('数据库连接有问题'%e)
    #     self.cur=self.con.cursor()

    def close(self):
        self.cur.close()
        self.con.close()

    # 1.连接  2.创建游标 3.写sql语句  4.执行sql  5.获得结果
    # 查询语句
    def get_all(self,sql):
        ret=None
        try:
            self.cur.execute(sql)
            ret=self.cur.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return ret

    def get_one(self,sql):
        ret=None
        try:
            self.cur.execute(sql)
            ret=self.cur.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return ret

    def edit(self,sql):
        try:
            self.cur.execute(sql)
            self.cur.execute('commit')
            self.close()
        except Exception as e:
            print(e)
        return True

# 子查询  灵活运用
# 存储过程  函数去学 传参  有返回
# python 连接数据库

