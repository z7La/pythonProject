test_string = '''
15
10
.
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во столбцов: '))
m = int(input('Кол-во строк: '))
symb = input('Знак: ')


pctr = (symb * n + '\n' +
        (symb + ' ' * (n-2) + symb + '\n') * (m-2) +
        symb * n)
print(pctr)
