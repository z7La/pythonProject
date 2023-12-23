test_string = '''
3 2 1
Ты и я
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


ind_list = input('Введите строку: ').split()
words_list = input('Введите строку: ').split()

print(' '.join(words_list[int(i)-1] for i in ind_list).capitalize())

# res = ''
# for i in ind_list:
#     res += words_list[int(i)-1] + ' '
#
# print(res.capitalize())
