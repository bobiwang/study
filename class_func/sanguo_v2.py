# 人物出现次数
import re


def item_num(hero):
    with open('sanguo.txt') as f:
        data = f.read().replace('/n', '')
        name_num = re.findall(hero, data)
        # print('主角 %s 出现 %s 次' % (hero, len(name_num)))
        return len(name_num)

    # 读取人物信息


name_dict = {}
with open('name.txt') as f:
    names = f.read().split('|')
#   print(names)
    for n in names:
        name_dict[n] = item_num(n)
print(name_dict)

