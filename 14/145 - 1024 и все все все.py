# test_string = '''
# 302231454903657293676544
# '''[1:-1].split('\n')[::-1]
#
# def input(prompt=''):
#     if prompt:
#         print(prompt, end='')
#     tmp = test_string.pop()
#     print(tmp)
#     return tmp
#
# def is_power_of_two(n):
#     if n <= 0:
#         return "НЕТ"
#     elif (n & (n - 1)) == 0:
#         print(num.bit_length() - 1)
#     else:
#         print("НЕТ")
#
# num = int(input())
# result = is_power_of_two(num)

num = 2 ** 20 + 1

if num & (num - 1) == 0:
    cnt = 0
    while num & 1 == 0:
        num >>= 1
        cnt += 1
    print(cnt)
else:
    print('nein')