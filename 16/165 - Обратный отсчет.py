import time

test_string = '''
5
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


seconds = int(input('Таймер (в секундах): '))

for i in range(seconds, -1, -1):
    print(f"Осталось секунд: {i}")
    time.sleep(1)
print('Пуск')
