test_string = '''
20
вперед
2
разворот
вперед
11
разворот
вперед
20
'''[1:-1].split('\n')[::-1]



def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


length = int(input('Длина: '))
dom = 0
pos = 0
count = 0

while pos < length:
    cmd = input('Команда: ')
    count += 1
    if cmd == ('вперед' or 'вперёд'):
        step = int(input('Кол-во шагов: '))
        if dom % 2 == 0:
            pos += step
        elif dom % 2 != 0:
            pos -= step
    elif cmd == 'разворот':
        dom += 1
    if pos < 0:
        pos = 0

print(f'Кол-во выполненных команд: "{count}"')