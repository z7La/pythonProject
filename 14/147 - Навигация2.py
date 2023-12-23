test_string = '''
9
3
вперед
4
разворот
вперед
2
вперед
6
разворот
вперед
10
вперед
2
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


length = int(input('Длина: '))
pos = int(input('Позиция: '))
dom = 0
count = 0
side = ''
while 0 < pos < length:
    cmd = input('Команда: ')
    count += 1
    if cmd == ('вперед' or 'вперёд'):
        if dom % 2 == 0:
            step = int(input('Кол-во шагов: '))
            pos += step
        elif dom % 2 != 0:
            step = int(input('Кол-во шагов: '))
            pos -= step
        if pos >= length:
            side = 'справа'
            break
        elif pos <= 0:
            side = 'слева'
            break
    elif cmd == 'разворот':
        dom += 1

print(f'Кол-во выполненных команд: "{count}". \nТаракан вышел "{side}".')