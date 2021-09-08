"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
my_string = 'Главный вопрос Жизни, Вселенной и вообще!
The Ultimate Question of Life, the Universe, and Everything!'
"""
my_string = input('Input the string: ')
template = "The longest word is : {longest_word}"
punctuation_marks = '\'"#!$%&()*+,-./:;<=>?@[\]^_{|}~'
for mark in punctuation_marks:
    my_string = my_string.replace(mark, '')
clear_string = my_string.split(' ')
longest_word = ''
for word in clear_string:
    if len(word) > len(longest_word):
        longest_word = word
print(template.format(longest_word=longest_word))
