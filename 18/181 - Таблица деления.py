test_string = '''
3
2
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во столбцов: '))
m = int(input('Кол-во строк: '))

for j in range(1, m + 1):
    for i in range(1, n + 1):
        print(i / j,  ' ', end='')
    print()
