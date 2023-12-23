test_string = '''
2
3
470
430
465
2
451
450

'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во дорог: '))
max_weight = 0
way_number = 0
all_weight_dict = {}

for i in range(n):
    amount = int(input('Кол-во туннелей: '))
    all_weight_list = []
    for j in range(amount):
        all_weight_list.append(int(input(f'Высота {j + 1}-го туннеля в дороге {i + 1}: ')))
        if j == amount - 1:
            all_weight_dict[i] = all_weight_list

for i in all_weight_dict:
    min_weight_list = min(all_weight_dict[i])

    if max_weight < min_weight_list:
        max_weight = min_weight_list
        way_number = i + 1

print(f'{way_number} {max_weight}')
