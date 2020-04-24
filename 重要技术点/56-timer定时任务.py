import threading
import time
from threading import Timer

'''
每个 10 秒打印当前时间。
'''


# 定时任务
def task():
    print("定时任务执行了")
    '''
    第一个参数: 延迟多长时间执行任务(单位: 秒)
    第二个参数: 要执行的任务, 即函数
    第三个参数: 调用函数的参数(tuple)
    '''
    t = Timer(10, task)
    t.start()
    # 定时任务是非阻塞的
    for i in range(10):
        print(f"还剩{9 - i}秒---->\r")
        time.sleep(1)


if __name__ == '__main__':
    task()
