test_string = '''
привет
6
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


word = input('Слово: ')
n = int(input('Номер буквы в этом слове (начиная с 1): '))

if (n < 1) or (n > len(word)):
    print('ОШИБКА')
else:
    print(f'{n} буква в слове {word} = "{word[n-1]}"')

