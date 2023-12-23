test_string = '''
питон
пилот
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


word1 = input('Первое слово: ')
word2 = input('Второе слово: ')

res1 = res2 = 0

for i in set(word1) & set(word2):
    if word1.find(i) == word2.find(i):
        res1 += 1
    else:
        res2 += 1

print(f'символов, которые есть в обеих строках и стоят на одном и том же месте "{res1}" \n'
      f'символов, которые есть в обеих строках, но на разных местах "{res2}"')