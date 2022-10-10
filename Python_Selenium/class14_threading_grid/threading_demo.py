'''
    多线程库的用例并发处理实现
        多线程的操作
'''
import threading
from time import sleep


def run(name):
    print(name + '在跑步')
    sleep(3)
    print(name + '跑累了')


# 单线程效果
li = ['狐狸', '网恋', '寒灯']

# for i in li:
#     run(i)

# 一起跑步：通过多线程的形态实现多用户一起跑步的效果
# 建立线程池
th = list()

# 分配线程
th.append(threading.Thread(target=run, args=['狐狸']))
th.append(threading.Thread(target=run, args=['网恋']))
th.append(threading.Thread(target=run, args=['寒灯']))

# 启动线程:如果你的多条线程是针对同一个文件来进行读写操作的话，为防止出现线程锁，需要添加join
for t in th:
    t.start()
    # 为了避免多线程对同一文件或内容进行操作，造成的锁
    t.join()
