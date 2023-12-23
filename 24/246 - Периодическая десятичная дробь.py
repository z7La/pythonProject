test_string = '''
1
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


# n = int(input('Число: '))
# r = 1
# rr = []
# dd = []
# while r not in rr:
#     rr.append(r)
#     dd.append(10 * r // n)
#     r = 10 * r % n
#
# print(*dd[rr.index(r):])


n = int(input('Введите число: '))
res = ''
my_str = str(1/n)

if '0.' in my_str:
    my_str = my_str[2:]

    for i in range(len(my_str)):
        if res == my_str[i:i+len(res)] and i != 0:
            print(res)
            break
        else:
            res += my_str[i]
print(res)
