test_string = '''
собака
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = input("введите слово: ")
length = len(value0)
print(f'Слово "{value0}" имеет длину "{length}"')