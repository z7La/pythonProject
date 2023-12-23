test_string = '''
5
лук 1 головка
картофелин штук 6
картошку почистить
лук порезать кольцами
зажарить всё
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во пунктов в рецепте: '))

recipe_list = [input('Продукты: ') for _ in range(n)]
print(', '.join(product for product in recipe_list if 'лук' not in product))
