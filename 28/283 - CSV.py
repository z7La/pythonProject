test_string = '''
4
Дама,сдавала в багаж,
диван, чемодан, саквояж
картину, корзину, картонку
и маленькую собачонку,,
4
0,0
1,2
3,1
3,0
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


r = int(input('Кол-во строк: '))
my_list = [input('Ввод: ').split(',') for _ in range(r)]

n = int(input('Кол-во выводимых слов: '))
res = ''
for _ in range(r):
    pos = input('Индексы: ').split(',')
    i, j = int(pos[0]), int(pos[1])
    res += my_list[i][j] + '\n'

print(res)
