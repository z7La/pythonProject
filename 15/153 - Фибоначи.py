test_string = '''
10
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


total = int(input('Ограничение до: '))

value0, value1 = 0, 1
print(value1)

while value0 + value1 < total:
    print(value0 + value1)
    value0, value1 = value1, value0 + value1

