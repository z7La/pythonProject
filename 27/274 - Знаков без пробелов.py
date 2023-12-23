test_string = '''
Раз два три
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


print(len((input().replace('\t', '').replace(' ', ''))))
