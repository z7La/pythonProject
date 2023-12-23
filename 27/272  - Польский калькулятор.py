test_string = '''
7 2 3 * -
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


my_list = input('Введите строку: ').split(' ')
nums_list = []

for el in my_list:
    if el == '+':
        v1 = nums_list.pop()
        v2 = nums_list.pop()
        nums_list.append(v1 + v2)
    elif el == '-':
        v1 = nums_list.pop()
        v2 = nums_list.pop()
        nums_list.append(v2 - v1)
    elif el == '*':
        v1 = nums_list.pop()
        v2 = nums_list.pop()
        nums_list.append(v1 * v2)
    elif el == '/':
        v1 = nums_list.pop()
        v2 = nums_list.pop()
        nums_list.append(v1 / v2)
    else:
        nums_list.append(int(el))
    print(nums_list)