test_string = '''
110
130
120
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = int(input('рост 1: '))
value1 = int(input('рост 2: '))
value2 = int(input('рост 3: '))

l = [value0, value1, value2]
l.sort(reverse=True)

print('\nРезультат: ')
for i in range(len(l)):
    print(l[i])
