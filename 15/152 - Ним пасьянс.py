test_string = '''
10
1
1
5
3
2
4
4
3
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


total = int(input('Всего: '))

while total:
    value = int(input('Введите число: '))
    if 1 <= value <= 3:
        total -= value if value <= total else total
        print(f'Результат: "{total}"')
    else:
        print(f'Результат: "{total}"')

