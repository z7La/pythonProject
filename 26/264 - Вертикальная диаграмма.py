test_string = '''
3
Просто
Приятный  Парень
*
Самый
Продуктивный
  Выращиватель
Бобов
*
Джек
Победитель Великанов
*
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во титулов: '))

titles = []
for i in range(n):
    value = input()
    title = []
    while value != '*':
        title.append('-'.join(value.split()))
        value = input()
    titles.append('-'.join(title))

print(*titles[::-1], sep=', ')
