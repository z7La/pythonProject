test_string = '''
4
2
7
10
5
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во строк с данными: '))

my_list = []
for i in range(n):
    my_list.append(int(input('Число: ')))

for i in range(len(my_list)):
    if i != n-1:
        print(f'{my_list[i]} + {my_list[i + 1]} = {my_list[i] + my_list[i + 1]}')
