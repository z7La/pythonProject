test_string = '''
ivanov:qwerty:100:1:Сергей Иванов, менеджер:/home/ivanov:/bin/sh
ilyina:gfhjkm:101:1:Мария Ильина, старший программист, HL3:/home/ilyina:/bin/sh
kuznetsova:jxtym[bnhsqgfhjkm:102:1:Дарья Кузнецова, младший программист:/home/kuznetsova:/bin/sh
polivanov:qwerty:103:1:Андрей Поливанов, младший программист, TF3:/home/polivanov:/bin/sh

123456;qwerty;password
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


user_name = []
password = []
name = []
while True:
    user_info = input('Информация о пользователе: ').split(':')
    if user_info[0] == '':
        break
    else:
        user_name.append(user_info[0])
        password.append(user_info[1])
        name.append(user_info[4].split(', '))

pass_list = input('Список часто используемых паролей: ').split(';')

for i in range(len(password)):
    if password[i] in pass_list:
        print(f'To: {user_name[i]}')
        print(f'{name[i][0]}, ваш пароль слишком простой, смените его.')

