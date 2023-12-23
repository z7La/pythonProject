test_string = '''
5
6122802
14406496
15230209
2541121
1758741
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во блоков: '))
previous_hash = 0

for i in range(n):
    b = int(input(f'Блок b({i}): '))
    h = b % 256
    r = (b // 256) % 256
    m = b // 256 ** 2
    previous_hash = (37 * (m + r + previous_hash)) % 256

    if previous_hash > 100 or (previous_hash != h):
        print(f'Неправильный блок "{b}" с хэшем "{previous_hash}"')
    else:
        print(-1)

    previous_hash = h
