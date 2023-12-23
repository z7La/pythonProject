test_string = '''
20
1
1
5
3
2
4
4
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
    total -= value
    print(f'Результат: "{total}"')
