# year = int(input('请输入年份'))
# try:
#     year = int(input('请输入年份'))
# except ValueError:
#     print('请输入数字')

# a = 123
# try:
#     a.append('def')
# except (AttributeError,KeyError,ValueError):
#     print('不可扩展')

# try:
#     print(1/a)
# except (ZeroDivisionError,TypeError,NameError) as err:
#     print('0不能做除数 %s' %err)
#


try:
    a = int(input('请输入被除数'))
    b = int(input('请输入除数'))
    c = a / b
    print('结果为', c)
except Exception as e:
    print('异常是%s' % e)

finally:
    print(a, b)
