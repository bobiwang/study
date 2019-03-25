# list1 = [1,2,3,4]
# # n = iter(list1)
# # print(next(n))
# # print(next(n))


# def frange(start, stop, step):
#     x = start
#     while x < stop:
#
#       #  print(x)
#         yield x
#         x = x + step
#
# for i in frange(10,20,0.5):
#     print(i)
#
# x = True
# country_counter = {}
#
# def addone(country):
#     if country in country_counter:
#         country_counter[country] += 1
#         print(country_counter[country])
#     else:
#         country_counter[country] = 1
#         print(country_counter[country])
#
#
# addone('China')
# addone('Japan')
# addone('china')
#
# print(country_counter)


confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] += 1
print(confusion)
sum = 0
for k in confusion:
    sum += confusion[k]

print(sum)