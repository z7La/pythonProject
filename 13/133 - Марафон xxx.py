test_string = '''
42
20
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = int(input("За день спортсмен пробегает: "))
value1 = int(input("Длина марафона: "))

res = value0 // value1
print(f'Спортсмен пробежит марафон за: "{res}"')
