test_string = '''
4
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Число не превышающее 9: '))
res = ''
for i in range(n, 0, -1):
    for j in range(n):
        res += chr(ord('A') + j) + str(i) + ' '
    res += '\n'

print(res)
