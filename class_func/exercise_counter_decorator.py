# 统计函数开始执行时间和结束时间
import time


# 统计运行时间
# def timecounter(func):
def wrapper(func):
    starttime = time.time()
    func()
    stoptime = time.time()
    print('运行时间是 %s 秒' % (stoptime - starttime))
    return stoptime - starttime


# 求和
@wrapper
def add(x, y):
    print(x + y)
    return x + y


# 计数器
# def counter(x):
#     num = [x]
#     def add_ome():


add(4, 5)
