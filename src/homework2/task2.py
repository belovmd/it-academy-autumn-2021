"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
"""
my_string = 'Главный вопрос Жизни, Вселенной и вообще!..'
punctuation_marks = '.,/?!-:;'
for mark in punctuation_marks:
    my_string = my_string.replace(mark, '')
clear_string = my_string.split(' ')
longest_word = ''
for word in clear_string:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)
