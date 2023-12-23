test_string = '''
-11.11
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = float(input("Введите число: "))

if value0 > 0:
    print('+')
elif value0 < 0:
    print('-')
else:
    print('0')
