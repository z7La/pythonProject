test_string = '''
Железный человек 2
Восток
12:00
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = input("Название фильма: ")
value1 = input("Название кинотеатра: ")
value2 = input("Время: ")

print('Билет на ', value0, ' в ', value1, ' на ', value2, ' забронирован.')
