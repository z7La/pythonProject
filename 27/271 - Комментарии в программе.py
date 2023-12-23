test_string = '''
#2
name = input()  
print('Привет,', name) # здороваемся	name = input()
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во титулов: ')[1:])

res_str = ''
for i in range(n):
    res_str += input('Введите строку: ').rstrip() + '\n'
    if '#' in res_str:
        res_str = res_str[:res_str.index('#')].rstrip()

print(res_str)
