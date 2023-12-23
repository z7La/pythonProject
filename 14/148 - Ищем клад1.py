test_string = '''
0
1
вперёд
2
разворот
вперёд
1
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


x_treasure = int(input('x координата клада: '))
y_treasure = int(input('y координата клада: '))
pos = {'x': 0, 'y': 0}
all_direction = ['север', 'восток', 'юг', 'запад']
direction = 'север'
count = 0
stop = ''

while True:
    if ((pos['x'] == x_treasure and abs(pos['y']) == abs(y_treasure)) or
            (pos['y'] == y_treasure and abs(pos['x']) == abs(x_treasure))):
        print(f'Кол-во выполненных команд: "{count}". \nНаправление: "{direction}".')
        break

    cmd = input('команда: ')

    if cmd == 'стоп':
        break

    count += 1
    if cmd in ('направо', 'налево', 'разворот', 'вперёд'):
        if cmd == 'направо':
            index_i = all_direction.index(direction)
            direction = all_direction[(index_i + 1) % 4]
        elif cmd == 'налево':
            index_i = all_direction.index(direction)
            direction = all_direction[(index_i - 1) % 4]
        elif cmd == 'разворот':
            index_i = all_direction.index(direction)
            direction = all_direction[(index_i + 2) % 4]
        elif cmd == 'вперёд':
            step = int(input('шаг: '))
            if direction == 'север':
                pos['y'] += step
            elif direction == 'юг':
                pos['y'] -= step
            elif direction == 'запад':
                pos['x'] += step
            elif direction == 'восток':
                pos['x'] -= step