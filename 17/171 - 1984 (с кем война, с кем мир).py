test_string = '''
6
С кем война?
С кем мир?
Меняем
С кем война?
Меняем
С кем война?
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


peace = 'Остазия'
war = 'Евразия'
n = int(input('Кол-во команд: '))

for i in range(n):
    cmd = input('Команда: ')

    if cmd == 'С кем война?':
        print(war)
    if cmd == 'С кем мир?':
        print(peace)
    if cmd == 'Меняем':
        war, peace = peace, war

