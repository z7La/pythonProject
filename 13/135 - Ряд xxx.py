test_string = '''
11
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = int(input('число: '))


def calc(v0):
    v1 = 0
    res3 = 0
    for i in range(4):
        if i == 0:
            v1 = v0 + 1
            res1 = v0 + v1
            v1 += 1
            res2 = res1 * v1
            res3 = res2
        else:
            v1 += 1
            res11 = res3 + v1
            v1 += 1
            res22 = res11 * v1
            res3 = res22
    return res3


result = calc(value0)
print(result)
