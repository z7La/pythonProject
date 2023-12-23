test_string = '''
3
стеклянный шарик
монета
жук
2
3
3
2
1
2
1
2
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во наперстков: '))
my_list = []
for i in range(n):
    my_list.append(input('Ввод:'))

k = int(input('Кол-во перестановок напёрстков: '))
for i in range(k):
    my_list2 = [''] * int(input('Кол-во напёрстков: '))
    for j in range(len(my_list2)):
        my_list2[j] = my_list[int(input('Порядок расположения: ')) - 1]
    my_list = my_list2

for i in my_list:
    print(i)
