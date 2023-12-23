test_string = '''
4
Как устроен типичный фрукт:
кожура;
мякоть;
косточки.
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во команд: '))

for i in range(n):
    str = input('Введите строку: ')
    if 'Кот'.lower() in str:
        print('МЯУ')
        break
