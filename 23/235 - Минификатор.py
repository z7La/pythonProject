test_string = '''
6
easy   =  2   +   2
if  easy ==   4:# А вдруг нет?
    pprint('Квадрат    с обрезанными углами:')
    print('/-\\')
    print('|#|')
    print('\\_/')
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во строк: '))

for i in range(n):
    my_str = input()
    edit_str = ''

    # пробелы в начале
    count = 0
    if my_str[0] == ' ':
        while my_str[count] == ' ':
            edit_str += my_str[count]
            count += 1

    count_quotes1 = 0
    for j in range(count, len(my_str)):
        if my_str[j] == "'":
            edit_str += my_str[j]
            count_quotes1 += 1 if my_str[j - 1] != '\\' else 0
        elif (my_str[j] == ' ') and (my_str[j + 1] == ' ') and (count_quotes1 % 2 == 0):
            continue
        else:
            edit_str += my_str[j]

    count_quotes2 = 0
    for j in edit_str:
        if j == "'":
            count_quotes2 += 1
        elif j == '#' and count_quotes2 % 2 == 0:
            edit_str = edit_str[:edit_str.index(j)]

    print(edit_str, '\n')

