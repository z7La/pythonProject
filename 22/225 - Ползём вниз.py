test_string = '''
@VVV>>>>>>>>V<<VVVV<<<VV>>>
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


symbol, *s, = input('Команды: ')
rows = 1
columns = 1
for cmd in s:
    if cmd == '>':
        columns += 1
    elif cmd == 'V':
        rows += 1

my_list = [[' ' for _ in range(columns)] for _ in range(rows)]

x = y = 0
my_list[0][0] = symbol

for ch in s:
    if ch == '>':
        x += 1
        my_list[y][x] = symbol
    elif ch == '<':
        x -= 1
        my_list[y][x] = symbol
    elif ch == 'V':
        y += 1
        my_list[y][x] = symbol

for row in my_list:
    print(' '.join(row))

# s = input('Команды: ')
# pos = 0
# res = s[0]
# left_symbol = s[0]
#
# for i in range(1, len(s)):
#     cmd = s[i]
#
#     if (s[i-1] == '<') and (s[i] != '<'):
#         res += '\n' + ' ' * pos + left_symbol
#         left_symbol = s[0]
#
#     if cmd == 'V':
#         res += '\n' + ' ' * pos + s[0] if s[i+1] != '<' else ''
#
#     elif cmd == '<':
#         left_symbol += s[0]
#         pos -= 1
#
#     elif cmd == '>':
#         res += s[0]
#         pos += 1
#
# print(res)
