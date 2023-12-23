test_string = '''
192
189
145
162
172
!
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


height = input('Введите рост несколько раз: ')
max_height = 150
min_height = 190
amount = 0

while height != '!':
    h = int(height)

    if 150 <= h <= 190:
        amount += 1
        max_height = h if max_height < h else max_height
        min_height = h if min_height > h else min_height

    height = input()

print(f'Кол-во кандидатов: "{amount}"\n'
      f'Максимальный рост среди кандидатов: "{max_height}"\n'
      f'Минимальный рост среди кандидатов: "{min_height}"')
