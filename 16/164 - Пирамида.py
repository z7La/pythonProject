test_string = '''
3
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value = int(input('Высота пирамиды: '))

for i in range(value):
    print(" " * (value - i - 1) + "*" * (2 * i + 1))
