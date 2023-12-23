test_string = '''
3
АБВ
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


step = int(input('Шаг шифрования: '))
phrase = input('Номер буквы в этом слове (начиная с 1): ')

for i in phrase:
    if chr(ord(i)) == ' ' or chr(ord(i)) == '!':
        print(i, end='')
    else:
        print(chr(ord(i) + step), end='')

