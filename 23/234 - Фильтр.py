test_string = '''
3
SVO TRS 29481292
%%LJPZ DME 11113283675
####&%^^^^
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во строк: '))

for i in range(n):
    my_str = input(f'{i+1}-я строка: ')

    if my_str[:4] == '####':
        continue
    elif my_str[:2] == '%%':
        my_str = my_str[2:]

    print(f'Вывод: {my_str}\n')
