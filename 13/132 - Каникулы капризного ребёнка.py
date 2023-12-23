test_string = '''
Тула
Нижний Новгород
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = input('первый город: ')
value1 = input('второй город: ')

if ((value0.lower() == 'тула' and value1.lower() != 'тула' and value1.lower() != 'пенза') or
        (value0.lower() != 'тула' and value0.lower() != 'пенза' and value1.lower() == 'пеза')):
    print('ДА')
else:
    print('НЕТ')
