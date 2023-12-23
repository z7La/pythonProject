test_string = '''
3
1
60
1
30
1
100
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


def gcd(a, b):
    num = a
    den = b
    while b:
        a, b = b, a % b
    return num // a, den // a


count = int(input('Кол-во дробинок: '))
common_denominator = 1
common_numerator = 0

for i in range(count):
    numerator = int(input('Урон от дробинки (числитель): '))
    denominator = int(input('Урон от дробинки (знаменатель): '))

    common_numerator = common_numerator * denominator + numerator * common_denominator
    common_denominator *= denominator

    common_numerator, common_denominator = gcd(common_numerator, common_denominator)

print(common_numerator, '/', common_denominator)
