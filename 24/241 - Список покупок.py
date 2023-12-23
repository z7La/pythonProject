test_string = '''
4
картину
корзину
картонку
маленькую собачонку
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во покупок: '))

shopping_list = []
for i in range(n):
    shopping_list.append(input())

print('\nСписок покупок: ')
for el in shopping_list:
    print(el)
