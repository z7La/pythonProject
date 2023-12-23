test_string = '''
520
100
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp

def find_stocks(subsidy, total_cattle):
    for bulls in range(1, total_cattle + 1):
        cows = (subsidy // 5) - (3 * bulls) - total_cattle
        calves = (-1 * (subsidy // 5)) + (2 * bulls) + 2 * total_cattle
        total_cost = bulls * 20 + cows * 10 + calves * 5

        if total_cost == subsidy and calves >= 0 and cows >= 0:
             print(f"{bulls} {cows} {calves}")


subsidy = int(input())
total_cattle = int(input())

find_stocks(subsidy, total_cattle)