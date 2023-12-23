# test_string = '''
# раз
# два
# три
# '''[1:-1].split('\n')[::-1]
#
#
# def input(prompt=''):
#     if prompt:
#         print(prompt, end='')
#     tmp = test_string.pop()
#     print(tmp)
#     return tmp

#
# value0 = input("первый ввод: ")
# value1 = input("второй ввод: ")
# value2 = input("третий ввод: ")

for val0 in '1=':
    for val1 in '2=':
        for val2 in '3=':
            if val0 == '1' and val1 == '2' and val2 == '3':
                print('ГОРИ')
            else:
                print('НЕ ГОРИ')
