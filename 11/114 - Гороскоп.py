test_string = '''
Иван
Кузнецов
лис
овен
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = input("Имя: ")
value1 = input("Фамилия: ")
value2 = input("Любимое животное: ")
value3 = input("Знак зодиака: ")

print('Индивидуальный гороскоп для пользователя ', value0, value1,
      '\nКем вы были в прошлой жизни: ', value2,
      '\nВаш знак зодиака - ', value3, ' , поэтому вы - тонко чувствующая натура.')
