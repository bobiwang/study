# 读取任务名称
#
# file1 = open('name.txt')
# data = file1.read()
# print(data.split('|'))
#
# # 读取兵器名称
# file2 = open('weapon.txt')
#
# i = 1
# for line in file2.readlines():
#     if i % 2 == 1:
#         print(line.strip('\n'))
#     i += 1
#
# file3 = open('sanguo.txt')
# print(file3.read().replace('\n',''))

def func(filename):
    print(open(filename).read())
    print('test func')

func('weapon.txt')

