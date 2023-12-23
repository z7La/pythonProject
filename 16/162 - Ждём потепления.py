test_string = '''
15.9
16.3
16.8
19.11
20.5
20.11
21.8
22.4
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


t = float(input('Температура: '))
count = 0
while t < 22:
    count += 1
    t = float(input('Температура: '))

week = count // 7
print(f'Кол-во полных недель, прошедших до дня потепления: "{week}"')
