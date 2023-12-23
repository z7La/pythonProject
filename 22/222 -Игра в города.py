test_string = '''
новгород
дублин
новгород
дублин
тула
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


previous_city = input('Название города: ')

while True:
    new_city = input('Название города: ')

    if previous_city[-1] == new_city[0]:
        previous_city = new_city
    else:
        print(new_city)
        break


