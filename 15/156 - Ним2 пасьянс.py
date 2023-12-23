test_string = '''
10
10
1
5
2
10
1
5
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


bunch1 = int(input('Кол-во камней в первой куче: '))
bunch2 = int(input('Кол-во камней во второй куче: '))

while not (bunch1 == 0 and bunch2 == 0):
    bunch_num = int(input('Номер кучи (11 или 2): '))
    amount = int(input('Кол-во забираемых камней: '))
    if bunch_num == 1:
        bunch1 -= amount
    elif bunch_num == 2:
        bunch2 -= amount
    print(f'Кол-во камней в первой куче: "{bunch1}"\n'
          f'Кол-во камней во второй куче: "{bunch2}"')
