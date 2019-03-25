info = {('name1','name2'): ('wangbo', 'zhangsan'),'adr': 'hangzhou','sex':'female'}

l = len(info)
print(l)

print(str(info))
print(type(info))
if 'adr' in info:
    print(info['adr'])