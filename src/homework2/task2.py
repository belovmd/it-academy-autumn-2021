'''Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
'''

string = input('Kindly input some text: ')
punctuation = '.,?-:;!'
for mark in punctuation:
    string = string.replace(mark, '')
words = string.split(' ')
longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print('The longest word is ', longest_word)
