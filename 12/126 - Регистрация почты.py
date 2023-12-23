test_string = '''
S.L.Jackson
MEGAKILLER@example.com
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


login = input("логин: ")
mail = input("пароль: ")

if '@' in login:
    print('Некорректный логин')
elif '@' not in mail:
    print('Некорректный адрес')
else:
    print('OK')
