test_string = '''
И мне, и жене, и Тотоше.
Мой милый, хороший,
Пришли мне калоши,

'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = input("первый ввод: ")
value1 = input("второй ввод: ")
value2 = input("третий ввод: ")

print(f'Данные в правильном порядке: \n{value1} \n{value2} \n{value0}')
