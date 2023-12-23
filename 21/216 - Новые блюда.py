test_string = '''
5
Овсянка
Рис
Суп
МаннаяКаша
Рыба
2
3
Рис
Суп
Рыба
2
Рис
Рыба
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


m = int(input('Кол-во блюд, которые можно приготовить: '))
s1 = set(input('Блюдо которое можно приготовить:') for _ in range(m))

n = int(input('Число дней, для которых есть списки блюд: '))
for i in range(n):
    n_dishes = int(input('Кол-во блюд, в данный день: '))
    s2 = set(input('Блюдо: ') for _ in range(n_dishes))
    s1 = s1.difference(s2)

print(s1)
