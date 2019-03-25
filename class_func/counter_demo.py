# 使用闭包实现计数器
def counter(x):
    num = [x]

    def add_one():
        num[0] += 1
        return num[0]

    return add_one


num1 = counter(0)
print(num1)
print(num1())
print(num1())

num5 = counter(5)
print(num5())
print(num5())
