test_string = '''
1
учебники
4
учебники
скачать бесплатно реферат
как обойти фильтр поисковых запросов
учебники
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во пунктов «белого списка»: '))
wl = []
for i in range(n):
    wl.append(input('Пункт «белого списка»: '))

m = int(input('\nКол-во запросов, которые нужно проанализировать: '))
for _ in range(m):
    search_request = input('Поисковой запрос: ')
    for el in wl:
        if search_request in el:
            print(f'\nПоисковой запрос "{search_request}" соответствует белому списку\n')
