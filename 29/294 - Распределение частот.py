test_string = '''
2
Ехал Грека через реку. Видит Грека в реке рак.
Сунул Грека руку в реку, рак за руку Греку цап.
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во строк: '))
words_dict = {}
val_list = " ".join(input() for _ in range(n)).split()

for el in val_list:
    el = el.strip('.,!?:;')
    words_dict[el] = words_dict.get(el, 0) + 1

word_dict = sorted(words_dict.items(), key=lambda x: (-x[1], x[0]))

print('\n'.join(key.capitalize() for key, value in word_dict))
