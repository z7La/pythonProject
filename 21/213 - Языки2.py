test_string = '''
2
2
2
Иванов
Петров
Сидоров
Иванов
Петров
Иванов
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Английский изучают: '))
m = int(input('Немецкий изучают: '))
k = int(input('Немецкий изучают: '))
s1 = set()
s2 = set()
s3 = set()

for i in range(n+m+k):
    lastname = input('Фамилия: ')
    if lastname not in s1:
        s1.add(lastname)
    elif lastname in (s1 and s2):
        s3.add(lastname)
    elif lastname in s1:
        s2.add(lastname)

res = len(s2.difference(s3))
if res:
    print(f'Кол-во учеников изучающие только два предмета "{res}"')
else:
    print('NO')


