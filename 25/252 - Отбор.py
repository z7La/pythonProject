test_string = '''
5
Кузнецов	5
Круглов	4
Федин	4
Тарасов	2
Словецкий	3
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во школьников: '))
students_list = [input('Фамилия с оценкой: ') for _ in range(n)]


for el in students_list:
    print(el)
print()
for el in students_list:
    if el[-1] in ('4', '5'):
        print(el)
