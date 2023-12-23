test_string = '''
9
10 18
17 15
25 21
0 21
1 16
25 29
24 24
8 26
10 20
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во точек: '))
first_num_xy_dict = {}

for i in range(n):
    x, y = input('Координаты: ').split()

    first_num_x = x[:-1] if int(x) >= 10 else 0
    first_num_y = y[:-1] if int(y) >= 10 else 0
    res = str(first_num_x) + str(first_num_y)

    first_num_xy_dict[res] = first_num_xy_dict.get(res, 0) + 1

print(max(first_num_xy_dict.values()))


