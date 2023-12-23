test_string = '''
23
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


num = int(input('Кол-во дорог: '))
print(2, 3, sep='\n')
for i in range(4, num + 1):
    if (i % 2 != 0) and (i % 3 != 0):
        print(i)
