class firstclass():
    """打印类的属性和方法"""
    i = 1234

    def f(self):
        return 'hello'


x = firstclass()
print(x.i)
print(x.f())


# self理解
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()



