test_string = '''
+++>+++++<-.>.>.-.
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


my_str = input('Введите строку: ')
my_list = [0 for _ in range(30_000)]

pos = 0
for i in range(len(my_str)):
    cmd = my_str[i]

    if cmd == '+':
        my_list[pos] += 1 if my_list[pos] + 1 != 256 else -255
    elif cmd == '-':
        my_list[pos] -= 1 if my_list[pos] - 1 != -1 else -255
    elif cmd == '>':
        pos += 1 if pos + 1 != 3_000 else -29_999
    elif cmd == '<':
        pos -= 1 if pos - 1 != -1 else -29_999
    elif cmd == '.':
        print(my_list[pos])
