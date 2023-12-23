test_string = '''
11
2
3
0.5
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = float(input("a: "))
value1 = float(input("b: "))
value2 = float(input("c: "))
speed = float(input("d: "))

sqr = value0 * value1 * value2
time = sqr / speed

print(f'Время через которое заполнится бассейн: "{time}"')
