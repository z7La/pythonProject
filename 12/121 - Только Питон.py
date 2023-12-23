test_string = '''
Python
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = input('ввод: ')

if value0 == 'Python':
    print('ДА')
else:
    print('НЕТ')
