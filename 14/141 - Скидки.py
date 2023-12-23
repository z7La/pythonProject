test_string = '''
25
2000
370.35
-11
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


total = 0
price = float(input('Вводите цены; для остановки введите -11'))

while price > 0:
    total += price
    price = float(input())
discount = total * 5 / 100 if total >= 1000 else total
discounted_price = round((total - discount), 2)
print(f'Цена без скидки: {total}, со скидкой: {discounted_price}')
