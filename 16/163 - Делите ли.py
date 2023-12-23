test_string = '''
12
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value = int(input('Введите число: '))
count = 0

print(f'{value} делится на: ', end='')
for i in range(1, value + 1):
    if value % i == 0:
        count += 1
        print(i, end=' ')

msg = 'ПРОСТОЕ' if count <= 2 else 'НЕТ'
print(f'\nПростое или нет: {msg}')

