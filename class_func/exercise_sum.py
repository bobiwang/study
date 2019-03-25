# 计算用户输入数字总和
# 把所有输入存入字典


def sum_demo():
    number_list_user_input = receive_user_input()

    sum_result = sum(number_list_user_input)

    print(sum_result)


def receive_user_input():
    data_list_user_input = list(input('请输入数字，以逗号分隔').split(','))
    number_list_user_input = list(map(int, data_list_user_input))
    return number_list_user_input


def sum(data_list):
    counter = 0
    for data in data_list:
        counter += data
    return counter


sum_demo()
