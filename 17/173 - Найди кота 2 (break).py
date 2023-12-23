test_string = '''
Как устроен типичный фрукт:
кожура;
мякоть;
косточки.
СТОП
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


count = 0

while True:
    str = input('Введите строку: ')
    count += 1
    if 'Кот'.lower() in str:
        print(count)
        break
    elif str == 'СТОП':
        print(-1)
        break
