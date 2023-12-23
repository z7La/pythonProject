test_string = '''
8
сериал шерлок смотреть онлайн
учебник питона
мемы
социальная сеть
упражнения по питону
кормовые мыши для питонов
ответы егэ скачать бесплатно
компьютерные мыши
питон
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во строк с данными: '))

my_list = []
for i in range(n):
    my_list.append(input('Строка'))

search = input('Поисковый запрос: ')

print('\nСтроки, где встречается поисковый запрос: ')
for el in my_list:
    if search in el:
        print(el)
