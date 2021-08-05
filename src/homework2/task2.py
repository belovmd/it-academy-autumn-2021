'''Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
'''

my_string = input('Kindly input some text: ')
a = my_string.replace('.', '')
not_useful1 = a.replace('-', '')
not_useful2 = not_useful1.replace('!', '')
not_useful3 = not_useful2.replace('?', '')
b = not_useful3.replace(',', '')
words = b.split(' ')
separate = list(map(len, b.split()))
print(b, len(b), separate)  # just to make sure that this works properly
print('Here is the longest word: ', max(words, key=len))
