test_string = '''
3   2300
99     *2   =199
20     *100 =2000
11     *4   =55
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


info = input('Кол-во разных товаров и их сумма: ')
n = int(info[:4].rstrip())
total = int(info[4:])
total_price_list = []
my_total_price_list = []

for i in range(n):
    value = input('Стоимость товара: ')
    price = int(value[:7].rstrip())
    quantity = int(value[8:12])
    total_price_list.append(int(value[13:]))
    my_total_price_list.append(price * quantity)

print(f'\nРазность между указанной итоговой суммой и истинной суммой: {total - sum(my_total_price_list)}')
for i in range(n):
    if total_price_list[i] != my_total_price_list[i]:
        print(i+1, end=' ')
