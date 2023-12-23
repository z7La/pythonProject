test_string = '''
да
нет
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = input("первый ввод: ")
value1 = input("второй ввод: ")

if value0 == 'да' or value0 == 'нет' and value1 == 'да' or value1 == 'нет':
    print('ВЕРНО')
else:
    print('НЕВЕРНО')
