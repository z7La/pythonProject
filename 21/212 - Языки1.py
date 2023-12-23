test_string = '''
3
2
Иванов
Петров
Васечкин
Иванов
Михайлов
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Английский изучают: '))
m = int(input('Немецкий изучают: '))
s1 = set()
s2 = set()

for i in range(n+m):
    lastname = input('Фамилия: ')
    if lastname not in s1:
        s1.add(lastname)
    else:
        s2.add(lastname)

res = len(s1.difference(s2))
if res:
    print(f'Кол-во учеников изучающие только один предмет "{res}"')
else:
    print('NO')


