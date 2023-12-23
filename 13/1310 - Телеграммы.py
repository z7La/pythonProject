test_string = '''
Привет! Как дела?
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = input("Введите строку: ")
length = len(value0)


def calc(length):
    res_str = ''
    kopeyka = length * 40

    if kopeyka >= 100:
        RUB = kopeyka // 100
        kopeyka -= (RUB * 100)
        res_str = f'{RUB} руб. '
    if 0 < length < 100:
        res_str += f'{kopeyka} коп.'
    return res_str


res = calc(length)
print(f'Результат:', res)
