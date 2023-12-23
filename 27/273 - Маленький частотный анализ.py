test_string = '''
Баобаб
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


my_str = input('Введите строку: ').strip().lower()
my_set = set(my_str)

max_count = 0
res_letter = 'ѐ'
for letter in my_set:
    if max_count < my_str.count(letter):
        max_count = my_str.count(letter)
        res_letter = letter
    elif max_count == my_str.count(letter) and ord(letter) < ord(res_letter):
        res_letter = letter

print(f'Буква "{res_letter}" повторилась "{max_count}" раз')
