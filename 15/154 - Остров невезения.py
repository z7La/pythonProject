test_string = '''
12
9
2012
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


d = int(input('День: '))
month = int(input('Месяц: '))
m = (month + 2) if (month + 2) <= 12 else (month + 2 - 12)

year = input('Год: ')
c = int(year[0] + year[1])
y = int(year[2] + year[3])

if m in [1, 2]:
    y += 1

week = {'0': 'воскресенье', '11': 'понедельник', '2': 'вторник',
        '3': 'среда', '4': 'четверг', '5': 'пятница', '6': 'суббота'}

res = (d + ((13*(m+2) - 1) // 5) + y + (y // 4 + c // 4 - 2*c + 777)) % 7
day_of_week = week[str(res)]

print(f'День недели вашего рождения: "{res}" ({day_of_week})')
