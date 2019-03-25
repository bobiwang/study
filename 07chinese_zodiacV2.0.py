# 根据用户输入年份打印属相
chinese_zodiac = ['猴', '鸡', '狗', '猪', '鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊']
year = int(input("请输入年份"))


def nom():
    n = year % 12
    print(n)
    return n


print(chinese_zodiac[nom()])
