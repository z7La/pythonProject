test_string = '''
Париж
Житомир
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


city_name1 = input('Название 1-го города: ')
city_name2 = input('Название 2-го города: ')

if city_name1[-1] == city_name2[0].lower():
    print('ВЕРНО')
else:
    print('НЕВЕРНО')
