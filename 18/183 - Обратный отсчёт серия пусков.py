test_string = '''
3
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во запусков: '))

for i in range(n):
    for j in range(i+1):
        print(f'Осталось секунд: {j}')
    print(f'Пуск {i + 1}')

