test_string = '''
4
4
Хоббит
Алиса в стране чудес
Том Сойер
Остров сокровищ
Буратино
Хоббит
Остров сокровищ
Война и мир
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


m = int(input('число книг в домашней библиотеке: '))
n = int(input('число книг в списке на лето: '))
s1 = set()

for i in range(m):
    book_title1 = input('Книга из домашней библиотеки: ')
    s1.add(book_title1)

for i in range(n):
    book_title2 = input('Книга из списка на лето: ')
    if book_title2 in s1:
        print(f'YES')
    else:
        print('NO')




