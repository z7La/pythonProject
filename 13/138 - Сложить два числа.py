test_string = '''
34234324
52354436
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = int(input("первое число: "))
value1 = int(input("второе число: "))

summ = value0 + value1
print(f'Результат сложения: "{summ}"')
