test_string = '''
11
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


stones = int(input('Число камней: '))

count = 0
while stones != 1:
    count += 1
    if stones % 2 == 0:
        stones //= 2
    else:
        stones -= 1
print(f'Кол-во выполненных команд: "{count}"')
