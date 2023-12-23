test_string = '''
11
2
3
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

if (value0 == 'раз' and value1 == 'два' and value2 == 'три') or\
       (value0 == '11' and value1 == '2' and value2 == '3'):
    print('ГОРИ')
else:
    print('НЕ ГОРИ')
