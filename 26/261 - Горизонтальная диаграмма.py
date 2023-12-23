test_string = '''
3 7 1 10 8
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


print('\n'.join(['*' * int(i) for i in input('Введите числа через пробел: ').split()]))
