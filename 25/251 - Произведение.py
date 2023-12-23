test_string = '''
4
37
3
99
55
111
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во чисел: '))

my_list = [int(input('Число: ')) for _ in range(n)]

res = 'НЕТ'
product = int(input('Результат произведения двух чисел: '))

for num1 in my_list:
    for num2 in my_list:
        if my_list.index(num1) != my_list.index(num2) and num1 * num2 == product:
            print(num1, num2)
            res = 'ДА'
    if res == 'ДА':
        break

print(res)
