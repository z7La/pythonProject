test_string = '''
3 5 4 2
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


nums_list = list(map(int, input('Введите числа через пробел: ').split(' ')))
columns = len(nums_list) + 2
rows = max(nums_list) + 2

res = [[' ' for _ in range(columns)] for _ in range(rows)]

for i in range(rows):
    for j in range(columns):
        # заполнение сверху
        if i == 0:
            res[i][j] = '*'
        # заполнение слева и справа
        elif j in (0, columns-1):
            res[i][j] = '*'
        elif 1 <= j <= columns-2 and i >= 2:
            res[i][j] = '*' if (rows - i <= nums_list[j-1]) else ' '

for row in res:
    print(' '.join(row))
