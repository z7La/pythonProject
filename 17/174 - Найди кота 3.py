test_string = '''
Животное такое.
С усами, хвостом.
Мяукать умеет.
Мышей ловит.
(Если настроение подходящее.)
Кто бы это мог быть?
СТОП
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


count = 0
amount = 0
first = -1

while True:
    count += 1
    current_str = input('Введите строку: ')
    if 'Кот'.lower() in current_str:
        amount += 1
        if amount == 1:
            first = count
    elif current_str == 'СТОП':
        break

print(amount, first)