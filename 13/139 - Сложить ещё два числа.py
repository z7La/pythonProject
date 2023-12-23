test_string = '''
11.25
2.3
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = float(input("первое число: "))
value1 = float(input("второе число: "))

summ = value0 + value1
print(f'Результат сложения: "{summ}"')