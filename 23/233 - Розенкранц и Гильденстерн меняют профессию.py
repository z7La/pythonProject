test_string = '''
рооррооор
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


my_str = input('Выпавшие стороны монеты: ')
max_o = count_o = 0

for i in my_str:
    if i == 'о':
        count_o += 1
    else:
        max_o = count_o if count_o > max_o else max_o
        count_o = 0

print(max_o)

# print(len(max(my_str.split('р'), key=len)))
