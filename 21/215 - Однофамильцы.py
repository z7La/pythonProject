test_string = '''
6
Иванов
Петров
Сидоров
Петров
Иванов
Петров
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во фамилий: '))
count = 0
s1 = set()
s2 = set()
for i in range(n):
    lastname = input('Фамилия: ')
    if lastname in (s1 and s2):
        count += 1
    elif lastname in s1:
        s2.add(lastname)
        count += 2
    else:
        s1.add(lastname)

print(f'Кол-во однофамильцев: "{count}"')
