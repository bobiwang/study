import time
import datetime

#
# now = datetime.datetime.now()
# file1 = open('time.txt', 'r+')
# file1.write(str(now))
# # file1.close()
# file1 = open('time.txt','r')
# file1.flush()
# print(file1.tell())
# text1 = file1.read()
# print(text1)
# file1.close()

print('以下另一种方式======')

now = datetime.datetime.now()
with open('time', 'w') as f:
    # 写入当前日期
    f.write(str(now))

with open('time', 'r') as f:
    text = f.read()
   
print(text)
f.close()
