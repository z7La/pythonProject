test_string = '''
984
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = int(input("Фартингов: "))

pens = 4
shilling = 48
GBP = 960


def calc(value0):
    res_str = ''

    if value0 >= 960:
        GBP = value0 // 960
        value0 -= (960 * GBP)
        res_str = f'Фунтов: {GBP}\n'

    if value0 >= 48:
        sh = value0 // 48
        value0 -= (48 * sh)
        res_str += f'Шиллингов: {sh}\n'

    if value0 >= 4:
        p = value0 // 4
        value0 -= (4 * p)
        res_str += f'Пенсов: {p}\n'

    if 0 < value0 < 4:
        res_str += f'Фартингов: {value0}\n'

    return res_str


res = calc(value0)
print(res)

