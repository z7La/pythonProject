test_string = '''
5
Иванова встала в очередь.
Кузнецов встал в очередь.
Поливанов встал в очередь.
Привет, Кузнецов! Зорина будет за тобой.
Иванова, хватит тут стоять, пошли отсюда.
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во событий: '))
queue_list = []

for i in range(n):
    event = input()
    if 'встала в очередь.' in event:
        queue_list.append(event[:-18])
    elif 'встал в очередь.' in event:
        queue_list.append(event[:-17])
    elif 'будет за тобой.' in event:
        print(queue_list.index(event[8: -24]), event[18:-16])
        queue_list.insert(queue_list.index(event[8: -24])+1, event[18:-16])
    elif 'хватит тут стоять, пошли отсюда.' in event:
        queue_list.remove(event[0:-34])

print('\nОчередь: ', *queue_list, sep='\n')

