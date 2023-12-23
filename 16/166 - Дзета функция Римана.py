import math

test_string = '''
1000
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value = int(input('Введите число: '))
summ = 0
for i in range(1, value + 1):
    summ += 1/(i**2)
res = math.pi**2 / summ
print(res)
