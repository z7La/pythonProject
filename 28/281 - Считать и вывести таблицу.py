test_string = '''
3
2
тройка
треф
семёрка
червей
дама
пик
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во строк: '))
m = int(input('Кол-во столбцов: '))

table = [[input('Ввод: ') for j in range(m)] for i in range(n)]

for row in table:
    print(' '.join(row))

