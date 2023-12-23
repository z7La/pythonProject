test_string = '''
678
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = input('Пароль: ')

first = int(value0[0]) + int(value0[1])
second = int(value0[1]) + int(value0[2])

if first > second:
    password = str(first) + str(second)
else:
    password = str(second) + str(first)

print(f'Новый пароль: {password}')