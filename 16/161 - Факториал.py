import math

test_string = '''
4
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end= '')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value = int(input('Введите число: '))
res = 1
for i in range(2, value + 1):
    res *= i

print(f'Факториал {value} = "{res}"')
