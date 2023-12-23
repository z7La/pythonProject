test_string = '''
3
101010 Ваня
79076192073 Коля
79234120156 Ваня
3
Коля
Ваня
Олег
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во номеров: '))
phone_dict = {}

for _ in range(n):
    val, key = input().split()
    if key in phone_dict:
        phone_dict[key].append(val)
    else:
        phone_dict[key] = [val]

m = int(input('\nКол-во выводимых номеров: '))
for _ in range(m):
    key = input('Имя: ')
    print(*phone_dict.get(key, ['Нет в телефонной книге']))

print(phone_dict)
