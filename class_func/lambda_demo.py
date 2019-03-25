# def ture():
#     return True
#
# print(ture())
#
# lambda: True
#
# lambda x, y: x + y
#

dict = {'a': "aa", 'b': 'bb'}

# def fun2(item):
#     return item[1]

fun = lambda item: item[1]

for i in dict.items():
    print(fun(i))