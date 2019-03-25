# print(b)

b = []
for i in range(0, 10):

    b.append(i)
try:
     print(b[10])
except Exception as e:
    print('超出索引%s' %e)



# a = {'key1':1,'key2':2}
# print(a['key3'])
