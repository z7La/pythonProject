test_string = '''
129
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value = int(input('Кол-во монет: '))

while value >= 8:
    value //= 8

print(f'Остаток: {value}')