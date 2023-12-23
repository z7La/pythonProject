test_string = '''
5
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


time = int(input('Число от 0 до 23: '))
if 5 <= time <= 10:
    print('Утро')
elif 11 <= time <= 17:
    print('День')
elif 18 <= time <= 22:
    print('Вечер')
elif time == 23 or (0 <= time <= 4):
    print('Ночь')
else:
    print('Ошибка')

