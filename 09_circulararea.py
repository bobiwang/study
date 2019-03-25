# 圆形面积

rInput = float(input("半径"))
pi = 3.1415926


def area(r):
    return pi * r ** 2


print("半径为", rInput, "圆形面积为", area(rInput))
