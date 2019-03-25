# 输出姓名和年龄
class Member:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print(self.__weight)
        print(self.name, self.age, self.__weight)


# 实例化类
p = Member('10', 1, 100)
p.speak()

print(p.age)

