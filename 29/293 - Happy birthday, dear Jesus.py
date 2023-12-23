test_string = '''
4
Ваня 20 янв
Петя 15 июн
Вася 10 янв
Коля 20 июл
3
июн
дек
янв
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во: '))
birthday_dict = {}

for _ in range(n):
    val, day, key = input().split()
    if key in birthday_dict:
        birthday_dict[key].append(val)
    else:
        birthday_dict[key] = [val]
    birthday_dict[key].sort()

m = int(input('\nКол-во выводимых номеров: '))
for _ in range(m):
    key = input('Месяц: ')
    print(*birthday_dict.get(key, ''))

print(birthday_dict)
