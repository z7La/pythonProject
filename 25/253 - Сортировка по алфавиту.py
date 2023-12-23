test_string = '''
4
три
четыре
пять
шесть
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во строк: '))
a = []
for i in range(n):
    a.append(input('Ввод:'))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

for i in range(n):
    print(a[i])

