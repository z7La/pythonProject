test_string = '''
32
30
31
34
38
37
39
0
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


buy_price = 0
sell_price = 0
previous_price = int(input('Цена акции: '))
while True:
    current_price = int(input('Цена акции: '))
    if not current_price:
        break
    elif current_price > previous_price:
        if not buy_price:
            buy_price = current_price
    elif current_price <= previous_price and buy_price:
        sell_price = current_price
        break
    previous_price = current_price


print(f'Цена покупки: "{buy_price}". '
      f'Цена продажи: "{sell_price}". '
      f'Профит: "{sell_price - buy_price}".')
