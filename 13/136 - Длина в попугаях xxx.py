test_string = '''
38 попугаев и еще одно попугайское крылышко
parrot
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


value0 = input("фраза: ")
value1 = input("слово: ")

length1 = len(value0)
length2 = len(value1)

res = length1 // length2

print(f'"{value1}" укладывается в "{value0}", {res} раз')
