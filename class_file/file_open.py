# 写入文件
# file1 = open('name.txt', 'w')
# file1.write('劉備''曹操''孫權''關羽''張飛''呂布''周瑜''趙雲''龐統''司馬懿''黃忠''馬超')
# file1.close()
#
#
# file2 = open('name.txt', 'r')
# print(file2.read())
#
# file2.close()
#
#
# file3 = open('name.txt','a')
# file3.write('新增')
# file3.close()
#
# file4 = open('name.txt')
# print(file4.readline())
# file4.close()
#
#
# file5 = open('name.txt')
# for line in file5.readlines():
#     print(line)
#     print('======')

file6 = open('name.txt')
# print('当前指针位置是',file6.tell())
# print('读取3个字符',file6.read(3))
# print('再读取1个字符',file6.read(1))
# print('读4个字符后指针位置',file6.tell())
# file6.seek(9)
# print(file6.tell())
# print(file6.read(1))
file6.seek(5,2)
print(file6.tell())
print(file6.read(1))