# 例子：函数中返回函数
#
# def hi(name):
#     def greet():
#         return 'now in greet() function'
#     def welcome():
#         return  'now in welcome() function'
#     if name ==  'momo':
#         return greet
#     if name !=  'momo':
#         return welcome
#
#
# a = hi('momo')
# print(a())

# 将函数作为参数传给另一个函数

# def hi():
#     return 'hi wangbo'
#
# def beforehi(func):
#     print('doing something before executing hi()')
#     print(func())
#
# beforehi(hi)
