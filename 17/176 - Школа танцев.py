test_string = '''
2
раз
два
три
четыре
раз
двыа
раз
два
три
три
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


count_format = ['раз', 'два', 'три', 'четыре']
n = int(input('Запас терпения учителя: '))
count = 0

while n:
    for i in range(len(count_format)):
        value = input()

        if value == count_format[i]:
            count += 1
            i = 0 if value == count_format[-1] else i
        else:
            print(f'Правильных отсчётов было {count}, но теперь вы ошиблись.')
            n -= 1
            count = 0
            break

print('На сегодня хватит.')

