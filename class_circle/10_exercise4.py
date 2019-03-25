# 输出1-100哪些可被3整除
"""
方法一
for i in range(1, 101):
  if i % 3 == 0:
        print(i, "可被3整除")
  else:
        print(i, "不可被3整除")

# 方法二
i = 0
while i < 100:
    i = i + 1
    if i % 3 == 0:
        print(i, "可被3整除")
    else:
        print(i,'不可被3整除')

# 方法三？
for i in range(1, 100):
    while i % 3 == 0:
        print(i, "可被3整除")
        i = i + 1
    else:
        print(i, "不可被3整除")

# 方法四continue
i = 100
while i > 0:
    i = i - 1
    if i % 3 != 0:
        continue
    print(i, "可被3整除")
else:
  print(i ,"不可被3整除")

"""
# 方法五break  ?
for i in range(1, 100):
    while i % 3 != 0:
        print(i, "不可被3整除")
        break
    else:
        print(i, "可被3整除")
