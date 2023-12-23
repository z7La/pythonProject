test_string = '''
пароль
пароль
пароль123
пароль12
пароль123
пароль123
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


while True:
    password = input('пароль:')
    repeat_password = input('повторите пароль:')

    if len(password) < 8:
        print('"короткий!"')
    elif password != repeat_password:
        print('"различаются"')
    else:
        print('"OK"')
        break

